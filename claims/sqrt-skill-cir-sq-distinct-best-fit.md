---
type: claim
title: A hypothesis-driven KC model splitting forward/backward only for circle and square area items predicts student performance best on the novel dataset
description: A hypothesis-driven KC model splitting forward/backward only for circle and square area items predicts student performance best on the novel dataset
id: sqrt-skill-cir-sq-distinct-best-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-02
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: liu-and-koedinger-2017
    resource: "https://eric.ed.gov/?id=EJ1155896"
    title: "Ran Liu, Kenneth R. Koedinger. (2017). Closing the loop: Automated data-driven cognitive model discoveries lead to improved instruction and learning gains. Journal of Educational Data Mining, Volume 9, No 1. https://eric.ed.gov/?id=EJ1155896"
    author: Ran Liu, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A hypothesis-driven KC model splitting forward/backward only for circle and square area items predicts student performance best on the novel dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The SQRT SKILL: CIR-SQ DISTINCT model outperformed both a merged-KC model and a model splitting forward/backward for all shapes, by BIC and cross-validation RMSE. [→ Liu and Koedinger 2017](#liu-and-koedinger-2017)

## Evidence

### Liu and Koedinger 2017

Ran Liu, Kenneth R. Koedinger. (2017). Closing the loop: Automated data-driven cognitive model discoveries lead to improved instruction and learning gains. Journal of Educational Data Mining, Volume 9, No 1. https://eric.ed.gov/?id=EJ1155896

`q2 · i?` · `causal · r2`

KC model comparison on the 2012 dataset using AIC, BIC, and 10-fold item- and student-stratified cross validation repeated 20 times (Table 1). The SQRT SKILL: CIR-SQ DISTINCT model (58 KCs) achieved lower RMSE (0.28087 item-stratified) than ALL SHAPES: F-B MERGED (56 KCs, 0.28208) and ALL SHAPES: F-B DISTINCT (66 KCs, 0.28104).

> "The SQRT SKILL: CIR-SQ DISTINCT model performs best by BIC, item-stratified, and student-stratified CV measures."

## Discussion


## Related Claims
- [The redesigned condition completed more backward circle and square area items while the control completed more forward items, a significant condition-by-item-type interaction](condition-item-type-practice-interaction.md) — related
- [In a novel dataset, forward-to-backward performance drops were specific to items requiring square-root application (circle and square area), supporting generalization of the hidden-difficulty interpretation](square-root-difficulty-generalizes-novel-dataset.md) — related
- [LFA discovered that backward application of the circle area formula is a distinct, harder skill with no transfer from forward application](lfa-circle-area-backward-separate-skill.md) — related
- [LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets](lfa-discovered-models-beat-hand-generated-eleven-datasets.md) — a broader claim this one bears on
