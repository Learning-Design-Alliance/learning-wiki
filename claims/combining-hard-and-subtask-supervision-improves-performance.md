---
type: claim
title: Combining hard task supervision with corresponding subtask supervision improves performance over sole hard task supervision and beats doubling training epochs or merging rephrased hard supervision.
description: Combining hard task supervision with corresponding subtask supervision improves performance over sole hard task supervision and beats doubling training epochs or merging rephrased hard supervision.
id: combining-hard-and-subtask-supervision-improves-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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
  - id: xuan-he-2025-2
    resource: "https://doi.org/10.18653/v1/2025.naacl-long.550"
    title: "Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)"
    author: Xuan He, Da Yin, and Nanyun Peng
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Combining hard task supervision with corresponding subtask supervision improves performance over sole hard task supervision and beats doubling training epochs or merging rephrased hard supervision.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The (50%, 10%) combination of hard and subtask outcome error rates achieves the highest accuracy on MATH, Gaokao-Mathcloze and SAT-Math among all previously trained baselines. [→ Xuan He 2025](#xuan-he-2025)
`q2 i?` The combined supervision outperforms doubling the training epochs and mixing rephrased data with original SFT supervision. [→ Xuan He 2025 (2)](#xuan-he-2025-2)

## Evidence

### Xuan He 2025

Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)

`q2 · i?` · `causal · r2`

Section 6 experiments (Table 2) test seven hard/subtask error-rate combinations, e.g. (20%,10%) through (80%,0%), against sole hard task supervision on the five benchmarks.

> "combining hard task supervision with a 50% outcome error rate and subtask supervision with a 10% outcome error rate leads to the highest accuracy on the MATH, Gaokao-Mathcloze and SAT-Math among all previously trained baselines."

### Xuan He 2025 (2)

Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)

`q2 · i?` · `causal · r2`

Table 2b compares the (50%,10%) combination against a doubled-epochs baseline (4 epochs on hard task supervision) and a merge-rephrased baseline combining original hard tasks with rephrased versions.

> "It also outperforms doubling the training epochs or mixing rephrased data with original SFT supervision, highlighting that integrating subtask supervision can push performance limits beyond repetitive supervision."

## Discussion


## Related Claims
- Models trained on augmented data converge to the best model in fewer epochs than models trained on original data — related
- [In combined hard-plus-subtask supervision, the teacher model's step-wise error rate determines the gain: lower step-wise error rates yield higher combined-supervision accuracy.](step-wise-error-rate-governs-combined-supervision-gains.md) — related
- Hard full task supervision consistently outperforms easier subtask supervision on hard math benchmarks, even when its outcome error rate is much higher (90% vs 10%). — related
- Under similar outcome error rates, teacher models with lower step-wise error rates produce supervision that yields higher downstream accuracy, with gaps up to roughly 12% on MATH. — related
- [Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy.](step-wise-error-rate-correlates-with-performance.md) — related
