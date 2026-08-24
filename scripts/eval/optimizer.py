"""
optimizer.py — Proposes a revised extraction prompt from a baseline run's
actual failure data. One call here is one iteration's "propose" step;
eval_harness.py's `optimize` command drives the full propose -> re-run ->
compare -> keep/reject loop (never auto-adopting a regression — see
prompts.py's CURRENT-pointer ratchet).

Uses Claude Opus (already an judge dependency, so no new credential) with the
same real failure_analysis output already shown to a human in the "Failure
patterns" tab — the model sees exactly what a person reviewing the dashboard
would, not a hand-picked subset.
"""

import time

from .jsonutil import extract_json, JSONExtractionError

PROMPT_ENGINEER_SYSTEM = """\
You are an expert prompt engineer improving a system prompt for a smaller open-weight LLM \
that extracts structured JSON contributions (claims, principles, elements, patterns, \
strategies, theories) from research articles into a learning-design wiki.

You will be given the CURRENT system prompt in full, and aggregated failure data from a real \
test batch: the most common validator issues (exact field + message + how many times), judge \
complaint categories with counts, and a handful of verbatim judge complaints.

Your job: produce a REVISED version of the ENTIRE system prompt that addresses the specific, \
concrete failure patterns shown — not generic prompt-engineering platitudes. Rules:

1. Preserve everything in the current prompt that isn't implicated in a failure category. \
Don't rewrite working instructions to make room for new ones unless they genuinely conflict.
2. Where the current prompt ALREADY has a rule addressing a failure category and the model is \
still failing that way, a light rephrase won't fix it — figure out what's actually different \
your version needs: a sharper trigger condition, a concrete example matching the exact failure \
shown, moving the rule earlier, or an explicit self-check step referencing it.
3. Where a NEW rule is needed, make it concrete — name the exact behavior to avoid and give a \
right/wrong example when that helps (this prompt already uses that pattern for its id-format \
and DOI rules; match that style).
4. Do not just append rules forever — if two rules can be merged or one supersedes another, \
consolidate. A bloated prompt degrades a smaller model's instruction-following as much as a \
missing rule does.
5. Keep the same output JSON contract (types, field names, structure) — you're revising \
instructions and examples, not the schema itself, unless a schema-level change would directly \
fix a validator failure category shown in the data.

Output ONLY a single JSON object, no markdown fences, no commentary outside the JSON:
{
  "revised_prompt": "the complete new system prompt text, ready to use as-is",
  "changes_summary": "2-4 sentences: what changed and why, referencing the specific failure data you were given"
}
"""


def _format_failure_data(failure_summary: dict) -> str:
    sections = []
    for model, data in failure_summary.items():
        sections.append(f"### {model}")
        if data.get("validator_top_issues"):
            sections.append("Validator issues:")
            for i in data["validator_top_issues"]:
                sections.append(f"- {i['count']}x [{i['severity']}] {i['field']}: {i['message']}")
        if data.get("judge_keyword_tally"):
            tally = ", ".join(f"{k}={v}" for k, v in data["judge_keyword_tally"].items())
            sections.append(f"Judge complaint categories: {tally}")
        if data.get("judge_sample_issues"):
            sections.append("Sample verbatim judge complaints:")
            for s in data["judge_sample_issues"]:
                sections.append(f"- ({s['article_id']}, {s['judge']} judge): {s['issue']}")
        sections.append("")
    return "\n".join(sections)


def build_user_prompt(current_prompt: str, failure_summary: dict) -> str:
    return f"""## Current system prompt

{current_prompt}

## Failure data from the last test batch

{_format_failure_data(failure_summary)}

Produce a revised system prompt addressing these specific patterns, per the rules in your instructions."""


def propose_revision(current_prompt: str, failure_summary: dict, model: str = "claude-opus-5") -> dict:
    """Returns {revised_prompt, changes_summary, input_tokens, output_tokens, latency_s}."""
    import anthropic

    client = anthropic.Anthropic()
    user_prompt = build_user_prompt(current_prompt, failure_summary)

    start = time.monotonic()
    response = client.messages.create(
        model=model,
        # 8000 was too tight for a non-streaming call to a thinking-by-default
        # model: the revised prompt alone runs ~2000+ tokens (v2.txt is ~900
        # words), and adaptive thinking's own budget comes out of the same
        # max_tokens ceiling — hit it mid-JSON and got "Unterminated string".
        max_tokens=16000,
        system=PROMPT_ENGINEER_SYSTEM,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": user_prompt}],
    )
    latency = time.monotonic() - start

    raw_text = next((b.text for b in response.content if b.type == "text"), "")
    try:
        parsed = extract_json(raw_text)
    except JSONExtractionError as e:
        raise RuntimeError(f"Prompt-engineer response wasn't valid JSON: {e}\nRaw: {raw_text[:500]}") from e

    if not parsed.get("revised_prompt"):
        raise RuntimeError(f"Prompt-engineer response had no revised_prompt: {raw_text[:500]}")

    return {
        "revised_prompt": parsed["revised_prompt"],
        "changes_summary": parsed.get("changes_summary", ""),
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "latency_s": round(latency, 2),
    }
