---
type: claim
title: LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets
description: LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets
id: lfa-discovered-models-beat-hand-generated-eleven-datasets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2012
recheck_by: 2015
sources:
  - id: kenneth-r-koedinger-2012
    resource: "http://learnlab.org/datashop"
    title: "Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop"
    author: Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2012 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2015**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across eleven datasets, the best machine-generated Q-matrix model achieved lower cross-validated RMSE than both the original in-use model and the best hand-generated model, though the overall improvement was small. [→ Kenneth R. Koedinger 2012](#kenneth-r-koedinger-2012)

## Evidence

### Kenneth R. Koedinger 2012

Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop

`q2 · i?` · `associational · r2`

Automated LFA search over Q matrices was run on eleven DataShop datasets across five domains, comparing discovered models to prior models by cross-validated RMSE. The article reports that "In all eleven datasets the best machine-generated model outperformed both the original (in-use) model and the best hand-generated model."

> "Discovered models were compared to prior models using the root mean square error (RMSE) of predicted versus observed student correctness from a 10-fold item-stratified cross validation. In all eleven datasets the best machine-generated model outperformed both the original (in-use) model and the best hand-generated model."

## Discussion


## Related Claims

- [LFA discovered that backward application of the circle area formula is a distinct, harder skill with no transfer from forward application](lfa-circle-area-backward-separate-skill.md)
- [LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines](lt-mkt-outperforms-kt-baselines-four-datasets.md) — related
- [A DataShop-derived cognitive model of problem-decomposition planning skills improved learner mastery when used to redesign a geometry cognitive tutor unit](datashop-model-improved-geometry-mastery.md) — related
