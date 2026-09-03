#!/usr/bin/env python3
"""
okf_lib.py — Shared helpers for reading/writing OKF-conformant wiki pages.

OKF = Open Knowledge Format (https://github.com/GoogleCloudPlatform/knowledge-catalog
/blob/main/okf/SPEC.md), v0.2. Every content page keeps a `type` field plus the
recommended `title`/`description`, and carries provenance via `generated`/`sources`
instead of the old ad hoc `edited_by`/`last_edited` pair. Cross-links are plain
bundle-relative markdown links (`[Label](/folder/slug.md)`) instead of Obsidian
wikilinks.
"""

import re
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent

# The one list of content folders. Thirteen scripts each carried their own
# copy of this before `processes` and `methods` were added, which is the same
# shape of defect that left learner-variables out of build_indexes for weeks:
# a set written down N times drifts at the first addition. The copies that
# mean "every content folder" now derive from here; the ones that mean a
# genuine subset derive from here too, minus what they exclude and why.
CONTENT_FOLDERS = ["principles", "elements", "patterns", "strategies",
                   "processes", "methods",
                   "theories", "learner-variables", "claims"]

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")
TITLE_RE = re.compile(r"^# (.+)$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

# Existing edited_by values are freeform names/tool labels already committed to the
# wiki's history (e.g. "Claude", "Codex", "David Porcaro"). Map them onto OKF's actor
# convention (`<producer>/<version>`, `human:<id>`, `process:<id>`) without inventing
# new identities.
KNOWN_AGENTS = {"claude", "codex", "gemini"}


ACTOR_FORM_RE = re.compile(r"^(human|process):\S+$|^[a-z0-9_-]+/\S+$")


def actor_for(edited_by: str | None) -> str:
    if not edited_by:
        return "process:wiki-ingest"
    name = edited_by.strip()
    if ACTOR_FORM_RE.match(name):
        return name  # already a well-formed actor string (human:<id>, process:<id>, tool/version)
    key = name.lower()
    if key in KNOWN_AGENTS:
        return f"{key}/unspecified"
    return f"process:{slugify(name)}"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def split_frontmatter(text: str) -> tuple[list, str]:
    """Return (frontmatter_lines, body) — frontmatter_lines is the raw list of
    'key: value' lines (order-preserving, comments dropped), body is everything after."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [], text
    raw = m.group(1)
    body = text[m.end():]
    lines = [line for line in raw.split("\n") if line.strip()]
    return lines, body


def parse_frontmatter_scalars(lines: list) -> dict:
    """Very small YAML-scalar-only parser: `key: value` pairs, no nesting/lists.
    Sufficient because every existing frontmatter block in this wiki is flat scalars."""
    out = {}
    for line in lines:
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            val = val[1:-1]
        out[key] = val
    return out


def get_title(body: str, fm: dict, fallback_slug: str) -> str:
    if fm.get("title"):
        return fm["title"]
    m = TITLE_RE.search(body)
    if m:
        return m.group(1).strip()
    return fallback_slug.replace("-", " ").title()


def build_title_index() -> dict:
    """Map 'folder/slug' -> display title for every content page, plus bare 'slug'
    when unambiguous, plus a few known root pages."""
    index = {}
    bare_counts = {}
    for folder in CONTENT_FOLDERS:
        d = WIKI_ROOT / folder
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            if p.stem == "index":
                continue
            text = p.read_text(encoding="utf-8")
            lines, body = split_frontmatter(text)
            fm = parse_frontmatter_scalars(lines)
            title = get_title(body, fm, p.stem)
            key = f"{folder}/{p.stem}"
            index[key] = title
            bare_counts[p.stem] = bare_counts.get(p.stem, 0) + 1

    for folder in CONTENT_FOLDERS:
        d = WIKI_ROOT / folder
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            if p.stem == "index":
                continue
            if bare_counts.get(p.stem) == 1:
                index[p.stem] = index[f"{folder}/{p.stem}"]

    # Root-level pages referenced by bare wikilinks (e.g. [[CLAUDE|CLAUDE.md]], [[log|...]])
    index["CLAUDE"] = "CLAUDE.md"
    index["log"] = "Ingest & edit log"
    index["index"] = "Learning Design Wiki"
    for folder in CONTENT_FOLDERS + ["sources"]:
        index[f"{folder}/index"] = folder.title()

    return index


def resolve_link_path(target: str) -> str:
    """Turn a wikilink target (e.g. 'claims/foo', 'CLAUDE', 'principles/index') into
    a bundle-relative OKF path (e.g. '/claims/foo.md', '/CLAUDE.md')."""
    target = target.strip()
    if "/" in target:
        folder, slug = target.split("/", 1)
        return f"/{folder}/{slug}.md"
    if target == "CLAUDE":
        return "/CLAUDE.md"
    if target in ("log", "index"):
        return f"/{target}.md"
    return f"/{target}.md"


def convert_wikilinks(text: str, title_index: dict) -> str:
    """Convert every [[target]] / [[target|Label]] wikilink in `text` to a standard
    markdown link, per OKF's cross-linking convention. Falls back to a title-cased
    label from the slug when the target isn't in the index (tolerating a link to a
    page that doesn't exist, per OKF's 'consumers must tolerate broken links')."""

    def _sub(m):
        target, label = m.group(1).strip(), m.group(2)
        path = resolve_link_path(target)
        if label:
            display = label
        elif target in title_index:
            display = title_index[target]
        else:
            bare = target.split("/")[-1]
            display = title_index.get(bare, bare.replace("-", " ").title())
        return f"[{display}]({path})"

    return WIKILINK_RE.sub(_sub, text)


CITATION_LINE_RE = re.compile(
    r"^-\s+(?P<citation>.+?)\s*\[(?:doi:)?[^\]]*\]\((?P<url>https?://[^\s)]+)\)\s*$"
)
YEAR_RE = re.compile(r"\((\d{4}[a-z]?)\)")


def _derive_id_and_author(citation: str) -> tuple[str, str | None]:
    """From a full APA-style citation string, derive a short id ('sweller-2010') and
    the lead-author string ('Sweller, J., & Cooper, G. A.'), when the year is findable."""
    ym = YEAR_RE.search(citation)
    if not ym:
        return slugify(" ".join(citation.split()[:5])), None
    year = ym.group(1)
    # Strip the sentence period before "(2022)" — but not when that period
    # belongs to a final initial, which in APA is the normal case:
    # "Koedinger, K. R. (2022)" has exactly one period and it is part of the
    # name. A bare rstrip(".") took it, so every author list ending in an
    # initial was recorded one character short. That only became visible when
    # a page carried both spellings at once.
    prefix = citation[: ym.start()].strip()
    if not re.search(r"(?:\b[A-Z]|\.)\.$", prefix):
        prefix = prefix.rstrip(".")
    lead_author = prefix.split(",")[0].strip()
    return slugify(f"{lead_author}-{year}"), prefix or None


def parse_key_sources(section_text: str) -> list:
    """Parse a '## Key Sources' bullet list into OKF sources[] entries.
    Skips bullets with no discoverable citation (e.g. '<!-- TODO -->')."""
    sources = []
    for line in section_text.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        m = CITATION_LINE_RE.match(line)
        if not m:
            continue
        citation = m.group("citation").strip().rstrip(".")
        url = m.group("url")
        sid, author = _derive_id_and_author(citation)
        entry = {"id": sid, "resource": url, "title": citation}
        if author:
            entry["author"] = author
        sources.append(entry)
    return sources


EVIDENCE_HEADING_RE = re.compile(r"^### (.+)$", re.MULTILINE)


def parse_evidence_sources(evidence_section: str) -> list:
    """Parse a claim page's '## Evidence' section: one '### Author Year' subsection
    per study, each starting with a full APA citation line containing a doi/URL link."""
    sources = []
    headings = list(EVIDENCE_HEADING_RE.finditer(evidence_section))
    for i, h in enumerate(headings):
        heading_text = h.group(1).strip()
        start = h.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(evidence_section)
        block = evidence_section[start:end]
        url_m = re.search(r"\((https?://[^\s)]+)\)", block)
        citation_m = re.search(r"^\s*\n?(.+?\(\d{4}[a-z]?\)\..+?)$", block, re.MULTILINE)
        # Anchor-stable id: matches the heading slug so existing `#author-year`
        # same-page anchor links from ## Subclaims keep working.
        sid = slugify(heading_text)
        entry = {"id": sid}
        if url_m:
            entry["resource"] = url_m.group(1)
        if citation_m:
            entry["title"] = citation_m.group(1).strip()
        else:
            entry["title"] = heading_text
        _, author = _derive_id_and_author(entry["title"])
        if author:
            entry["author"] = author
        entry.update(parse_evidence_codes(block))
        sources.append(entry)
    return sources


# The codes line under an evidence entry's citation. It is written two ways,
# and only one of them was handled at first:
#
#   `q3 · peer-reviewed experiment · i2 · medium effect · n=48`      one span
#   `q3 · peer-reviewed experiment` · `i2 · medium effect` · `n=48`  three spans
#
# The three-span form is the DOMINANT one — 108 entries against 22 — and a
# pattern requiring a single span captured q from both but i and n from only
# the 22, silently. It was written from one example page without checking
# which spelling the corpus actually used. So this now reads the codes line,
# takes every backtick span on it, and looks for each code independently:
# whichever way an author split the spans, the same three values come out.
_CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
_Q_RE = re.compile(r"(?:^|·)\s*q\s*([0-9?])(?![0-9A-Za-z])", re.I)
_I_RE = re.compile(r"(?:^|·)\s*i\s*([0-9?])(?![0-9A-Za-z])", re.I)
_N_RE = re.compile(r"(?:^|·)\s*n\s*=\s*([^·]*)", re.I)


def parse_evidence_codes(block: str) -> dict:
    """{q, i, n} from an evidence entry's codes line, omitting what is absent.

    The shorthand was designed to be read by an agent, and until recently an
    agent had to find it in prose. Mirroring it into `sources[]` puts it where
    the rest of the entry already is.

    A `?` is preserved rather than dropped. `q?` means somebody looked and
    could not establish the tier, which is a different statement from an entry
    with no q at all, and collapsing the two would lose the only record that
    the question was asked — the same distinction as `crossref_reachable:
    false` against a missing field."""
    out = {}
    for line in (block or "").split("\n"):
        spans = _CODE_SPAN_RE.findall(line)
        if not any(_Q_RE.search(sp) for sp in spans):
            continue          # not the codes line
        for sp in spans:
            for key, rx in (("q", _Q_RE), ("i", _I_RE)):
                m = rx.search(sp)
                if m and key not in out:
                    v = m.group(1)
                    out[key] = int(v) if v.isdigit() else v
            m = _N_RE.search(sp)
            if m and "n" not in out and m.group(1).strip():
                out["n"] = m.group(1).strip()
        break                 # first codes line wins
    return out


def get_section(body: str, heading: str) -> str | None:
    """Return the text under a '## Heading' (up to the next '##' or EOF), or None."""
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)", re.MULTILINE | re.DOTALL
    )
    m = pattern.search(body)
    return m.group(1) if m else None


def yaml_escape(s: str) -> str:
    # A leading `?` needs quoting: in value position YAML reads it as the
    # complex-mapping-key indicator and raises "mapping keys are not allowed
    # here". That matters because `q?`/`i?` are legal evidence codes — CLAUDE.md
    # keeps them deliberately, since "somebody looked and could not establish
    # it" is a different statement from an absent field — so `i: ?` is a value
    # this schema is *supposed* to produce. dump_frontmatter's comment already
    # claimed `?` was quoted here; it was not, and the first page to carry one
    # would have had its codes silently dropped by sync_evidence_codes' YAML
    # write gate. A `?` anywhere else in a string is harmless and stays bare.
    if re.search(r'[:#\[\]{}"\'|>*&!%@`]', s) or s.startswith("?") or s.strip() != s or s == "":
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def markdown_link(name: str, folder: str) -> str:
    """A standard OKF cross-link, replacing the old Obsidian wikilink() helper."""
    return f"[{name}](/{folder}/{slugify(name)}.md)"


def to_relative(target_path: str, from_folder: str | None) -> str:
    """Convert a bundle-root-absolute path ('/claims/foo.md', '/CLAUDE.md') into a path
    relative to the current file's location. `from_folder` is the current file's
    containing content folder ('principles', 'claims', ...), or None for a file that
    lives at the wiki root (index.md, log.md, CLAUDE.md, README.md). Every content
    folder is exactly one level deep, so the relative form is always one of:
    'slug.md' (same folder), '../folder/slug.md' (sibling folder), or 'folder/slug.md'
    / '../name.md' (to/from a root-level file)."""
    parts = target_path.lstrip("/").split("/", 1)
    if len(parts) == 1:
        return parts[0] if from_folder is None else f"../{parts[0]}"
    folder, rest = parts
    if from_folder is None:
        return f"{folder}/{rest}"
    if from_folder == folder:
        return rest
    return f"../{folder}/{rest}"


LINK_TARGET_RE = re.compile(r"(\]\()(/[^)\s]+\.md)(\))")


def relativize_links(text: str, from_folder: str | None) -> str:
    """Rewrite every bundle-root-absolute markdown link target in `text` to a path
    relative to a file located in `from_folder` (or the wiki root, if None)."""
    return LINK_TARGET_RE.sub(lambda m: m.group(1) + to_relative(m.group(2), from_folder) + m.group(3), text)


def relative_link(name: str, target_folder: str, from_folder: str | None) -> str:
    """Build a cross-link from a file in `from_folder` (or the wiki root, if None) to
    `name` in `target_folder`, already in relative form."""
    slug = slugify(name)
    return f"[{name}]({to_relative(f'/{target_folder}/{slug}.md', from_folder)})"


def append_log_entries(bullet_lines: list) -> None:
    """Insert one or more '* **Op**: ...' bullets under today's '## YYYY-MM-DD'
    heading in log.md (OKF's date-grouped, newest-first log convention),
    creating that heading if this is the first entry logged today."""
    log_path = WIKI_ROOT / "log.md"
    text = log_path.read_text(encoding="utf-8")
    today = date.today().isoformat()
    heading = f"## {today}"
    block = "\n".join(bullet_lines)

    if heading in text:
        idx = text.index(heading) + len(heading)
        rest = text[idx:].lstrip("\n")
        insert_at = idx + (len(text[idx:]) - len(rest))
        text = text[:insert_at] + block + "\n" + text[insert_at:]
    else:
        marker = "---\n"
        pos = text.index(marker) + len(marker)
        text = text[:pos] + f"\n{heading}\n\n{block}\n" + text[pos:]

    log_path.write_text(text, encoding="utf-8")


def append_manifest_entry(
    source_id: str,
    title: str,
    status: str,
    doi: str | None = None,
    reason: str | None = None,
    pages: list | None = None,
    citations: dict | None = None,
) -> None:
    """Append one line to sources/manifest.ndjson — the append-only record of every
    source article the ingest pipeline has reviewed, ingested or rejected, so
    external users can audit or search what's been covered without scanning
    tens of thousands of individual pages. See CLAUDE.md's Source Manifest
    section for the schema and query examples.

    status must be "ingested" or "rejected". `pages` is a list of
    bundle-relative page paths (e.g. "claims/foo.md") the source contributed
    to — required (non-empty) for "ingested", omitted for "rejected". `reason`
    is required for "rejected" (why it didn't contribute), omitted for
    "ingested".

    `citations` records what the citation gate found on the pages this source
    wrote — {"checked": bool, "removed": [...], "flagged": [...]}. Without it
    an "ingested" line says only that the pages were structurally valid, which
    is the weakest of the three gates and the one least likely to catch the
    defects that actually occur: a DOI that resolves to the wrong paper, or a
    correct DOI wearing an invented journal. "checked": false is written
    deliberately when the gate could not run (no network) so a later audit can
    tell an unverified ingest from a clean one, rather than both reading as a
    bare "ingested".
    """
    import json

    if status not in ("ingested", "rejected"):
        raise ValueError(f"status must be 'ingested' or 'rejected', got {status!r}")
    if status == "ingested" and not pages:
        raise ValueError("'pages' is required and must be non-empty when status='ingested'")
    if status == "rejected" and not reason:
        raise ValueError("'reason' is required when status='rejected'")

    entry = {
        "id": source_id,
        "title": title,
        "doi": doi,
        "reviewed_at": date.today().isoformat(),
        "status": status,
    }
    if status == "rejected":
        entry["reason"] = reason
    else:
        entry["pages"] = pages
        if citations is not None:
            entry["citations"] = citations

    manifest_path = WIKI_ROOT / "sources" / "manifest.ndjson"
    manifest_path.parent.mkdir(exist_ok=True)
    with manifest_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def add_verified_entry(fm_text: str, actor: str, at: str) -> str:
    """Append a `{by, at}` confirmation event to the frontmatter's `verified:` list,
    creating the list if this is the page's first verification. `fm_text` is the raw
    frontmatter block (between the `---` delimiters, as returned by text.split('---', 2)[1])."""
    entry = f"  - by: {yaml_escape(actor)}\n    at: {at}\n"
    if re.search(r"^verified:\s*$", fm_text, re.MULTILINE):
        # Insert the new entry right after the `verified:` line, before any existing entries.
        return re.sub(r"^(verified:\s*\n)", r"\1" + entry, fm_text, count=1, flags=re.MULTILINE)
    return fm_text.rstrip("\n") + f"\nverified:\n{entry}"


def dump_frontmatter(fm: dict) -> str:
    """Serialize an ordered dict of OKF frontmatter into a YAML block (no external
    yaml dependency needed — every value here is a scalar, string-list, or the two
    small nested shapes `generated` / `sources[]` we build ourselves)."""
    lines = ["---"]
    for key, val in fm.items():
        if val is None:
            continue
        if key == "generated":
            lines.append("generated:")
            lines.append(f"  by: {yaml_escape(val['by'])}")
            lines.append(f"  at: {yaml_escape(str(val['at']))}")
        elif key == "sources":
            if not val:
                continue
            lines.append("sources:")
            for src in val:
                lines.append(f"  - id: {yaml_escape(src['id'])}")
                for k in ("resource", "title", "author"):
                    if src.get(k):
                        lines.append(f"    {k}: {yaml_escape(src[k])}")
                # q/i/n from the entry's codes line — see parse_evidence_codes.
                # Emitted unquoted when numeric so a consumer gets an int, and
                # `?` quoted, since bare ? starts a YAML complex-key.
                for k in ("q", "i"):
                    if k in src:
                        v = src[k]
                        lines.append(f"    {k}: {v}" if isinstance(v, int)
                                     else f"    {k}: {yaml_escape(str(v))}")
                if src.get("n"):
                    lines.append(f"    n: {yaml_escape(str(src['n']))}")
        elif isinstance(val, list):
            if not val:
                continue
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {yaml_escape(str(item))}")
        else:
            lines.append(f"{key}: {yaml_escape(str(val))}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def iter_markdown_links(text: str):
    """Yield (start, end, dest, is_angle) for every ](...) link in `text`,
    matching the destination by paren BALANCE the way CommonMark does.

    A regex like r"\\]\\(([^)\\s]+\\.md)\\)" cannot do this: it stops at the
    first ')', so a link to a real page whose filename contains parentheses —
    "../strategies/project-based_learning_(pbl).md" — is captured truncated,
    or skipped entirely. lint.py's link check excluded those deliberately and
    therefore never saw them, while mkdocs could not resolve them either (a
    bare '(' in a destination breaks markdown parsing), so they rendered as
    dead literal text. 58 such links were live in the wiki when this was
    written, every one pointing at a file that exists.

    is_angle marks the <...> destination form, which is how a destination
    containing parens is written safely."""
    i = 0
    while True:
        i = text.find("](", i)
        if i == -1:
            return
        j = i + 2
        if j < len(text) and text[j] == "<":
            k = text.find(">", j)
            if k == -1:
                i += 2
                continue
            yield i, k + 2, text[j + 1:k], True
            i = k + 2
            continue
        depth, k = 1, j
        while k < len(text) and text[k] != "\n":
            if text[k] == "(":
                depth += 1
            elif text[k] == ")":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        if k < len(text) and depth == 0:
            yield i, k + 1, text[j:k], False
        i = j


def link_needs_angle_brackets(dest: str) -> bool:
    """A destination containing parens must use the <...> form (or be
    percent-encoded) to survive markdown parsing."""
    return ("(" in dest or ")" in dest) and not dest.startswith("<")
