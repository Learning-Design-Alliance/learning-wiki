#!/usr/bin/env python3
"""
build_indexes.py — Generate per-folder index pages and update the root index hub,
in Open Knowledge Format (OKF) v0.2 style.

index.md is a reserved OKF filename: no frontmatter except the bundle-root's
`okf_version`, plain markdown links (not wikilinks), and a bulleted
`* [Title](relative-url) - description` listing per section.

Produces:
  principles/index.md
  elements/index.md
  patterns/index.md
  strategies/index.md
  theories/index.md
  claims/index.md
  sources/index.md
  index.md  (hub pointing to folder indexes + summary counts, carries okf_version)

Usage:
    python3 scripts/build_indexes.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

WIKI_ROOT = ok.WIKI_ROOT

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


def get_page_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines, body = ok.split_frontmatter(text)
    fm = ok.parse_frontmatter_scalars(lines)
    return {
        "title": ok.get_title(body, fm, path.stem),
        "description": fm.get("description", ""),
        "status": fm.get("status", "draft"),
        "slug": path.stem,
    }


def bullet(page_type: str, p: dict) -> str:
    line = f"* [{p['title']}]({p['slug']}.md)"
    if p["description"]:
        line += f" - {p['description']}"
    return line


def build_folder_index(page_type: str, config: dict) -> str:
    folder = WIKI_ROOT / page_type
    pages = [get_page_meta(p) for p in sorted(folder.glob("*.md")) if p.stem != "index"]
    pages.sort(key=lambda x: x["title"].lower())

    by_status = {"stable": [], "review": [], "draft": []}
    for p in pages:
        status = p["status"] if p["status"] in by_status else "draft"
        by_status[status].append(p)

    lines = [
        f"# {config['label']}",
        "",
        config["description"],
        "",
        f"**{len(pages)} entries** · "
        f"{len(by_status['stable'])} stable · "
        f"{len(by_status['review'])} in review · "
        f"{len(by_status['draft'])} drafts",
        "",
        "---",
        "",
    ]

    if not pages:
        empty_guidance = {
            "theories": (
                "## How to add a theory\n\n"
                "Create a file in `theories/` using the Theory template in [CLAUDE.md](../CLAUDE.md).\n\n"
                "Examples of theories to add: Cognitive Load Theory, Self-Regulated Learning, "
                "Constructivism, Information Processing Theory, Situated Cognition, "
                "Dual Coding Theory, Worked Example Effect."
            ),
            "claims": (
                "## How to add a claim\n\n"
                "Create a file in `claims/` using the Claim template in [CLAUDE.md](../CLAUDE.md).\n\n"
                "Claims are empirical statements with evidence ratings. "
                "Each claim page needs: an ID (e.g. `CL-0001`), evidence strength, "
                "at least one source with a DOI, and links to any competing claims.\n\n"
                "Start by extracting claims from principle pages that have raw citations in their `### Claims` sections."
            ),
            "sources": (
                "## How to add a source\n\n"
                "Create a file in `sources/` using the Source template in [CLAUDE.md](../CLAUDE.md).\n\n"
                "Source pages are created when a claim or principle cites a specific paper or book. "
                "Each source page needs: full citation, DOI/URL, a 2–4 sentence summary, "
                "and links to claim pages the source supports."
            ),
        }
        guidance = empty_guidance.get(
            page_type, "## No entries yet\n\nUse the template in [CLAUDE.md](../CLAUDE.md) to add pages."
        )
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
                lines.append(bullet(page_type, p))
            lines.append("")
    else:
        lines.append("## All Entries")
        lines.append("")
        for p in pages:
            lines.append(bullet(page_type, p))
        lines.append("")

    return "\n".join(lines)


def build_root_index(counts: dict) -> str:
    type_links = []
    for page_type in ROOT_INDEX_TYPES:
        config = PAGE_TYPES.get(page_type, {})
        label = config.get("label", page_type.title())
        count = counts.get(page_type, {}).get("total", 0)
        type_links.append(f"[{label}]({page_type}/index.md) ({count})")
    type_line = ", ".join(type_links[:-1]) + f", and {type_links[-1]}"

    lines = [
        "---",
        'okf_version: "0.2"',
        "---",
        "",
        "# Learning Design Wiki",
        "",
        "A persistent, LLM-maintained knowledge base for learning design: "
        f"{type_line} — cross-linked and evidence-tagged. "
        "Read [CLAUDE.md](CLAUDE.md) for the schema, page templates, and agent operating instructions.",
        "",
        "---",
        "",
        "## Quick navigation",
        "",
        "* [Ingest & edit log](log.md)",
        "* [Schema & agent guide](CLAUDE.md)",
        "",
        "## How to use this wiki",
        "",
        "**As an agent**: read `CLAUDE.md` first. Use `index.md` as your entry point, "
        "follow the markdown links in each page to traverse the graph, and use `grep` for targeted search.",
        "",
        "**As a human**: browse the folder indexes above, or open the "
        "[docs site](https://learning-design-alliance.github.io/learning-wiki/). "
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
