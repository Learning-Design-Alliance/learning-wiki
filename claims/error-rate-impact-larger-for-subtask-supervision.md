---
type: claim
title: Changes in outcome error rate hurt subtask supervision performance more than hard task supervision performance.
description: Changes in outcome error rate hurt subtask supervision performance more than hard task supervision performance.
id: error-rate-impact-larger-for-subtask-supervision
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

# Changes in outcome error rate hurt subtask supervision performance more than hard task supervision performance.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On MATH, the performance drop across varying outcome error rates is 9.4% for subtask supervision versus 4.6% for hard full task supervision. [→ Xuan He 2025](#xuan-he-2025)

## Evidence

### Xuan He 2025

Xuan He, Da Yin, and Nanyun Peng. (2025). Guiding Through Complexity: What Makes Good Supervision for Hard Math Reasoning Tasks?. [doi:10.18653/v1/2025.naacl-long.550](https://doi.org/10.18653/v1/2025.naacl-long.550)

`q2 · i?` · `causal · r2`

Figure 2 analysis in Section 4.2 comparing the gap between highest and lowest results across outcome error rates. The authors conclude SFT is "more robust to outcome error rate variations when using hard full task supervision".

> "For instance, on MATH, the performance drop for sub-task supervision is 9.4%, whereas for hard full task supervision, it is only 4.6%."

## Discussion


## Related Claims
- Hard full task supervision consistently outperforms easier subtask supervision on hard math benchmarks, even when its outcome error rate is much higher (90% vs 10%). — related
- Under similar outcome error rates, teacher models with lower step-wise error rates produce supervision that yields higher downstream accuracy, with gaps up to roughly 12% on MATH. — related
- Downstream accuracy does not decrease monotonically as supervision outcome error rate rises from 0% to 100%. — related
- [Step-wise error rate, the average ratio of erroneous steps to total steps in supervision, correlates strongly with downstream performance: lower rates correspond to higher accuracy.](step-wise-error-rate-correlates-with-performance.md) — related
