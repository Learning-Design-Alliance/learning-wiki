---
type: claim
title: Claude Sonnet 4.5 struggles most to identify anti-stereotypes in tutoring dialogues, with very low recall (0.177) and lower confidence in correct than in incorrect anti-stereotype predictions
description: Claude Sonnet 4.5 struggles most to identify anti-stereotypes in tutoring dialogues, with very low recall (0.177) and lower confidence in correct than in incorrect anti-stereotype predictions
id: sonnet-antistereotype-low-recall-inverted-confidence
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

# Claude Sonnet 4.5 struggles most to identify anti-stereotypes in tutoring dialogues, with very low recall (0.177) and lower confidence in correct than in incorrect anti-stereotype predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Sonnet 4.5's recall for anti-stereotypical statements in the tutoring dataset is 0.177, indicating a high rate of false negatives, and its confidence is lower for correct anti-stereotype predictions (0.730) than incorrect ones (0.826). [→ Arronte Alvarez 2026](#arronte-alvarez-2026)

## Evidence

### Arronte Alvarez 2026

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `design · r2`

Per-class computational evaluation of Sonnet 4.5 on the tutoring dataset (Table 4); the article reports it "struggles to identify anti-stereotypes the most as evidenced by very low recall (0.177)", with stereotype confidence uniformly 0.835 in correct and incorrect predictions.

> "Most notably, the model exhibits lower confidence in its correct anti-stereotype predictions than in its incorrect ones (0.730 vs. 0.826)."

## Discussion


## Related Claims
- [State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence](llm-overconfidence-incorrect-bias-judgments-tutoring.md) — related
- [LLM bias detection is substantially less accurate in conversational tutoring contexts than on the StereoSet benchmark, with a mean relative metric degradation of 16.3%](llm-bias-detection-harder-tutoring-than-benchmark.md) — related
