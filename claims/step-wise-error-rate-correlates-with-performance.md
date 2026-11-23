---
type: claim
title: "Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy."
description: "Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy."
id: step-wise-error-rate-correlates-with-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: xuan-he-2025
    resource: "https://doi.org/10.18653/v1/2025.naacl-long.550"
    title: "Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)"
    author: Xuan He, Da Yin, and Nanyun Peng
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Human evaluation of 60 sampled incorrect solutions finds step-wise error rates ranging from 11.7% (GPT-4o-mini) to 62.6% (Command-R-2024-03), and lower rates align with higher downstream performance. [→ Xuan He 2025](#xuan-he-2025)

## Evidence

### Xuan He 2025

Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)

`q2 · i?` · `causal · r2`

Human evaluation in Section 5.3 manually counts total and erroneous steps in 60 incorrect solutions per teacher model. The authors report "a strong correlation between the step-wise error rates and downstream performance: lower rates correspond to higher downstream performance".

> "the step-wise error rates vary among these teacher models, with Command-R-2024-03 exhibiting the highest ratio at 62.6% and GPT-4o-mini having the lowest at 11.7%."

## Discussion


## Related Claims
- Downstream accuracy does not decrease monotonically as supervision outcome error rate rises from 0% to 100%. — related
- [Combining hard task supervision with corresponding subtask supervision improves performance over sole hard task supervision and beats doubling training epochs or merging rephrased hard supervision.](combining-hard-and-subtask-supervision-improves-performance.md) — related
- [Changes in outcome error rate hurt subtask supervision performance more than hard task supervision performance.](error-rate-impact-larger-for-subtask-supervision.md) — related
- Under similar outcome error rates, teacher models with lower step-wise error rates produce supervision that yields higher downstream accuracy, with gaps up to roughly 12% on MATH. — a narrower finding that bears on this claim
- [In combined hard-plus-subtask supervision, the teacher model's step-wise error rate determines the gain: lower step-wise error rates yield higher combined-supervision accuracy.](step-wise-error-rate-governs-combined-supervision-gains.md) — a narrower finding that bears on this claim
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
