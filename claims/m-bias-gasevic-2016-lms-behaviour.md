---
type: claim
title: Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success
description: Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success
id: m-bias-gasevic-2016-lms-behaviour
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

# Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` In the Gašević et al. (2016) analysis, conditioning on ESAP inclusion may have opened a spurious back-door path between student behaviour and student success, yielding M-bias. [→ Weidlich 2022](#weidlich-2022)

## Evidence

### Weidlich 2022

Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577

`q2 · i?` · `theoretical · r3`

The article's tentative DAG analysis of Gašević et al. (2016), a large analysis (N=4134) of LMS behaviours predicting grades and course pass/fail across nine ESAP courses, argues course-level selection on prior retention produced an M-bias configuration. It cites the printed negative association between accessing the LMS feature "book" and student percent marks for some courses as potentially explicable by this bias.

> "This would introduce spurious associations between student behaviour and student success and could help explain some of the difficult-to-interpret negative associations between student behaviour and student success"

## Discussion


## Related Claims
- [Sample truncation based on at-risk status can induce collider bias that undermines internal as well as external validity](collider-bias-sample-truncation-at-risk.md) — a broader claim this one bears on
- [Restricting a sample to students who used the treatment can block a mediating path and induce overcontrol bias, attenuating estimated effects](overcontrol-bias-blocking-mediator.md) — related
