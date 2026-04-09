#!/usr/bin/env python3
"""
build_indexes.py — Generate per-folder index pages and update the root index hub.

Produces:
  principles/index.md
  elements/index.md
  patterns/index.md
  strategies/index.md
  theories/index.md
  claims/index.md
  sources/index.md
  index.md  (hub pointing to folder indexes + summary counts)

Usage:
    python3 scripts/build_indexes.py
"""

import re
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
TODAY = date.today().isoformat()

PAGE_TYPES = {
    "principles": {
        "label": "Principles",
        "description": "Research-backed design commitments: what to do and why.",
        "status_field": True,
    },
    "elements": {
        "label": "Elements",
        "description": "Instructional building blocks — the components you compose into patterns.",
        "status_field": True,
    },
    "patterns": {
        "label": "Patterns",
        "description": "Reusable instructional designs at the lesson or unit level.",
        "status_field": True,
    },
    "strategies": {
        "label": "Strategies",
        "description": "Concrete teaching activity recipes — specific, implementable approaches.",
        "status_field": True,
        "list_drafts_in_index": False,
    },
    "theories": {
        "label": "Theories",
        "description": "Explanatory frameworks that ground principles and claims.",
        "status_field": True,
    },
    "claims": {
        "label": "Claims",
        "description": "Empirical claims with evidence ratings, sources, and competing views.",
        "status_field": True,
    },
    "sources": {
        "label": "Sources",
        "description": "Bibliographic source pages with DOI links and claim summaries.",
        "status_field": False,
    },
}

ROOT_INDEX_TYPES = ["principles", "elements", "patterns", "strategies", "theories", "claims"]

STATUS_RE = re.compile(r"^status:\s*(.+)$", re.MULTILINE)
TITLE_RE  = re.compile(r"^# (.+)$", re.MULTILINE)


def get_page_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title_m = TITLE_RE.search(text)
    status_m = STATUS_RE.search(text)
    return {
        "title": title_m.group(1) if title_m else path.stem.replace("-", " ").title(),
        "status": status_m.group(1).strip() if status_m else "draft",
        "slug": path.stem,
    }


def build_folder_index(page_type: str, config: dict) -> str:
    folder = WIKI_ROOT / page_type
    pages = []
    for p in sorted(folder.glob("*.md")):
        if p.stem == "index":
            continue
        meta = get_page_meta(p)
        pages.append(meta)

    pages.sort(key=lambda x: x["title"].lower())

    # Group by status if applicable
    by_status = {"stable": [], "review": [], "draft": []}
    for p in pages:
        status = p["status"] if p["status"] in by_status else "draft"
        by_status[status].append(p)

    lines = [
        f"---",
        f"type: index",
        f"title: {config['label']}",
        *((f"evidence_strength: n/a",) if page_type == "claims" else ()),
        f"last_edited: {TODAY}",
        f"---",
        f"",
        f"# {config['label']}",
        f"",
        config["description"],
        f"",
        f"**{len(pages)} entries** · "
        f"{len(by_status['stable'])} stable · "
        f"{len(by_status['review'])} in review · "
        f"{len(by_status['draft'])} drafts",
        f"",
        f"---",
        f"",
    ]

    if not pages:
        # Empty section — add a how-to note so it's clear what belongs here
        empty_guidance = {
            "theories": (
                "## How to add a theory\n\n"
                "Create a file in `theories/` using the Theory template in [[CLAUDE]].\n\n"
                "Examples of theories to add: Cognitive Load Theory, Self-Regulated Learning, "
                "Constructivism, Information Processing Theory, Situated Cognition, "
                "Dual Coding Theory, Worked Example Effect."
            ),
            "claims": (
                "## How to add a claim\n\n"
                "Create a file in `claims/` using the Claim template in [[CLAUDE]].\n\n"
                "Claims are empirical statements with evidence ratings. "
                "Each claim page needs: an ID (e.g. `CL-0001`), evidence strength, "
                "at least one source with a DOI, and links to any competing claims.\n\n"
                "Start by extracting claims from principle pages that have raw citations in their `### Claims` sections."
            ),
            "sources": (
                "## How to add a source\n\n"
                "Create a file in `sources/` using the Source template in [[CLAUDE]].\n\n"
                "Source pages are created when a claim or principle cites a specific paper or book. "
                "Each source page needs: full citation, DOI/URL, a 2–4 sentence summary, "
                "and links to claim pages the source supports."
            ),
        }
        guidance = empty_guidance.get(page_type, "## No entries yet\n\nUse the template in [[CLAUDE]] to add pages.")
        lines.append(guidance)
        lines.append("")
    elif config["status_field"]:
        for status_key, status_label in [("stable", "Stable"), ("review", "In Review"), ("draft", "Draft")]:
            if not by_status[status_key]:
                continue
            if status_key == "draft" and config.get("list_drafts_in_index") is False:
                lines.append(f"## {status_label}")
                lines.append("")
                lines.append(
                    f"{len(by_status['draft'])} draft entries are currently omitted from this section page "
                    f"to keep the index navigable. Browse the folder directly or promote pages to `review` "
                    f"as they are curated."
                )
                lines.append("")
                continue
            lines.append(f"## {status_label}")
            lines.append("")
            for p in by_status[status_key]:
                lines.append(f"- [[{page_type}/{p['slug']}|{p['title']}]]")
            lines.append("")
    else:
        lines.append("## All Entries")
        lines.append("")
        for p in pages:
            lines.append(f"- [[{page_type}/{p['slug']}|{p['title']}]]")
        lines.append("")

    return "\n".join(lines)


