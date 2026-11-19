---
type: claim
title: Students under the LinUCB policy spent more study time on the platform in the free cohort (174 vs 109 minutes), but slightly less in the customer cohort (258 vs 265 minutes)
description: Students under the LinUCB policy spent more study time on the platform in the free cohort (174 vs 109 minutes), but slightly less in the customer cohort (258 vs 265 minutes)
id: linucb-study-time-free-cohort-only
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
newest_evidence: 2022
sources:
  - id: robert-belfer-2022
    resource: "https://doi.org/10.1007/978-3-031-11644-5_74"
    title: "Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)"
    author: Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Students under the LinUCB policy spent more study time on the platform in the free cohort (174 vs 109 minutes), but slightly less in the customer cohort (258 vs 265 minutes)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Free-cohort students under LinUCB averaged 174 minutes of study time versus 109 minutes under the Heuristic, while customer-cohort students averaged 258 versus 265 minutes. [→ Robert Belfer 2022](#robert-belfer-2022)

## Evidence

### Robert Belfer 2022

Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)

`q2 · i?` · `causal · r2`

Study-time measure from the same randomized controlled trial, reported separately per cohort. The free cohort shows "174minutes" under LinUCB versus 109 under Heuristic; the customer cohort shows 258 versus 265 minutes, a slight decrease under LinUCB. No statistical test is printed.

> "the average study time under the adaptiveHeuristicmodel is109 minutes, and the average study time under theLinUCBpolicy is174minutes. For the students in the customer cohort, the average study time under the adaptiveHeuristicis 265minutes, and the average study time under theLinUCBpolicy is258 minutes."

## Discussion


## Related Claims
- [In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts](linucb-rct-higher-completion-lower-skip.md) — related
- [Platform B participants spent 2.23 times more time on active learning activities (solving exercises) than Platform A participants](platform-b-more-active-learning-time.md) — related
