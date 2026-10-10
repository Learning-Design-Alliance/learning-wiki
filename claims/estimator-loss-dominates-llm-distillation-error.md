---
type: claim
title: Under a realistic estimator, remaining error originates upstream rather than from the distillation step
description: Under a realistic estimator, remaining error originates upstream rather than from the distillation step
id: estimator-loss-dominates-llm-distillation-error
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: chenguang-pan-2026
    resource: "https://arxiv.org/abs/2608.21165"
    title: "Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165"
    author: Chenguang Pan, Airui Meng, and Youmi Suk
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Under a realistic estimator, remaining error originates upstream rather than from the distillation step

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When the X-learner replaces the oracle, the mentee's correlation with truth falls to about 0.72 and slope to about 0.50, but the paired mentor shows comparable compression, with every mentee–mentor gap at most 0.074. [→ Chenguang Pan 2026](#chenguang-pan-2026)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i?` · `design · r2`

Simulation study switching the upstream estimator from oracle CATE to X-learner. "The performance degradation can be clearly explained by the metrics of the paired mentor." The mentee's point estimation is actually closer to ground truth than the mentor's (r = 0.723 vs. 0.654), attributed to ALE decomposition and LLM distillation smoothing the noisy CATE.

> "The performance degradation can be clearly explained by the metrics of the paired mentor, whose own slope against the truth is0.535and0.539, so the compression is present in the estimator before any narration is written, and every mentee–mentor gap in these two columns is at most0.074."

## Discussion


## Related Claims
- [Distillation step is nearly lossless when the mentor signal is an oracle](distillation-step-nearly-lossless-oracle-signal.md) — related
- [Decision quality collapses toward the majority action in severely imbalanced settings](decision-collapse-severely-imbalanced-settings.md) — related
- [Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit](hsls-mentee-fidelity-attribution-better-than-decisions.md) — related
- [Narration fluency is no evidence of correctness: narration quality is independent of signal quality](narration-quality-independent-of-signal-quality.md) — related
