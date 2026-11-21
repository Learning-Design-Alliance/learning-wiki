---
type: claim
title: "Semi-supervised label propagation separates experience levels into distinct clusters with accuracy close to 58%"
description: "Semi-supervised label propagation separates experience levels into distinct clusters with accuracy close to 58%"
id: ssl-label-propagation-refines-experience-clusters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: weihs-2025
    resource: "https://doi.org/10.48550/arXiv.2508.03840"
    title: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)"
    author: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: weihs-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.03840"
    title: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)"
    author: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: weihs-2025-3
    resource: "https://doi.org/10.48550/arXiv.2508.03840"
    title: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)"
    author: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Semi-supervised label propagation separates experience levels into distinct clusters with accuracy close to 58%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SSL clusters separate the experience levels into respective clusters more distinctly than unsupervised clusters, differentiating Novice from Adept learners. [→ Weihs 2025](#weihs-2025)
`q2 i?` With accuracy-maximising parameters, SSL clustering reaches accuracy close to 58%, comparable with the unsupervised maximum of 60%. [→ Weihs 2025 (2)](#weihs-2025-2)
`q2 i?` Poisson learning performs better than Laplace learning until a label rate around r = 0.5, after which Laplace surpasses it and increases in accuracy until rmax = 0.7. [→ Weihs 2025 (3)](#weihs-2025-3)

## Evidence

### Weihs 2025

Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)

`q2 · i?` · `associational · r1`

Comparison of semi-supervised (SSL) and unsupervised cluster compositions (Figure 9, discussed). The article notes 'a striking difference lies in how well the SSL method separated the experience levels into respective clusters', identifying distinct Adept and Novice SSL clusters.

> "A striking difference lies in how well the SSL method separated the experience levels into respective clusters, with cluster 1-SSL being the Advanced cluster, and therefore comparable to cluster 2-spectral."

### Weihs 2025 (2)

Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)

`q2 · i?` · `associational · r1`

Label-propagation experiments across label rates and neighbour counts (Figure 8, discussed). With the accuracy-maximising parameters, 'the resulting accuracy is close to 58%', which the article calls comparable with the unsupervised maximum of 60%.

> "The resulting accuracy is close to 58%, which is comparable with the maximal accuracy of 60% for the unsupervised method."

### Weihs 2025 (3)

Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. [doi:10.48550/arXiv.2508.03840](https://doi.org/10.48550/arXiv.2508.03840)

`q2 · i?` · `associational · r2`

Label-propagation experiments comparing Poisson and Laplace learning across label rates (Figure 8). 'Until a label rate around r = 0.5, the Poisson model performs better than the Laplace model', after which Laplace surpasses it up to rmax = 0.7.

> "Until a label rate around r = 0.5, the Poisson model performs better than the Laplace model. Afterwards, the Laplace model surpasses the Poisson model and increases in accuracy until the label rate value of rmax = 0.7."

## Discussion


## Related Claims
- [Clustering Favors Advanced Merge Novice Adept Unseparated](clustering-favors-advanced-merge-novice-adept-unseparated.md)
- [Node-level metrics are the most significant graph-derived metrics distinguishing learner experience groups](node-level-metrics-distinguish-experience-clusters.md) — related
- [The 3-clusters analysis yields better clustering performance than the 4-clusters analysis](three-experience-levels-clustering-outperforms-four.md) — related
