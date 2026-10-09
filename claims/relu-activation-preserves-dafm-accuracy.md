---
type: claim
title: Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values
description: Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values
id: relu-activation-preserves-dafm-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: pardos-2018
    resource: "https://github.com/CAHLR/dAFM"
    title: "Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM"
    author: "Pardos, Z. A., & Dadu, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the Geometry test set, dAFM fine-tuned with ReLU averaged RMSE 0.4205 versus linear's 0.4202, so very little predictive gain was lost. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

Activation-function comparison on the Cognitive Tutor Geometry dataset (Table 9), testing ReLU against linear for the qk layer to support interpretable, non-negative Q-matrix refinements. The article reports the two average RMSE values; no effect size is printed.

> "We found that very little was lost, with an average RMSE of 0.4205 compared to linear's 0.4202 on the test set (Table 9)."

## Discussion


## Related Claims
- [Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations](dafm-qualitative-remapping-triangle-rectangle.md) — related
- [Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments](dafm-fine-tuned-improves-prediction-over-afm.md) — related
