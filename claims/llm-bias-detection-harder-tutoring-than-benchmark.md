---
type: claim
title: "LLM bias detection is substantially less accurate in conversational tutoring contexts than on the StereoSet benchmark, with a mean relative metric degradation of 16.3%"
description: "LLM bias detection is substantially less accurate in conversational tutoring contexts than on the StereoSet benchmark, with a mean relative metric degradation of 16.3%"
id: llm-bias-detection-harder-tutoring-than-benchmark
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
---

# LLM bias detection is substantially less accurate in conversational tutoring contexts than on the StereoSet benchmark, with a mean relative metric degradation of 16.3%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three state-of-the-art LLMs, classification metrics for stereotypical-bias detection drop by a mean relative 16.3% when moving from StereoSet to the Biased Conversational Tutoring dataset. [→ Arronte Alvarez 2026](#arronte-alvarez-2026)

## Evidence

### Arronte Alvarez 2026

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `design · r2`

Computational evaluation (Experiment #1) of GPT-5.1, Gemini 2.5 Pro and Claude Sonnet 4.5 on 1,689 matched samples, reporting precision, recall, F2 and accuracy on both datasets; the article reports "a mean relative degradation across metrics of 16.3%".

> "We see a mean relative degradation across metrics of 16.3% when moving from StereoSet to the Biased Conversational Tutoring dataset."

## Discussion


## Related Claims
- [State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence](llm-overconfidence-incorrect-bias-judgments-tutoring.md) — related
- [Claude Sonnet 4.5 struggles most to identify anti-stereotypes in tutoring dialogues, with very low recall (0.177) and lower confidence in correct than in incorrect anti-stereotype predictions](sonnet-antistereotype-low-recall-inverted-confidence.md) — related
