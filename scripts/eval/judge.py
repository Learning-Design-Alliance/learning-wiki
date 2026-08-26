"""
judge.py — LLM-as-judge quality check: does the generated JSON extraction
actually reflect the source article, independent of whether it's structurally
well-formed (that's validator.py's job)?

Two judges are supported (Claude Opus 5 and an OpenAI model) so a single
judge's bias/blind spots don't set the bar alone — run both and compare, or
average, per eval/README.md.
"""

import time
from dataclasses import dataclass, field
from typing import Optional

from .jsonutil import extract_json, JSONExtractionError
from .pricing import judge_cost

JUDGE_SYSTEM_PROMPT = """\
You are auditing an automated extraction pipeline for a learning-science wiki. Another \
model read a research article and produced a JSON object listing "contributions" \
(claims, principles, elements, patterns, strategies, theories) it believes the article \
supports. Your job is to check that extraction against the actual article text — not to \
re-grade the article's own research quality.

Score each of these 1-5 (5 = excellent, 1 = seriously flawed):
- faithfulness: Are all citations, statistics, study designs, and described findings \
actually present in the article? Penalize any fabricated detail heavily, even a small one.
- accuracy: Do claim direction, evidence tags, and effect descriptions correctly represent \
what the article actually found (not the opposite or an overstated version of it)?
- completeness: Does the extraction capture the article's main citable contribution(s), \
without dropping something a learning-design wiki would clearly want?
- schema_fit: Are evidence tags, quality (q) and impact (i) codes, and evidence_strength \
ratings reasonable given the study design actually described?

Output ONLY a single JSON object, no markdown fences, no commentary:
{
  "faithfulness": 1-5, "accuracy": 1-5, "completeness": 1-5, "schema_fit": 1-5,
  "verdict": "pass" or "fail",
  "issues": ["specific problem, naming which contribution/field it's in", "..."]
}
verdict should be "fail" if any score is 1-2, or if there is a fabricated citation or \
finding — even if other scores are high.
"""


def build_judge_user_prompt(article_text: str, extraction_json_text: str, max_chars: int = 40_000) -> str:
    text = article_text.strip()
    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[TRUNCATED]"
    return f"""## Source article
{text}

## Extraction to audit
{extraction_json_text}

Score this extraction against the source article per the rubric."""


@dataclass
class JudgeResult:
    judge_name: str
    scores: dict = field(default_factory=dict)  # faithfulness/accuracy/completeness/schema_fit
    verdict: str = "error"  # "pass" | "fail" | "error"
    issues: list = field(default_factory=list)
    latency_s: float = 0.0
    cost_usd: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    parse_error: str = ""

    @property
    def average_score(self) -> Optional[float]:
        if not self.scores:
            return None
        return round(sum(self.scores.values()) / len(self.scores), 2)


def _parse_judge_response(raw_text: str) -> tuple[dict, str]:
    try:
        parsed = extract_json(raw_text)
    except JSONExtractionError as e:
        return {}, str(e)
    return parsed, ""


def judge_with_claude(article_text: str, extraction_json_text: str,
                       model: str = "claude-opus-5") -> JudgeResult:
    import anthropic

    client = anthropic.Anthropic()
    user_prompt = build_judge_user_prompt(article_text, extraction_json_text)

    start = time.monotonic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=JUDGE_SYSTEM_PROMPT,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": user_prompt}],
    )
    latency = time.monotonic() - start

    raw_text = next((b.text for b in response.content if b.type == "text"), "")
    parsed, parse_error = _parse_judge_response(raw_text)

    result = JudgeResult(
        judge_name="claude-opus-5",
        latency_s=latency,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        parse_error=parse_error,
    )
    result.cost_usd = judge_cost("claude-opus-5", result.input_tokens, result.output_tokens)
    if parsed:
        result.scores = {k: parsed[k] for k in ("faithfulness", "accuracy", "completeness", "schema_fit") if k in parsed}
        result.verdict = parsed.get("verdict", "error")
        result.issues = parsed.get("issues", [])
    return result


