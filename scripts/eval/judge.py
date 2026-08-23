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
