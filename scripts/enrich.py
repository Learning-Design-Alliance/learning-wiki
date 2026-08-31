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

SECRETS_ENV_FILE = Path("/etc/eval-harness.env")


def _load_secrets_env(path: Path = SECRETS_ENV_FILE) -> None:
    """Load API keys from /etc/eval-harness.env when this script is run
    directly on the droplet (bypassing systemd, which normally supplies them
    via EnvironmentFile=) — e.g. `sudo -u evalrunner venv/bin/python
    scripts/enrich.py run ...`. Same helper as eval_harness.py's own
    _load_secrets_env(); duplicated rather than imported so enrich.py stays
    runnable standalone without pulling in eval_harness.py's much larger
    module. A no-op wherever the file doesn't exist (a local dev machine).
    Never overrides a variable already set in the environment, so an
    explicit `export` still wins."""
    if not path.exists():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except PermissionError:
        print(f"[WARN] {path} exists but isn't readable by this user — secrets in it won't be "
              f"auto-loaded (systemd's EnvironmentFile= reads it as root before dropping "
              f"privileges, which is why the service itself still works). To fix ad-hoc runs: "
              f"chown root:evalrunner {path} && chmod 640 {path}", file=sys.stderr)
        return
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


_load_secrets_env()

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


def anthropic_text(content_blocks) -> str:
    """Join the text blocks of an Anthropic response.

    Claude 4.6+ models — Sonnet 5 included — think adaptively by default, so
    `response.content` can lead with a ThinkingBlock. Reaching for
    `content[0].text` then raises "'ThinkingBlock' object has no attribute
    'text'" and the page is silently lost to the per-page error handler.
    Confirmed in production: a `--model sonnet` run over claims failed on 4 of
    5 pages this way, and the one that succeeded only did so because it
    happened not to emit a thinking block.

    Select by block type rather than trusting position, and join rather than
    taking the first — a response may contain more than one text block."""
    return "".join(b.text for b in content_blocks if getattr(b, "type", None) == "text")


def unwrap_json_response(content: str) -> str:
    """Some model responses (confirmed in production with GLM-5.3-flash via
    OpenRouter) come back as a JSON envelope like {"answer": "...markdown..."}
    instead of raw markdown, despite SYSTEM_PROMPT rule 10 ("Output ONLY the
    enriched markdown. No commentary, no code fences."). Detect and unwrap
    it before it ever reaches write_enriched_page; otherwise return content
    unchanged (the overwhelmingly common case)."""
    stripped = content.strip()
    if not stripped.startswith("{"):
        return content
    try:
        parsed = json.loads(stripped)
    except (json.JSONDecodeError, ValueError):
        return content
    if isinstance(parsed, dict):
        for key in ("answer", "content", "markdown", "text"):
            if key in parsed and isinstance(parsed[key], str):
                return parsed[key]
    return content


def salvage_leading_junk(content: str) -> str:
    """Second, best-effort recovery pass for the two other leak patterns
    found alongside JSON-wrapping in production (989 JSON-wrapped + 34 of
    these, all in one batch): a leftover code-fence language tag
    ("markdown\n---\ntype: ...") where the ``` fence itself got stripped
    but not the language word, and raw chain-of-thought preamble
    ("Let me analyze this task carefully.\n\nI need to write...\n---\n
    type: ...") — the model narrating instead of just answering, despite
    SYSTEM_PROMPT rule 10. In both cases the real page is still in there,
    just after some junk; slicing from the first "\n---\n" recovers it for
    free instead of discarding a real, well-formed page over a wrapper the
    model added on top of it."""
    idx = content.find("\n---\n")
    if idx != -1:
        return content[idx + 1:]
    return content


def _error_hint(e: Exception) -> str:
    """Extra guidance appended to an [ERROR] line for a known, previously-seen
    failure class — so the fix is visible in the log itself instead of
    needing to be re-diagnosed each time it recurs. Seen repeatedly this
    session: a page written by a command run as bare root (not
    `sudo -u evalrunner ...`) ends up root-owned, and evalrunner can't
    overwrite it on the next enrichment pass."""
    if isinstance(e, PermissionError):
        return (" — likely a file owned by a different user (e.g. written by a command run as "
                "root instead of `sudo -u evalrunner ...`). Fix with: "
                "sudo chown -R evalrunner:evalrunner " + str(WIKI_ROOT))
    return ""


class InvalidPageContentError(ValueError):
    """Raised when a model's response doesn't look like a real OKF page
    (post unwrap_json_response/salvage_leading_junk) — never write this to
    disk."""


