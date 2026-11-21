---
type: claim
title: "A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays"
description: "A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays"
id: llm-84-percent-agreement-ct-subpractices
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

# A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The LLM pipeline matched human consensus on 84% of binary sub-practice scores, with substantial PABAK agreement (average 0.69) on 15 of 20 sub-practices. [→ Savage 2026](#savage-2026)

## Evidence

### Savage 2026

Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. [doi:10.48550/arXiv.2605.07036](https://doi.org/10.48550/arXiv.2605.07036)

`q3 · i?` · `design · r2`

Analysis of 100 randomly sampled student CPE notebooks coded by three human raters, scored by the LLM in three independent runs. The article reports "the LLM achieved 84% agreement overall" with human ground truth, and PABAK ≥ 0.6 for 15 of 20 sub-practices (average PABAK = 0.69).

> "When comparing the automated outputs directly to the human ground truth, the LLM achieved 84% agreement overall."

## Discussion


## Related Claims
- [LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices](llm-71-percent-holistic-quality-agreement.md) — related
- [A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking](llm-human-agreement-ct-practices.md) — related
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](llm-discourse-coding-kappa-078-expert-agreement.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification](llm-positive-bias-tool-justification.md) — a narrower finding that bears on this claim
- [Students in introductory mechanics showed high CT engagement on CPEs, averaging 16.51 of 20 sub-practices, with systems investigation most common (99%) and modular solutions least common (50%)](student-cpe-ct-engagement-baseline.md) — related
