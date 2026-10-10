---
type: claim
title: Decision quality collapses toward the majority action in severely imbalanced settings
description: Decision quality collapses toward the majority action in severely imbalanced settings
id: decision-collapse-severely-imbalanced-settings
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: chenguang-pan-2026
    resource: "https://arxiv.org/abs/2608.21165"
    title: "Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165"
    author: Chenguang Pan, Airui Meng, and Youmi Suk
    q: 2
    i: "?"
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

# Decision quality collapses toward the majority action in severely imbalanced settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Under severe imbalance with an X-learner, the mentee recommends treatment for every harmed student (UnsafeTreat = 1.000), where the mentor already recommends treatment for 0.926 of them. [→ Chenguang Pan 2026](#chenguang-pan-2026)
`q2 i?` Under an oracle mentor in the severely imbalanced case, the mentee still misrecommends 28.9% of the harmed subgroup, which the article identifies as pure distillation loss and the largest such gap anywhere in the table. [→ Chenguang Pan 2026 (2)](#chenguang-pan-2026-2)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i?` · `design · r2`

Simulation study decision and safety metrics in the severely imbalanced case (97.1% truly treated). "the mentee recommends treatment for every such student (UnsafeTreat= 1.000)". Most of the failure originates in the X-learner estimator (UnsafeTreat = 0.926).

> "the mentee recommends treatment for every such student (UnsafeTreat= 1.000) where the mentor already recommends treatment for0.926of them, so the estimator introduces most of the failure and distillation closes the remainder."

### Chenguang Pan 2026 (2)

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i?` · `design · r2`

Simulation study oracle condition, severely imbalanced case. "the mentee still misrecommends28.9%of the harmed subgroup." In the balanced case distillation loss drops to 2.8% under oracle CATE.

> "the mentee still misrecommends28.9%of the harmed subgroup, which is pure distillation loss specific to the severely imbalanced case, and it is the largest such gap anywhere in the table."

## Discussion


## Related Claims
- [Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit](hsls-mentee-fidelity-attribution-better-than-decisions.md) — related
- [Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment](cv-test-misalignment-small-imbalanced-data.md) — related
- [Under a realistic estimator, remaining error originates upstream rather than from the distillation step](estimator-loss-dominates-llm-distillation-error.md) — related