# Phrases that can only be the model narrating its own authoring task. Kept
# deliberately narrow: each one was verified against the whole wiki to fire on
# real leaked deliberation and NOT on legitimate prose. Broader tells were
# tried and rejected — "exemplar" is a real instructional-design term
# (elements/exemplars.md), pages legitimately open "Wait time is...", and
# quoted teacher speech contains "I'll say its sounds: /m/ /o/ /p/".
_DELIBERATION_MARKERS = [
    r"\(\+\d{2,} more\)",                              # the truncated slug list from the prompt
    r"Visible relevant ones",
    r"the exemplar (?:frontmatter|has|is|matches|also includes)",
    r"template stub",
    r"the (?:page|stub) to write",
    r"I need to match",
    r"\bthe draft stub\b",
]
_DELIBERATION_RE = re.compile("|".join(_DELIBERATION_MARKERS), re.IGNORECASE)


# folder name -> the singular value frontmatter `type:` must carry. Same
# mapping add_type_banner.py uses; duplicated here so the write guard has no
# dependency that could be skipped.
_FOLDER_TYPE = {
    "principles": "principle", "elements": "element", "patterns": "pattern",
    "strategies": "strategy", "theories": "theory", "claims": "claim",
    "learner-variables": "learner-variable",
}

# Literal placeholder strings from the page templates. A response that echoes
# the blank template back passes every structural check: the frontmatter
# closes, there is an H1 (`# [Strategy Name]`), and there are `##` sections.
# Fourteen pages reached disk exactly this way — nine of them also keeping
# `title: [Strategy Name]`, so the strategies index listed nine pages by that
# name — and two carried no authoring commentary at all, so the marker scan
# above could not see them either.
_TEMPLATE_PLACEHOLDERS = re.compile(
    r"\[(?:"
    r"Strategy Name|Principle Name|Element Name|Pattern Name|Theory Name"
    r"|One-line summary|One-sentence summary[^\]]*"
    r"|What this (?:strategy|principle|element|pattern|theory) is[^\]]*"
    r"|1-2 sentence overview[^\]]*|2-3 sentences"
    r"|what is needed|conditions where effectiveness drops|variations or adaptations"
    r"|who benefits most|types of objectives served|Step with links to elements"
    r"|Related Strategy|Concrete example in a real context"
    r"|APA citation with DOI link if available|Claim statement[^\]]*"
    r")\]",
    re.IGNORECASE,
)


def _reject_non_page_body(path: Path, content: str) -> None:
    """Refuse output that has valid frontmatter but isn't a wiki page.

    The existing "must start with ---" check catches a raw JSON envelope, but
    not the failure this pipeline actually produced at scale: correct
    frontmatter wrapping a body that is the model's own planning notes.
    Roughly 13 pages reached the published site carrying lines like "The
    exemplar (Demonstration) matches this template closely. I need to match
    its density, structure, and voice." and "strategies/: huge list (+2097
    more). Visible relevant ones: ...". Five more had no H1 at all, because
    the body never became a page.

    Raises InvalidPageContentError so the caller's per-page handler reports
    it and leaves the file on disk untouched — the same contract as the
    frontmatter check."""
    # Frontmatter must actually CLOSE. A response truncated at max_tokens
    # partway through the `sources:` list opens the block and never ends it,
    # so there is no body at all — strategies/a_finders_guide_to_facts.md
    # reached disk that way. split("---", 2) cannot tell that apart from a
    # real page, so parse it properly.
    fm_lines, body = ok.split_frontmatter(content)
    if not fm_lines:
        raise InvalidPageContentError(
            f"Model response has no closed frontmatter block — refusing to write over "
            f"{path}. Either the response was truncated partway through the frontmatter, "
            f"or a bare '---' rule opened a prose preamble. "
            f"First 200 chars: {content.strip()[:200]!r}"
        )

    # The folder is what actually determines a page's section (see
    # add_type_banner.py), so a mismatch means the response is describing a
    # different page than the one being written. strategies/on-the-job_training_(ojt).md
    # reached disk declaring `type: element` with the template exemplar's own
    # title, "Demonstration" — the salvage pass had sliced into the exemplar's
    # frontmatter rather than the page's.
    declared = ok.parse_frontmatter_scalars(fm_lines).get("type", "").strip()
    expected = _FOLDER_TYPE.get(path.parent.name)
    if expected and declared and declared != expected:
        raise InvalidPageContentError(
            f"Model response declares type: {declared!r} but the page is in "
            f"{path.parent.name}/ — expected {expected!r}. Refusing to write over {path}."
        )

    placeholders = _TEMPLATE_PLACEHOLDERS.findall(content)
    if placeholders:
        raise InvalidPageContentError(
            f"Model response still contains unfilled template placeholders "
            f"({sorted(set(placeholders))[:4]!r}) — it echoed the blank template instead "
            f"of writing the page. Refusing to write over {path}."
        )

    # An orphan closing fence as the body's first content is the signature of a
    # response whose opening ```markdown fence was only half-stripped by
    # salvage_leading_junk().
    if body.lstrip().startswith("```"):
        raise InvalidPageContentError(
            f"Model response body opens with a stray code fence — the response was "
            f"wrapped in a fenced block that only got half-stripped. Refusing to write "
            f"over {path}."
        )

    if not re.search(r"^# \S", body, re.MULTILINE):
        raise InvalidPageContentError(
            f"Model response has frontmatter but no '# ' H1 heading — refusing to write "
            f"over {path}. A page without an H1 is not a page (and lint's type-banner "
            f"check will flag it). Body starts: {body.strip()[:200]!r}"
        )

    if not re.search(r"^## \S", body, re.MULTILINE):
        raise InvalidPageContentError(
            f"Model response has no '## ' section headings — refusing to write over "
            f"{path}. Every page template defines sections; a body without any means "
            f"the template wasn't followed. Body starts: {body.strip()[:200]!r}"
        )

    # Scan prose only. The page templates put their own instructions in HTML
    # comments — the claim template says "Summarize ONLY the Evidence entries
    # already present in the draft stub below" — and matching those would
    # reject pages for following the template correctly (claims/activation.md
    # was rejected by exactly that before this).
    prose = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    m = _DELIBERATION_RE.search(prose)
    if m:
        line = next((l for l in prose.split("\n") if m.group(0).lower() in l.lower()), "")
        raise InvalidPageContentError(
            f"Model response contains its own authoring commentary rather than page "
            f"content — refusing to write over {path}. Matched {m.group(0)!r} in: "
            f"{line.strip()[:200]!r}"
        )


