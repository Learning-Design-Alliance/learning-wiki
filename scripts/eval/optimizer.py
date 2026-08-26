"""
optimizer.py — Proposes a revised extraction prompt from a baseline run's
actual failure data. One call here is one iteration's "propose" step;
eval_harness.py's `optimize` and `auto-optimize` commands both drive the
full propose -> re-run -> compare -> advance loop, one test per round,
strictly sequential — the next round's test never starts until the
current one has fully completed, failed pairs included (see
cmd_auto_optimize's docstring).

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
and DOI rules; match that style). When you're given WORKED EXAMPLES below (a real article excerpt \
paired with an extraction that scored well on this exact test), prefer distilling a short, concrete \
in-prompt example from one of them over inventing an abstract rule — that's a real demonstration of \
the target model succeeding, not a guess at what might help. Trim it down to the minimum illustrative \
snippet; pasting a full worked example verbatim bloats the prompt more than the rule it's meant to replace.
4. Do not just append rules forever — if two rules can be merged or one supersedes another, \
consolidate. A bloated prompt degrades a smaller model's instruction-following as much as a \
missing rule does.
5. Keep the same output JSON contract (types, field names, structure) — you're revising \
instructions and examples, not the schema itself, unless a schema-level change would directly \
fix a validator failure category shown in the data.
6. If "inaccuracy" or "fabrication" is the dominant judge complaint category (check the counts — \
this is a different signal from validator issues, which only catch structural/schema problems and \
say nothing about whether a citation or claim is actually TRUE), do not respond with another \
prohibition rule ("don't fabricate citations," "only cite what's really there") — a model that is \
already fabricating despite similar rules already in the prompt will not stop because the wording \
changed again. Instead, restructure the extraction PROCEDURE: add an explicit step, before any \
contribution is written, that requires identifying and quoting the exact supporting sentence(s) from \
the article for each claim/citation it is about to make, and requires every claim's evidence to \
reference one of those quotes. This targets *how the model produces an answer* (grounding it in a \
quote it must first locate) rather than *what it's told not to do* — the latter has already been \
tried repeatedly against this exact failure category without success.
7. If the validator issues show `evidence[N].source_quote` failing — either "missing" or "does not \
appear in the source article" — this is a harness-side check already live (not something you're \
choosing to add): each evidence entry must carry a `source_quote` field, a short (roughly 15-40 word) \
excerpt copied VERBATIM, character-for-character, from the article text, that directly supports the \
claim. It is checked by exact text match (with a fuzzy fallback tolerating minor whitespace/punctuation \
reformatting) against the actual article this exact request was given — a paraphrase, a summary, or a \
quote from a different part of the article than the one that actually supports this specific claim will \
fail it. If the schema doesn't yet have this field, add it to the evidence object contract and instruct \
the model explicitly: copy the exact sentence (or clause) it is relying on, do not paraphrase, do not \
add or remove words, do not fix apparent typos in the source. If a "missing" failure dominates, the \
field simply isn't in the schema yet — add it. If "does not appear" dominates instead, the field exists \
but the model is paraphrasing anyway — tighten the instruction with a right/wrong example (right: a \
quote that could be found with Ctrl-F in the article; wrong: a rephrased or summarized version of what \
the article said) rather than just repeating "verbatim" once more.

8. If `citation should include a year and a DOI/URL` is a common validator failure — especially \
alongside a judge "fabrication" complaint about invented DOIs — do not just tell the model to leave \
doi_or_url blank when a source has no DOI. That trades one failure for the other: this validator check \
requires every citation to carry a year AND at least one link, but the link can be ANY real http(s) URL, \
not specifically a doi.org one — a citation with a year and no link at all still fails it. Instruct the \
model explicitly: if a source genuinely has no DOI, provide its real URL instead (publisher page, \
conference proceedings page, ISBN/library record, institutional repository link) — a citation should \
almost never have a year but zero link, and never invent a DOI or URL that isn't real.

9. If the failure data includes "Subclaim-level judging" entries, each one names a SPECIFIC subclaim \
sentence that an independent judge checked in isolation against only its own cited evidence and found \
unsupported — this is a sharper signal than a whole-extraction judge complaint (which blends everything \
in one article into one verdict) because it tells you exactly which sentence-and-reason pattern is \
failing, not just that "omission" or "inaccuracy" happened somewhere. Read the actual subclaim texts and \
reasons given: if several share a pattern (e.g. the subclaim states a specific number/percentage that \
isn't in the cited evidence's description, or asserts a causal/comparative claim the evidence only \
supports descriptively), write a rule or example targeting that specific pattern rather than a generic \
"be more accurate" reminder — you have the exact failing sentences to calibrate against.

10. If a "## Full trajectory so far" section is given, it lists EVERY prompt version ever tried, oldest \
to newest, with its score/pass-rate/completeness and a summary of what it changed and why — not just \
this search's own recent rounds. You are stateless between calls; this is the only way you can know what's \
already been attempted. Use it two ways: (a) Before proposing a new rule or rewrite, check whether an \
equivalent fix already appears in a past version's summary. If it does and the score didn't hold or \
improve in the version(s) after it, do not just repeat the same wording again — that will very likely fail \
the same way. Either identify concretely what the earlier attempt was missing (a right/wrong example, a \
sharper trigger condition, addressing a different root cause than assumed) or take a genuinely different \
approach, and say in changes_summary that this is a deliberate retry of an earlier idea and why it should \
work this time. (b) If the trajectory shows a past version scored meaningfully higher than the CURRENT \
baseline you were given, and nothing since has recovered that level, say so explicitly in changes_summary \
— name the version and its score. You cannot revert to it yourself (you can only propose a revision of the \
prompt you were handed), but a human reviewing your output may want to manually resume from that better \
version instead of continuing to build on a worse one.

The failure data may also list generation/API errors (rate limits, an expired key, an exhausted \
account, a model outage) alongside validator and judge issues. Those are infrastructure failures, \
not prompt-content problems — no wording change to the system prompt fixes a rate limit. Do not \
invent a prompt change to address them. If a large share of the batch is generation errors rather \
than validator/judge issues, say so plainly in changes_summary (e.g. "most of this batch failed at \
generation, not on content — little validator/judge signal to act on this round") and make your \
best revision from whatever validator/judge signal remains, however little.

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
        if data.get("generation_error_count"):
            sections.append(f"Generation/API errors (infrastructure failures, NOT prompt-content "
                             f"issues — see instructions): {data['generation_error_count']} of this "
                             f"model's requests failed outright. Sample: "
                             f"{'; '.join(data['generation_error_samples'][:2])}")
        if data.get("subclaim_unsupported_samples"):
            sections.append(f"Subclaim-level judging (FActScore avg: {data.get('subclaim_factscore_avg')}) — "
                             f"specific subclaims independently judged unsupported by their own evidence:")
            for s in data["subclaim_unsupported_samples"]:
                sections.append(f"- ({s['article_id']}, {s['judge']} judge): \"{s['subclaim_text']}\" "
                                 f"— {s['reasoning']}")
        sections.append("")
    return "\n".join(sections)


def _format_trajectory(trajectory: dict) -> str:
    entries = (trajectory or {}).get("entries")
    if not entries:
        return ""
    lines = []
    omitted = trajectory.get("omitted_count", 0)
    if omitted:
        lines.append(f"(showing the {len(entries)} most recent of {len(entries) + omitted} total prompt "
                      f"versions tried; earlier ones omitted for length)")
    for e in entries:
        score = f"{e['avg_judge_score']:.2f}/5" if e["avg_judge_score"] is not None else "?"
        pass_rate = f"{e['avg_pass_rate'] * 100:.0f}%" if e["avg_pass_rate"] is not None else "?"
        completeness = f"{e['avg_completeness'] * 100:.0f}%" if e["avg_completeness"] is not None else "?"
        delta = f" (Δ{e['delta_vs_previous']:+.2f})" if e["delta_vs_previous"] is not None else ""
        summary = (e["changes_summary"] or "(no summary recorded)")[:160].replace("\n", " ")
        lines.append(f"- {e['version']}: score {score}{delta}, pass {pass_rate}, complete {completeness} "
                      f"— {summary}")
    return "\n".join(lines)


def _format_worked_examples(worked_examples: list) -> str:
    blocks = []
    for ex in worked_examples:
        blocks.append(
            f"### {ex['article_title']} (avg judge score {ex['avg_judge_score']}/5, validator-clean)\n"
            f"Article excerpt (truncated):\n{ex['article_excerpt']}\n\n"
            f"Extraction that scored well against it:\n{ex['extraction_json']}"
        )
    return "\n\n".join(blocks)


def build_user_prompt(current_prompt: str, failure_summary: dict, worked_examples: list = None,
                       trajectory: dict = None) -> str:
    examples_block = _format_worked_examples(worked_examples) if worked_examples else ""
    examples_section = (
        f"\n\n## Worked examples from this run (validator-clean, high judge score — real "
        f"demonstrations to calibrate against, not to copy verbatim)\n\n{examples_block}\n"
        if examples_block else ""
    )
    trajectory_block = _format_trajectory(trajectory)
    trajectory_section = (
        f"\n\n## Full trajectory so far (every prompt version tried across every test run, oldest to "
        f"newest — not just this search's own rounds)\n\n{trajectory_block}\n"
        if trajectory_block else ""
    )
    return f"""## Current system prompt

