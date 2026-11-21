---
type: claim
title: The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification
description: The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification
id: llm-positive-bias-tool-justification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: savage-2026
    resource: "https://doi.org/10.48550/arXiv.2605.07036"
    title: "Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. [doi:10.48550/arXiv.2605.07036](https://doi.org/10.48550/arXiv.2605.07036)"
    author: "Savage, S., Bralin, A., Hur, P., & Rebello, N. S."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On Choosing Effective Computational Tools (κ = 0.02, PABAK = 0.24), the LLM credited 93% of groups versus the human baseline of 63%, confusing descriptive tool mention with epistemic justification. [→ Savage 2026](#savage-2026)

## Evidence

### Savage 2026

Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. [doi:10.48550/arXiv.2605.07036](https://doi.org/10.48550/arXiv.2605.07036)

`q3 · i?` · `design · r2`

Qualitative audit of LLM reasoning on the lowest-reliability sub-practice in the 100-notebook analysis set. The article reports the sub-practice had "κ= 0.02, PABAK = 0.24" and that the model "confused the existence of syntax with scientific justification".

> "The LLM exhibited a severe positive bias here, award- ing this practice to 93% of groups compared to the hu- man baseline of 63%."

## Discussion


## Related Claims
- [A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays](llm-84-percent-agreement-ct-subpractices.md) — a broader claim this one bears on
- [LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices](llm-71-percent-holistic-quality-agreement.md) — related