def verify_page_citations(path: Path, apply: bool = True) -> list[dict]:
    """Resolve every DOI this page cites against Crossref and strip the ones
    that don't check out, BEFORE the page is treated as done.

    This is the gate the wiki did not have. Verification previously ran only
    as a separate, deliberate resolve_doi_conflicts.py sweep long after
    ingest, and when one was audited, 4 of 11 distinct DOIs it had applied
    across 120 pages were wrong — including a Springer chapter, "Model of
    Causality in Social Learning Theory", attached to Bandura's 1977
    Prentice-Hall book on 69 pages. Each had passed a title-overlap check.

    A DOI that resolves to the wrong paper is worse than no DOI: it reads as
    verified, so nothing downstream questions it. So anything not returning
    'verified' is removed and reported, leaving the citation intact but
    unlinked for a human to source properly.

    Returns one record per removal. Makes live Crossref calls, but they are
    cache-backed (eval/corpus/doi_resolution_cache.json) and scoped to this
    page's own citations."""
    import check_citations as cc
    import resolve_doi_conflicts as rdc

    path = Path(path)
    text = path.read_text(encoding="utf-8")
    # Callers pass either an absolute path or one relative to the wiki root;
    # resolve() normalises both so this never raises on a relative path.
    rel = str(path.resolve().relative_to(WIKI_ROOT.resolve()))
    removals = []
    for entry in cc.extract_citations(text, rel):
        doi = entry.get("doi")
        if not doi:
            continue
        year = entry["key"].rsplit("-", 1)[-1]
        located = None
        for line in text.split("\n"):
            if doi.lower() in line.lower():
                located = line
                break
        cited_title = cc._extract_title_text(located or entry["line"], year)
        try:
            res = rdc.classify_doi(doi, cc._words_from_text(cited_title), cited_title)
        except Exception as e:                      # network trouble must not lose the page
            print(f"  [citation check skipped for {doi}: {e}]", file=sys.stderr)
            continue
        if res["status"] == "verified":
            continue
        # 'error' means the lookup itself failed (network, proxy, Crossref
        # down) — NOT that the DOI is wrong. Stripping on error would delete
        # every DOI on every page touched during an outage. Report it as
        # unchecked and leave it alone; the nightly doi_resolver sweep will
        # catch it once the network is back.
        if res["status"] == "error":
            print(f"  [citation unchecked] {rel}: {doi} — Crossref lookup failed, "
                  f"left in place", file=sys.stderr)
            continue
        removals.append({"doi": doi, "status": res["status"],
                         "cited_as": cited_title, "resolves_to": res.get("title")})
        if apply:
            for form in (f" [doi:{doi}](https://doi.org/{doi})",
                         f" [https://doi.org/{doi}](https://doi.org/{doi})"):
                text = text.replace(form, "")
                text = text.replace(form.replace(doi, doi.upper()), "")
    if apply and removals:
        path.write_text(text, encoding="utf-8")

    # Offline backstop. Everything above needs Crossref, and on an 'error'
    # status it deliberately leaves the DOI alone rather than deleting good
    # data during an outage — which means a whole batch can be written with
    # no DOI verification at all and nothing says so. This check needs no
    # network: it asks whether the DOIs this page just asserted are cited
    # for a *different* paper elsewhere in the wiki. Reported, never
    # stripped — which of the two citations is wrong is a human call, and
    # guessing is how the wrong one becomes canonical.
    try:
        collisions = cc.find_doi_collisions(cc.load_by_doi(cc.load_all_citations()), {rel})
    except Exception as e:
        print(f"  [collision check skipped: {e}]", file=sys.stderr)
        collisions = []
    for c in collisions:
        others = sorted({e["source"] for cl in c["clusters"] for e in cl} - {rel})
        print(f"  [DOI collision] {rel}: {c['doi']} is also cited for a different "
              f"paper in {', '.join(others)} — one of them is wrong", file=sys.stderr)

    return removals


