#!/usr/bin/env python3
"""
link_pages.py — connect theories, principles, patterns, elements and strategies
that nothing links to.

`link_claims.py` joined the claims to each other. It left 718 pages with no link
in or out (2026-09-27), none of them claims: 220 strategies, 186 theories, 154
elements, 81 principles and 67 patterns, almost all written by a batch. An
extraction writes a pattern, a strategy and a claim from one article and links
none of them to the others, or to the pages the wiki already had on the topic.

For each page outside the main connected component, this takes the pages written
from the same source (`sources/manifest.ndjson`) and the most similar pages of
any kind (search_index.py, BM25), and asks a model which of them the page bears
on and how. Each answer is written where the page template already puts that
kind of link, and nowhere else:

    related     same kind, a neighbouring idea  -> both pages' `## Related <Kind>`
    applies     the page puts the other into practice (a strategy using an
                element, a pattern applying a principle, anything drawing on a
                theory) -> the other page's `## Examples`
    applied_by  the reverse -> this page's `## Examples`
    evidence    the other is a claim bearing on this page -> `### Claims` with
                the model's [±~][SMW] marker, on the kinds whose template has a
                Claims section (theory, principle, pattern, process, learner
                variable); on a pattern, `#### Supporting` or `#### Contradicting`
                by polarity

`applies` is refused unless the other page is the more abstract kind (a theory
does not apply a strategy), and a claim is never written onto a strategy or an
element, whose templates weave claims into prose sections a script should not
edit. A marker is the model's reading of how this page uses the claim, as the
extractor's markers are; the decision record keeps it, so it can be audited.

    python3 scripts/link_pages.py --unlinked --out eval/runs/page-links/unlinked.ndjson
    python3 scripts/link_pages.py --new --apply
    python3 scripts/link_pages.py --apply --from eval/runs/page-links/unlinked.ndjson
"""
import argparse
import collections
import concurrent.futures
import json
import os
import re
import sqlite3
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
import search_index  # noqa: E402

KIND = {"principles": "principle", "elements": "element", "patterns": "pattern",
        "strategies": "strategy", "processes": "process", "methods": "method",
        "theories": "theory", "learner-variables": "learner variable", "claims": "claim"}
RELATED_HEAD = {"principles": "Related Principles", "elements": "Related Elements",
                "patterns": "Related Patterns", "strategies": "Related Strategies",
                "processes": "Related Processes", "methods": "Related Methods",
                "theories": "Related Theories", "learner-variables": "Related Learner Variables",
                "claims": "Related Claims"}
# How abstract a kind is. `applies` needs the other page strictly more abstract,
# except that a strategy or method may use an element.
RANK = {"theories": 4, "learner-variables": 4, "principles": 3, "patterns": 2, "processes": 2,
        "elements": 1, "strategies": 1, "methods": 1, "claims": 0}
CLAIMS_ON = {"theories", "principles", "patterns", "processes", "learner-variables"}
MARKER_RE = re.compile(r"^[+~-][SMW]$")
LINK_RE = re.compile(r"\]\(<?([^)>\s#]+\.md)")
HEAD_RE = re.compile(r"^(#{2,4}) +(.+?)\s*$")
SYSTEM = "You organise a learning-design wiki. Reply with one JSON object and nothing else."


def all_pages() -> dict:
    return {f"{f}/{p.stem}": p for f in okf_lib.CONTENT_FOLDERS
            for p in (WIKI_ROOT / f).glob("*.md") if p.stem != "index"}


def link_graph(pages: dict) -> dict:
    """Undirected adjacency over content pages, from every markdown link on them."""
    adj = collections.defaultdict(set)
    root = WIKI_ROOT.resolve()
    for key, path in pages.items():
        for m in LINK_RE.finditer(path.read_text(encoding="utf-8")):
            try:
                rel = (path.parent / unquote(m.group(1))).resolve().relative_to(root)
            except ValueError:
                continue
            other = str(rel.with_suffix(""))
            if other in pages and other != key:
                adj[key].add(other)
                adj[other].add(key)
    return adj


