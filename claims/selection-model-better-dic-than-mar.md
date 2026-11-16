---
type: claim
title: A random effects selection model allowing MNAR data fits longitudinal value-added achievement data better than the MAR model by DIC
description: A random effects selection model allowing MNAR data fits longitudinal value-added achievement data better than the MAR model by DIC
id: selection-model-better-dic-than-mar
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-16
evidence_strength: moderate
newest_evidence: 2011
sources:
  - id: mccaffrey-2011
    resource: "https://doi.org/10.1214/10-AOAS405"
    title: "McCaffrey, D. F. and Lockwood, J. R. (2011). Missing data in value-added modeling of teacher effects. The Annals of Applied Statistics, 5(2A), 773-797. https://doi.org/10.1214/10-AOAS405"
    author: McCaffrey, D. F. and Lockwood, J. R.
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# A random effects selection model allowing MNAR data fits longitudinal value-added achievement data better than the MAR model by DIC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The selection model obtained a smaller DIC (40,658) than the MAR model (40,824), a difference well above the 10 points generally considered important. [→ McCaffrey 2011](#mccaffrey-2011)

## Evidence

### McCaffrey 2011

McCaffrey, D. F. and Lockwood, J. R. (2011). Missing data in value-added modeling of teacher effects. The Annals of Applied Statistics, 5(2A), 773-797. https://doi.org/10.1214/10-AOAS405

`q2 · i?` · `associational · r3`

Bayesian model comparison using Deviance Information Criterion in WinBUGS on the district mathematics data, based on 5,000 post-burn-in iterations per model. The article reports DIC values "of 40,824 for the MAR model and 40,658 for the selection model" and states the selection model is clearly preferred.

> "We obtained DIC values of 40,824 for the MAR model and 40,658 for the selection model."

## Discussion


## Related Claims
- [Allowing achievement data to be missing not at random has little impact on estimated teacher effects in value-added modeling, with MNAR and MAR estimates correlating at 0.98 or better](mnar-little-impact-teacher-effect-estimates.md) — related
- [For the memorizing subscale, MAR and MCAR models indicated a significant decline over time while MNAR models did not, so models assuming different missingness mechanisms disagreed on average growth](memorizing-growth-disagrees-across-missing-data-techniques.md) — related