def judge_with_openai(article_text: str, extraction_json_text: str,
                       model: str = "gpt-5.6") -> JudgeResult:
    """Requires OPENAI_API_KEY. `model` defaults to the id given at design time —
    verify it against your OpenAI account's available models before a real run;
    swap via --gpt-judge-model if it's since been renamed/retired."""
    from openai import OpenAI

    client = OpenAI()
    user_prompt = build_judge_user_prompt(article_text, extraction_json_text)

    start = time.monotonic()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
    )
    latency = time.monotonic() - start

    raw_text = response.choices[0].message.content or ""
    parsed, parse_error = _parse_judge_response(raw_text)

    usage = response.usage
    result = JudgeResult(
        judge_name=model,
        latency_s=latency,
        input_tokens=usage.prompt_tokens if usage else 0,
        output_tokens=usage.completion_tokens if usage else 0,
        parse_error=parse_error,
    )
    result.cost_usd = judge_cost("gpt-5.6", result.input_tokens, result.output_tokens)
    if parsed:
        result.scores = {k: parsed[k] for k in ("faithfulness", "accuracy", "completeness", "schema_fit") if k in parsed}
        result.verdict = parsed.get("verdict", "error")
        result.issues = parsed.get("issues", [])
    return result


JUDGES = {
    "opus": judge_with_claude,
    "gpt": judge_with_openai,
}


JUDGE_SUBCLAIM_SYSTEM = """\
You are fact-checking ONE specific atomic claim extracted from a research article, independent of \
everything else in the surrounding extraction — FActScore-style atomic fact verification (Min et al., \
EMNLP 2023): one claim in, one verdict out, rather than one blended score for an entire extraction.

You will be given the source article's full text, ONE subclaim's exact wording, and the citation/quote/\
description the extraction attributes as its support. Your only job: is this ONE specific statement \
actually supported by the article?

Output ONLY a single JSON object, no markdown fences, no commentary:
{
  "verdict": "supported" | "unsupported" | "ambiguous",
  "reasoning": "1-2 sentences: what in the article does (or doesn't) support this, or why it's ambiguous"
}
"supported": the article clearly states or directly implies this. "unsupported": the article contradicts \
this, or says nothing that would let a careful reader conclude it — this includes a fabricated citation \
or a quote that doesn't actually appear in the article. "ambiguous": the article touches the topic but \
doesn't clearly confirm or deny this specific, exact statement.
"""


def build_subclaim_judge_user_prompt(article_text: str, subclaim_text: str, evidence_context: str,
                                      max_chars: int = 40_000) -> str:
    text = article_text.strip()
    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[TRUNCATED]"
    return f"""## Source article
{text}

## Subclaim to fact-check
{subclaim_text}

## Evidence the extraction cites for it
{evidence_context}

Is this ONE subclaim supported by the article? Judge it in isolation from anything else in the extraction."""


@dataclass
class SubclaimJudgment:
    verdict: str = "error"  # "supported" | "unsupported" | "ambiguous" | "error"
    reasoning: str = ""
    latency_s: float = 0.0
    cost_usd: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    parse_error: str = ""


def judge_subclaim_with_claude(article_text: str, subclaim_text: str, evidence_context: str,
                                model: str = "claude-opus-5") -> SubclaimJudgment:
    import anthropic

    client = anthropic.Anthropic()
    user_prompt = build_subclaim_judge_user_prompt(article_text, subclaim_text, evidence_context)

    start = time.monotonic()
    response = client.messages.create(
        model=model,
        # "low" effort, unlike the main judge's "high" — a single atomic
        # fact-check needs far less reasoning depth than auditing a whole
        # extraction at once, and this runs roughly once per subclaim
        # rather than once per article, so the effort/cost tradeoff matters
        # more here.
        max_tokens=1024,
        system=JUDGE_SUBCLAIM_SYSTEM,
        thinking={"type": "adaptive"},
        output_config={"effort": "low"},
        messages=[{"role": "user", "content": user_prompt}],
    )
    latency = time.monotonic() - start

    raw_text = next((b.text for b in response.content if b.type == "text"), "")
    parsed, parse_error = _parse_judge_response(raw_text)

    result = SubclaimJudgment(
        latency_s=latency,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        parse_error=parse_error,
    )
    result.cost_usd = judge_cost("claude-opus-5", result.input_tokens, result.output_tokens)
    if parsed:
        result.verdict = parsed.get("verdict", "error")
        result.reasoning = parsed.get("reasoning", "")
    return result


def judge_subclaim_with_openai(article_text: str, subclaim_text: str, evidence_context: str,
                                model: str = "gpt-5.6") -> SubclaimJudgment:
    from openai import OpenAI

    client = OpenAI()
    user_prompt = build_subclaim_judge_user_prompt(article_text, subclaim_text, evidence_context)

    start = time.monotonic()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": JUDGE_SUBCLAIM_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
    )
    latency = time.monotonic() - start

    raw_text = response.choices[0].message.content or ""
    parsed, parse_error = _parse_judge_response(raw_text)

    usage = response.usage
    result = SubclaimJudgment(
        latency_s=latency,
        input_tokens=usage.prompt_tokens if usage else 0,
        output_tokens=usage.completion_tokens if usage else 0,
        parse_error=parse_error,
    )
    result.cost_usd = judge_cost("gpt-5.6", result.input_tokens, result.output_tokens)
    if parsed:
        result.verdict = parsed.get("verdict", "error")
        result.reasoning = parsed.get("reasoning", "")
    return result