def outside_main(pages: dict, adj: dict) -> list:
    """Pages not in the largest connected component, isolated pages first."""
    seen, comps = set(), []
    for k in pages:
        if k in seen:
            continue
        comp, stack = [], [k]
        seen.add(k)
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        comps.append(comp)
    comps.sort(key=len, reverse=True)
    rest = [k for c in comps[1:] for k in c]
    return sorted(rest, key=lambda k: (len(adj[k]) > 0, k))


def siblings() -> dict:
    """page key -> the other pages its source contributed, from the manifest."""
    out = collections.defaultdict(set)
    path = WIKI_ROOT / "sources" / "manifest.ndjson"
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        keys = [p[:-3] for p in rec.get("pages") or [] if p.endswith(".md")]
        for k in keys:
            out[k].update(x for x in keys if x != k)
    return out


def record(key: str, path: Path) -> dict:
    fm_lines, body = okf_lib.split_frontmatter(path.read_text(encoding="utf-8"))
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)
    evidence = re.search(r"^> \*\*Evidence\*\* · (.+)$", body, re.M)
    return {"key": key, "folder": key.split("/")[0], "title": str(fm.get("title") or key.split("/")[1]),
            "description": str(fm.get("description") or "")[:300],
            "evidence": evidence.group(1)[:160] if evidence else ""}


def new_pages() -> list:
    out = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", *okf_lib.CONTENT_FOLDERS],
                         cwd=WIKI_ROOT, capture_output=True, text=True).stdout.split()
    out += subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", "HEAD", "--",
                           *okf_lib.CONTENT_FOLDERS], cwd=WIKI_ROOT, capture_output=True, text=True).stdout.split()
    return sorted({p[:-3] for p in out if p.endswith(".md") and not p.endswith("index.md")
                   and p.split("/")[0] != "claims"})


def candidates(db, rec: dict, sibs: set, k: int = 10) -> list:
    rows = search_index.query(db, rec["title"] + " " + rec["description"], limit=k + 1, mode="OR")
    found = [f"{r[1]}/{r[2]}" for r in rows]
    out = sorted(sibs)[:6]                     # the pages its own source wrote, first
    out += [x for x in found if x != rec["key"] and x not in out][:k]
    return out


def allowed(src: str, dst: str, rel: str) -> bool:
    a, b = src.split("/")[0], dst.split("/")[0]
    if rel == "related":
        return a == b
    if rel == "evidence":
        return b == "claims" and a in CLAIMS_ON
    if rel == "applies":
        return b != "claims" and a != "claims" and (RANK[b] > RANK[a] or (b == "elements" and a in ("strategies", "methods")))
    if rel == "applied_by":
        return allowed(dst, src, "applies")
    return False


def strength_cap(evidence: str) -> str:
    """The strongest marker a claim's recorded evidence allows: S needs two or more
    studies with one coded q3 or above, M one study coded q2 or above; anything else,
    including no coded evidence, is W. A cap only lowers the model's marker, never
    sets one: the direction and the reading stay the model's, and the decision
    record keeps what it said."""
    import re as _re
    studies = _re.search(r"(\d+) stud", evidence)
    qs = [int(q) for q in _re.findall(r"`q(\d)", evidence)]
    n, q = (int(studies.group(1)) if studies else 0), (max(qs) if qs else 0)
    return "S" if n >= 2 and q >= 3 else "M" if n >= 1 and q >= 2 else "W"


