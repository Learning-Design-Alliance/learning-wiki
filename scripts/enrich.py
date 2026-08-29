#!/usr/bin/env python3
"""
enrich.py — Enrich ld-wiki stub pages using Claude or Gemini Flex API + CSV data.

Providers:
    anthropic  Uses Anthropic Batch API (submit/collect) or streaming (run).
               Set ANTHROPIC_API_KEY.

    gemini     Uses Gemini GenerateContent with service_tier=flex for 50% cost
               reduction. Handles 1–15 min queuing with 15-min client timeout
               and exponential backoff on 503/429. Set GEMINI_API_KEY.

Workflow:
    # Gemini Flex — process all draft pages of a type (recommended)
    python3 scripts/enrich.py run --type principles --provider gemini

    # Anthropic Batch — submit overnight job
    python3 scripts/enrich.py submit --type principles
    python3 scripts/enrich.py collect --type principles [--poll]

    # Test a few pages
    python3 scripts/enrich.py run --type principles --limit 3

    # Dry-run: show prompts without calling API
    python3 scripts/enrich.py run --type principles --limit 1 --dry-run

    # Show status of pending Anthropic batches
    python3 scripts/enrich.py status

Options:
    --type      principles | elements | patterns | strategies
    --provider  anthropic (default) | gemini
    --limit     Max pages to process (default: all for gemini, 3 for run)
    --model     anthropic: haiku (default) | sonnet
                gemini:    flash (default) | pro
    --overwrite Re-enrich pages already at status: review
    --dry-run   Preview prompts without calling API
    --poll      With collect: wait until batch completes (checks every 60s)
"""

import argparse
import concurrent.futures
import csv
import json
import os
import re
import sys
import threading
import time
from datetime import date
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

sys.path.insert(0, str(Path(__file__).parent.parent))  # for scripts.eval (openrouter_client, model_catalog)

# ── Paths ─────────────────────────────────────────────────────────────────────

WIKI_ROOT   = Path(__file__).parent.parent
BRIEFS_ROOT = Path.home() / "research_briefs"
BATCHES_DIR = Path(__file__).parent / "batches"
TODAY       = date.today().isoformat()

CSV_FILES = {
    "principles": BRIEFS_ROOT / "learning database - Principles.csv",
    "elements":   BRIEFS_ROOT / "learning database - Elements.csv",
    "patterns":   BRIEFS_ROOT / "learning database - Patterns.csv",
    "strategies": BRIEFS_ROOT / "learning database - Strategies.csv",
}

MODELS = {
    "haiku":  "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-5",
}

GEMINI_MODELS = {
    "flash-lite": "gemini-3.1-flash-lite-preview",  # cheapest, Flex-eligible, default
    "flash":      "gemini-2.5-flash",
    "pro":        "gemini-2.5-pro",
}

# --provider openrouter: any OpenRouter model slug works via --model, not just
# these — this is just the default. z-ai/glm-5.3-flash is the only GLM slug
# actually verified in this project (see model_catalog.py's MODEL_DESCRIPTIONS
# and its reasoning_effort_for()/needs_reasoning_disabled() tuning from the
# eval harness work) — don't substitute an unverified "GLM 5.6" or similar
# without confirming the exact slug against OpenRouter's own model list first.
OPENROUTER_DEFAULT_MODEL = "z-ai/glm-5.3-flash"

# Gemini Flex: requests may queue 1–15 min; use 15-min client timeout.
# Retry on 503 (capacity shed) and 429 (rate limit) with exponential backoff.
GEMINI_FLEX_TIMEOUT_MS  = 900_000   # 15 minutes in milliseconds
GEMINI_FLEX_MAX_RETRIES = 6
GEMINI_FLEX_BACKOFF_BASE = 30       # seconds; doubles each retry

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def get_page_status(path: Path) -> str:
    """Read the status field from a page's frontmatter."""
    try:
        content = path.read_text(encoding="utf-8")
        m = re.search(r"^status:\s*(\S+)", content, re.MULTILINE)
        return m.group(1) if m else "draft"
    except Exception:
        return "draft"


def get_wiki_slugs() -> dict[str, list[str]]:
    """Return {folder: [slug, ...]} for all existing wiki pages."""
    result: dict[str, list[str]] = {}
    for folder in ("principles", "elements", "patterns", "strategies", "theories", "claims"):
        folder_path = WIKI_ROOT / folder
        if folder_path.exists():
            result[folder] = [p.stem for p in sorted(folder_path.glob("*.md"))
                              if p.stem != "index"]
    return result


