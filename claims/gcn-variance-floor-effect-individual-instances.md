---
type: claim
title: Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts
description: Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts
id: gcn-variance-floor-effect-individual-instances
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

# Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Individual on-campus course instances show relatively higher per-run variance in AUC scores compared to aggregated on-campus courses and online course instances, theorized to result from a floor effect when splitting data at low user counts. [→ Trask 2024](#trask-2024)

## Evidence

### Trask 2024

Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. [doi:10.48550/arXiv.2407.12153](https://doi.org/10.48550/arXiv.2407.12153)

`q2 · i?` · `associational · r1`

Analysis of GCN AUC variance across training runs (Fig. 3) for individual course instances versus aggregates. The article theorizes that "as the course user count lowers, course data may be more susceptible to successful/unsuccessful students being grouped together, impacting results".

> "It is important to note that there is significant variance within and between GCN training runs when looking at any individual course instance, as see in fig. 3."

## Discussion


## Related Claims
- [GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022](gcn-aggregated-oncampus-data-higher-auc.md) — related
- [A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy](gcn-hkg-predicts-problem-set-pass-70-90-accuracy.md) — related
- [GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape](gcn-models-non-transferable-across-instances.md) — related
