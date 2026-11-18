---
type: claim
title: "Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model"
description: "Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model"
id: xal-explanations-calibrate-trust-across-learning-stages
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

# Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Annotators in the XAL condition reported significantly lower trust in deploying the early-stage model but enhanced trust in the late-stage model, an interaction not produced by showing predictions alone (CL). [→ Bhavya Ghai 2021](#bhavya-ghai-2021)

## Evidence

### Bhavya Ghai 2021

Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)

`q2 · i?` · `causal · r?`

Crowdsourced between-subjects experiment (AL, CL, XAL; early vs. late stage within-subject) measuring trust with an 8-item scale (Cronbach's alpha 0.89). Mixed-effects regression found a significant XAL × Stage interaction (β = 0.70, SE = 0.31, p = 0.03), confirming H1: "explanations help calibrate annotators' trust in the model at different stages".

> "compared to the other two conditions, participants in the XAL Condition had significantly lower trust in deploying the early stage model, but enhanced their trust in the later stage model."

## Discussion


## Related Claims
- [As an active learning model matures under uncertainty sampling, its queried instances become more challenging for annotators to judge correctly](al-late-stage-instances-harder-to-judge.md) — related
- [Annotators without AI experience show exceptionally high trust in an unexplained active learning model, and explanations bring their trust to an appropriate level](xal-appropriates-trust-for-ai-inexperienced-annotators.md) — related
- [Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered](xal-model-performance-did-not-differ-across-conditions.md) — related
- [Reasoning-trace exposure raised trust and hedonic appeal without performance benefits, shifting subjective appraisal of the interaction](trace-exposure-raises-trust-and-hedonic-appeal.md) — related
- [Local explanations polarize annotation outcomes by task knowledge: they help high-knowledge annotators label better but impair low-knowledge annotators' judgment](xal-explanations-polarize-annotation-by-task-knowledge.md) — related
- [Explanations reduce annotator satisfaction only for those with low Need for Cognition](xal-satisfaction-depends-on-need-for-cognition.md) — related
