"""
page_metadata.py — show a page's frontmatter on the rendered page.

mkdocs strips YAML frontmatter out of the rendered output entirely, so on the
docs site none of it is visible: not `status`, not who generated the page or
when, not whether a human has ever checked it, and not the `id` the
design-spec pipeline resolves the page by. The page-type banner exists
precisely because of that gap, and covers exactly one field of it.

This appends a collapsed **Page metadata** block to every content page. A
mkdocs hook rather than a plugin: `hooks:` is native config (mkdocs >= 1.4), so
this adds no dependency to requirements-docs.txt and nothing to install.

Two things it surfaces that are not simply a reprint of the YAML:

  * **the trust tier.** CLAUDE.md derives three tiers from `verified` —
    unverified / machine-confirmed / human-reviewed — and until now nothing
    rendered them. A reader could not tell whether a page had ever been
    checked by a person, which is the single most useful thing to know about
    an LLM-maintained wiki and the whole reason the field exists.
  * **`sources` as a count plus ids**, not a dumped list. Some pages carry
    thirty; printing them in full would bury the fields a reader came for,
    and the citations themselves are already in `## Key Sources` right above.
"""

from __future__ import annotations

# index.md and log.md carry no page frontmatter worth showing (index files are
# OKF-reserved and deliberately bare), and CLAUDE.md is the schema guide
# itself.
SKIP_BASENAMES = {"index.md", "log.md", "CLAUDE.md"}

# Rendered in this order when present. Anything else the page carries is shown
# afterwards in its own order, so a field added to the schema later appears
# without this list needing an edit — a panel that silently omits a new field
# is worse than one that shows it plainly.
FIELD_ORDER = ("type", "id", "aliases", "title", "description", "status",
               "grain_size", "author", "evidence_strength")

HIDE = {"generated", "verified", "sources", "template", "hide", "search", "nav_order"}


def _trust_tier(verified) -> str:
    """unverified | machine-confirmed | human-reviewed — see CLAUDE.md."""
    if not verified:
        return "unverified — no one has confirmed this page's content"
    entries = verified if isinstance(verified, list) else [verified]
    actors = [str((e or {}).get("by", "")) for e in entries if isinstance(e, dict)]
    if any(a.startswith("human:") for a in actors):
        who = ", ".join(a for a in actors if a.startswith("human:"))
        return f"human-reviewed — checked by {who}"
    return "machine-confirmed — recorded by a tool, not a person"


def _fmt(value) -> str:
    if isinstance(value, list):
        return ", ".join(f"`{v}`" for v in value) if value else "—"
    if isinstance(value, dict):
        return ", ".join(f"{k}: `{v}`" for k, v in value.items())
    text = str(value).strip()
    return f"`{text}`" if text else "—"


def _rows(meta: dict) -> list:
    rows = []
    for key in FIELD_ORDER:
        if key in meta and meta[key] not in (None, ""):
            rows.append((key, _fmt(meta[key])))
    for key, value in meta.items():
        if key in FIELD_ORDER or key in HIDE or value in (None, ""):
            continue
        rows.append((key, _fmt(value)))

    gen = meta.get("generated")
    if isinstance(gen, dict):
        rows.append(("generated", f"by `{gen.get('by', '?')}` on `{gen.get('at', '?')}`"))
    rows.append(("trust", _trust_tier(meta.get("verified"))))

    sources = meta.get("sources") or []
    if sources:
        ids = [str(s.get("id")) for s in sources if isinstance(s, dict) and s.get("id")]
        shown = ", ".join(f"`{i}`" for i in ids[:12])
        more = f" … and {len(ids) - 12} more" if len(ids) > 12 else ""
        rows.append(("sources", f"{len(sources)} — {shown}{more}" if ids else str(len(sources))))
    return rows


def on_page_markdown(markdown: str, page, config, files) -> str:
    if page.file.src_path.split("/")[-1] in SKIP_BASENAMES:
        return markdown
    meta = page.meta or {}
    if not meta.get("type"):
        return markdown          # not a content page

    rows = _rows(meta)
    lines = ["", "", '??? info "Page metadata"', "", "    | Field | Value |",
             "    |---|---|"]
    lines += [f"    | `{k}` | {v} |" for k, v in rows]
    lines += ["",
              "    Frontmatter is the page's machine-readable record — see the "
              "[Schema & Guide](../CLAUDE.md).", ""]
    return markdown + "\n".join(lines)