SUBCLAIM_JUDGES = {
    "opus": judge_subclaim_with_claude,
    "gpt": judge_subclaim_with_openai,
}


def _evidence_context_for_subclaim(contrib: dict, evidence_ref) -> str:
    """The citation/quote/description text a subclaim's evidence_ref points
    to, formatted for the subclaim judge prompt. A ref that doesn't resolve
    to a real evidence entry is already a validator error on its own (see
    validator.py's evidence_ref check) — the subclaim judge still runs, it
    just gets told there's nothing to go on."""
    for ev in (contrib.get("evidence") or []):
        if isinstance(ev, dict) and ev.get("anchor") == evidence_ref:
            parts = []
            if ev.get("citation"):
                parts.append(f"Citation: {ev['citation']}")
            if ev.get("source_quote"):
                parts.append(f"Quoted support: {ev['source_quote']}")
            if ev.get("description"):
                parts.append(f"Description: {ev['description']}")
            return "\n".join(parts) if parts else "(evidence entry found but has no citation/quote/description)"
    return "(no matching evidence entry found for this subclaim's evidence_ref)"


def judge_subclaims(article_text: str, parsed: dict, judges: list, gpt_judge_model: str = "gpt-5.6") -> dict:
    """FActScore-style (Min et al., EMNLP 2023): instead of one holistic
    score for a whole extraction, judge each atomic subclaim independently
    and aggregate the fraction "supported" into a factscore. A blended
    per-article score can't say WHICH contribution is the problem when 5
    are fine and 1 is fabricated; this localizes the signal to the exact
    sentence. Real cost multiplier — roughly one extra judge call per
    subclaim in the extraction, not one per article — so it's opt-in
    (--subclaim-judging), reusing the same `judges` list the normal
    whole-extraction judges use to pick which judge model(s) run it.

    Returns {judge_name: {factscore, n_judged, n_supported, n_unsupported,
    n_ambiguous, cost_usd, results: [...]}}."""
    contributions = parsed.get("contributions") if isinstance(parsed, dict) else None
    contributions = contributions if isinstance(contributions, list) else []

    tasks = []  # (contrib_slug, subclaim_index, subclaim_text, evidence_context)
    for contrib in contributions:
        if not isinstance(contrib, dict) or contrib.get("type") != "claim":
            continue
        subclaims = contrib.get("subclaims")
        if not isinstance(subclaims, list):
            continue
        for idx, sc in enumerate(subclaims):
            if not isinstance(sc, dict) or not sc.get("text"):
                continue
            evidence_context = _evidence_context_for_subclaim(contrib, sc.get("evidence_ref"))
            tasks.append((contrib.get("slug", "?"), idx, sc["text"], evidence_context))

    out = {}
    for jname in judges:
        fn = SUBCLAIM_JUDGES.get(jname)
        if fn is None:
            continue
        results = []
        total_cost = 0.0
        for slug, idx, text, evidence_context in tasks:
            try:
                r = fn(article_text, text, evidence_context) if jname == "opus" \
                    else fn(article_text, text, evidence_context, model=gpt_judge_model)
            except Exception as e:
                r = SubclaimJudgment(verdict="error", parse_error=f"{type(e).__name__}: {e}")
            total_cost += r.cost_usd
            results.append({
                "contribution_slug": slug, "subclaim_index": idx, "subclaim_text": text,
                "verdict": r.verdict, "reasoning": r.reasoning, "parse_error": r.parse_error,
            })

        judged = [r for r in results if r["verdict"] in ("supported", "unsupported", "ambiguous")]
        supported = sum(1 for r in judged if r["verdict"] == "supported")
        unsupported = sum(1 for r in judged if r["verdict"] == "unsupported")
        ambiguous = sum(1 for r in judged if r["verdict"] == "ambiguous")
        out[jname] = {
            "factscore": round(supported / len(judged), 3) if judged else None,
            "n_judged": len(judged),
            "n_supported": supported,
            "n_unsupported": unsupported,
            "n_ambiguous": ambiguous,
            "cost_usd": round(total_cost, 6),
            "results": results,
        }
    return out
