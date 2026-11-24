---
type: claim
title: The CPRL model predicts KC prerequisite relations from a KCs-LOs heterogeneous graph with weakly supervised variants
description: The CPRL model predicts KC prerequisite relations from a KCs-LOs heterogeneous graph with weakly supervised variants
id: cprl-heterogeneous-graph-weak-supervision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
sources:
  - id: bai-et-al-2025
    title: Bai et al. 2025
    q: 2
    i: "?"
    kind: review
    rigour: "?"
---

# The CPRL model predicts KC prerequisite relations from a KCs-LOs heterogeneous graph with weakly supervised variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r?` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` CPRL constructs a KCs-LOs heterogeneous graph, learns KC representations with R-GCN, and predicts prerequisite relations with a Siamese network, with weakly supervised variants (CPRL_lo, CPRL_dp) reducing dependence on labeled data. [→ Bai et al. 2025](#bai-et-al-2025)

## Evidence

### Bai et al. 2025

Youheng Bai, Zitao Liu, Teng Guo, Mingliang Hou, and Kui Xiao. 2025. Prerequisite Relation Learning: A Survey and Outlook. ACM Comput. Surv. 57, 11, Article 279. https://doi.org/10.1145/3733593

`q2 · i?` · `review · r?`

The survey reports, citing Jia et al., the CPRL model and its two weakly supervised variants: one learning from learning object dependencies (CPRL_lo) and one generating probabilistic training data via a data programming paradigm (CPRL_dp), reducing dependence on large labeled data. No performance numbers are printed.

> "proposed the CPRL model, which first models multiple complex learning resource relations by constructing a KCs-LOs heterogeneous graph, then learns representations of KCs by using R-GCN, and finally predicts prerequisite relations between KCs using a Siamese network"

## Discussion


## Related Claims
- [Heterogeneous KCs-LOs graphs leverage LO contextual information to bridge sparsity in direct KC-KC prerequisite relations](heterogeneous-kc-lo-graph-pr-learning.md) — a broader claim this one bears on
- [The PREREQ model, synthesizing multiple educational data sources, outperforms existing methods on standard datasets](prereq-outperforms-standard-datasets.md) — related
