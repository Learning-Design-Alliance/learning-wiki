---
type: claim
title: "LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices"
description: "LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices"
id: llm-71-percent-holistic-quality-agreement
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

# LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On the 0-to-2 holistic quality scale the LLM reached 71% exact agreement with human consensus with a mean absolute error of 0.29, and Krippendorff's alpha of 0.39 indicated weak absolute agreement. [→ Savage 2026](#savage-2026)

## Evidence

### Savage 2026

Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. [doi:10.48550/arXiv.2605.07036](https://doi.org/10.48550/arXiv.2605.07036)

`q3 · i?` · `design · r2`

Comparison of LLM versus human consensus holistic quality scores (0-2 scale) across four domains and overall for the same 100 notebooks. The article also reports "The overallα= 0.39 indicates weak absolute agreement" and a positive LLM bias (LLM overall 1.77 vs human 1.62).

> "As shown in Table III, the LLM achieved 71% exact agreement overall with an MAE of just 0.29."

## Discussion


## Related Claims
- [A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays](llm-84-percent-agreement-ct-subpractices.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [Expert-based re-annotation with reconciliation raises Fleiss's κ from 0.486 to 0.851, with GPT-4 and PaLM2 near expert reliability and MTurk near random](expert-reconciliation-raises-fleiss-kappa.md) — related
- [The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification](llm-positive-bias-tool-justification.md) — related
