---
type: claim
title: "DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation"
description: "DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation"
id: dkvmn-automatic-concept-discovery
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: zhang-et-al-2017
    resource: "https://doi.org/10.1145/3038912.3052580"
    title: "Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580"
    author: Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhang-et-al-2017-2
    resource: "https://doi.org/10.1145/3038912.3052580"
    title: "Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580"
    author: Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Synthetic-5 with memory size 5, clustering each exercise to its maximum-weight concept yields a perfect clustering of the five ground-truth concepts, with adjusted mutual information of 1.0. [→ Zhang et al. 2017](#zhang-et-al-2017)
`q2 i?` On ASSISTments2009, the model groups 110 exercise tags into 10 clusters with plausible semantic groupings, e.g. ordering-fraction, ordering-integer, ordering-decimal and ordering-real-number exercises clustered together. [→ Zhang et al. 2017 (2)](#zhang-et-al-2017-2)

## Evidence

### Zhang et al. 2017

Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580

`q2 · i?` · `design · r2`

Concept-discovery analysis on the Synthetic-5 dataset using the learned correlation weights (Figure 4); weights are sparse with one value near 1 per exercise, and clustering matches ground truth with adjusted mutual information 1.0. With memory size 50, adjusted mutual information is 0.879 (1.0 after t-SNE clustering).

> "After clustering each exercise to the concept with the maximum weight value, we get the graph shown in the right part of Figure 4, which reveals a perfect clustering of five latent concepts. The adjusted mutual information [29] of our clustering result and the ground truth is 1.0"

### Zhang et al. 2017 (2)

Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580

`q2 · i?` · `design · r2`

Concept discovery on ASSISTments2009 (Figure 5), visualized via t-SNE projection of correlation weights; no ground-truth concepts exist, so the article evaluates plausibility qualitatively, citing the elementary-arithmetic cluster of ordering exercises as an example.

> "All exercises are grouped into 10 clusters, where the exercises from the same cluster (concept) are labeled in the same color. The clustering graph reveals many reasonable results. Some related exercises are close to one another in the cluster"

## Discussion


## Related Claims
- [Latent concepts discovered by GRATE are meaningful and go beyond the labeled topics in the data](grate-latent-concepts-beyond-topics.md) — related
- [The framework generalizes under automatically generated Q-matrices without requiring expert annotation](automatic-qmatrix-extraction-generalization.md) — related
- [DKVMN can depict a student's changing mastery state of individual concepts over a practice sequence](dkvmn-knowledge-state-depiction.md) — related
- [A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations](prerequisite-score-skill-relation-discovery.md) — related
