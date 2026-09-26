#!/usr/bin/env python3
"""
mcp_server.py — the wiki as a Model Context Protocol server.

`wiki-index.json` and `reverse-index.json` are committed so that other repos
can resolve against the wiki without a checkout, but a file is something an
agent has to know how to read. This serves the same data as tools, so an agent
in Claude Code, Claude Desktop, ChatGPT or anything else that speaks MCP can
query the wiki directly.

The shape is borrowed from the Renaissance AI and Education Resource Hub's
worker (github.com/jchoi92k/Learning-Engineering-Resource-Hub, worker/src/index.js):
a `search` / `fetch` pair in the form deep-research clients expect, every
result returned as both structured content and its JSON text, and an unknown
tool answered with a hint that the client's cached tool list is stale. No code
was copied: that repo has no licence yet.

Tools:

    search(query, kind?, limit?)   ranked pages; ids are "<kind>/<slug>"
    fetch(id)                      one page's full markdown, with its metadata
    resolve(slug, kind?)           a slug (current OR retired) -> the page it names
    backlinks(id)                  which pages link TO this one, with evidence markers
    why(claim)                     claim <- evidence <- release <- protocol, from research/

Everything is read-only, and nothing here is newer than the checkout it runs
from. Every page result carries `status` and `trust_tier`. At the time of
writing no page has a `verified:` entry, so every tier reads `unverified`, and
the server says so rather than letting a fluent page read as a checked one.

    python3 scripts/mcp_server.py                    # stdio (Claude Code, Claude Desktop)
    python3 scripts/mcp_server.py --http 8765        # stateless HTTP on 127.0.0.1:8765/mcp
    python3 scripts/mcp_server.py --call search '{"query": "retrieval practice"}'

Claude Code:  claude mcp add learning-wiki -- python3 /path/to/learning-wiki/scripts/mcp_server.py

Standard library plus PyYAML, which the docs build already requires.
"""

import argparse
import contextlib
import inspect
import io
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib

WIKI_ROOT = Path(__file__).parent.parent
SITE_URL = "https://learning-design-alliance.github.io/learning-wiki/"
SERVER_INFO = {"name": "learning-wiki", "version": "1.0.0"}
PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"]

UNVERIFIED_NOTE = (
    "This wiki is written and maintained by language models. trust_tier says whether a "
    "person has checked a page against its sources; 'unverified' means nobody has. Cite "
    "the primary sources a page names, not the page."
)


# ---------------------------------------------------------------------------
# The corpus, loaded once
# ---------------------------------------------------------------------------

class Wiki:
    def __init__(self, root: Path = WIKI_ROOT):
        self.root = root
        index = json.loads((root / "wiki-index.json").read_text(encoding="utf-8"))
        reverse = json.loads((root / "reverse-index.json").read_text(encoding="utf-8"))
        self.pages = {f"{p['type']}/{p['id']}": p for p in index["pages"]}
        self.resolve_map = index["resolve"]            # {kind: {slug-or-alias: id}}
        self.folder_of = {kind: folder for folder, kind in reverse["kinds"].items()}
        self.folder_of.setdefault("strategy", "strategies")
        self.kind_of = {folder: kind for kind, folder in self.folder_of.items()}
        self.edges = reverse["edges"]                  # {folder: {slug: {src_folder: [...]}}}
        self._text = {}

    @property
    def kinds(self) -> list[str]:
        return sorted(self.resolve_map)

    def text(self, pid: str) -> str:
        if pid not in self._text:
            path = self.root / self.pages[pid]["path"]
            self._text[pid] = path.read_text(encoding="utf-8") if path.is_file() else ""
        return self._text[pid]

    def url(self, pid: str) -> str:
        path = self.pages[pid]["path"][: -len(".md")]
        return SITE_URL + quote(path) + "/"

    def resolve(self, slug: str, kind: str | None = None) -> list[dict]:
        slug = slug.strip().removesuffix(".md")
        if "/" in slug and kind is None:
            head, _, rest = slug.partition("/")
            kind = self.kind_of.get(head, head)
            slug = rest
        out = []
        for k in ([kind] if kind else self.kinds):
            target = self.resolve_map.get(k, {}).get(slug)
            if target:
                out.append({"id": f"{k}/{target}", "kind": k, "slug": target,
                            "via_alias": target != slug})
        return out