def build_root_index(counts: dict[str, dict]) -> str:
    lines = [
        "# Learning Design Wiki",
        "",
        f"*Last updated: {TODAY}*",
        "",
        "A persistent, LLM-maintained knowledge base for learning design. "
        "Read [[CLAUDE|CLAUDE.md]] for the schema, page templates, and agent operating instructions.",
        "",
        "---",
        "",
        "## Knowledge Types",
        "",
    ]

    for page_type in ROOT_INDEX_TYPES:
        config = PAGE_TYPES.get(page_type, {})
        label = config.get("label", page_type.title())
        desc = config.get("description", "")
        count = counts.get(page_type, {}).get("total", 0)
        stable = counts.get(page_type, {}).get("stable", 0)
        lines.append(f"### [[{page_type}/index|{label}]] ({count})")
        lines.append(f"{desc}")
        if stable:
            lines.append(f"*{stable} stable*")
        lines.append("")

    lines += [
        "---",
        "",
        "## Quick navigation",
        "",
        "- [[log|Ingest & edit log]]",
        "- [[CLAUDE|Schema & agent guide]]",
        "",
        "## How to use this wiki",
        "",
        "**As an agent**: read `CLAUDE.md` first. Use `index.md` as your entry point, "
        "follow links in wiki-link format to traverse the graph, and use `grep` for targeted search.",
        "",
        "**As a human**: open this vault in Obsidian or browse the folder indexes above. "
        "Evidence tags (**[+S]**, **[+M]**, **[~M]**, **[-W]**) indicate claim support strength. "
        "Pages marked `status: draft` are stubs; `review` pages need expert check; `stable` pages are reliable.",
        "",
    ]

    return "\n".join(lines)


def main():
    print(f"Building folder indexes from {WIKI_ROOT} ...\n")

    counts = {}

    for page_type, config in PAGE_TYPES.items():
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            folder.mkdir(parents=True)

        pages = [p for p in folder.glob("*.md") if p.stem != "index"]
        total = len(pages)

        by_status = {"stable": 0, "review": 0, "draft": 0}
        for p in pages:
            meta = get_page_meta(p)
            s = meta["status"] if meta["status"] in by_status else "draft"
            by_status[s] += 1

        counts[page_type] = {"total": total, **by_status}

        content = build_folder_index(page_type, config)
        index_path = folder / "index.md"
        index_path.write_text(content, encoding="utf-8")
        print(f"  [{page_type}/index.md] {total} entries "
              f"({by_status['stable']} stable / {by_status['review']} review / {by_status['draft']} draft)")

    root_content = build_root_index(counts)
    (WIKI_ROOT / "index.md").write_text(root_content, encoding="utf-8")
    print(f"\n  [index.md] root hub updated")

    total_pages = sum(c["total"] for c in counts.values())
    print(f"\nDone. {total_pages} content pages across {len(PAGE_TYPES)} types.")


if __name__ == "__main__":
    main()
