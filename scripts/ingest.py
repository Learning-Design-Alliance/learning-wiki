#!/usr/bin/env python3
"""
ingest.py — Batch-convert research_briefs CSVs into ld-wiki markdown pages.

Usage:
    python3 scripts/ingest.py [--dry-run] [--type principles|elements|patterns|strategies|all]

Writes pages to ../principles/, ../elements/, ../patterns/, ../strategies/
Updates ../index.md and ../log.md
"""

import csv
import os
import re
import sys
import argparse
from datetime import date
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────

WIKI_ROOT = Path(__file__).parent.parent
BRIEFS_ROOT = Path.home() / "research_briefs"
TODAY = date.today().isoformat()

CSV_FILES = {
    "principles": BRIEFS_ROOT / "learning database - Principles.csv",
    "elements":   BRIEFS_ROOT / "learning database - Elements.csv",
    "patterns":   BRIEFS_ROOT / "learning database - Patterns.csv",
    "strategies": BRIEFS_ROOT / "learning database - Strategies.csv",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert a display name to a filesystem-safe slug."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def wikilink(name: str, folder: str = "") -> str:
    """Return an Obsidian wikilink for a cross-reference."""
    slug = slugify(name)
    if folder:
        return f"[[{folder}/{slug}|{name}]]"
    return f"[[{slug}|{name}]]"


def comma_list_to_wikilinks(text: str, folder: str = "") -> list[str]:
    """Split a comma/semicolon-separated string and return wikilink list items."""
    if not text or not text.strip():
        return []
    items = re.split(r"[,;]+", text)
    return [f"- {wikilink(item.strip(), folder)}" for item in items if item.strip()]


def bullet_list(text: str) -> str:
    """Convert a raw multi-value field to a markdown bullet list string."""
    if not text or not text.strip():
        return "- "
    items = re.split(r"[,;]+", text)
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return "- "
    return "\n".join(f"- {item}" for item in cleaned)


def safe_field(row: dict, *keys: str) -> str:
    """Return first non-empty value from the given keys."""
    for key in keys:
        val = row.get(key, "").strip()
        if val:
            return val
    return ""


def write_page(path: Path, content: str, dry_run: bool = False) -> str:
    """Write a page if it doesn't exist; return 'created', 'exists', or 'dry-run'."""
    if dry_run:
        return "dry-run"
    if path.exists():
        return "exists"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "created"


# ── Page builders ─────────────────────────────────────────────────────────────

def build_principle(row: dict) -> tuple[str, str]:
    """Return (slug, markdown) for a principle row."""
    name = safe_field(row, "Name", "name")
    if not name or name.lower() in ("name", ""):
        return "", ""
    slug = slugify(name)

    theories = bullet_list(safe_field(row, "theories"))
    learner_factors = bullet_list(safe_field(row, "learner factors supported"))
    research = safe_field(row, "research support").strip()
    description = safe_field(row, "description").strip()

    # Build theory wikilinks
    theory_links = "\n".join(
        f"- {wikilink(t.strip(), 'theories')}"
        for t in re.split(r"[,;]+", safe_field(row, "theories"))
        if t.strip()
    )

    content = f"""---
type: principle
status: draft
last_edited: {TODAY}
---

# {name}

## Description
{description or "<!-- TODO: add description -->"}

## Implications

### Context
#### Requirements
- <!-- TODO -->
#### Constraints
- <!-- TODO -->

### Target Learners
{learner_factors or "- <!-- TODO -->"}

### Target Learning Objectives
- <!-- TODO -->

### Theory
#### Supporting
{theory_links or "- <!-- TODO -->"}
#### Contradicting / Qualifying
- <!-- TODO -->

### Claims
<!-- Link claims with evidence tags: [[claims/claim-slug]] [+M] -->
{("- " + research) if research else "- <!-- TODO -->"}

## Related Principles
- <!-- TODO -->

## Examples
<!-- Links to elements or patterns that apply this principle -->
- <!-- TODO -->

## Key Sources
- <!-- TODO -->
"""
    return slug, content.strip() + "\n"


def build_element(row: dict) -> tuple[str, str]:
    """Return (slug, markdown) for an element row."""
    name = safe_field(row, "", "Element", "name")
    if not name or name.lower() in ("element", ""):
        return "", ""
    slug = slugify(name)

    description = safe_field(row, "description", "Description").strip()
    related_raw = safe_field(row, "related_elements")
    objectives = safe_field(row, "objectives").strip()
    principles_raw = safe_field(row, "principles")
    target_audience = safe_field(row, "target_audience").strip()
    patterns_raw = safe_field(row, "pattern")

    related_links = "\n".join(
        f"- {wikilink(e.strip(), 'elements')}"
        for e in re.split(r"[,;]+", related_raw)
        if e.strip()
    )
    principle_links = "\n".join(
        f"- {wikilink(p.strip(), 'principles')}"
        for p in re.split(r"[,;]+", principles_raw)
        if p.strip()
    )
    pattern_links = "\n".join(
        f"- {wikilink(p.strip(), 'patterns')}"
        for p in re.split(r"[,;]+", patterns_raw)
        if p.strip()
    )

    content = f"""---
type: element
status: draft
last_edited: {TODAY}
---

# {name}

## Description
{description or "<!-- TODO: add description -->"}

## Design Implications

### Context
#### Requirements
- <!-- TODO -->
#### Constraints
- <!-- TODO -->

### Target Learners
<!-- Link to sub-claims: [[claims/claim-slug]] -->
{("- " + target_audience) if target_audience else "- <!-- TODO -->"}

### Target Learning Goals
<!-- Link to sub-claims: [[claims/claim-slug]] -->
{("- " + objectives) if objectives else "- <!-- TODO -->"}

### Affordances
<!-- Links to principles applied -->
{principle_links or "- <!-- TODO -->"}

## Related Elements
{related_links or "- <!-- TODO -->"}

## Patterns That Use This Element
{pattern_links or "- <!-- TODO -->"}

## Examples
<!-- Links to strategies that use this element, with ratings -->
- <!-- TODO -->

## Key Sources
- <!-- TODO -->
"""
    return slug, content.strip() + "\n"


def build_pattern(row: dict) -> tuple[str, str]:
    """Return (slug, markdown) for a pattern row."""
    name = safe_field(row, "name")
    if not name or name.lower() in ("name", ""):
        return "", ""
    slug = slugify(name)

    description = safe_field(row, "description").strip()
    author = safe_field(row, "author").strip()
    grain_size = safe_field(row, "grain_size").strip()
    elements_raw = safe_field(row, "elements")
    principles_raw = safe_field(row, "principles")
    goals = safe_field(row, "goals").strip()
    target_audience = safe_field(row, "target_audience").strip()
    affordances = safe_field(row, "affordances").strip()
    sequence = safe_field(row, "sequence").strip()
    personalization = safe_field(row, "personalization").strip()
    requirements = safe_field(row, "requirements").strip()
    limitations = safe_field(row, "limitations").strip()
    impact = safe_field(row, "impact").strip()
    examples = safe_field(row, "examples").strip()
    sources = safe_field(row, "sources").strip()

    element_links = "\n".join(
        f"- {wikilink(e.strip(), 'elements')}"
        for e in re.split(r"[,;]+", elements_raw)
        if e.strip()
    )
    principle_links = "\n".join(
        f"- {wikilink(p.strip(), 'principles')}"
        for p in re.split(r"[,;]+", principles_raw)
        if p.strip()
    )

    # Format sequence as numbered list if it looks like prose
    seq_formatted = sequence
    if sequence and not sequence.strip().startswith(("1.", "-")):
        seq_formatted = "- " + sequence

    content = f"""---
type: pattern
status: draft
last_edited: {TODAY}
author: {author}
grain_size: {grain_size}
---

# {name}

## Description
{description or "<!-- TODO: add description -->"}

## Implications

### Context
#### Requirements
{("- " + requirements) if requirements else "- <!-- TODO -->"}
#### Constraints
{("- " + limitations) if limitations else "- <!-- TODO -->"}
#### Grain Size
{grain_size or "<!-- TODO: program / course / unit / lesson -->"}

### Target Goals
<!-- Link to claims: [[claims/claim-slug]] -->
{("- " + goals) if goals else "- <!-- TODO -->"}

### Target Learners
<!-- Link to claims: [[claims/claim-slug]] -->
{("- " + target_audience) if target_audience else "- <!-- TODO -->"}

### Theory
#### Supporting
- <!-- TODO -->
#### Contradicting / Qualifying
- <!-- TODO -->

### Claims
#### Supporting
- <!-- TODO -->
#### Contradicting
- <!-- TODO -->

## Design

### Sequence
<!-- Steps with links to elements -->
{seq_formatted or "1. <!-- TODO -->"}

### Elements Used
{element_links or "- <!-- TODO -->"}

### Affordances
<!-- Links to principles applied -->
{principle_links or "- <!-- TODO -->"}
{("- " + affordances) if affordances and not principle_links else ""}

### Personalization
{("- " + personalization) if personalization else "- <!-- TODO -->"}

## Related Patterns
- <!-- TODO -->

## Examples
{("- " + examples) if examples else "- <!-- TODO -->"}

## Impact
{("- " + impact) if impact else "- <!-- TODO -->"}

## Key Sources
{("- " + sources) if sources else "- <!-- TODO -->"}
"""
    return slug, content.strip() + "\n"


def build_strategy(row: dict) -> tuple[str, str]:
    """Return (slug, markdown) for a strategy row."""
    name = safe_field(row, "name")
    if not name or name.lower() in ("name", ""):
        return "", ""

    # Prefer the provided id as slug, fall back to slugified name
    provided_id = safe_field(row, "id").strip()
    slug = provided_id if provided_id else slugify(name)

    description = safe_field(row, "description").strip()
    objectives = safe_field(row, "objectives").strip()
    target = safe_field(row, "target").strip()
    affordances = safe_field(row, "affordances").strip()
    personalization = safe_field(row, "personalization").strip()
    requirements = safe_field(row, "requirements").strip()
    limitations = safe_field(row, "limitations").strip()
    assessment_evidence = safe_field(row, "assessment_evidence").strip()
    impact = safe_field(row, "impact").strip()
    examples = safe_field(row, "examples").strip()
    elements_raw = safe_field(row, "elements")
    tools_raw = safe_field(row, "tools")
    related_elements_raw = safe_field(row, "related Elements")
    related_tools_raw = safe_field(row, "related Tools")

    element_links = "\n".join(
        f"- {wikilink(e.strip(), 'elements')}"
        for e in re.split(r"[,;]+", elements_raw)
        if e.strip()
    )
    related_element_links = "\n".join(
        f"- {wikilink(e.strip(), 'elements')}"
        for e in re.split(r"[,;]+", related_elements_raw)
        if e.strip()
    )

    content = f"""---
type: strategy
status: draft
last_edited: {TODAY}
---

# {name}

## Description
{description or "<!-- TODO: add description -->"}

## Design Implications

### Context
#### Requirements
{("- " + requirements) if requirements else "- <!-- TODO -->"}
#### Constraints
{("- " + limitations) if limitations else "- <!-- TODO -->"}
#### Implementation Variability
- <!-- TODO -->

### Target Learners
<!-- Link to sub-claims: [[claims/claim-slug]] -->
{("- " + target) if target else "- <!-- TODO -->"}

### Target Learning Goals
<!-- Link to sub-claims: [[claims/claim-slug]] -->
{("- " + objectives) if objectives else "- <!-- TODO -->"}

### Affordances
{("- " + affordances) if affordances else "- <!-- TODO -->"}

### Personalization
{("- " + personalization) if personalization else "- <!-- TODO -->"}

### Instructions
<!-- Steps with links to elements -->
{element_links or "- <!-- TODO -->"}

## Assessment Evidence
{("- " + assessment_evidence) if assessment_evidence else "- <!-- TODO -->"}

## Impact
{("- " + impact) if impact else "- <!-- TODO -->"}

## Related Strategies
- <!-- TODO -->

## Related Elements
{related_element_links or "- <!-- TODO -->"}

## Tools
{("- " + tools_raw) if tools_raw else "- <!-- TODO -->"}

## Examples
{("- " + examples) if examples else "- <!-- TODO -->"}

## Key Sources
- <!-- TODO -->
"""
    return slug, content.strip() + "\n"


# ── Ingest runners ────────────────────────────────────────────────────────────

def ingest_csv(
    csv_path: Path,
    page_type: str,
    builder,
    dry_run: bool = False,
) -> list[tuple[str, str, str]]:
    """
    Read a CSV, build pages, write them.
    Returns list of (name, slug, status) tuples.
    """
    folder = WIKI_ROOT / page_type
    results = []

    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug, content = builder(row)
            if not slug:
                continue
            name = slug.replace("-", " ").title()
            # Use actual name from content header
            m = re.search(r"^# (.+)$", content, re.MULTILINE)
            if m:
                name = m.group(1)
            path = folder / f"{slug}.md"
            status = write_page(path, content, dry_run)
            results.append((name, slug, status))

    return results


def update_index(entries_by_type: dict[str, list[tuple[str, str, str]]], dry_run: bool = False):
    """Regenerate index.md from current entries."""
    index_path = WIKI_ROOT / "index.md"

    # Read existing index to preserve manually added entries
    existing = {}
    if index_path.exists():
        existing_text = index_path.read_text(encoding="utf-8")
        # We'll overwrite — the ingest is the source of truth for stubs
        pass

    lines = [
        "# Learning Design Wiki — Index",
        "",
        f"Last updated: {TODAY}",
        "",
        "---",
        "",
    ]

    type_labels = {
        "principles": "Principles",
        "elements": "Elements",
        "patterns": "Patterns",
        "strategies": "Strategies",
        "theories": "Theories",
        "claims": "Claims",
        "sources": "Sources",
    }

    for page_type, label in type_labels.items():
        lines.append(f"## {label}")
        entries = entries_by_type.get(page_type, [])
        if not entries:
            # Scan folder for existing pages
            folder = WIKI_ROOT / page_type
            if folder.exists():
                for p in sorted(folder.glob("*.md")):
                    slug = p.stem
                    name = slug.replace("-", " ").title()
                    m = re.search(r"^# (.+)$", p.read_text(encoding="utf-8"), re.MULTILINE)
                    if m:
                        name = m.group(1)
                    entries.append((name, slug, "existing"))
        for name, slug, _status in sorted(entries, key=lambda x: x[0].lower()):
            lines.append(f"- [[{page_type}/{slug}|{name}]]")
        lines.append("")

    if not dry_run:
        index_path.write_text("\n".join(lines), encoding="utf-8")
    else:
        print("\n--- index.md preview ---")
        print("\n".join(lines[:40]))


def append_log(entries_by_type: dict[str, list[tuple[str, str, str]]], dry_run: bool = False):
    """Append a batch ingest entry to log.md."""
    log_path = WIKI_ROOT / "log.md"
    counts = {k: len([e for e in v if e[2] == "created"]) for k, v in entries_by_type.items()}
    total = sum(counts.values())
    if total == 0:
        return

    detail = "; ".join(f"{v} {k}" for k, v in counts.items() if v > 0)
    entry = f"\n## [{TODAY}] ingest | batch from research_briefs CSVs | {detail} pages created\n"

    if not dry_run:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry)
    else:
        print("\n--- log.md append ---")
        print(entry)


