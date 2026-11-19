---
type: claim
title: "In simulation, the LinUCB policy achieved a higher average success rate (64%) than the Heuristic (60%) and Random (58%) policies on historical student trajectories"
description: "In simulation, the LinUCB policy achieved a higher average success rate (64%) than the Heuristic (60%) and Random (58%) policies on historical student trajectories"
id: linucb-simulation-beats-heuristic-random
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: robert-belfer-2022
    resource: "https://doi.org/10.1007/978-3-031-11644-5_74"
    title: "Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)"
    author: Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# In simulation, the LinUCB policy achieved a higher average success rate (64%) than the Heuristic (60%) and Random (58%) policies on historical student trajectories

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Simulating every student under each policy 20 times, LinUCB reached 64% average success rate versus 60% for Heuristic and 58% for Random. [→ Robert Belfer 2022](#robert-belfer-2022)

## Evidence

### Robert Belfer 2022

Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)

`q1 · i?` · `causal · r1`

Simulation on the historical dataset of 129,000 exercise attempts from 1,977 students, with unattempted exercises filled by predictions from the exercise affinity model; each policy was simulated 20 times due to randomness. The article reports "64%for LinUCB" versus 60% Heuristic and 58% Random, with run-to-run deviation of no more than 0.5%.

> "We observe an average success rate of58%for theRandompolicy,60%for the Heuristicpolicy, and64%for LinUCB. These values are consistent throughout each run, deviating by no more than0.5%."

## Discussion


## Related Claims
- [In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts](linucb-rct-higher-completion-lower-skip.md) — related
