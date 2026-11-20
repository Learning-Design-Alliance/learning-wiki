---
type: claim
title: GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape
description: GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape
id: gcn-models-non-transferable-across-instances
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: trask-2024
    resource: "https://doi.org/10.48550/arXiv.2407.12153"
    title: "Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. [doi:10.48550/arXiv.2407.12153](https://doi.org/10.48550/arXiv.2407.12153)"
    author: "Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Despite the GCN successfully generating prediction models for each course instance, the difference in data shape caused models to be non-transferable between course instances; a translation layer is proposed as a solution. [→ Trask 2024](#trask-2024)

## Evidence

### Trask 2024

Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. [doi:10.48550/arXiv.2407.12153](https://doi.org/10.48550/arXiv.2407.12153)

`q2 · i?` · `associational · r1`

Finding from the repeatability and transferability analysis (Section 4.1). The article states "the difference in the data's shape caused the model for one class to be non-transferable" and proposes that "a translation layer must be developed to normalize available course content between courses".

> "Even though the GCN model successfully generated prediction models for each course instance, the difference in the data's shape caused the model for one class to be non-transferable to other course instances."

## Discussion


## Related Claims
- [GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022](gcn-aggregated-oncampus-data-higher-auc.md) — related
- [A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy](gcn-hkg-predicts-problem-set-pass-70-90-accuracy.md) — related
- [Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts](gcn-variance-floor-effect-individual-instances.md) — related