def frontmatter(text: str) -> dict:
    import yaml

    m = okf_lib.FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def trust_tier(fm: dict) -> str:
    """CLAUDE.md's three tiers, derived from `verified:`."""
    v = fm.get("verified")
    if not v:
        return "unverified"
    entries = v if isinstance(v, list) else [v]
    actors = [str((e or {}).get("by", "")) for e in entries if isinstance(e, dict)]
    return "human-reviewed" if any(a.startswith("human:") for a in actors) else "machine-confirmed"


def jsonable(value):
    """PyYAML turns `at: 2026-09-24` into a date; JSON cannot carry one."""
    return json.loads(json.dumps(value, default=str))


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

class ToolError(Exception):
    """Bad arguments: reported to the client as a tool error it can act on."""


def _tokens(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", s.lower())


def _search_indexed(wiki: Wiki, query: str, terms: list, phrase: str, kind, limit: int):
    """The same search through search_index.py's FTS5 index, which answers in
    milliseconds at any wiki size where the scan below reads every page. Returns
    None when the index cannot be used (no sqlite FTS5, or a checkout the index
    cannot be written into), and the scan answers instead."""
    try:
        if str(Path(__file__).parent) not in sys.path:
            sys.path.insert(0, str(Path(__file__).parent))
        import search_index
        db = search_index.ensure(wiki.root)
        folder = wiki.folder_of.get(kind) if kind else None
        rows = search_index.query(db, query, folder=folder, limit=limit * 4, mode="AND")
        total = db.execute("select count(*) from pages where pages match ?" + (" and folder = ?" if folder else ""),
                           [search_index.match_expr(query, mode="AND")] + ([folder] if folder else [])).fetchone()[0]
    except Exception:
        return None
    scored = []
    for pid_path, folder_name, slug, title, desc, status, score in rows:
        k = wiki.kind_of.get(folder_name)
        pid = f"{k}/{slug}"
        if pid not in wiki.pages:
            continue
        fields = set()
        for name, text in (("title", title), ("id", slug.replace("-", " ")), ("description", desc)):
            if any(re.search(rf"\b{re.escape(t)}", text.lower()) for t in terms):
                fields.add(name)
        score += 10 if phrase in " ".join(_tokens(title)) else 0
        if status == "draft":
            score *= 0.8
        scored.append((score, pid, sorted(fields or {"body"})))
    scored.sort(key=lambda x: (-x[0], x[1]))
    results = []
    for score, pid, fields in scored[:limit]:
        p = wiki.pages[pid]
        results.append({"id": pid, "title": p.get("title") or p["id"], "url": wiki.url(pid),
                        "kind": p["type"], "status": p.get("status"),
                        "description": p.get("description") or "", "matched": fields})
    return {"query": query, "total_matches": total, "results": results, "engine": "fts5"}


def tool_search(wiki: Wiki, query: str, kind: str | None = None, limit: int = 10) -> dict:
    """Keyword search, scored title > id > description > body. Deliberately
    simple and explainable: every hit says which fields matched, so an agent
    can tell a title match from one stray word in a 5,000-word page."""
    if not isinstance(query, str) or not query.strip():
        raise ToolError("query must be a non-empty string")
    if kind and kind not in wiki.resolve_map:
        raise ToolError(f"unknown kind {kind!r}; kinds are {wiki.kinds}")
    limit = max(1, min(int(limit or 10), 50))
    terms = [t for t in _tokens(query) if len(t) > 1]
    if not terms:
        raise ToolError("query has no searchable words")
    phrase = " ".join(terms)
    indexed = _search_indexed(wiki, query, terms, phrase, kind, limit)
    if indexed is not None:
        return indexed
    scored = []
    for pid, p in wiki.pages.items():
        if kind and p["type"] != kind:
            continue
        title = " ".join(_tokens(p.get("title") or ""))
        slug = " ".join(_tokens(p["id"]))
        desc = " ".join(_tokens(p.get("description") or ""))
        score, fields = 0.0, set()
        for t in terms:
            for name, text, weight in (("title", title, 6), ("id", slug, 4), ("description", desc, 2)):
                if re.search(rf"\b{re.escape(t)}", text):
                    score += weight
                    fields.add(name)
        if phrase in title:
            score += 10
        if score == 0 and len(terms) > 0:
            body = wiki.text(pid).lower()
            hits = sum(1 for t in terms if t in body)
            if hits == len(terms):
                score, fields = 1.0, {"body"}
        if score:
            # A stub ranks below a written page on the same words.
            if p.get("status") == "draft":
                score *= 0.8
            scored.append((score, pid, sorted(fields)))
    scored.sort(key=lambda x: (-x[0], x[1]))
    results = []
    for score, pid, fields in scored[:limit]:
        p = wiki.pages[pid]
        results.append({"id": pid, "title": p.get("title") or p["id"], "url": wiki.url(pid),
                        "kind": p["type"], "status": p.get("status"),
                        "description": p.get("description") or "", "matched": fields})
    return {"query": query, "total_matches": len(scored), "results": results}


def tool_fetch(wiki: Wiki, id: str) -> dict:
    matches = wiki.resolve(id)
    if not matches:
        raise ToolError(f"no page {id!r}; ids look like 'claim/<slug>' — take them from search")
    if len(matches) > 1:
        raise ToolError(f"{id!r} names a page in {len(matches)} kinds: "
                        f"{[m['id'] for m in matches]}; ask for one of those ids")
    pid = matches[0]["id"]
    p = wiki.pages[pid]
    text = wiki.text(pid)
    fm = frontmatter(text)
    return {
        "id": pid,
        "title": p.get("title") or p["id"],
        "url": wiki.url(pid),
        "text": text,
        "metadata": {
            "kind": p["type"],
            "path": p["path"],
            "status": p.get("status"),
            "trust_tier": trust_tier(fm),
            "aliases": p.get("aliases") or [],
            "generated": jsonable(fm.get("generated")),
            "resolved_from": id if matches[0]["via_alias"] else None,
            "note": UNVERIFIED_NOTE,
        },
    }


def tool_resolve(wiki: Wiki, slug: str, kind: str | None = None) -> dict:
    if kind and kind not in wiki.resolve_map:
        raise ToolError(f"unknown kind {kind!r}; kinds are {wiki.kinds}")
    matches = wiki.resolve(slug, kind)
    for m in matches:
        p = wiki.pages[m["id"]]
        m.update(title=p.get("title"), status=p.get("status"), path=p["path"], url=wiki.url(m["id"]))
    return {"slug": slug, "kind": kind, "resolved": bool(matches), "matches": matches}


def tool_backlinks(wiki: Wiki, id: str) -> dict:
    matches = wiki.resolve(id)
    if len(matches) != 1:
        raise ToolError(f"{id!r} resolves to {[m['id'] for m in matches] or 'nothing'}; "
                        "pass one id like 'principle/<slug>'")
    pid = matches[0]["id"]
    kind, slug = pid.split("/", 1)
    by_folder = wiki.edges.get(wiki.folder_of.get(kind, ""), {}).get(slug, {})
    links = []
    for folder, items in sorted(by_folder.items()):
        for it in items:
            src = f"{wiki.kind_of.get(folder, folder)}/{it['slug']}"
            row = {"id": src, "title": (wiki.pages.get(src) or {}).get("title")}
            if "polarity" in it:
                row["marker"] = f"[{it['polarity']}{it.get('strength', '')}]"
            links.append(row)
    return {"id": pid, "count": len(links), "backlinks": links,
            "note": "A marker is how the linking page tags its use of this claim: + supports, "
                    "~ mixed or contextual, - contradicts; S/M/W strong/moderate/weak."
                    if kind == "claim" else None}


def tool_why(wiki: Wiki, claim: str) -> dict:
    """check_research.why() is the acceptance test for the research layer, and
    it prints. Its output is captured rather than re-implemented, so the tool
    and the command can never disagree."""
    matches = wiki.resolve(claim, "claim")
    if not matches:
        raise ToolError(f"no claim {claim!r}")
    slug = matches[0]["slug"]
    import check_research

    buf, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
        code = check_research.why(slug)
    return {"claim": f"claim/{slug}", "exit_code": code, "traversal": buf.getvalue(),
            "stderr": err.getvalue() or None}


def _schema(props: dict, required: list[str]) -> dict:
    return {"type": "object", "properties": props, "required": required, "additionalProperties": False}


def tool_definitions(wiki: Wiki) -> list[dict]:
    kinds = {"type": "string", "enum": wiki.kinds, "description": "Restrict to one kind of page."}
    ro = {"readOnlyHint": True, "openWorldHint": False}
    return [
        {"name": "search", "annotations": ro,
         "description": "Search the Learning Design Wiki (principles, elements, patterns, strategies, "
                        "processes, methods, theories, learner variables and empirical claims). Returns "
                        "ids of the form '<kind>/<slug>' for fetch. " + UNVERIFIED_NOTE,
         "inputSchema": _schema({"query": {"type": "string"}, "kind": kinds,
                                 "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10}},
                                ["query"])},
        {"name": "fetch", "annotations": ro,
         "description": "The full markdown of one wiki page, by an id from search ('claim/<slug>'). "
                        "Retired slugs still resolve. Metadata carries status and trust_tier.",
         "inputSchema": _schema({"id": {"type": "string"}}, ["id"])},
        {"name": "resolve", "annotations": ro,
         "description": "Resolve a slug to the page it names, including slugs retired by a rename "
                        "(aliases). Without kind, returns every kind the slug exists in — the same slug "
                        "can be, say, both a process and a strategy.",
         "inputSchema": _schema({"slug": {"type": "string"}, "kind": kinds}, ["slug"])},
        {"name": "backlinks", "annotations": ro,
         "description": "Which pages link to this one. For a claim, each backlink carries the evidence "
                        "marker the linking page gave it, e.g. [+S] or [~M].",
         "inputSchema": _schema({"id": {"type": "string"}}, ["id"])},
        {"name": "why", "annotations": ro,
         "description": "Why the wiki believes a claim: its structured evidence records, the research "
                        "release and protocol behind each, and what is contested. Records that are not "
                        "published findings (simulations, telemetry) are labelled loudly. Most claims "
                        "have no structured record yet, and the result says so.",
         "inputSchema": _schema({"claim": {"type": "string"}}, ["claim"])},
    ]


TOOLS = {"search": tool_search, "fetch": tool_fetch, "resolve": tool_resolve,
         "backlinks": tool_backlinks, "why": tool_why}


# ---------------------------------------------------------------------------
# JSON-RPC
# ---------------------------------------------------------------------------

def call_tool(wiki: Wiki, name: str, args: dict) -> dict:
    fn = TOOLS.get(name)
    if fn is None:
        return {"isError": True, "content": [{"type": "text", "text":
                f"Unknown tool: {name}. Available tools: {', '.join(TOOLS)}. If your client still "
                f"lists this tool, its tool list is stale — reconnect to refresh it."}]}
    try:
        # Checked against the signature before the call, so a TypeError raised
        # INSIDE a tool is a bug that surfaces, not "bad arguments".
        inspect.signature(fn).bind(wiki, **(args or {}))
    except TypeError as exc:
        return {"isError": True, "content": [{"type": "text", "text":
                f"Tool '{name}' got bad arguments ({exc}). Check them against its input schema."}]}
    try:
        result = fn(wiki, **(args or {}))
    except ToolError as exc:
        return {"isError": True, "content": [{"type": "text", "text": f"Tool '{name}': {exc}"}]}
    # Structured content for clients that read it, and the same object as text
    # for those that do not — the spec says a tool returning structured content
    # SHOULD also return it serialised.
    return {"structuredContent": result,
            "content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=1)}]}


def handle(wiki: Wiki, msg: dict) -> dict | None:
    """One JSON-RPC message in, one response out (None for a notification)."""
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}

    def ok(result):
        return {"jsonrpc": "2.0", "id": mid, "result": result}

    def err(code, message):
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": code, "message": message}}

    if mid is None:  # notifications (initialized, cancelled) need no answer
        return None
    if method == "initialize":
        asked = params.get("protocolVersion")
        version = asked if asked in PROTOCOL_VERSIONS else PROTOCOL_VERSIONS[0]
        return ok({"protocolVersion": version, "capabilities": {"tools": {}},
                   "serverInfo": SERVER_INFO,
                   "instructions": "Read-only access to the Learning Design Wiki. Start with search, "
                                   "then fetch. " + UNVERIFIED_NOTE})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": tool_definitions(wiki)})
    if method == "tools/call":
        if not params.get("name"):
            return err(-32602, "tools/call requires params.name")
        return ok(call_tool(wiki, params["name"], params.get("arguments") or {}))
    return err(-32601, f"method not found: {method}")


def serve_stdio(wiki: Wiki) -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            out = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"parse error: {exc}"}}
        else:
            out = handle(wiki, msg) if isinstance(msg, dict) else {
                "jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "batches are not supported"}}
        if out is not None:
            sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
            sys.stdout.flush()


def serve_http(wiki: Wiki, port: int, host: str) -> None:
    """Stateless Streamable HTTP: POST /mcp with one JSON-RPC message, answered
    with one JSON response. No sessions and no server-initiated messages, which
    is all a read-only tools server needs."""
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    class Handler(BaseHTTPRequestHandler):
        def _send(self, status, body=None):
            data = b"" if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            if body is not None:
                self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_POST(self):
            if self.path.rstrip("/") != "/mcp":
                return self._send(404, {"error": "POST to /mcp"})
            try:
                msg = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)))
            except (ValueError, json.JSONDecodeError):
                return self._send(400, {"jsonrpc": "2.0", "id": None,
                                        "error": {"code": -32700, "message": "parse error"}})
            out = handle(wiki, msg) if isinstance(msg, dict) else None
            return self._send(202) if out is None else self._send(200, out)

        def do_GET(self):
            if self.path.rstrip("/") == "/mcp":
                # No server-to-client stream; the spec's answer for that is 405.
                return self._send(405, {"error": "this server does not open an SSE stream"})
            return self._send(200, {**SERVER_INFO, "tools": list(TOOLS), "endpoint": "/mcp"})

        def log_message(self, *a):
            pass

    print(f"learning-wiki MCP server on http://{host}:{port}/mcp", file=sys.stderr)
    ThreadingHTTPServer((host, port), Handler).serve_forever()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--http", type=int, metavar="PORT", help="serve stateless HTTP instead of stdio")
    ap.add_argument("--host", default="127.0.0.1", help="HTTP bind address (default 127.0.0.1)")
    ap.add_argument("--call", nargs=2, metavar=("TOOL", "JSON_ARGS"), help="run one tool and print it")
    args = ap.parse_args()
    wiki = Wiki()
    if args.call:
        result = call_tool(wiki, args.call[0], json.loads(args.call[1]))
        print(result["content"][0]["text"])
        return 1 if result.get("isError") else 0
    if args.http:
        serve_http(wiki, args.http, args.host)
    else:
        serve_stdio(wiki)
    return 0


if __name__ == "__main__":
    sys.exit(main())
