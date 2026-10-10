---
type: claim
title: AI agents recover a smaller share of reference patterns from the synthetic WindowDash dataset than from the real-world Olist dataset
description: AI agents recover a smaller share of reference patterns from the synthetic WindowDash dataset than from the real-world Olist dataset
id: agent-pattern-discovery-gap-windowdash-vs-olist
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: bang-an-2026
    resource: "https://arxiv.org/abs/2609.19617"
    title: "Bang An, Maria Hamdani, Joseph Fox. (2026). DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education. https://arxiv.org/abs/2609.19617"
    author: Bang An, Maria Hamdani, Joseph Fox
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI agents recover a smaller share of reference patterns from the synthetic WindowDash dataset than from the real-world Olist dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 600 simulations at six agent levels, all six agent levels recovered a smaller share of the nine reference patterns in WindowDash than in Olist when partial matches received half credit. [→ Bang An 2026](#bang-an-2026)

## Evidence

### Bang An 2026

Bang An, Maria Hamdani, Joseph Fox. (2026). DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education. https://arxiv.org/abs/2609.19617

`q2 · i?` · `design · r2`

Simulation study comparing AI-agent pattern discovery on Olist and WindowDash: 50 simulations at each of six agent levels per dataset, totaling 600 simulations, each scored against nine dataset-specific reference patterns with half credit for partial matches. The authors note the "consistent discovery gap" favoring recovery on Olist.

> "Figure 1 reveals a consistent discovery gap: with partial matches receiving half credit, all six agent levels recovered a smaller share of the reference patterns in WindowDash than in Olist."

## Discussion


## Related Claims
- [The Olist and WindowDash simulation inputs are matched in scale and analytical scope, with overlapping distributions but differing duration-rating associations](windowdash-olist-comparability.md) — related
- [Designed patterns can rest on very small supporting subgroups: only three orders meet the Price-Rating Sensitivity conditions, with a mean rating of 2.0](windowdash-price-rating-small-subgroup.md) — related
