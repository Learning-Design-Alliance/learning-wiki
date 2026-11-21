---
type: claim
title: LLM confidence is strongly aligned with its reasoning explanations and student-facing feedback in incorrect bias judgments, with most cases rated highly coherent by human raters
description: LLM confidence is strongly aligned with its reasoning explanations and student-facing feedback in incorrect bias judgments, with most cases rated highly coherent by human raters
id: confidence-coherent-with-reasoning-and-feedback
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

# LLM confidence is strongly aligned with its reasoning explanations and student-facing feedback in incorrect bias judgments, with most cases rated highly coherent by human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Sonnet 4.5's incorrect classifications, 75% of reasoning explanations and 68% of feedback instances were rated highly coherent with the expressed confidence. [→ Arronte Alvarez 2026](#arronte-alvarez-2026)

## Evidence

### Arronte Alvarez 2026

Arronte Alvarez, A., and Xie Fincham, N. (2026). Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents. Accepted for AIED 2026. [doi:10.1007/978-3-032-29773-0_22](https://doi.org/10.1007/978-3-032-29773-0_22)

`q2 · i?` · `design · r2`

Human evaluation of Sonnet 4.5's reasoning explanations for incorrect bias judgments; feedback showed a similar pattern with 68% highly coherent, 31% partially coherent and 1% incoherent, indicating "a strong alignment between the model’s elicited confidence, its reasoning, and the feedback".

> "with 75% of cases rated as highly coherent and 23% as partially coherent, and only 2% as incoherent."

## Discussion


## Related Claims
- [State-of-the-art LLMs are overconfident in incorrect judgments of stereotypical bias in tutoring conversations, with most errors made at high or very high confidence](llm-overconfidence-incorrect-bias-judgments-tutoring.md) — related
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — related
