---
type: claim
title: "A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy"
description: "A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy"
id: gcn-hkg-predicts-problem-set-pass-70-90-accuracy
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
    rigour: 2
---

# A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A Graph Convolutional Network operating on a heterogeneous knowledge graph of students, videos, assessments and interactions predicts whether a student will pass a particular problem set with 70-90% accuracy based on content consumed, course instance, and modality. [→ Trask 2024](#trask-2024)

## Evidence

### Trask 2024

Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. [doi:10.48550/arXiv.2407.12153](https://doi.org/10.48550/arXiv.2407.12153)

`q2 · i?` · `associational · r2`

Model evaluation across five on-campus and two online instances of GTX1301 on EdX, using a heterogeneous knowledge graph built from 16M on-campus and 55M online clickstream events. The GCN achieved "a 70-90% accuracy of predicting whether a student would pass a particular problem set". No effect size is printed.

> "The model developed achieved a 70-90% accuracy of predicting whether a student would pass a particular problem set based on content consumed, course instance, and modality."

## Discussion


## Related Claims
- [GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022](gcn-aggregated-oncampus-data-higher-auc.md) — related
- [GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape](gcn-models-non-transferable-across-instances.md) — related
- [Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts](gcn-variance-floor-effect-individual-instances.md) — related
