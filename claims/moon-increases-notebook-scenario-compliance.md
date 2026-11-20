---
type: claim
title: "MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario"
description: "MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario"
id: moon-increases-notebook-scenario-compliance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: christophe-casseau-2023
    resource: "https://doi.org/10.1109/vl-hcc57772.2023.00026"
    title: "Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. [doi:10.1109/vl-hcc57772.2023.00026](https://doi.org/10.1109/vl-hcc57772.2023.00026)"
    author: Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` In a randomized controlled experiment, students using MOON executed far fewer out-of-scenario (red) cells than control students, with fitness near 1 versus about 0.25–0.75 in the control group. [→ Christophe Casseau 2023](#christophe-casseau-2023)

## Evidence

### Christophe Casseau 2023

Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. [doi:10.1109/vl-hcc57772.2023.00026](https://doi.org/10.1109/vl-hcc57772.2023.00026)

`q3 · i?` · `causal · r2`

A/B testing controlled experiment with 21 first-year bachelor students (11 control, 10 experimental) during a graph-theory practical session; log traces of cell executions were replayed offline to compute fitness. The article reports the Mann-Whitney U test yields "a p-value p = 0.000122 and an effect size rbc = −1", favoring the MOON group.

> "The fitness in the control group varies between about 0.25 (meaning only a quarter of the executions are in a green or orange cell) to about 0.75. In the experimental group, the fitness values are very close to 1 for all traces"

## Discussion


## Related Claims
- [Notebook grades (correctness) do not differ significantly between MOON and control groups, though descriptively higher with MOON](moon-correctness-no-significant-difference.md) — related
- [Most surveyed students perceived MOON as useful and reported it helped them follow the execution order](moon-user-study-perceived-usefulness.md) — related
- [MOON does not hinder students' progression through the notebook (no significant completeness difference)](moon-no-completeness-hindrance.md) — related