def classify(rec: dict, cands: list, key: str, model: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    listing = "\n".join(
        f"{i + 1}. [{KIND[c['folder']]}] {c['title']} — {c['description'][:200]}"
        + (f" [evidence: {c['evidence'] or 'none recorded'}]" if c["folder"] == "claims" else "")
        for i, c in enumerate(cands))
    prompt = f"""PAGE [{KIND[rec['folder']]}]: {rec['title']}
{rec['description']}

OTHER PAGES:
{listing}

For each OTHER page that PAGE genuinely bears on, give its number and relation:
- "related": the same kind of page about a neighbouring idea a reader of PAGE would want next.
- "applies": PAGE puts the other page into practice: a strategy or pattern using an element,
  applying a principle or drawing on a theory; a principle resting on a theory.
- "applied_by": the other page puts PAGE into practice (the reverse of "applies").
- "evidence": the other page is a claim that bears on PAGE. Also give "marker": its direction
  (+ supports PAGE, ~ depends on conditions, - counts against it) and strength from the claim's
  evidence line in brackets, not from its title (S strong: several studies, experiments or
  meta-analysis; M moderate; W weak: one small or non-experimental study, or an argument), e.g. "+W".
Leave out pages that only share words with PAGE. An empty list is a good answer when nothing fits.
Reply: {{"links": [{{"n": <number>, "relation": "<relation>", "marker": "<only for evidence>"}}]}}"""
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=6000,
                      reasoning_effort="low" if "glm" in model else None)
    data = extract_json(gen.raw_text)
    links = []
    for item in (data.get("links") or []) if isinstance(data, dict) else []:
        n, rel = item.get("n"), item.get("relation")
        if not (isinstance(n, int) and 1 <= n <= len(cands)):
            continue
        dst = cands[n - 1]["key"]
        marker = item.get("marker") if rel == "evidence" else None
        if rel == "evidence" and not (isinstance(marker, str) and MARKER_RE.match(marker)):
            continue
        extra = {}
        if marker:
            cap = strength_cap(cands[n - 1]["evidence"])
            if "WMS".index(marker[1]) > "WMS".index(cap):
                extra = {"marker": marker[0] + cap, "model_marker": marker}
            else:
                extra = {"marker": marker}
        if allowed(rec["key"], dst, rel):
            links.append({"target": dst, "relation": rel, **extra})
    return {"page": rec["key"], "candidates": [c["key"] for c in cands], "links": links,
            "model": model, "cost_usd": gen.cost_usd, "provider": gen.provider}


def run(keys: list, out: Path, model: str, concurrency: int) -> list:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not set")
    pages = all_pages()
    sibs = siblings()
    search_index.ensure().close()
    cache = {}

    def rec(k):
        if k not in cache:
            cache[k] = record(k, pages[k])
        return cache[k]

    results = []
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        def worker(k):
            local = sqlite3.connect(search_index.DB_PATH)
            try:
                r = rec(k)
                cands = [rec(c) for c in candidates(local, r, {s for s in sibs.get(k, ()) if s in pages})
                         if c in pages]
                return classify(r, cands, api_key, model) if cands else {"page": k, "candidates": [], "links": []}
            except Exception as e:
                return {"page": k, "error": f"{type(e).__name__}: {e}"[:300]}
            finally:
                local.close()
        for res in ex.map(worker, keys):
            fh.write(json.dumps(res) + "\n")
            fh.flush()
            results.append(res)
    return results


def href(src: str, dst: str) -> str:
    a, b = src.split("/")[0], dst.split("/")
    return f"{b[1]}.md" if a == b[0] else f"../{b[0]}/{b[1]}.md"