def write_enriched_page(path: Path, content: str) -> None:
    """Write enriched content; ensure status/generated are set (OKF style).

    Refuses to write anything that doesn't start with a frontmatter "---"
    after unwrapping/salvage — found the hard way in production: a raw JSON
    envelope ({"answer": "..."}) got written verbatim over a real page's
    content with no validation at all (strategies/build_a_community_on_
    student_voice.md), destroying it — and it turned out to be one of
    three distinct leak patterns from the same batch, not a one-off. A
    page that fails this check is left completely untouched on disk; the
    caller should treat this as an error for that one page, not silently
    skip it."""
    content = unwrap_json_response(content)
    if not content.strip().startswith("---"):
        content = salvage_leading_junk(content)
    if not content.strip().startswith("---"):
        raise InvalidPageContentError(
            f"Model response doesn't look like a real page (doesn't start with '---' "
            f"frontmatter after JSON-unwrap and leading-junk salvage attempts) — refusing "
            f"to write over {path}. First 200 chars: {content.strip()[:200]!r}"
        )
    _reject_non_page_body(path, content)
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

    # Whole-wiki health sweep (lint, dedupe collision counts, TODO backlog),
    # same as run_scrape_batch.py runs after every scrape batch — so both
    # pipelines feed the same eval/health/history.ndjson trend log
    # regardless of which one touched the wiki. --skip-doi equivalent
    # (no Crossref calls) since this fires after every enrich.py batch,
    # potentially several times an hour; the nightly systemd timer
    # (deploy/wiki-health-check.timer) covers full DOI resolution.
    import wiki_health_check
    result = wiki_health_check.run(skip_doi=True)
    wiki_health_check.append_history(result)
    wiki_health_check.write_dashboard_page(result)  # eval/runs/health.html, served by dashboard_server.py
    # Report draft-status and unfilled-TODO counts SEPARATELY, not just
    # summed as one "TODO" figure — a bare stub (created by
    # create_missing_stubs() for a dangling cross-link) has status: draft
    # but no literal <!-- TODO --> string at all, so a TODO-only count
    # silently hides however many of those a batch just created. Confirmed
    # the hard way: a strategies batch reported "8 pages remaining" this
    # way while hundreds of freshly-created bare stubs (from that same
    # batch's own cross-links) went completely uncounted.
    draft_total = sum(c["draft"] for c in result["incomplete_pages"].values())
    todo_total = sum(c["todo"] for c in result["incomplete_pages"].values())
    total_incomplete = wiki_health_check.count_total_incomplete_pages()
    print(f"[post-batch check] Wiki-wide: {sum(result['lint'].values())} lint issue(s), "
          f"{result['citation_conflicts']} citation conflict(s) wiki-wide, "
          f"{result['cross_folder_needs_judgment']} cross-folder duplicate candidate(s) needing judgment, "
          f"{draft_total} draft page(s) + {todo_total} page(s) with unfilled TODOs "
          f"({total_incomplete} total incomplete, exact — draft/TODO can overlap on the same page).")


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

> **Principle** · [All principles](index.md)

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

> **Element** · [All elements](index.md)

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

> **Pattern** · [All patterns](index.md)

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

> **Strategy** · [All strategies](index.md)

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

THEORY_TEMPLATE = """\
---
type: theory
title: [Theory Name]
description: [One-sentence summary of what this theory proposes]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
---

# [Theory Name]

> **Theory** · [All theories](index.md)

## Description
[What this theory proposes; its core mechanism or claim — 2-4 sentences.]

## Implications

### Context
- [conditions under which this theory applies or was studied]

### Target Learners
- [who this theory's mechanism applies to]

### Target Learning Objectives
- [types of learning outcomes this theory explains or predicts]

## Claims
<!-- Claims that derive from or test this theory: [Claim](../claims/claim-slug.md) [+M] -->
- [Claim statement](../claims/slug.md) [+M] — brief note on the connection

## Related Theories
- [Related Theory](slug.md) — brief note on the relationship

## Examples
<!-- Links to patterns and principles that apply this theory -->
- [Pattern or Principle Name](../patterns/slug.md) — how it applies this theory

## Key Sources
- [APA citation with DOI link if available]
"""

