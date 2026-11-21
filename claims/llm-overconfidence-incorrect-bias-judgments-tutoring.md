---
type: claim
title: State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence
description: State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence
id: llm-overconfidence-incorrect-bias-judgments-tutoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: arronte-alvarez-2026
    resource: "https://doi.org/10.1007/978-3-032-29773-0_22"
    title: "Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)"
    author: Arronte Alvarez, A., and Xie Fincham, N.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: arronte-alvarez-2026-2
    resource: "https://doi.org/10.1007/978-3-032-29773-0_22"
    title: "Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)"
    author: Arronte Alvarez, A., and Xie Fincham, N.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the tutoring dataset, 34% of Sonnet 4.5's incorrect predictions occur with very high confidence (≥90%) and a further 38% with high confidence (≥80% and <90%). [→ Arronte Alvarez 2026](#arronte-alvarez-2026)
`q2 i?` By the confidence-weighted bias score, Claude Sonnet 4.5 is the least confident model in its incorrect stereotypical assessments, though its score remains high (82.5 vs. 84.1 for GPT-5.1 and 82.9 for Gemini-2.5-Pro). [→ Arronte Alvarez 2026 (2)](#arronte-alvarez-2026-2)

## Evidence

### Arronte Alvarez 2026

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `design · r2`

Computational analysis of Sonnet 4.5's self-reported confidence on incorrect tutoring-dataset predictions; 24% of errors are moderate confidence and only 4% low confidence, indicating "overconfidence and limited calibration".

> "An analysis of the model’s self-reported confidence on incorrect predictions shows that 34% of errors occur with very high confidence (≥90%). High-confidence errors (≥80%and<90%) account for an additional 38%"

### Arronte Alvarez 2026 (2)

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `design · r2`

Computational comparison of the confidence-weighted bias score across the three models in Experiment #1; Sonnet 4.5 scores 82.5, GPT-5.1 84.1, Gemini-2.5-Pro 82.9, so "Sonnet 4.5 is the least confident model" when incorrect.

> "The average confidence-weighted bias score indicates that Sonnet 4.5 is the least confident model in its incorrect stereotypical assessments in tutoring scenarios as seen in Table 3."

## Discussion


## Related Claims
- [LLM confidence is strongly aligned with its reasoning explanations and student-facing feedback in incorrect bias judgments, with most cases rated highly coherent by human raters](confidence-coherent-with-reasoning-and-feedback.md) — related
- [LLM bias detection is substantially less accurate in conversational tutoring contexts than on the StereoSet benchmark, with a mean relative metric degradation of 16.3%](llm-bias-detection-harder-tutoring-than-benchmark.md) — related
- [Claude Sonnet 4.5 struggles most to identify anti-stereotypes in tutoring dialogues, with very low recall (0.177) and lower confidence in correct than in incorrect anti-stereotype predictions](sonnet-antistereotype-low-recall-inverted-confidence.md) — related
- [A class-specific confidence prompt reduces LLM confidence in incorrect bias judgments but also lowers confidence in correct ones, without changing accuracy](class-specific-confidence-prompt-reduces-incorrect-confidence.md) — related
- [Overconfidence rates differ significantly among LLMs, with Gemini highest and Claude showing none](llm-overconfidence-rates-differ-endodontic-questions.md) — reports the opposite
