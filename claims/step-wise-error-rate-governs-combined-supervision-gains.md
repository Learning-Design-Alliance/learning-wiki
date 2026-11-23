---
type: claim
title: "In combined hard-plus-subtask supervision, the teacher model's step-wise error rate determines the gain: lower step-wise error rates yield higher combined-supervision accuracy."
description: "In combined hard-plus-subtask supervision, the teacher model's step-wise error rate determines the gain: lower step-wise error rates yield higher combined-supervision accuracy."
id: step-wise-error-rate-governs-combined-supervision-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
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

# In combined hard-plus-subtask supervision, the teacher model's step-wise error rate determines the gain: lower step-wise error rates yield higher combined-supervision accuracy.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Combining hard task supervision from GPT-4o-mini (11.7% step-wise error rate), Llama-3-70B-Instruct (30.2%) or Command-R-2024-03 (62.6%) with subtask supervision shows Command-R-2024-03 yielding the lowest accuracy. [→ Xuan He 2025](#xuan-he-2025)

## Evidence

### Xuan He 2025

Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)

`q2 · i?` · `causal · r2`

Section 6 (Table 3) combines hard task supervision from three teacher models with original easy subtask supervision at a (roughly 80-88%, 10%) error-rate combination. The authors state Command-R-2024-03, with the highest step-wise error rate, yields the lowest test accuracy.

> "when a teacher model exhibits a lower step-wise error rate, the performance of the combined hard and easy supervision improves."

## Discussion


## Related Claims
- [Combining hard task supervision with corresponding subtask supervision improves performance over sole hard task supervision and beats doubling training epochs or merging rephrased hard supervision.](combining-hard-and-subtask-supervision-improves-performance.md) — related
- Hard full task supervision consistently outperforms easier subtask supervision on hard math benchmarks, even when its outcome error rate is much higher (90% vs 10%). — related
- [Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy.](step-wise-error-rate-correlates-with-performance.md) — a broader claim this one bears on
- Under similar outcome error rates, teacher models with lower step-wise error rates produce supervision that yields higher downstream accuracy, with gaps up to roughly 12% on MATH. — related