CLAIM_TEMPLATE = """\
---
type: claim
title: [Claim statement — one sentence, present tense]
id: {id}
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
evidence_strength: {evidence_strength}
---

# [Claim statement — one sentence, present tense]

> **Claim** · [All claims](index.md)

[Optional 1-2 sentence clarification of scope or mechanism — using ONLY what the draft stub already states.]

## Subclaims
<!-- Summarize ONLY the Evidence entries already present in the draft stub
     below. Do NOT invent a new study or finding to summarize here. -->
[If the draft stub has no real Evidence entries yet, write exactly this one
line here and nothing else — the exact bare marker, no extra words inside
it: <!-- TODO --> . A longer/descriptive TODO comment will silently never be
picked up again by the wiki's health-check or future enrichment passes,
which scan for that exact literal string.]
`q? i?` [One-sentence summary of an EXISTING Evidence entry's finding and scope.] [→ Author Year](#author-year)

## Evidence
<!-- Do NOT add a new study, citation, or DOI that isn't already in the draft
     stub below. If it DOES have real entries already, you may reformat or
     clarify them (plain-language description, quality/impact/n codes) but
     never change which study they cite or add a DOI that wasn't already
     given. -->
[If the draft stub has no real Evidence entries yet, replace this whole
section with exactly this one line and nothing else — the exact bare
marker, no extra words inside it: <!-- TODO --> . Never fabricate a study to
fill the gap. A longer/descriptive TODO comment will silently never be
picked up again by future enrichment passes, which scan for that exact
literal string.]

## Discussion
[Prose covering contradictions, moderators, boundary conditions, open questions —
drawing only on information already present in the draft stub or general reasoning
about scope. Never cite a new specific study here that isn't already in Evidence.]

## Related Claims
- [Related Claim](slug.md)
"""

LEARNER_VARIABLE_TEMPLATE = """\
---
type: learner-variable
title: [Variable Name]
description: [One-sentence definition of this learner characteristic]
status: review
generated:
  by: "claude/unspecified"
  at: {TODAY}
---

# [Variable Name]

> **Learner Variable** · [All learner variables](index.md)

## Description
[What this learner variable is; how it's typically measured or operationalized — 2-3 sentences.]

## Implications

### Context
- [conditions under which this variable matters most]

### Target Learners
- [which learner populations this characteristic is most relevant for]

### Target Learning Objectives
<!-- Learning outcomes this variable has been shown to affect -->
- [outcomes affected]

## Claims
<!-- Claims reporting findings about this variable, with evidence tags: [Claim](../claims/claim-slug.md) [+M] -->
- [Claim statement](../claims/slug.md) [+M] — brief note on the finding

## Related Learner Variables
- [Related Variable](slug.md) — brief note on the relationship

## Examples
<!-- Links to principles/elements/patterns/strategies that account for this variable -->
- [Principle, Element, Pattern, or Strategy Name](../folder/slug.md) — how it accounts for this variable

## Key Sources
- [APA citation with DOI link if available]
"""

TEMPLATES = {
    "principles":        PRINCIPLE_TEMPLATE,
    "elements":           ELEMENT_TEMPLATE,
    "patterns":           PATTERN_TEMPLATE,
    "strategies":         STRATEGY_TEMPLATE,
    "theories":           THEORY_TEMPLATE,
    "claims":             CLAIM_TEMPLATE,
    "learner-variables":  LEARNER_VARIABLE_TEMPLATE,
}

# Types with no CSV backing at all (enrich.py's CSV_FILES only ever covered
# principles/elements/patterns/strategies) — find_pages_to_enrich() would
# KeyError on CSV_FILES[page_type] for these, so cmd_run always routes them
# through find_pages_to_enrich_no_csv() regardless of --no-csv. Templates
# above exist for all three, but note: learner-variables is deliberately
# NOT in STUB_TEMPLATES/STUB_FOLDERS below — CLAUDE.md defers creating new
# learner-variable pages to a human ("factor... out by hand"), so this only
# enables enriching one a human already created, never auto-stubbing a new
# one from a cross-link the way theories/claims/elements/etc. are.
NO_CSV_ONLY_TYPES = ("theories", "claims", "learner-variables")

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

# Appended only for page_type == "claims" (see get_system_prompt below). Claims
# pages carry per-study Evidence entries with real citations/DOIs — unlike a
# principle/element/pattern/strategy page, where "enrich" mostly means better
# synthesis and organization, a claim's whole value IS its cited evidence, so
# inventing a plausible-but-fake study here is the single worst failure mode
# this pipeline can produce (see check_citations.py's docstring, describing a
# real fabricated-citation incident this wiki already caught once).
CLAIMS_ADDENDUM = """

## Special rules for claims pages (in addition to all rules above)

- NEVER invent a new study, citation, DOI, or Evidence entry that isn't already
  present in the current draft stub below. Only synthesize, reformat, and
  clarify Evidence entries the stub already contains — do not add new ones from
  your own knowledge, even if you are confident a real study would fit.
- If the draft stub's Evidence section has no real entries yet, leave a single
  TODO comment there noting studies still need to be added, rather than
  inventing content to fill the gap.
- You may write or improve the Subclaims, Discussion, and Related Claims
  sections, and the quality/impact/n codes on existing entries, but every
  underlying study must come only from what the draft stub already gives you.
"""