def insert(path: Path, heads: list, bullet: str, fallback: str) -> None:
    """Append `bullet` to the first of `heads` present on the page (any level),
    replacing an empty template placeholder; else add `## fallback` at the end."""
    lines = path.read_text(encoding="utf-8").split("\n")
    at = None
    for want in heads:
        at = next((i for i, l in enumerate(lines) if (m := HEAD_RE.match(l)) and m.group(2) == want), None)
        if at is not None:
            break
    if at is None:
        while lines and not lines[-1].strip():
            lines.pop()
        lines += ["", f"## {fallback}", "", bullet, ""]
    else:
        end = next((i for i in range(at + 1, len(lines)) if HEAD_RE.match(lines[i])), len(lines))
        body = [l for l in lines[at + 1:end] if l.strip() not in ("-",)]
        while body and not body[-1].strip():
            body.pop()
        while body and not body[0].strip():
            body.pop(0)
        lines[at + 1:end] = [""] + body + [bullet, ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def links_to(path: Path, dst: str) -> bool:
    root = WIKI_ROOT.resolve()
    for m in LINK_RE.finditer(path.read_text(encoding="utf-8")):
        try:
            if str((path.parent / unquote(m.group(1))).resolve().relative_to(root).with_suffix("")) == dst:
                return True
        except ValueError:
            pass
    return False


def write(src: str, dst: str, rel: str, marker: str, pages: dict, titles: dict) -> bool:
    """One link, on the page the relation says it belongs to. False if already there."""
    if rel == "applies":
        src, dst, rel = dst, src, "applied_by"
    path = pages[src]
    if links_to(path, dst):
        return False
    title = titles[dst].replace("[", "(").replace("]", ")")
    folder = src.split("/")[0]
    if rel == "related":
        insert(path, [RELATED_HEAD[folder]], f"- [{title}]({href(src, dst)})", RELATED_HEAD[folder])
    elif rel == "applied_by":
        insert(path, ["Examples"], f"- [{title}]({href(src, dst)})", "Examples")
    elif rel == "evidence":
        heads = (["Supporting"] if marker[0] == "+" else ["Contradicting"]) if folder == "patterns" else []
        insert(path, heads + ["Claims"], f"- [{title}]({href(src, dst)}) [{marker}]", "Claims")
    return True


def apply(results: list) -> dict:
    pages = all_pages()
    titles = {}
    stats = collections.Counter()
    changed = set()
    for res in results:
        for link in res.get("links") or []:
            src, dst, rel = res["page"], link["target"], link["relation"]
            if src not in pages or dst not in pages:
                continue
            for k in (src, dst):
                if k not in titles:
                    titles[k] = record(k, pages[k])["title"]
            wrote = write(src, dst, rel, link.get("marker"), pages, titles)
            if rel == "related":
                wrote = write(dst, src, rel, None, pages, titles) or wrote
            if wrote:
                stats[rel] += 1
                changed.update((src, dst))
    stats["pages_changed"] = len(changed)
    return dict(stats)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--unlinked", action="store_true", help="every page outside the main connected component")
    src.add_argument("--new", action="store_true", help="non-claim pages added in the working tree")
    src.add_argument("--pages", nargs="+", help="these <folder>/<slug> keys")
    src.add_argument("--from", dest="from_file", help="apply a previous run's decisions without re-asking")
    ap.add_argument("--out", default=None)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--model", default="z-ai/glm-5.3-flash")
    ap.add_argument("--concurrency", type=int, default=16)
    args = ap.parse_args()

    if args.from_file:
        results = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        if args.unlinked:
            pages = all_pages()
            keys = outside_main(pages, link_graph(pages))
        else:
            keys = new_pages() if args.new else args.pages
        if not keys:
            print("no pages to link")
            return
        mode = "unlinked" if args.unlinked else "new" if args.new else "pages"
        out = Path(args.out) if args.out else WIKI_ROOT / "eval" / "runs" / "page-links" / f"{mode}.ndjson"
        print(f"linking {len(keys)} page(s) with {args.model}; decisions -> {out}", flush=True)
        results = run(keys, out, args.model, args.concurrency)
        print(f"asked {len(results)}, errors {sum(1 for r in results if r.get('error'))}, "
              f"cost ${sum(r.get('cost_usd') or 0 for r in results):.4f}")
    rels = collections.Counter(l["relation"] for r in results for l in r.get("links") or [])
    print("proposed:", dict(rels) or "nothing")
    if args.apply:
        print("applied:", apply(results))


if __name__ == "__main__":
    main()
