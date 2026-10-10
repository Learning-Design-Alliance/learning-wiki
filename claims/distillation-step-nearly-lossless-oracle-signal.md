---
type: claim
title: Distillation step is nearly lossless when the mentor signal is an oracle
description: Distillation step is nearly lossless when the mentor signal is an oracle
id: distillation-step-nearly-lossless-oracle-signal
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
---

# Distillation step is nearly lossless when the mentor signal is an oracle

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Under an oracle mentor, the fine-tuned 2-billion-parameter LLM recovers the true CATE surface with Pearson r = 0.925 and r = 0.910 in the two decision distributions, and ranks the true moderators perfectly (AUC = 1.000), never citing a spurious covariate. [→ Chenguang Pan 2026](#chenguang-pan-2026)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i3` · `design · r2`

Simulation study comparing oracle mentor to X-learner mentor in a 2-by-2 design of imbalanced case by oracle/X-learner CATE, computed against ground-truth CATE on a held-out test set over five repetitions. The printed effect sizes are r = 0.925 and r = 0.910 between mentee estimates and true CATE. The mentee also achieves moderator AUC = 1.000 and FalseCite = 0.000 under oracle conditions.

> "Pearson correlations reach0.925and0.910, and slopes reach0.902and0.918in the two decision distributions, so the E2B Gemma model fine-tuned on roughly seven thousand narrations both ranks students correctly and reproduces the scale of the effects"

## Discussion


## Related Claims
- [Under a realistic estimator, remaining error originates upstream rather than from the distillation step](estimator-loss-dominates-llm-distillation-error.md) — related
- [Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit](hsls-mentee-fidelity-attribution-better-than-decisions.md) — a narrower finding that bears on this claim
