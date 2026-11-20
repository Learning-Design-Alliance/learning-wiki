---
type: claim
title: "GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022"
description: "GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022"
id: gcn-aggregated-oncampus-data-higher-auc
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
    kind: design
    rigour: 2
---

# GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The GCN predictor achieves higher AUC when trained on each year's on-campus data in aggregate (90% for 2021, 82% for 2022) compared to individual on-campus course instances (50-80%). [→ Trask 2024](#trask-2024)

## Evidence

### Trask 2024

Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. [doi:10.48550/arXiv.2407.12153](https://doi.org/10.48550/arXiv.2407.12153)

`q2 · i?` · `design · r2`

Results from GCN model evaluation shown in Fig. 2, comparing individual on-campus course instances (average AUC 50-80%) with yearly aggregates. The article reports "the AUC score rises to 90% for 2021 and 82% for 2022". The lower 2022 AUC is attributed to missing Fall 2022 data.

> "It shows that the GCN predictor performs better when looking at each year's data in aggregate; the AUC score rises to 90% for 2021 and 82% for 2022."

## Discussion


## Related Claims
- [Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts](gcn-variance-floor-effect-individual-instances.md) — related
- [GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape](gcn-models-non-transferable-across-instances.md) — related
- [A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy](gcn-hkg-predicts-problem-set-pass-70-90-accuracy.md) — related
