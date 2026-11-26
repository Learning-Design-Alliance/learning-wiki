---
type: claim
title: LFA finds alternative cognitive models with better statistical fit than the original Geometry Area Unit model
description: LFA finds alternative cognitive models with better statistical fit than the original Geometry Area Unit model
id: lfa-improves-cognitive-model-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2005
recheck_by: 2008
sources:
  - id: cen-et-al-2005
    resource: "https://doi.org/10.1007/11774303_17"
    title: "Hao Cen, Kenneth Koedinger, Brian Junker. (2005). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17"
    author: Hao Cen, Kenneth Koedinger, Brian Junker
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LFA finds alternative cognitive models with better statistical fit than the original Geometry Area Unit model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2005 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2008**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models found by LFA with AIC and BIC heuristics achieve lower statistical scores than the original 15-skill model, with the best BIC model reducing BIC by 37, AIC by 62, and MAD by .012. [→ Cen et al. 2005](#cen-et-al-2005)

## Evidence

### Cen et al. 2005

Hao Cen, Kenneth Koedinger, Brian Junker. (2005). Learning Factors Analysis – A General Method for Cognitive Model Evaluation and Improvement. https://doi.org/10.1007/11774303_17

`q2 · i?` · `design · r2`

Model-search experiment (Experiment 2) running LFA on Geometry Area Unit tutor log data with A* search guided by AIC and BIC. The article reports the best BIC model's "BIC is reduced by 37, and AIC by 62" and MAD reduced by .012 relative to the original model's baseline (AIC 3,950; BIC 4,285; MAD 0.083).

> "All the better models found by AIC and BIC have better (i.e. lower) statistical scores than those of the original. For the best BIC model, its BIC is reduced by 37, and AIC by 62. The fit of the new model, as measured by MAD, is reduced by .012."

## Discussion


## Related Claims
- [LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets](lfa-discovered-models-beat-hand-generated-eleven-datasets.md) — a broader claim this one bears on
- [LFA discovered that backward application of the circle area formula is a distinct, harder skill with no transfer from forward application](lfa-circle-area-backward-separate-skill.md) — related
- The LFA implementation evaluates a single model in seconds and searches hundreds of models in 4-5 hours — related
- [Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset](pfa-approaches-lfa-accuracy.md) — related
