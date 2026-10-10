---
type: claim
title: LCF outperformed k-means, RPMM, and SS-RPMM on cluster validity indices in the same PSY 101 data
description: LCF outperformed k-means, RPMM, and SS-RPMM on cluster validity indices in the same PSY 101 data
id: lcf-outperforms-comparison-methods-validity-indices
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: pelaez-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    title: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    author: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LCF outperformed k-means, RPMM, and SS-RPMM on cluster validity indices in the same PSY 101 data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Davies-Bouldin, Dunn, and Calinski-Harabasz indices all favored LCF over k-means, RPMM, and SS-RPMM on the same dataset. [→ Pelaez 2019](#pelaez-2019)

## Evidence

### Pelaez 2019

Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283

`q2 · i?` · `design · r2`

Method comparison on the same 2188-student PSY 101 dataset: LCF scored Davies-Bouldin 1.56, Dunn 53.24 x10^3, and Calinski-Harabasz 451.39 versus k-means, RPMM, and SS-RPMM. "All three measures suggest that the LCF model better ﬁts the data."

> "All three measures suggest that the LCF model better ﬁts the data."

## Discussion


## Related Claims
- [LCF showed the most differentiated input patterns across risk groups (11 inputs) versus comparison methods](lcf-most-differentiated-input-patterns.md) — related
- [LCF identifies three PSY 101 risk groups with strongly differentiated DFW rates of 28%, 12%, and 6%](lcf-three-risk-groups-dfw-rates.md) — related
- [High-risk LCF groups concentrate URM, first-generation, EOP, Compact, commuter, and lower-academic-preparation students](lcf-high-risk-group-demographic-composition.md) — related
- [Gaussian Mixture Modeling identifies two latent clusters of delayed start behavior, outperforming three-cluster and unimodal models](gmm-two-clusters-delayed-start.md) — related
