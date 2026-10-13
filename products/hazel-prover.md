---
type: product
id: hazel-prover
title: Hazel Prover
description: Hazel Prover is a web-based classroom proof assistant developed as an extension to the Hazel live typed functional programming environment for teaching equational and inductive reasoning about typed functional programs.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Hazel Prover

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (2 for, 1 mixed, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Hazel Prover is a web-based classroom proof assistant developed as an extension to the Hazel live typed functional programming environment for teaching equational and inductive reasoning about typed functional programs.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Hazel Prover, a web-based classroom proof assistant for equational and inductive reasoning about typed functional programs**: Hazel Prover is "implemented as an extension to Hazel, a live typed functional programming environment". Students interleave programs and theorem specifications in the Hazel editor; theorem constructs appear as proof obligations at the bottom of the screen. Students highlight sub-expressions and choose to rewrite or perform an induction, with evaluation steps, algebra steps checked by an external computer algebra checker, and assumption steps. There is no proof-assistant-specific syntax; all proof logic is expressed via a graphical user interface, and proofs are laid out similarly to written proofs. (Matthew Keenan et al. (2026))

### Claims

- [Student backtracking before setting up the correct induction decreased across exercises in both deployments, indicating a learning curve](../claims/backtracking-decreases-across-exercises.md) [+W]
- [Students backtracked far more before applying the inductive hypothesis than after, suggesting difficulty finding where to place it](../claims/backtracking-higher-before-inductive-hypothesis.md) [~W]
- [After the design iteration, no student deleted an evaluation step, in contrast to frequent step deletion in the first deployment](../claims/no-evaluation-step-deletion-second-deployment.md) [+W]
- [In the first deployment, exam scores on the induction question were visibly lower than in previous semesters taught without the tool](../claims/first-deployment-exam-scores-lower.md) [-W]

## Related Products and Programmes
-

## Key Sources
- Matthew Keenan, Nishant Kheterpal, Jean-Baptiste Jeannin, Cyrus Omar. (2026). Hazel Prover: A Classroom Proof Assistant for Learning Structural Induction. https://arxiv.org/abs/2608.23309
