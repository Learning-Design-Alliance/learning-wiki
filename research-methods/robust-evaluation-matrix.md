---
type: research-method
id: robust-evaluation-matrix
title: Robust Evaluation Matrix (REM)
description: "A way to estimate before an experiment whether a new instructional policy is likely to help students, by simulating it under several plausible student models rather than only the one used to derive it."
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
---

# Robust Evaluation Matrix (REM)

> **Research Method** · [All research methods](index.md)

## Description
The robust evaluation matrix (REM) is a method for offline evaluation of instructional policies, such as new ways to sequence existing material in a tutoring system. Student models fitted to earlier data can be used as simulators to estimate how learners would do under a proposed policy, but the abstract notes that existing methods for doing so "can overestimate the performance of new teaching methods". REM addresses this by explicitly considering model mismatch: each candidate policy, including one derived from a particular student model, is evaluated by simulation under other plausible student models as well, so a policy is favoured only if it looks better across models rather than under the model it was optimised for. It is meant to be used before running an experiment with real students, to decide whether a new policy is worth testing. It applies only to the kinds of change a student model can simulate, such as reordering existing material, and it is limited by the set of models considered.

## Accounts
<!-- How each source describes or uses the method -->
- **REM: evaluating a teaching strategy under student models other than the one used to derive it**: The authors argue that experiments are the gold standard but costly, that a hypothesised improvement often does not yield an improved effect, and that this holds even at scale because each experiment affects many real students. They propose REM, "which explicitly considers model mismatch between the student model used to derive the teaching strategy and that used as a simulator to evaluate the teaching strategy effectiveness", and present two case studies, one from a fractions intelligent tutoring system and one from a concept-learning task from prior work, showing how it could detect when a new instructional policy may not be effective on actual students and when it may improve learning. (Doroudi, Aleven & Brunskill (2017); described here from the published abstract, as the full text was not available to this ingest)

### Claims

## Related Research Methods
- [KT-grounded simulated learner](kt-grounded-simulated-learner.md) — another use of a fitted student model as a simulator
- [Turing-like validation criterion for simulated learners](turing-like-validation-criterion-for-simulated-learners.md) — validating the simulated learners such evaluations rely on

## Key Sources
- Doroudi, S., Aleven, V., & Brunskill, E. (2017). Robust evaluation matrix: Towards a more principled offline exploration of instructional policies. In *Proceedings of the Fourth (2017) ACM Conference on Learning @ Scale* (pp. 3-12). ACM. [doi:10.1145/3051457.3051463](https://doi.org/10.1145/3051457.3051463)
