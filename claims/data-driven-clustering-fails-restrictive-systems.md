---
type: claim
title: Data-driven and hybrid trace clustering failed to separate study from no-study traces and normal from short attempts in a restrictive system
description: Data-driven and hybrid trace clustering failed to separate study from no-study traces and normal from short attempts in a restrictive system
id: data-driven-clustering-fails-restrictive-systems
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: tom-zhang-2022
    resource: "https://doi.org/10.1145/3506860.3506887"
    title: Tom Zhang 2022
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Data-driven and hybrid trace clustering failed to separate study from no-study traces and normal from short attempts in a restrictive system

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Clusters from pure data and hybrid methods grouped traces with and without study events together and could not distinguish normal from short attempts. [→ Tom Zhang 2022](#tom-zhang-2022)

## Evidence

### Tom Zhang 2022

Tom Zhang, Michelle Taub, and Zhongzhou Chen. 2022. A Multi-level Trace Clustering Analysis Scheme for Measuring Students' Self-Regulated Learning Behavior in a Mastery-Based Online Learning Environment. In LAK22: 12th International Learning Analytics and Knowledge Conference (LAK22). ACM, New York, NY, USA. [doi:10.1145/3506860.3506887](https://doi.org/10.1145/3506860.3506887)

`q2 · i?` · `design · r2`

Process maps generated for clusters from the INDEL (pure data) and hybrid cost-matrix methods showed that traces both with and without a study event fell in the same cluster, and the pure data method "cannot distinguish between normal and short assessment attempts," features the authors deem essential for interpreting SRL strategies.

> "For all the clusters identified by either the pure data or the hybrid methods, the corresponding process maps (PMs) show that traces both with and without a study event are grouped into the same cluster, as shown in the example PM in Figure 3. Furthermore, the pure data method also cannot distinguish between normal and short assessment attempts."

## Discussion


## Related Claims
- [In a restrictive mastery-based online learning system, a purely theory-based distance metric produced better module-level trace clusters than data-driven and hybrid metrics](theory-based-distance-metric-outperforms-data-driven-clustering.md) — possibly the same claim (merge candidate)
- [Students overwhelmingly studied immediately after their first failed attempt, consistent with reflection or planned learning rather than failure-driven study](study-immediately-after-first-attempt.md) — related
