---
type: claim
title: In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts
description: In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-use...
id: linucb-rct-higher-completion-lower-skip
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: robert-belfer-2022
    resource: "https://doi.org/10.1007/978-3-031-11644-5_74"
    title: "Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)"
    author: Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Free-user students under LinUCB had a success rate of 87.4±1.3% versus 82.4±1.8% under the Heuristic policy, with skip rates of 7.8±0.8% versus 12.5±1.4%. [→ Robert Belfer 2022](#robert-belfer-2022)
`q2 i?` Customer-organization students under LinUCB had a success rate of 88.6±0.9% versus 85.9±0.7% under the Heuristic policy, with skip rates of 5.6±0.4% versus 8.3±0.4%. [→ Robert Belfer 2022](#robert-belfer-2022)

## Evidence

### Robert Belfer 2022

Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)

`q2 · i?` · `causal · r1`

Randomized controlled trial on the Korbit platform with students signing up December 2021–February 2022: 44 free users (21 LinUCB, 23 Heuristic) and 26 customer-organization users (11 LinUCB, 15 Heuristic). Table 1 reports free-cohort success of "87.4±1.3%" vs 82.4±1.8% and customer success of 88.6±0.9% vs 85.9±0.7%; no significance test is printed for these contrasts.

> "As Table 1 demonstrates, the students from both cohorts have a substantially higher success rate underLinUCBthan the adaptive Heuristicmodel.Wealsoobservethatforbothcohorts,studentsunderthe LinUCB policy have a substantially lower skip rate than under the adaptive heuristic baseline."

## Discussion


## Related Claims
- [Students under the LinUCB policy spent more study time on the platform in the free cohort (174 vs 109 minutes), but slightly less in the customer cohort (258 vs 265 minutes)](linucb-study-time-free-cohort-only.md) — related
- [In simulation, the LinUCB policy achieved a higher average success rate (64%) than the Heuristic (60%) and Random (58%) policies on historical student trajectories](linucb-simulation-beats-heuristic-random.md) — related
- [A logistic regression exercise affinity model predicted exercise outcomes with 66% cross-validated accuracy, above a 60% majority-class baseline, and was used to simulate unattempted exercises for bandit pre-training](exercise-affinity-model-66-percent-accuracy.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
