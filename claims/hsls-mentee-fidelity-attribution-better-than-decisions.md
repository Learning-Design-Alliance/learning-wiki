---
type: claim
title: "Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit"
description: "Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit"
id: hsls-mentee-fidelity-attribution-better-than-decisions
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
    i: 3
    kind: design
    rigour: 2
  - id: chenguang-pan-2026-2
    resource: "https://arxiv.org/abs/2608.21165"
    title: "Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165"
    author: Chenguang Pan, Airui Meng, and Youmi Suk
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` On the held-out test split of 1,834 students, the mentee's estimates correlate with the mentor's at r = 0.71 with slope 0.55; top-cited covariates match the mentor's for 80.6% of students with an intersection-over-union of 0.77, but the mentee recommends treatment for all students while the mentor recommends 1,800 of 1,834. [→ Chenguang Pan 2026](#chenguang-pan-2026)
`q2 i?` On the HSLS:09 test set, 98.8% of mentee narrations pass the faithfulness audit in full, decompositions self-close for 99.7%, and 99.9% are unique; the residual 1.2% consists of minor slips rather than hallucinated quantities. [→ Chenguang Pan 2026 (2)](#chenguang-pan-2026-2)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i3` · `design · r2`

Empirical HSLS:09 analysis evaluating the fine-tuned Gemma E2B mentee against its X-learner mentor on a held-out test split of 1,834 students. The printed fidelity effect sizes are r = 0.71 and slope 0.55. "The mentee's top-cited covariates match the mentor's for80.6%of students" with an IoU of 0.77; the mentee recommends treatment for all 1,834 while the mentor recommends 1,800.

> "As shown in the right panel in Figure 5, on the held-out test split of1,834students, the mentee's estimates correlate with the mentor's atr= 0.71, with a regression slope of0.55, which reflects the similar compression towards the mean from the simulation study."

### Chenguang Pan 2026 (2)

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i?` · `design · r2`

Empirical HSLS:09 analysis applying the faithfulness audit with no repair step to mentee narrations on the test set. "98.8%of narrations pass in full"; the residual 1.2% consists of minor slips, such as a direction word inconsistent with the sign of a small cited contribution, rather than hallucinated quantities.

> "On the test set,98.8%of narrations pass in full, the stated decomposition sums to the stated effect for99.7%and99.9%of narrations are unique."

## Discussion


## Related Claims
- [Decision quality collapses toward the majority action in severely imbalanced settings](decision-collapse-severely-imbalanced-settings.md) — related
- [Under a realistic estimator, remaining error originates upstream rather than from the distillation step](estimator-loss-dominates-llm-distillation-error.md) — related
- [Distillation step is nearly lossless when the mentor signal is an oracle](distillation-step-nearly-lossless-oracle-signal.md) — a broader claim this one bears on
- [Narration fluency is no evidence of correctness: narration quality is independent of signal quality](narration-quality-independent-of-signal-quality.md) — related
- [Pipeline applied to HSLS:09 recovers that advanced mathematics coursework benefits students least likely to enroll in four-year college the most](ap-ib-math-benefits-lowest-college-likelihood-most-hsls.md) — related
