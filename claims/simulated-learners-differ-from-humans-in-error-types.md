---
type: claim
title: Simulated learners can match human error rates overall while learning faster and making different kinds of errors than the students they model
description: Apprentice Learner agents trained on the same fraction-tutor problems as 117 students learned about twice as fast per opportunity, made input and selection errors in a different ratio, and asked for hints more often early on, so matching aggregate error curves alone hides how a simulated learner differs from humans.
id: simulated-learners-differ-from-humans-in-error-types
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2020
sources:
  - id: weitekamp-2020
    resource: "https://doi.org/10.1007/978-3-030-52237-7_47"
    title: "Weitekamp, D., Ye, Z., Rachatasumrit, N., Harpstead, E., & Koedinger, K. (2020). Investigating differential error types between human and simulated learners. In I. I. Bittencourt, M. Cukurova, K. Muldner, R. Luckin, & E. Millán (Eds.), *Artificial Intelligence in Education (AIED 2020)*, Lecture Notes in Computer Science, vol. 12163 (pp. 586-597). Springer. [doi:10.1007/978-3-030-52237-7_47](https://doi.org/10.1007/978-3-030-52237-7_47)"
    author: "Weitekamp, D., Ye, Z., Rachatasumrit, N., Harpstead, E., & Koedinger, K."
    q: 2
    i: "?"
    n: 117 students
    kind: design
    rigour: 2
---

# Simulated learners can match human error rates overall while learning faster and making different kinds of errors than the students they model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=117 students
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

Simulated learners are computational agents that learn from a tutoring system the way a student does, and are proposed for testing tutors, authoring them and giving teachers practice. This claim is about how faithfully one such system reproduces real students' errors, which bears on how far a design decision can rest on a simulated learner's behaviour.

## Subclaims

`q2 i?` Apprentice Learner agents learned faster per practice opportunity than the 117 students they were matched to in a fraction-arithmetic tutor: the slope of the fitted learning curve, averaged over skills, was 2.1 times the human slope for both agent configurations. [→ Weitekamp 2020](#weitekamp-2020)

`q2 i?` Split by error type, the agents differed from humans in ways an aggregate error curve hides: their ratio of input errors (a wrong value on a correct step) to selection errors (working on the wrong step) was about 1.1 against 1.7 for the students, and in the first five opportunities hint requests made up 26% of errors for one agent configuration and 8% for the other, against 5% for the students. [→ Weitekamp 2020](#weitekamp-2020)

`q2 i?` A new way of pre-training agents to stand for students' unobserved prior knowledge matched the human first-opportunity error rate to within less than 0.1% for one configuration and left it 4% lower for the other, against an 11% discrepancy reported by earlier work on the same data. [→ Weitekamp 2020](#weitekamp-2020)

## Evidence

### Weitekamp 2020

Weitekamp, D., Ye, Z., Rachatasumrit, N., Harpstead, E., & Koedinger, K. (2020). Investigating differential error types between human and simulated learners. In I. I. Bittencourt, M. Cukurova, K. Muldner, R. Luckin, & E. Millán (Eds.), *Artificial Intelligence in Education (AIED 2020)*, Lecture Notes in Computer Science, vol. 12163 (pp. 586-597). Springer. [doi:10.1007/978-3-030-52237-7_47](https://doi.org/10.1007/978-3-030-52237-7_47)

`q2 · model-to-human comparison on classroom tutor logs` · `i? · no effect size` · `n=117 students` · `design · r2`

The authors trained simulated learners built with the [Apprentice Learner Architecture](../products/apprentice-learner-architecture.md), in two configurations (a decision-tree and a Trestle concept-formation mechanism for deciding when a skill applies), on the same problems that 117 students solved in a classroom study of a fraction addition and multiplication tutor (DataShop project 243). Each agent was first pre-trained to approximate its student's prior knowledge. They then compared learning curves for overall errors and, using a new method, separately for hint requests, selection errors and input errors. The comparison is descriptive: no significance tests or effect sizes are reported, and the authors use the differences to suggest changes to the model (for example a memory or forgetting mechanism, or plausible guessing when no skill applies) rather than as a test of an instructional choice.

## Discussion

The authors argue that a simulated learner should be judged on whether it reproduces each type of error over time, not only the overall error rate, and that one matching humans on all three error types is a stronger model of human learning. For a designer using simulated learners to try out a tutor or a problem sequence, the practical point is that agents in this study improved about twice as fast per opportunity and made a different mix of errors from real students, so predictions about how much practice students need, or which errors a tutor must handle, would not transfer directly. Agents also start with no domain knowledge, so matching students who arrive with some requires an estimate of prior practice.

## Related Claims
- [Apprentice learner models act as a check against expert blind spots because they start without target skills](apprentice-learner-models-check-expert-blind-spots.md) — the same architecture used for tutor authoring
- [Simulated learner models in the reviewed literature tend to represent only narrow aspects of student learning.](simulated-learners-models-narrow-aspects.md) — the broader state of simulated-learner validity
