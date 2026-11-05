---
type: claim
title: Knowledge-tracing mastery decisions are more equitable than fixed practice but can still under-serve some students when the learner model is fit to the aggregate population or makes wrong assumptions
description: In simulations, knowledge-tracing algorithms were substantially more equitable than giving every student the same amount of practice, but Bayesian knowledge tracing and the N-consecutive-correct heuristic became inequitable when they relied on inaccurate models, while knowledge tracing with the additive factor model may be more equitable.
id: knowledge-tracing-equity-depends-on-model-accuracy
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2019
sources:
  - id: doroudi-2019
    resource: "https://doi.org/10.1145/3303772.3303838"
    title: "Doroudi, S., & Brunskill, E. (2019). Fairer but not fair enough: On the equitability of knowledge tracing. Proceedings of the 9th International Conference on Learning Analytics & Knowledge, 335-339"
    author: "Doroudi, S., & Brunskill, E."
    q: 1
    i: "?"
    kind: theoretical
    rigour: "?"
---

# Knowledge-tracing mastery decisions are more equitable than fixed practice but can still under-serve some students when the learner model is fit to the aggregate population or makes wrong assumptions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r?` · `q1` · n=simulated students (no real learners)
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

Knowledge tracing estimates whether a student has mastered a skill and so decides how much practice each student gets before moving on. This claim is about whether those decisions serve different groups of students equally well, as shown in simulation rather than with real students.

## Subclaims

`q1 i?` In simulations, knowledge-tracing algorithms were substantially more equitable than giving all students the same amount of practice, but could still be inequitable when they relied on inaccurate student models. [→ Doroudi 2019](#doroudi-2019)

`q1 i?` The inequity arose from two sources: student models fit to the aggregate population of students, and student models that make incorrect assumptions about how students learn; Bayesian knowledge tracing and the N-consecutive-correct-responses heuristic were both susceptible, while knowledge tracing with the additive factor model may be more equitable. [→ Doroudi 2019](#doroudi-2019)

## Evidence

### Doroudi 2019

Doroudi, S., & Brunskill, E. (2019). Fairer but not fair enough: On the equitability of knowledge tracing. In *Proceedings of the 9th International Conference on Learning Analytics & Knowledge* (pp. 335-339). ACM. [doi:10.1145/3303772.3303838](https://doi.org/10.1145/3303772.3303838)

`q1 · simulation study` · `i? · no effect size in the abstract` · `n=simulated students (no real learners)` · `theoretical · r?`

A short conference paper that uses simulated students to compare how equitably different mastery-decision algorithms allocate practice: Bayesian knowledge tracing, the N-consecutive-correct-responses heuristic (move on after N correct answers in a row), knowledge tracing with the additive factor model, and a fixed amount of practice for everyone. The authors conclude that designers of learning analytics algorithms need to check explicitly whether an algorithm acts fairly for different populations of students. This entry was written from the published abstract only, because the full text was not available to this ingest; the simulation settings, the student groups compared and any numbers are therefore not recorded here.

## Discussion

For an adaptive course that uses [mastery-based progression](../elements/adaptive-mastery-learning.md), the design consequence is that a single set of knowledge-tracing parameters fitted to all students can give some groups too little or too much practice, even though it does better than fixed practice. The finding comes from simulation, so it shows the mechanism can occur, not how large the gap is with real learners.

## Related Claims
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](bkt-most-efficient-online-mastery-learning.md) — another simulation comparison of knowledge-tracing approaches for mastery decisions
