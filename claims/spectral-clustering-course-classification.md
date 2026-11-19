---
type: claim
title: Spectral clustering on the course correlation-degree matrix reproduces manual course classification
description: Spectral clustering on the course correlation-degree matrix reproduces manual course classification
id: spectral-clustering-course-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: zeju-li-2023
    resource: "https://doi.org/10.1109/icalt58122.2023.00111"
    title: "Zeju Li, Linya Cheng, Chunhong Zhang, Xinning Zhu, Hui Zhao. (2023). Multi-source Education Knowledge Graph Construction and Fusion for College Curricula. [doi:10.1109/icalt58122.2023.00111](https://doi.org/10.1109/icalt58122.2023.00111)"
    author: Zeju Li, Linya Cheng, Chunhong Zhang, Xinning Zhu, Hui Zhao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Spectral clustering on the course correlation-degree matrix reproduces manual course classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Applying spectral clustering to the correlation degree matrix of ten courses yields groupings highly similar to manual classification. [→ Zeju Li 2023](#zeju-li-2023)

## Evidence

### Zeju Li 2023

Zeju Li, Linya Cheng, Chunhong Zhang, Xinning Zhu, Hui Zhao. (2023). Multi-source Education Knowledge Graph Construction and Fusion for College Curricula. [doi:10.1109/icalt58122.2023.00111](https://doi.org/10.1109/icalt58122.2023.00111)

`q2 · i?` · `design · r2`

Numerical clustering analysis over ten subjects with relatively complete data resources (n = 10 as printed), using normalized correlation degrees as weights. The authors report the clustering results are "highly similar to the results of the manual classification".

> "We used the spectral clustering method [14] and input the correlation degree matrix, and the results obtained are highly similar to the results of the manual classification mentioned above, which can be used as the clustering method of course classification."

## Discussion


## Related Claims
- [Course correlation degree computed from fused knowledge-concept overlap identifies most relevant course pairs in Electronic Information](kg-course-correlation-degree.md) — related
