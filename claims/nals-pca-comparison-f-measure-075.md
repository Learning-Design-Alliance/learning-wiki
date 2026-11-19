---
type: claim
title: NALS clusters closely resemble PCA components (F-measure 0.75) but reveal differences, such as component I dividing into two clusters
description: NALS clusters closely resemble PCA components (F-measure 0.75) but reveal differences, such as component I dividing into two clusters
id: nals-pca-comparison-f-measure-075
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: robert-p-dalka-2022
    resource: "https://doi.org/10.1103/physrevphyseducres.18.020113"
    title: "Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak. (2022). Network analysis approach to Likert-style surveys. [doi:10.1103/physrevphyseducres.18.020113](https://doi.org/10.1103/physrevphyseducres.18.020113)"
    author: Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: robert-p-dalka-2022-2
    resource: "https://doi.org/10.1103/physrevphyseducres.18.020113"
    title: "Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak. (2022). Network analysis approach to Likert-style surveys. [doi:10.1103/physrevphyseducres.18.020113](https://doi.org/10.1103/physrevphyseducres.18.020113)"
    author: Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# NALS clusters closely resemble PCA components (F-measure 0.75) but reveal differences, such as component I dividing into two clusters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The F-measure between PCA and NA partitions of the ASES survey is 0.75, indicating similarity between components and clusters. [→ Robert P. Dalka 2022](#robert-p-dalka-2022)
`q2 i?` Cluster C1 mixes items from PCA components I and E plus three items PCA did not load, exemplifying differences between the two approaches. [→ Robert P. Dalka 2022 (2)](#robert-p-dalka-2022-2)

## Evidence

### Robert P. Dalka 2022

Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak. (2022). Network analysis approach to Likert-style surveys. [doi:10.1103/physrevphyseducres.18.020113](https://doi.org/10.1103/physrevphyseducres.18.020113)

`q2 · i?` · `design · r2`

Quantitative two-way F-measure comparison of the fast-greedy NA partition against the previously published PCA components for the ASES data. The article reports the F-measure "is 0.75, indicating similarity between the principal components and the clusters", while noting interesting differences.

> "In particular, the calculated F-measure between the partitions from PCA and NA is 0.75, indicating similarity between the principal components and the clusters. However, there are some interesting differences, which we discuss in Sec. V."

### Robert P. Dalka 2022 (2)

Robert P. Dalka, Diana Sachmpazidi, Charles Henderson, and Justyna P. Zwolak. (2022). Network analysis approach to Likert-style surveys. [doi:10.1103/physrevphyseducres.18.020113](https://doi.org/10.1103/physrevphyseducres.18.020113)

`q2 · i?` · `associational · r2`

Cluster composition analysis of C1 in the ASES backbone network. The article describes C1 as "a mixture of two principal components" and states three items not loaded by PCA also appear in the cluster. Cluster C4 grouped the exact same items as PCA component S.

> "This cluster is a mixture of two principal components, with four items belonging to PCA component I and two to PCA component E. In addition, three items not loaded into a component by PCA are also grouped in this cluster."

## Discussion


## Related Claims
- [Principal component analysis finds the E-CLASS does not exhibit strong factors, consistent with its design targeting many distinct learning goals](eclass-pca-no-strong-factors.md) — related
- [Weighted degree centrality distinguishes essential from redundant survey items, and previously unloaded items X01 and X03 play important network roles](weighted-degree-centrality-essential-items.md) — related
- [Twenty online courses cluster into four quadrants of individual participation and interactivity derived from posting-activity indicators](courses-four-quadrants-participation-interactivity.md) — related
- [Joint clustering of receptive and expressive items yields six distinct clusters, supporting independent receptive and expressive dimensions](six-clusters-joint-receptive-expressive.md) — related
