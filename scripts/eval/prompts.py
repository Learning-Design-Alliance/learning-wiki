"""
prompts.py — System prompt and JSON output contract for headless article ingestion.

This condenses .claude/skills/ingest-article.md + the CLAUDE.md schema into a
single prompt a smaller open-weight model can follow without tool use: it reads
raw article text and returns one JSON object describing every wiki contribution,
instead of writing markdown files and opening a PR itself. eval_harness.py (and,
eventually, a real batch-ingest script) renders that JSON into OKF pages.

Structured JSON — rather than freeform markdown+YAML — is the point: it makes
"did the model fill in every required field correctly" a mechanical check
(see validator.py) instead of something only a human or another LLM can judge.

## Versioning

The prompt text itself lives in prompt_versions/vN.txt, not inline here, so it
can evolve across test batches with a record of what changed and why
(prompt_versions/CHANGELOG.md) — see eval_harness.py's `history` and `optimize`
commands, which both depend on being able to name and compare prompt versions.
SYSTEM_PROMPT below is the *current* version (see current_version()), kept as
a module-level constant for existing callers that don't care about versioning.

"Current" is a deliberate, ratchet-only pointer (prompt_versions/CURRENT) —
NOT simply the highest-numbered file. `optimize` saves every candidate it
generates so the history is complete, but only advances CURRENT when a
candidate actually beats its baseline; a regressed experiment stays on disk
for the record without becoming what `run` uses by default.
"""

import re
from pathlib import Path

PROMPT_VERSIONS_DIR = Path(__file__).parent / "prompt_versions"
CURRENT_POINTER = PROMPT_VERSIONS_DIR / "CURRENT"


def list_versions() -> list:
    """Version names (e.g. ['v1', 'v2']) sorted oldest to newest by number."""
    versions = [p.stem for p in PROMPT_VERSIONS_DIR.glob("v*.txt")]
    return sorted(versions, key=lambda v: int(re.sub(r"\D", "", v) or 0))


def current_version() -> str:
    """The ratcheted "best so far" version — CURRENT if set, else the highest
    numbered version on disk (bootstrap case, before CURRENT exists)."""
    if CURRENT_POINTER.exists():
        pinned = CURRENT_POINTER.read_text(encoding="utf-8").strip()
        if pinned:
            return pinned
    versions = list_versions()
    if not versions:
        raise FileNotFoundError(f"No prompt versions found in {PROMPT_VERSIONS_DIR}")
    return versions[-1]


# Old name, kept as an alias — "current" (ratcheted) is the more accurate name
# now that optimize() can save experimental versions that aren't the default.
latest_version = current_version


def set_current_version(version: str) -> None:
    """Advance the CURRENT pointer — call only after confirming `version`
    actually improved on its baseline (see eval_harness.py's optimize loop)."""
    if not (PROMPT_VERSIONS_DIR / f"{version}.txt").exists():
        raise FileNotFoundError(f"No such prompt version: {version}")
    CURRENT_POINTER.write_text(version + "\n", encoding="utf-8")


def load_prompt(version: str = None) -> str:
    """Load a specific version's prompt text, or the current one if omitted."""
    version = version or current_version()
    path = PROMPT_VERSIONS_DIR / f"{version}.txt"
    if not path.exists():
        raise FileNotFoundError(f"No such prompt version: {version} (looked for {path})")
    return path.read_text(encoding="utf-8")


def save_new_version(prompt_text: str) -> str:
    """Write prompt_text as the next version (vN+1) and return its name.
    Caller is responsible for appending a CHANGELOG.md entry explaining why."""
    versions = list_versions()
    next_n = (int(re.sub(r"\D", "", versions[-1]) or 0) + 1) if versions else 1
    name = f"v{next_n}"
    (PROMPT_VERSIONS_DIR / f"{name}.txt").write_text(prompt_text, encoding="utf-8")
    return name


SYSTEM_PROMPT = load_prompt()


def build_user_prompt(article_text: str, existing_slugs: dict, max_chars: int = 60_000) -> str:
    """existing_slugs: {folder: [slug, ...]} as produced by okf_lib-style slug scans."""
    slug_lines = []
    for folder, slugs in existing_slugs.items():
        shown = slugs[:40]
        line = f"{folder}/: " + ", ".join(shown)
        if len(slugs) > 40:
            line += f" ... (+{len(slugs) - 40} more, omitted)"
        slug_lines.append(line)
    slug_block = "\n".join(slug_lines)

    text = article_text.strip()
    truncated_note = ""
    if len(text) > max_chars:
        text = text[:max_chars]
        truncated_note = f"\n\n[TRUNCATED — article continues past {max_chars} characters; work from what you have.]"

    return f"""## Existing wiki slugs (only cross-link to these, or to a sibling contribution below)
{slug_block}

## Article full text
{text}{truncated_note}

Extract every wiki contribution this article supports, following the output contract exactly."""


def build_correction_prompt(previous_raw_output: str, issues: list, max_chars: int = 12_000) -> str:
    """Follow-up prompt for eval_harness.py's optional self-correction retry
    loop (--max-correction-attempts): shows the model its own previous
    output plus the exact structural issues it triggered, and asks for a
    corrected full replacement — not a diff, since a smaller model asked to
    describe a diff is more likely to produce an inconsistent partial edit
    than a clean full object. Distinct from build_user_prompt(), which is
    the original first-attempt prompt; this is never used unless a
    correction attempt is explicitly requested."""
    issue_lines = "\n".join(f"- [{i['severity']}] {i['field']}: {i['message']}" for i in issues) or "(none listed)"

    prev = previous_raw_output.strip()
    truncated_note = ""
    if len(prev) > max_chars:
        prev = prev[:max_chars]
        truncated_note = "\n\n[TRUNCATED — shown output continues past this point.]"

    return f"""Your previous JSON output failed structural validation with these issues:

{issue_lines}

## Your previous output
{prev}{truncated_note}

Produce a CORRECTED, COMPLETE JSON object fixing every issue listed above. Keep everything else \
from your previous output unchanged unless it is directly implicated in one of the issues — do not \
regenerate content that already passed validation. Follow the exact same output contract as before \
(the same JSON schema, same field names). Output ONLY the corrected JSON object, nothing else."""
