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

CONTENT_FOLDERS = ["principles", "elements", "patterns", "strategies", "theories", "claims"]

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")
TITLE_RE = re.compile(r"^# (.+)$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

# Existing edited_by values are freeform names/tool labels already committed to the
# wiki's history (e.g. "Claude", "Codex", "David Porcaro"). Map them onto OKF's actor
# convention (`<producer>/<version>`, `human:<id>`, `process:<id>`) without inventing
# new identities.
KNOWN_AGENTS = {"claude", "codex", "gemini"}


def actor_for(edited_by: str | None) -> str:
    if not edited_by:
        return "process:wiki-ingest"
    key = edited_by.strip().lower()
    if key in KNOWN_AGENTS:
        return f"{key}/unspecified"
    return f"process:{slugify(edited_by)}"


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
    prefix = citation[: ym.start()].strip().rstrip(".")
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
        sources.append(entry)
    return sources


def get_section(body: str, heading: str) -> str | None:
    """Return the text under a '## Heading' (up to the next '##' or EOF), or None."""
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)", re.MULTILINE | re.DOTALL
    )
    m = pattern.search(body)
    return m.group(1) if m else None


def yaml_escape(s: str) -> str:
    if re.search(r'[:#\[\]{}"\'|>*&!%@`]', s) or s.strip() != s or s == "":
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def markdown_link(name: str, folder: str) -> str:
    """A standard OKF cross-link, replacing the old Obsidian wikilink() helper."""
    return f"[{name}](/{folder}/{slugify(name)}.md)"


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
