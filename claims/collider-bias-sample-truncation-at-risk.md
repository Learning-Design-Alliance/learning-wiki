---
type: claim
title: Sample truncation based on at-risk status can induce collider bias that undermines internal as well as external validity
description: Sample truncation based on at-risk status can induce collider bias that undermines internal as well as external validity
id: collider-bias-sample-truncation-at-risk
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: weidlich-2022
    resource: "https://doi.org/10.18608/jla.2022.7577"
    title: "Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577"
    author: Weidlich, J., Gašević, D., Drachsler, H.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Sample truncation based on at-risk status can induce collider bias that undermines internal as well as external validity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Sampling only at-risk students makes estimates biased with respect to the variables of interest because causes of at-risk status are themselves causal factors for those variables. [→ Weidlich 2022](#weidlich-2022)

## Evidence

### Weidlich 2022

Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577

`q2 · i?` · `theoretical · r3`

The article's general argument from its section on collider bias by sample truncation: causes of at-risk status are causal factors for the variables of interest, so a sample truncated on them is biased. It recommends estimating effects on samples not truncated on the unobserved antecedents, e.g., by extending an initiative to all courses or a randomized subset.

> "sample truncation may also lead to inferences that themselves are biased, thus lacking not only external but also internal validity"

## Discussion


## Related Claims
- [The study's invariance findings may be biased by excluding students who missed a test and by sample heterogeneity](map-invariance-study-sample-bias-limitations.md) — related
- [Filtered students had much lower effort-moderated achievement, suggesting motivation filtering may bias mean estimates](filtering-removes-low-achievers-bias-risk.md) — related
- [Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success](m-bias-gasevic-2016-lms-behaviour.md) — a narrower finding that bears on this claim
