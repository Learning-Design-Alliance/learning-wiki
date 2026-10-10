---
type: claim
title: The Olist and WindowDash simulation inputs are matched in scale and analytical scope, with overlapping distributions but differing duration-rating associations
description: The Olist and WindowDash simulation inputs are matched in scale and analytical scope, with overlapping distributions but differing duration-rating associations
id: windowdash-olist-comparability
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

# The Olist and WindowDash simulation inputs are matched in scale and analytical scope, with overlapping distributions but differing duration-rating associations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both datasets contain 15,000 unique orders and nine reference patterns; ratings concentrate at four or five stars in both (77.6% in Olist, 79.5% in WindowDash), cumulative-distribution maxima are 0.084 for ratings, 0.127 for prices, and 0.201 for durations, and pooled Spearman correlations are −0.029/−0.006 for price-rating and −0.222/−0.010 for duration-rating. [→ Bang An 2026](#bang-an-2026)

## Evidence

### Bang An 2026

Bang An, Maria Hamdani, Joseph Fox. (2026). DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education. https://arxiv.org/abs/2609.19617

`q2 · i?` · `design · r2`

Descriptive distributional comparison of the two simulation inputs (Figure 8), using available observations and median-normalized prices and durations. The paper reports maximum empirical cumulative distribution differences of 0.084 (ratings), 0.127 (prices), and 0.201 (durations), and pooled Spearman correlations of −0.029 and −0.006 for price-rating versus −0.222 and −0.010 for duration-rating.

> "Ratings concentrate at four or five stars in both cases: 77.6% in Olist and 79.5% in WindowDash (Figure 8)."

## Discussion


## Related Claims
- [AI agents recover a smaller share of reference patterns from the synthetic WindowDash dataset than from the real-world Olist dataset](agent-pattern-discovery-gap-windowdash-vs-olist.md) — related
- [Designed patterns can rest on very small supporting subgroups: only three orders meet the Price-Rating Sensitivity conditions, with a mean rating of 2.0](windowdash-price-rating-small-subgroup.md) — related
