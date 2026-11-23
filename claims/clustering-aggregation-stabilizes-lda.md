---
type: claim
title: Random-initialization instability in LDA was addressed by clustering topics across 500 runs and selecting the most central model
description: Random-initialization instability in LDA was addressed by clustering topics across 500 runs and selecting the most central model
id: clustering-aggregation-stabilizes-lda
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2020
sources:
  - id: tor-ole-b-odden-2020
    resource: "https://doi.org/10.48550/arXiv.2001.10753"
    title: "Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2020). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. [doi:10.48550/arXiv.2001.10753](https://doi.org/10.48550/arXiv.2001.10753)"
    author: Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero
    q: 1
    i: "?"
    kind: associational
    rigour: 2
---

# Random-initialization instability in LDA was addressed by clustering topics across 500 runs and selecting the most central model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q1`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Because LDA's random initialization produces different topics run to run, the authors stabilized their analysis by aggregating topics from 500 runs, clustering them with Gaussian Mixture Modeling, and selecting the single model whose topics best matched the cluster centroids. [→ Tor Ole B. Odden 2020](#tor-ole-b-odden-2020)

## Evidence

### Tor Ole B. Odden 2020

Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2020). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. [doi:10.48550/arXiv.2001.10753](https://doi.org/10.48550/arXiv.2001.10753)

`q1 · i?` · `associational · r2`

Methodological result addressing run-to-run variability: topics from 500 runs were appended into a matrix, clustered with Gaussian Mixture Modeling set to 10 clusters, and a cosine-similarity search identified the most central model for final analysis. The authors liken this to computing a mean over repeated measurements.

> "we created an aggregate dataset composed of 500 runs of our chosen LDA model, each using the parameters we had defined above (10 topics, multiple α values, and removal of words that appeared less than 15 times or in greater than 55% of the dataset)"

## Discussion


## Related Claims
- [The final LDA model for the combined corpus achieved a coherence score of 0.577, selected from 15 averaged models using the elbow method and qualitative inspection.](lda-model-coherence-0-577-selection.md) — related
