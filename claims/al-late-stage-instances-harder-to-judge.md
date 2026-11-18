---
type: claim
title: As an active learning model matures under uncertainty sampling, its queried instances become more challenging for annotators to judge correctly
description: As an active learning model matures under uncertainty sampling, its queried instances become more challenging for annotators to judge correctly
id: al-late-stage-instances-harder-to-judge
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

# As an active learning model matures under uncertainty sampling, its queried instances become more challenging for annotators to judge correctly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Human accuracy showed a significant main negative effect of late Stage, confirming that late-stage queried instances were harder to judge correctly. [→ Bhavya Ghai 2021](#bhavya-ghai-2021)

## Evidence

### Bhavya Ghai 2021

Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)

`q2 · i?` · `causal · r?`

Human accuracy analysis in the crowdsourced AL experiment. The article also reports participants' agreement with Census ground truth on early-stage trials reached a mean of 0.65 (SE=0.08), versus 0.75 for an author highly familiar with the task, noting uncertainty-sampled instances are challenging by nature.

> "There was also a main negative effect of late Stage (SE = 0.21, t = 3.87, p < 0.001), confirming that queried instances in the later stage were more challenging for participants to judge correctly."

## Discussion


## Related Claims
- [Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered](xal-model-performance-did-not-differ-across-conditions.md) — related
- [Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model](xal-explanations-calibrate-trust-across-learning-stages.md) — related