{current_prompt}

## Failure data from the last test batch

{_format_failure_data(failure_summary)}
{examples_section}{trajectory_section}
Produce a revised system prompt addressing these specific patterns, per the rules in your instructions."""


def propose_revision(current_prompt: str, failure_summary: dict, worked_examples: list = None,
                      trajectory: dict = None, model: str = "claude-opus-5") -> dict:
    """Returns {revised_prompt, changes_summary, input_tokens, output_tokens, latency_s}.
    worked_examples (optional, see eval_harness.py's _collect_worked_examples) are real
    (article excerpt, high-scoring extraction) pairs from the baseline run itself — concrete
    demonstrations alongside the abstract failure-pattern summary."""
    import anthropic

    client = anthropic.Anthropic()
    user_prompt = build_user_prompt(current_prompt, failure_summary, worked_examples, trajectory)

    start = time.monotonic()
    # Non-streaming was capped at 16000 max_tokens (the safe ceiling for a
    # single HTTP response) and kept truncating mid-JSON ("Unterminated
    # string") once the accreted prompt (v77+) plus adaptive thinking's own
    # budget — drawn from the same ceiling — needed more room than that.
    # Streaming supports a much higher ceiling without hitting HTTP timeouts.
    with client.messages.stream(
        model=model,
        max_tokens=48000,
        system=PROMPT_ENGINEER_SYSTEM,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": user_prompt}],
    ) as stream:
        response = stream.get_final_message()
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