# ── Main ──────────────────────────────────────────────────────────────────────

BUILDERS = {
    "principles": (CSV_FILES["principles"], build_principle),
    "elements":   (CSV_FILES["elements"],   build_element),
    "patterns":   (CSV_FILES["patterns"],   build_pattern),
    "strategies": (CSV_FILES["strategies"], build_strategy),
}


def main():
    parser = argparse.ArgumentParser(description="Ingest research_briefs CSVs into ld-wiki")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument(
        "--type",
        choices=list(BUILDERS.keys()) + ["all"],
        default="all",
        help="Which CSV type(s) to ingest",
    )
    args = parser.parse_args()

    types_to_run = list(BUILDERS.keys()) if args.type == "all" else [args.type]

    entries_by_type: dict[str, list] = {}

    for page_type in types_to_run:
        csv_path, builder = BUILDERS[page_type]
        if not csv_path.exists():
            print(f"[SKIP] {csv_path} not found")
            continue
        print(f"[{page_type}] reading {csv_path.name} ...", end=" ", flush=True)
        results = ingest_csv(csv_path, page_type, builder, args.dry_run)
        created = sum(1 for _, _, s in results if s == "created")
        exists  = sum(1 for _, _, s in results if s == "exists")
        dry     = sum(1 for _, _, s in results if s == "dry-run")
        entries_by_type[page_type] = results
        print(f"{created} created, {exists} already exist, {dry} dry-run")

    print("\nUpdating index.md ...", end=" ", flush=True)
    update_index(entries_by_type, args.dry_run)
    print("done")

    print("Updating log.md ...", end=" ", flush=True)
    append_log(entries_by_type, args.dry_run)
    print("done")

    total_created = sum(
        sum(1 for _, _, s in v if s == "created")
        for v in entries_by_type.values()
    )
    print(f"\nDone. {total_created} pages written to {WIKI_ROOT}")


if __name__ == "__main__":
    main()