def format_slug_list(wiki_slugs: dict[str, list[str]]) -> str:
    """Format existing slugs as a compact reference for the model."""
    lines = []
    for folder, slugs in wiki_slugs.items():
        lines.append(f"{folder}/: " + ", ".join(slugs[:30]))
        if len(slugs) > 30:
            lines[-1] += f" ... (+{len(slugs)-30} more)"
    return "\n".join(lines)


def read_csv_lookup(csv_path: Path, name_col: str) -> dict[str, dict]:
    """Read CSV and return {slug: row_dict}."""
    lookup: dict[str, dict] = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get(name_col, "").strip()
            if not name or name.lower() in (name_col.lower(), ""):
                continue
            # Skip obviously malformed rows
            if name.startswith("{") or name.startswith('"'):
                continue
            slug = slugify(name)
            if slug:
                lookup[slug] = row
    return lookup


def write_enriched_page(path: Path, content: str) -> None:
    """Write enriched content; ensure status/generated are set (OKF style)."""
    content = re.sub(r"^status:\s*.+$", "status: review", content, flags=re.MULTILINE)
    generated_block = f'generated:\n  by: "claude/unspecified"\n  at: {TODAY}'
    if re.search(r"^generated:\s*\n\s+by:.*\n\s+at:.*$", content, re.MULTILINE):
        content = re.sub(r"^generated:\s*\n\s+by:.*\n\s+at:.*$", generated_block, content, flags=re.MULTILINE)
    else:
        content = re.sub(r"^(status:\s*.+)$", r"\1\n" + generated_block, content, count=1, flags=re.MULTILINE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _post_batch_checks(written_files: list[str]) -> None:
    """Run lint's broken-link check and the citation-consistency check,
    restricted to just this batch's freshly written pages, and print
    whatever they find. Informational only — never fails the run. Added
    after a manual review of the first --provider openrouter batch found a
    broken cross-folder link and a DOI cited two different ways for the
    same paper across two pages; neither is visible from reading one page
    at a time, so this runs automatically instead of relying on a human
    to remember to check."""
    if not written_files:
        return
    touched = set(written_files)

    import lint
    link_issues = [i for i in lint.check_broken_links(lint.all_pages()) if i["file"] in touched]
    print(f"\n[post-batch check] Broken links in this batch: {len(link_issues)}")
    for issue in link_issues:
        print(f"  {issue['file']}: {issue['detail']}")

    import check_citations
    conflicts = check_citations.find_conflicts(check_citations.load_all_citations(), touched)
    print(f"[post-batch check] Citation conflicts touching this batch: {len(conflicts)}")
    if conflicts:
        print(check_citations.format_report(conflicts))


def append_log(entries: list) -> None:
    """Append enrichment entries to log.md, OKF date-grouped style."""
    bullets = [f"* **Enrich**: {name} — enriched from {page_type} CSV via Claude" for page_type, name in entries]
    if bullets:
        ok.append_log_entries(bullets)


# ── Prompt builders ───────────────────────────────────────────────────────────

PRINCIPLE_TEMPLATE = """\
---
type: principle
title: [Principle Name]
description: [One-line summary of the recommendation]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
---

# [Principle Name]

## Description
[What this principle is and what it recommends — 2-4 sentences.]

## Implications

[1-2 sentence paragraph connecting the principle to learning science, citing related theories.]

### Context
#### Requirements
- [concrete prerequisites for applying this principle]

#### Constraints
- [conditions where this principle is less effective or could backfire]

### Target Learners
- [who benefits most, with specifics]

### Target Learning Objectives
- [types of learning goals this principle serves]

### Theory
#### Supporting
- [Theory Name](../theories/slug.md) — brief explanation of the connection
#### Contradicting / Qualifying
- [or leave as "- None identified"]

### Claims
<!-- Link claims with evidence tags: [Claim](../claims/claim-slug.md) [+M] -->
- <!-- TODO: add claim links when evidence pages exist -->

## Related Principles
- [Related Principle Name](slug.md)

## Examples
<!-- Links to elements or patterns that apply this principle -->
- [Element Name](../elements/slug.md) or [Pattern Name](../patterns/slug.md) — brief note on how it applies

## Key Sources
- [APA citation with DOI link if available]
"""

ELEMENT_TEMPLATE = """\
---
type: element
title: [Element Name]
description: [One-line summary of what this element is]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
---

# [Element Name]

## Description
[What this instructional element is; how it functions — 2-3 sentences.]

## Design Implications

[1-2 sentence overview of how this element supports learning.]

### Context
#### Requirements
- [what must be in place for this element to work]

#### Constraints
- [conditions where this element is less effective]

### Target Learners
<!-- Link to sub-claims: [Claim](../claims/claim-slug.md) -->
- [who benefits most]

### Target Learning Goals
<!-- Link to sub-claims: [Claim](../claims/claim-slug.md) -->
- [types of objectives this element serves]

### Affordances
<!-- Links to principles applied: [Principle](../principles/principle-slug.md) -->
- [Principle Name](../principles/slug.md) — [how this element enacts that principle]

## Related Elements
- [Related Element](slug.md)

## Examples
<!-- Links to strategies that use this element -->
- [Strategy or product name] — brief description

## Key Sources
- [APA citation with DOI link if available]
"""

PATTERN_TEMPLATE = """\
---
type: pattern
title: [Pattern Name]
description: [One-line summary of what this pattern is]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
author: {author}
grain_size: {grain_size}
---

# [Pattern Name]

## Description
[What this pattern is; how it works; what problem it solves — 3-4 sentences.]

## Implications

[1-2 sentence paragraph on the learning science grounding.]

### Context
#### Requirements
- [prerequisites]

#### Constraints
- [limitations]

#### Grain Size
[program / course / unit / lesson]

### Target Goals
<!-- Link to claims -->
- [learning objectives this pattern is best suited for]

### Target Learners
<!-- Link to claims -->
- [who this pattern was designed for]

### Theory
#### Supporting
- [Theory Name](../theories/slug.md) — brief explanation
#### Contradicting / Qualifying
- [or "- None identified"]

### Claims
#### Supporting
- <!-- TODO: add claim links when evidence pages exist -->
#### Contradicting
- <!-- TODO -->

## Design

### Sequence
<!-- Steps with links to elements -->
1. [Step] — [Element Name](../elements/slug.md)

### Affordances
<!-- Links to principles applied -->
- [Principle Name](../principles/slug.md) — [how the pattern applies this principle]

### Personalization
- [how to adapt for different learners]

## Related Patterns
- [Related Pattern](slug.md)

## Examples
- [Concrete example with context]

## Key Sources
- [APA citation with DOI link if available]
"""

STRATEGY_TEMPLATE = """\
---
type: strategy
title: [Strategy Name]
description: [One-line summary of what this strategy is]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
---

# [Strategy Name]

## Description
[What this strategy is and how it is carried out — 2-3 sentences.]

## Design Implications

[1-2 sentence overview connecting to learning science.]

### Context
#### Requirements
- [what is needed to implement this strategy]

#### Constraints
- [conditions where effectiveness drops]

#### Implementation Variability
- [variations or adaptations]

### Target Learners
<!-- Link to sub-claims: [Claim](../claims/claim-slug.md) -->
- [who benefits most]

### Target Learning Goals
<!-- Link to sub-claims: [Claim](../claims/claim-slug.md) -->
- [types of objectives served]

### Instructions
1. [Step with links to elements: [Element](../elements/slug.md)]

## Related Strategies
- [Related Strategy](slug.md)

## Examples
- [Concrete example in a real context]

## Key Sources
- [APA citation with DOI link if available]
"""

TEMPLATES = {
    "principles": PRINCIPLE_TEMPLATE,
    "elements":   ELEMENT_TEMPLATE,
    "patterns":   PATTERN_TEMPLATE,
    "strategies": STRATEGY_TEMPLATE,
}

SYSTEM_PROMPT = """\
You are a learning design wiki editor. Write authoritative, well-sourced wiki pages for learning design concepts.

Use the CSV data, slug list, and exemplar as your inputs. Draw freely on your knowledge of the educational psychology
and instructional design literature to produce pages that a practitioner would find genuinely useful.

## Evidence tags

Use these inline in prose wherever a claim is referenced. The tag describes the direction of the effect on the
page's topic:

| Tag  | Meaning |
|------|---------|
| [+S] | Supports — strong (consistent experimental/meta-analytic) |
| [+M] | Supports — moderate |
| [+W] | Supports — weak / emerging |
| [~S],[~M],[~W] | Contextual/mixed — effect depends on conditions |
| [-S],[-M],[-W] | Contradicts or reduces effectiveness |
| [X]  | Contradicted / discredited |

**Direction rule:** Claims in a Constraints section MUST use [-] or [~], never [+].
A constraint describes a condition where the approach fails — the tag must reflect that direction.

Always link to a claim page when one exists: [Display Name](../claims/slug.md) [+M]

## Rules

1. Match the exemplar exactly in density, structure, and voice.
2. Follow the template structure — same headings, same order.
3. Cross-links: relative markdown links only — [Display Name](slug.md) for a page in the SAME folder,
   [Display Name](../folder/slug.md) for a page in a DIFFERENT folder. Never use the absolute
   /folder/slug.md form — this wiki resolves links relative to the linking page, and an absolute
   link breaks.
   IMPORTANT: Only use slugs that appear verbatim in the provided slug list.
   Never invent or guess a slug. Write plain text if a page doesn't exist yet.
4. Embed claim tags inline in prose — in Description, Implications, Constraints, Target Learners — not only
   in a separate Claims list.
5. Be succinct. Every sentence should carry weight. Avoid preamble and generic framing.
6. Key Sources: 3–5 real peer-reviewed sources in APA format with DOI hyperlinks. Only cite sources you are
   confident exist. Omit DOI if uncertain rather than guessing. If a source is one you'd expect to
   already be cited elsewhere in this wiki (a well-known meta-analysis or seminal paper), use the exact
   DOI you would use anywhere else for that same paper — never vary the DOI, or include it on one page
   and drop it on another, for what is the same citation.
7. Examples: use real named platforms, programs, or published curricula with URLs where they exist.
8. Related items: one-line explanation per entry ("— why it matters here").
9. Constraints: specific research-grounded conditions, not generic hedges.
10. Output ONLY the enriched markdown. No commentary, no code fences.
"""

# ── Type-specific exemplar pages ──────────────────────────────────────────────
# Each entry maps a page type to a path (relative to WIKI_ROOT) that serves
# as the gold-standard quality exemplar for that type.

EXEMPLAR_PAGES = {
    "elements":   "elements/demonstration.md",
    "principles": "principles/worked-examples.md",
    "patterns":   "patterns/cognitive-apprenticeship.md",
    "claims":     "claims/worked-examples-example-problem-sequences.md",
    "theories":   "theories/cognitive-load-theory.md",
    "strategies": "elements/demonstration.md",   # fallback until a strategy exemplar exists
}


def load_exemplar(page_type: str) -> str:
    """Read the gold-standard exemplar page for this type, or return empty string."""
    rel = EXEMPLAR_PAGES.get(page_type)
    if not rel:
        return ""
    path = WIKI_ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_user_prompt(
    page_type: str,
    name: str,
    csv_row: dict,
    current_stub: str,
    wiki_slugs: dict[str, list[str]],
) -> str:
    template = TEMPLATES[page_type].replace("{TODAY}", TODAY)

    # Add author/grain_size substitutions for patterns
    if page_type == "patterns":
        template = template.replace("{author}", csv_row.get("author", "").strip())
        template = template.replace("{grain_size}", csv_row.get("grain_size", "").strip())

    slug_ref = format_slug_list(wiki_slugs)

    # Format CSV row as readable block
    csv_block = "\n".join(
        f"{k}: {v.strip()[:500]}" for k, v in csv_row.items() if v and v.strip()
    )

    exemplar = load_exemplar(page_type)
    exemplar_block = f"""## Gold-standard exemplar — match this quality exactly:

{exemplar}

---
""" if exemplar else ""

    return f"""## Page to enrich: {name}

{exemplar_block}## Template structure to follow:
{template}

## Existing wiki slugs for cross-linking:
{slug_ref}

## CSV source data:
{csv_block}

## Current draft stub:
{current_stub}

Write the complete enriched page for "{name}" following the template structure and matching the exemplar's density, depth, and wikilink style."""


# ── Page discovery ─────────────────────────────────────────────────────────────

NAME_COLS = {
    "principles": "Name",
    "elements":   "",       # blank header — actual name is in unnamed first col
    "patterns":   "name",
    "strategies": "name",
}


def get_element_name(row: dict) -> str:
    """Elements CSV has a blank first column header."""
    # Try the blank key, then 'Element', then first value
    for key in ("", "Element", "element"):
        val = row.get(key, "").strip()
        if val and val.lower() not in ("element", ""):
            return val
    # Fall back: first non-empty value
    for val in row.values():
        if val and val.strip().lower() not in ("element", "description"):
            return val.strip()
    return ""


def get_name(page_type: str, row: dict) -> str:
    if page_type == "elements":
        return get_element_name(row)
    col = NAME_COLS[page_type]
    return row.get(col, "").strip()


def _has_unfilled_todo(path: Path) -> bool:
    """Whether this page still has a literal <!-- TODO --> placeholder left
    over from the original page-template scaffolding."""
    try:
        return "<!-- TODO -->" in path.read_text(encoding="utf-8")
    except OSError:
        return False


def find_pages_to_enrich(page_type: str, overwrite: bool, limit: Optional[int]) -> list[tuple[Path, dict, str]]:
    """
    Return list of (page_path, csv_row, page_name) for stubs that need enrichment.

    A page qualifies if it's status: draft (never enriched at all), OR it's
    status: review/stable but still has a leftover <!-- TODO --> placeholder.
    That second case used to be skipped unconditionally unless --overwrite —
    but the bulk CSV ingest (generated.by: process:wiki-ingest) left the vast
    majority of its pages exactly there: promoted straight to "review" with
    whole sections (Related Strategies, Key Sources, Tools, Examples, ...)
    never actually filled in (1,719 of 2,119 wiki pages, as of 2026-08-29).
    --overwrite still means what it always did: re-process a page regardless,
    even one with no remaining TODOs at all.
    """
    csv_path = CSV_FILES[page_type]
    if not csv_path.exists():
        print(f"[ERROR] CSV not found: {csv_path}")
        return []

    # Build CSV lookup
    lookup: dict[str, dict] = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = get_name(page_type, row)
            if not name or name.startswith("{") or name.startswith('"'):
                continue
            slug = slugify(name)
            if slug:
                lookup[slug] = row

    folder = WIKI_ROOT / page_type
    results = []

    for slug, row in lookup.items():
        page_path = folder / f"{slug}.md"
        if not page_path.exists():
            continue  # stub doesn't exist yet (run ingest.py first)

        status = get_page_status(page_path)
        if status in ("review", "stable") and not overwrite and not _has_unfilled_todo(page_path):
            continue  # already curated, nothing left to fill in

        name = get_name(page_type, row)
        results.append((page_path, row, name))

        if limit and len(results) >= limit:
            break

    return results


# ── Batch API ─────────────────────────────────────────────────────────────────

def cmd_submit(args: argparse.Namespace) -> None:
    """Prepare and submit a batch to Anthropic."""
    try:
        import anthropic
    except ImportError:
        print("[ERROR] anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[ERROR] ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    model = MODELS.get(args.model, MODELS["haiku"])
    pages = find_pages_to_enrich(args.type, args.overwrite, args.limit)
    if not pages:
        print(f"No draft pages found for type={args.type}. "
              f"Run ingest.py first, or use --overwrite to re-enrich review pages.")
        return

    wiki_slugs = get_wiki_slugs()
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)

    client = anthropic.Anthropic(api_key=api_key)

    requests = []
    for page_path, csv_row, name in pages:
        current_stub = page_path.read_text(encoding="utf-8")
        user_prompt = build_user_prompt(args.type, name, csv_row, current_stub, wiki_slugs)
        slug = page_path.stem

        requests.append({
            "custom_id": f"{args.type}/{slug}",
            "params": {
                "model": model,
                "max_tokens": 4000,
                "system": SYSTEM_PROMPT,
                "messages": [{"role": "user", "content": user_prompt}],
            },
        })

    print(f"Submitting batch: {len(requests)} pages, model={model}")

    batch = client.messages.batches.create(
        requests=[
            anthropic.types.message_create_params.Request(
                custom_id=r["custom_id"],
                params=anthropic.types.message_create_params.MessageCreateParamsNonStreaming(
                    **r["params"]
                ),
            )
            for r in requests
        ]
    )

    batch_id = batch.id
    id_file = BATCHES_DIR / f"batch_id_{args.type}.txt"
    id_file.write_text(f"{batch_id}\n{model}\n{len(requests)}\n")
    print(f"Batch submitted: {batch_id}")
    print(f"Saved to: {id_file}")
    print(f"Run: python3 scripts/enrich.py collect --type {args.type} --poll")


def cmd_collect(args: argparse.Namespace) -> None:
    """Collect batch results and write enriched pages."""
    try:
        import anthropic
    except ImportError:
        print("[ERROR] anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[ERROR] ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    id_file = BATCHES_DIR / f"batch_id_{args.type}.txt"
    if not id_file.exists():
        print(f"[ERROR] No batch ID found for type={args.type}. Run submit first.")
        sys.exit(1)

    lines = id_file.read_text().strip().splitlines()
    batch_id = lines[0]
    client = anthropic.Anthropic(api_key=api_key)

    # Poll until done
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        print(f"Batch {batch_id}: {batch.processing_status} "
              f"(succeeded={batch.request_counts.succeeded}, "
              f"errored={batch.request_counts.errored}, "
              f"in_progress={batch.request_counts.in_progress})")

        if batch.processing_status == "ended":
            break
        if not args.poll:
            print("Batch not done yet. Re-run with --poll to wait, or check again later.")
            return
        print("Waiting 60s...")
        time.sleep(60)

    # Process results
    written = []
    written_files = []
    errors = []
    folder = WIKI_ROOT / args.type

    for result in client.messages.batches.results(batch_id):
        slug = result.custom_id.split("/", 1)[-1]
        page_path = folder / f"{slug}.md"

        if result.result.type == "succeeded":
            content = result.result.message.content[0].text
            write_enriched_page(page_path, content)
            written.append((args.type, slug))
            written_files.append(str(page_path.relative_to(WIKI_ROOT)))
            print(f"  [OK] {slug}")
        else:
            errors.append(slug)
            print(f"  [ERROR] {slug}: {result.result.type}")

    if written:
        append_log(written)
    print(f"\nDone: {len(written)} written, {len(errors)} errors")
    _post_batch_checks(written_files)

    # Clean up batch ID file
    id_file.unlink(missing_ok=True)


def cmd_status(args: argparse.Namespace) -> None:
    """Show status of pending batches."""
    try:
        import anthropic
    except ImportError:
        print("[ERROR] anthropic package not installed.")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[ERROR] ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    BATCHES_DIR.mkdir(parents=True, exist_ok=True)
    id_files = list(BATCHES_DIR.glob("batch_id_*.txt"))
    if not id_files:
        print("No pending batches.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    for id_file in id_files:
        batch_id = id_file.read_text().strip().splitlines()[0]
        batch = client.messages.batches.retrieve(batch_id)
        print(f"{id_file.stem}: {batch_id} — {batch.processing_status} "
              f"(done={batch.request_counts.succeeded}, "
              f"err={batch.request_counts.errored}, "
              f"pending={batch.request_counts.in_progress})")


# ── Gemini Flex call ──────────────────────────────────────────────────────────

def call_gemini_flex(client, model: str, system_prompt: str, user_prompt: str) -> str:
    """
    Call Gemini GenerateContent with service_tier=flex and Google Search grounding.
    Retries on 503/429 with exponential backoff.
    Timeout: 15 minutes (Flex requests may queue 1–15 min).
    """
    from google.api_core import exceptions as gexc
    from google.genai import types

    delay = GEMINI_FLEX_BACKOFF_BASE
    for attempt in range(1, GEMINI_FLEX_MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[types.Tool(google_search=types.GoogleSearch())],
                    service_tier="flex",
                    max_output_tokens=4000,
                    http_options={"timeout": GEMINI_FLEX_TIMEOUT_MS},
                ),
            )
            return response.text

        except (gexc.ServiceUnavailable, gexc.ResourceExhausted) as e:
            if attempt == GEMINI_FLEX_MAX_RETRIES:
                raise
            print(f"  [retry {attempt}/{GEMINI_FLEX_MAX_RETRIES}] {type(e).__name__} — "
                  f"waiting {delay}s before retry...")
            time.sleep(delay)
            delay = min(delay * 2, 300)   # cap at 5 minutes

        except Exception as e:
            raise


# ── Missing page creation ─────────────────────────────────────────────────────

def _stub(page_type: str, extra: str = "") -> str:
    return (
        f"---\ntype: {page_type}\ntitle: {{name}}\nstatus: draft\n"
        f"generated:\n  by: \"process:wiki-ingest\"\n  at: {{today}}\n{extra}---\n\n# {{name}}\n"
    )


STUB_TEMPLATES = {
    "elements":   _stub("element"),
    "principles": _stub("principle"),
    "patterns":   _stub("pattern"),
    "strategies": _stub("strategy"),
    "theories":   _stub("theory"),
    "claims":     _stub("claim", extra="id: \nevidence_strength:\n"),
}

STUB_FOLDERS = set(STUB_TEMPLATES.keys())


def parse_wikilinks(content: str, current_folder: str = None) -> list[tuple[str, str]]:
    """Return [(folder, slug), ...] for markdown links in content: the legacy
    OKF absolute form (/folder/slug.md), the cross-folder relative form
    (../folder/slug.md), and — when current_folder is given — same-folder
    relative links (slug.md) resolved against it. The prompt now tells the
    model to emit relative links only (per CLAUDE.md's convention), so the
    absolute-form match is kept only for old content that might still use it."""
    links: list[tuple[str, str]] = []
    for m in re.finditer(r'\]\(/([a-z]+)/([a-z0-9_-]+)\.md\)', content):
        links.append((m.group(1), m.group(2)))
    for m in re.finditer(r'\]\(\.\./([a-z]+)/([a-z0-9_-]+)\.md\)', content):
        links.append((m.group(1), m.group(2)))
    if current_folder:
        for m in re.finditer(r'\]\((?<!/)([a-z0-9_-]+)\.md\)', content):
            links.append((current_folder, m.group(1)))
    return links


def create_missing_stubs(content: str, current_folder: str = None) -> list[str]:
    """
    Scan content for wikilinks (see parse_wikilinks). For any that don't have
    a corresponding file, create a minimal draft stub. Returns list of created paths.
    """
    created = []
    seen = set()

    for folder, slug in parse_wikilinks(content, current_folder):
        if folder not in STUB_FOLDERS:
            continue
        key = (folder, slug)
        if key in seen:
            continue
        seen.add(key)

        page_path = WIKI_ROOT / folder / f"{slug}.md"
        if page_path.exists():
            continue

        # Derive a display name from the slug
        name = slug.replace("-", " ").title()
        stub = STUB_TEMPLATES[folder].format(today=TODAY, name=name)
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(stub, encoding="utf-8")
        created.append(str(page_path.relative_to(WIKI_ROOT)))
        print(f"  [stub] Created {page_path.relative_to(WIKI_ROOT)}")

    return created


# ── Streaming run (test mode) ─────────────────────────────────────────────────

def cmd_run(args: argparse.Namespace) -> None:
    """Process pages with API. Supports --provider anthropic (default), gemini, or openrouter."""
    provider = getattr(args, "provider", "anthropic")
    client = None
    openrouter_api_key = None

    if not args.dry_run:
        if provider == "gemini":
            try:
                from google import genai
            except ImportError:
                print("[ERROR] google-genai not installed. Run: pip install google-genai")
                sys.exit(1)
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                print("[ERROR] GEMINI_API_KEY environment variable not set.")
                sys.exit(1)
            client = genai.Client(api_key=api_key)
            model = GEMINI_MODELS.get(getattr(args, "model", "flash-lite"), GEMINI_MODELS["flash-lite"])
            print(f"Provider: Gemini Flex  |  Model: {model}")
        elif provider == "openrouter":
            openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
            if not openrouter_api_key:
                print("[ERROR] OPENROUTER_API_KEY environment variable not set.")
                sys.exit(1)
            model = args.model or OPENROUTER_DEFAULT_MODEL
            print(f"Provider: OpenRouter  |  Model: {model}")
        else:
            try:
                import anthropic
            except ImportError:
                print("[ERROR] anthropic package not installed. Run: pip install anthropic")
                sys.exit(1)
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                print("[ERROR] ANTHROPIC_API_KEY environment variable not set.")
                sys.exit(1)
            client = anthropic.Anthropic(api_key=api_key)
            model = MODELS.get(args.model, MODELS["haiku"])
            print(f"Provider: Anthropic  |  Model: {model}")
    else:
        model = args.model

    pages = find_pages_to_enrich(args.type, args.overwrite, args.limit)
    if not pages:
        print(f"No draft pages found for type={args.type}.")
        return

    total = len(pages)
    wiki_slugs = get_wiki_slugs()
    written = []
    written_files = []
    done = {"n": 0}
    print_lock = threading.Lock()      # keeps concurrent workers' output from interleaving
    slugs_lock = threading.Lock()      # guards the shared wiki_slugs dict + create_missing_stubs
    written_lock = threading.Lock()

    def process_page(page_path: Path, csv_row: dict, name: str) -> None:
        nonlocal wiki_slugs
        current_stub = page_path.read_text(encoding="utf-8")
        with slugs_lock:
            slugs_snapshot = dict(wiki_slugs)  # read under lock so a sibling's mid-run stub is visible
        user_prompt = build_user_prompt(args.type, name, csv_row, current_stub, slugs_snapshot)

        if args.dry_run:
            with print_lock:
                done["n"] += 1
                print(f"\n[{done['n']}/{total}] ── {name} ({page_path.name}) ──")
                print(f"[DRY RUN] Would call {model} via {provider}")
                print("SYSTEM PROMPT (truncated):", SYSTEM_PROMPT[:200], "...")
                print("USER PROMPT (truncated):", user_prompt[:500], "...")
            return

        with print_lock:
            print(f"\n[{done['n'] + 1}/{total}] ── {name} ({page_path.name}) started ──")

        try:
            if provider == "gemini":
                content = call_gemini_flex(client, model, SYSTEM_PROMPT, user_prompt)
            elif provider == "openrouter":
                from scripts.eval import openrouter_client, model_catalog
                gen = openrouter_client.generate(
                    model, SYSTEM_PROMPT, user_prompt, openrouter_api_key, max_tokens=4000,
                    disable_reasoning=model_catalog.needs_reasoning_disabled(model),
                    reasoning_effort=model_catalog.reasoning_effort_for(model),
                )
                content = gen.raw_text
            else:
                response = client.messages.create(
                    model=model,
                    max_tokens=4000,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_prompt}],
                )
                content = response.content[0].text

            write_enriched_page(page_path, content)
            with written_lock:
                written.append((args.type, name))
                written_files.append(str(page_path.relative_to(WIKI_ROOT)))

            # Create stubs for any wikilinked pages that don't exist yet, then
            # fold the refreshed slug list back into the shared dict so any
            # sibling worker still running (or the next one dispatched) can
            # cross-link to what this page just created.
            with slugs_lock:
                create_missing_stubs(content, args.type)
                wiki_slugs = get_wiki_slugs()

            with print_lock:
                done["n"] += 1
                print(f"[{done['n']}/{total}] [OK] {name} -> {page_path.relative_to(WIKI_ROOT)}")

        except Exception as e:
            with print_lock:
                done["n"] += 1
                print(f"[{done['n']}/{total}] [ERROR] {name}: {e}")

        # Brief pause per request — still applied per-worker under concurrency,
        # so it throttles each thread's own request rate, not the aggregate.
        time.sleep(1 if provider == "gemini" else 0.5)

    concurrency = max(1, getattr(args, "concurrency", 1))
    if concurrency <= 1:
        for page_path, csv_row, name in pages:
            process_page(page_path, csv_row, name)
    else:
        print(f"Running with concurrency={concurrency}...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = [executor.submit(process_page, page_path, csv_row, name)
                       for page_path, csv_row, name in pages]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # re-raise anything unexpected rather than swallow it silently

    if written:
        append_log(written)
    print(f"\nDone: {len(written)} pages enriched.")

    if not args.dry_run:
        _post_batch_checks(written_files)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich ld-wiki stub pages using Claude API + CSV data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- submit --
    p_submit = subparsers.add_parser("submit", help="Prepare and submit a batch to Anthropic")
    p_submit.add_argument("--type", required=True, choices=list(CSV_FILES.keys()))
    p_submit.add_argument("--limit", type=int, default=None)
    p_submit.add_argument("--model", default="haiku", choices=list(MODELS.keys()))
    p_submit.add_argument("--overwrite", action="store_true",
                          help="Re-enrich pages already at status: review")

    # -- collect --
    p_collect = subparsers.add_parser("collect", help="Collect batch results and write pages")
    p_collect.add_argument("--type", required=True, choices=list(CSV_FILES.keys()))
    p_collect.add_argument("--poll", action="store_true",
                           help="Wait until batch completes (checks every 60s)")

    # -- status --
    subparsers.add_parser("status", help="Show status of pending batches")

    # -- run --
    p_run = subparsers.add_parser("run", help="Process pages via API (Gemini Flex, Anthropic, or OpenRouter)")
    p_run.add_argument("--type", required=True, choices=list(CSV_FILES.keys()))
    p_run.add_argument("--provider", default="anthropic", choices=["anthropic", "gemini", "openrouter"],
                       help="API provider (default: anthropic)")
    p_run.add_argument("--limit", type=int, default=None,
                       help="Max pages to process (default: all)")
    p_run.add_argument("--model", default=None,
                       help="anthropic: haiku|sonnet (default: haiku)  gemini: flash-lite|flash|pro "
                            "(default: flash-lite)  openrouter: any OpenRouter model slug "
                            f"(default: {OPENROUTER_DEFAULT_MODEL})")
    p_run.add_argument("--overwrite", action="store_true")
    p_run.add_argument("--concurrency", type=int, default=1,
                       help="Max pages to enrich in parallel (default: 1, sequential — same "
                            "behavior as before this option existed). Rate limits are per-provider "
                            "and not enforced here, so raise this gradually and watch for 429s.")
    p_run.add_argument("--dry-run", action="store_true",
                       help="Show prompts without calling API")

    args = parser.parse_args()

    dispatch = {
        "submit":  cmd_submit,
        "collect": cmd_collect,
        "status":  cmd_status,
        "run":     cmd_run,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
