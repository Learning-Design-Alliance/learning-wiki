---
type: claim
title: Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered
description: Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered
id: xal-model-performance-did-not-differ-across-conditions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: bhavya-ghai-2021
    resource: "https://doi.org/10.1145/3432934"
    title: "Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)"
    author: Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For accuracy, F1, and their improvements, mixed-effects models found only a significant main effect of Stage (p < 0.001); improvement did not differ across learning conditions. [→ Bhavya Ghai 2021](#bhavya-ghai-2021)

## Evidence

### Bhavya Ghai 2021

Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)

`q2 · i?` · `causal · r?`

Mixed-effects regression on model performance metrics (accuracy and F1 on 25% reserved test data, with improvement over the initial model) after 20 queries in each condition and stage, reported in Table 1. Participants improved the early-stage model significantly more than the late-stage model, with no condition differences.

> "In all the models, we found only significant main effect of Stage for all performance and improvement metrics (p < 0.001)."

## Discussion


## Related Claims
- [As an active learning model matures under uncertainty sampling, its queried instances become more challenging for annotators to judge correctly](al-late-stage-instances-harder-to-judge.md) — related
- [Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model](xal-explanations-calibrate-trust-across-learning-stages.md) — related
- [Local explanations polarize annotation outcomes by task knowledge: they help high-knowledge annotators label better but impair low-knowledge annotators' judgment](xal-explanations-polarize-annotation-by-task-knowledge.md) — related
- [Explanations reduce annotator satisfaction only for those with low Need for Cognition](xal-satisfaction-depends-on-need-for-cognition.md) — related
- [Explanations raise perceived cognitive workload only for annotators with AI experience](xal-workload-higher-for-ai-experienced-annotators.md) — related