def get_system_prompt(page_type: str) -> str:
    """SYSTEM_PROMPT, plus CLAIMS_ADDENDUM's anti-fabrication rules when
    enriching a claims page. Kept as a function (not a per-type dict) since
    every other page type uses the same base prompt unmodified."""
    if page_type == "claims":
        return SYSTEM_PROMPT + CLAIMS_ADDENDUM
    return SYSTEM_PROMPT


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


def _extract_frontmatter_field(text: str, field: str) -> str:
    """Read a scalar frontmatter field's raw value from a page's current
    content — used to carry a field like id/evidence_strength forward into
    the enrichment template in code, rather than asking the model to copy
    it (or leave it blank) itself. See build_user_prompt's claims branch."""
    m = re.search(rf"^{re.escape(field)}:\s*(.*)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


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
    elif page_type == "claims":
        # Substituted in code, not left to the model: an earlier version
        # asked the model to "preserve the id/evidence_strength from the
        # draft stub, or leave blank if none" as a bracketed instruction —
        # confirmed in production to sometimes get echoed back literally
        # into the frontmatter value when there was nothing to preserve,
        # instead of being left blank. Extracting directly from the current
        # draft removes that failure mode the same way author/grain_size
        # already avoid it for patterns.
        template = template.replace("{id}", _extract_frontmatter_field(current_stub, "id"))
        template = template.replace(
            "{evidence_strength}", _extract_frontmatter_field(current_stub, "evidence_strength"))

    slug_ref = format_slug_list(wiki_slugs)

    # Format CSV row as readable block. Empty for the CSV-independent
    # discovery path (find_pages_to_enrich_no_csv) — this page was never
    # part of the bulk-ingest CSV, so there's no row to show. Say so
    # explicitly rather than leaving a blank, confusing "## CSV source
    # data:" section — the model should lean on the exemplar, the current
    # draft, and its own domain knowledge instead (already true per the
    # SYSTEM_PROMPT's own instructions; this just names it for this page).
    if csv_row:
        csv_block = "\n".join(
            f"{k}: {v.strip()[:500]}" for k, v in csv_row.items() if v and v.strip()
        )
        csv_section = f"## CSV source data:\n{csv_block}\n\n"
    else:
        csv_section = ("## CSV source data:\n"
                       "(none — this page was not part of the bulk-ingest CSV; ground it in the "
                       "exemplar, the current draft stub, and your own knowledge of the literature)\n\n")

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

{csv_section}## Current draft stub:
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


def _get_page_title(path: Path) -> str:
    """Read the title from a page's frontmatter — used by the CSV-independent
    discovery path below, where there's no CSV row to read a name from.
    Falls back to a slug-derived display name if the frontmatter is missing
    a title field."""
    try:
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    except OSError:
        pass
    return path.stem.replace("-", " ").replace("_", " ").title()


def find_pages_to_enrich_no_csv(page_type: str, overwrite: bool, limit: Optional[int]) -> list[tuple[Path, dict, str]]:
    """
    CSV-independent variant of find_pages_to_enrich(): iterates every page of
    this type directly from disk, rather than starting from CSV rows and
    checking which ones have a matching page.

    Built after discovering the CSV-driven path structurally cannot reach
    most of the wiki's real TODO backlog: of 1,569 strategies pages still
    carrying an unfilled <!-- TODO -->, ZERO had a slug matching any row in
    the CSV (checked 2026-08-29). Their filenames use underscores and raw
    punctuation straight from source titles (e.g.
    "graphic_organizers_and_visual_aids_(for_attention).md") — they were
    created by the scraper pipeline (ingest_extractions.py), which slugifies
    differently than enrich.py's own slugify(), not by the bulk-ingest CSV
    path this function's sibling was built for.

    Returns (page_path, {}, name) tuples — csv_row is always an empty dict,
    since there's no CSV data for these pages; build_user_prompt() and
    SYSTEM_PROMPT already lean on the exemplar, the page's own current
    draft, and general domain knowledge rather than requiring the CSV.
    """
    folder = WIKI_ROOT / page_type
    results = []
    for page_path in sorted(folder.glob("*.md")):
        if page_path.stem == "index":
            continue
        status = get_page_status(page_path)
        if not overwrite and status in ("review", "stable") and not _has_unfilled_todo(page_path):
            continue  # already curated, nothing left to fill in
        name = _get_page_title(page_path)
        results.append((page_path, {}, name))
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
            try:
                content = unwrap_json_response(anthropic_text(result.result.message.content))
                content, enc_repairs = repair_encoded_links(content, args.type)
                content, repairs = repair_misfiled_links(content, args.type)
                repairs = enc_repairs + repairs
                write_enriched_page(page_path, content)
                if not getattr(args, "no_verify_citations", False):
                    for r in verify_page_citations(page_path):
                        print(f"  [citation stripped] {slug}: {r['doi']} {r['status']} — "
                              f"cited as {r['cited_as'][:60]!r}"
                              + (f", resolves to {r['resolves_to'][:60]!r}" if r.get("resolves_to") else ""))
                create_missing_stubs(content, args.type)
                written.append((args.type, slug))
                written_files.append(str(page_path.relative_to(WIKI_ROOT)))
                print(f"  [OK] {slug}" + (f"  (fixed links: {', '.join(repairs)})" if repairs else ""))
            except Exception as e:
                errors.append(slug)
                print(f"  [ERROR] {slug}: {e}{_error_hint(e)}")
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


def repair_encoded_links(content: str, current_folder: str) -> tuple[str, list[str]]:
    """Normalise two mechanical link defects that leave a link broken even
    though its target exists.

    1. Percent-encoded punctuation. Many slugs here contain literal apostrophes,
       quotes, question marks and commas, and models URL-encode them on the way
       out (%27, %22, %3F, %2C). Nothing in this pipeline encodes link targets,
       so it comes straight from the model; fourteen links across the wiki were
       broken this way, every one pointing at a file that existed.
    2. Over-deep relative paths. Every content folder sits exactly one level
       under the bundle root, so "../../theories/x.md" can never resolve.

    Rewrites only when the corrected target exists on disk, so a repair can
    never turn a working link into a broken one.
    """
    ENCODINGS = {"%27": "'", "%22": '"', "%3F": "?", "%3f": "?", "%2C": ",",
                 "%2c": ",", "%20": " ", "%28": "(", "%29": ")"}
    repairs = []
    base = WIKI_ROOT / current_folder if current_folder else WIKI_ROOT

    def resolves(target: str) -> bool:
        try:
            return (base / target).resolve().is_file()
        except (OSError, ValueError):
            return False

    def fix(match: re.Match) -> str:
        target = match.group(1)
        fixed = target
        for enc, raw in ENCODINGS.items():
            fixed = fixed.replace(enc, raw)
        while fixed.startswith("../../"):
            fixed = fixed.replace("../../", "../", 1)
        if fixed != target and not resolves(target) and resolves(fixed):
            repairs.append(f"{target} -> {fixed}")
            return f"]({fixed})"
        return match.group(0)

    # `[^)\s]+` cannot match a target that itself contains parentheses, and this
    # wiki has many ("academic_choice_(planning,_working,_reflecting).md"). Match
    # lazily up to ".md)" instead, and accept the <...> form lint requires for
    # those targets.
    content = re.sub(r"\]\(<([^>\n]+?\.md)>\)", lambda m: fix(m), content)
    content = re.sub(r"\]\(([^\s<>]*?\.md)\)", fix, content)
    return content, repairs


def repair_misfiled_links(content: str, current_folder: str) -> tuple[str, list[str]]:
    """
    The single most common mistake seen from enrichment models in practice:
    a link to a page that DOES exist in the wiki, but filed under a
    different folder than the model guessed — most often it defaults to
    "same folder as me," or assumes an element/principle/pattern distinction
    it has no way to know from the slug alone (e.g. linking "practice.md"
    from a strategy page when the real page is elements/practice.md, or
    "case-based-learning.md" when it's actually patterns/case-based-learning.md).
    For every such link, check whether the slug exists under some OTHER
    folder and, if so, rewrite the link to point there instead of leaving
    it broken (or letting create_missing_stubs create a wrong-folder
    duplicate). Returns (possibly-modified content, [repair descriptions]).
    """
    repairs = []
    for folder, slug in parse_wikilinks(content, current_folder):
        if (WIKI_ROOT / folder / f"{slug}.md").exists():
            continue
        found_folders = sorted(
            f for f in STUB_FOLDERS if f != folder and (WIKI_ROOT / f / f"{slug}.md").exists()
        )
        if len(found_folders) != 1:
            # Zero matches: genuinely missing, leave for create_missing_stubs.
            # More than one: the same slug is filed under multiple folders
            # (a real case found in production — case-based-learning.md
            # exists as both an element and a pattern) — auto-picking one
            # would silently guess; leave the link as-is for a human to
            # disambiguate rather than risk linking the wrong page.
            if len(found_folders) > 1:
                repairs.append(f"AMBIGUOUS, not fixed — {slug}.md exists in: {', '.join(found_folders)}")
            continue
        found_folder = found_folders[0]
        correct_link = f"{slug}.md" if found_folder == current_folder else f"../{found_folder}/{slug}.md"
        for wrong in (f"/{folder}/{slug}.md", f"../{folder}/{slug}.md", f"{slug}.md"):
            pattern = re.compile(r"\]\(" + re.escape(wrong) + r"\)")
            if pattern.search(content):
                content = pattern.sub(f"]({correct_link})", content)
                repairs.append(f"{slug}.md: {folder}/ -> {found_folder}/")
                break
    return content, repairs


# Slugs that only ever appear as the *example* link target inside a page
# template ("[Claim statement](../claims/claim-slug.md)", "[Title](slug.md)").
# A model copying a template example verbatim used to get a real page created
# for it: claims/claim-slug.md, principles/principle-slug.md and
# strategies/slug.md all existed this way. Eleven real pages ended up citing
# claims/claim-slug.md as if it were evidence — each with a specific, plausible
# claim statement as the link text, resolving to a stub whose body reads "This
# page is a placeholder stub... It should not be cited." The third was worse:
# handed the filename "slug", the enricher confabulated a fully-formed strategy
# page, with four real citations attached to something that does not exist.
PLACEHOLDER_SLUGS = {
    "slug", "claim-slug", "principle-slug", "element-slug",
    "pattern-slug", "strategy-slug", "theory-slug",
}


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
        if slug in PLACEHOLDER_SLUGS:
            print(f"  [skip stub] {folder}/{slug}.md is a template example slug, not a real "
                  f"page — the response copied a template link verbatim; the citing page "
                  f"needs a real target.")
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

    if getattr(args, "no_csv", False) or args.type in NO_CSV_ONLY_TYPES:
        pages = find_pages_to_enrich_no_csv(args.type, args.overwrite, args.limit)
    else:
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
                print("SYSTEM PROMPT (truncated):", get_system_prompt(args.type)[:200], "...")
                print("USER PROMPT (truncated):", user_prompt[:500], "...")
            return

        with print_lock:
            print(f"\n[{done['n'] + 1}/{total}] ── {name} ({page_path.name}) started ──")

        try:
            if provider == "gemini":
                content = call_gemini_flex(client, model, get_system_prompt(args.type), user_prompt)
            elif provider == "openrouter":
                from scripts.eval import openrouter_client, model_catalog
                gen = openrouter_client.generate(
                    model, get_system_prompt(args.type), user_prompt, openrouter_api_key, max_tokens=4000,
                    disable_reasoning=model_catalog.needs_reasoning_disabled(model),
                    reasoning_effort=model_catalog.reasoning_effort_for(model),
                    json_mode=False,
                )
                content = gen.raw_text
            else:
                response = client.messages.create(
                    model=model,
                    max_tokens=4000,
                    system=get_system_prompt(args.type),
                    messages=[{"role": "user", "content": user_prompt}],
                )
                content = anthropic_text(response.content)

            content, enc_repairs = repair_encoded_links(content, args.type)
            content, repairs = repair_misfiled_links(content, args.type)
            repairs = enc_repairs + repairs
            if repairs:
                with print_lock:
                    print(f"  [fixed links] {name}: {', '.join(repairs)}")

            write_enriched_page(page_path, content)
            for r in verify_page_citations(page_path):
                print(f"  [citation stripped] {page_path.name}: {r['doi']} {r['status']}")
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
                print(f"[{done['n']}/{total}] [ERROR] {name}: {e}{_error_hint(e)}")

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
    p_run.add_argument("--type", required=True, choices=list(CSV_FILES.keys()) + list(NO_CSV_ONLY_TYPES),
                       help="theories/claims/learner-variables have no CSV backing — cmd_run always uses "
                            "disk-based (--no-csv-style) discovery for them regardless of --no-csv")
    p_run.add_argument("--provider", default="anthropic", choices=["anthropic", "gemini", "openrouter"],
                       help="API provider (default: anthropic)")
    p_run.add_argument("--limit", type=int, default=None,
                       help="Max pages to process (default: all)")
    p_run.add_argument("--model", default=None,
                       help="anthropic: haiku|sonnet (default: haiku)  gemini: flash-lite|flash|pro "
                            "(default: flash-lite)  openrouter: any OpenRouter model slug "
                            f"(default: {OPENROUTER_DEFAULT_MODEL})")
    p_run.add_argument("--overwrite", action="store_true")
    p_run.add_argument("--no-csv", action="store_true",
                       help="Discover pages directly from disk instead of from the bulk-ingest CSV — "
                            "for pages the scraper pipeline created (different filename convention, "
                            "no matching CSV row), which --type's normal CSV-driven discovery can "
                            "never reach no matter how many times it's run.")
    p_run.add_argument("--concurrency", type=int, default=1,
                       help="Max pages to enrich in parallel (default: 1, sequential — same "
                            "behavior as before this option existed). Rate limits are per-provider "
                            "and not enforced here, so raise this gradually and watch for 429s.")
    p_run.add_argument("--no-verify-citations", action="store_true",
                       help="Skip the per-page Crossref check that strips DOIs which don't resolve "
                            "to the cited work. On by default: a DOI resolving to the WRONG paper "
                            "reads as verified, so nothing downstream questions it — that is how one "
                            "Springer chapter ended up attached to Bandura (1977) across 69 pages.")
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
