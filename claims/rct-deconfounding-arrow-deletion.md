---
type: claim
title: Randomized experiments de-confound by deleting back-door paths, but imperfect compliance can reintroduce confounding
description: Randomized experiments de-confound by deleting back-door paths, but imperfect compliance can reintroduce confounding
id: rct-deconfounding-arrow-deletion
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

# Randomized experiments de-confound by deleting back-door paths, but imperfect compliance can reintroduce confounding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Experimental control works by deleting arrows into the independent variable, but in Hellings & Haelermans (2020) control-group students' non-access to the dashboard left unobserved causes reopening a confounding situation. [→ Weidlich 2022](#weidlich-2022)

## Evidence

### Weidlich 2022

Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577

`q2 · i?` · `theoretical · r3`

The article's explanation of experimental control, illustrated by Hellings & Haelermans (2020), where computer science students were randomly assigned to receive or not receive weekly emails with a learning analytics dashboard. The article notes randomization "was not entirely successful" because some control students refrained from accessing their dashboard for non-random reasons.

> "the de-confounding power of RCTs lies in the ability to eliminate back-door paths by deleting arrows into the independent variable"

## Discussion


## Related Claims
- [Nonexperimental methods incorporating pre-treatment outcome measures can replicate experimental ITT impact estimates when control-group crossover occurs](nonexperimental-pre-treatment-methods-replicate-itt-under-crossover.md) — related
- [Confounding may explain the large retention effects reported for the Course Signals early warning system](course-signals-confounding-number-of-classes.md) — related
- [PN-RCT design choices include random assignment possibilities, cluster formation, statistical power, and confounding factors](pn-rct-design-issues-random-assignment-power-confounding.md) — related
