---
type: claim
title: A computational model of learning reproduced the direction of two tutor A/B experiments without human training data, but not students' absolute performance
description: Simulated learners trained only on the tutors' task structure showed the same main effects as students in a blocked-versus-interleaved fractions experiment and a constrained-versus-unconstrained problem-design experiment, while over-predicting early errors where students had prior knowledge.
id: computational-learner-model-predicts-tutor-experiment-direction
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: maclellan-2025
    resource: "https://doi.org/10.48550/arXiv.2502.02456"
    title: "MacLellan, C. J. (2025). Model human learners: Computational models to guide instructional design. *arXiv preprint* arXiv:2502.02456 (v4). [doi:10.48550/arXiv.2502.02456](https://doi.org/10.48550/arXiv.2502.02456)"
    author: MacLellan, C. J.
    q: 2
    i: "?"
    n: 78 and 202 students
    kind: design
    rigour: 2
---

# A computational model of learning reproduced the direction of two tutor A/B experiments without human training data, but not students' absolute performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=78 and 202 students
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

The paper proposes a "Model Human Learner": a computational model of learning that a designer could run to compare candidate interventions before testing them on people. This claim is about how well one such model predicted the outcomes of two experiments already run with students.

## Subclaims

`q2 i?` Re-running a blocked-versus-interleaved fractions tutor experiment with simulated agents reproduced its pattern: students in the interleaved condition did worse during practice (odds ratio 0.50) and better on the posttest (odds ratio 2.35), and so did the agents (odds ratios 0.40 and 7.75), each p < 0.05. [→ MacLellan 2025](#maclellan-2025)

`q2 i?` In a problem-design experiment where only the correct procedure gave a whole-number answer, students given unconstrained problems were less likely to solve the hard problems (odds ratio 0.17, 95% CI [0.08, 0.37]) and so were the agents (odds ratio 0.46, 95% CI [0.37, 0.56]); accuracy was close in level, 19.1% for students and 19.6% for agents with constrained problems and 8.8% and 10% with unconstrained ones. [→ MacLellan 2025](#maclellan-2025)

`q2 i?` The model predicted direction, not level, where students arrived with prior knowledge: in the fractions tutor students' average first-problem error was 53.8% while the agents, which start with no fraction knowledge, erred 100% of the time. [→ MacLellan 2025](#maclellan-2025)

## Evidence

### MacLellan 2025

MacLellan, C. J. (2025). Model human learners: Computational models to guide instructional design. *arXiv preprint* arXiv:2502.02456 (v4). [doi:10.48550/arXiv.2502.02456](https://doi.org/10.48550/arXiv.2502.02456)

`q2 · model predictions compared with two archived randomised experiments` · `i? · odds ratios only, no standardised effect` · `n=78 and 202 students` · `design · r2`

A preprint (not peer reviewed) in which agents built on the [Apprentice Learner Architecture](../products/apprentice-learner-architecture.md) learn from worked examples and correctness feedback in machine-readable copies of two tutors, and their results are compared with archived DataShop data. Study 1 used a fraction arithmetic experiment that randomly assigned students to blocked or [interleaved](interleaving-improves-inductive-learning.md) problem order (tutor data for 78 students and posttest data for 71 after removing corrupted records); Study 2 used a Mechanical Turk experiment with 202 learners on a box-and-arrows rule-discovery task, comparing constrained and unconstrained problems, analysed on the 16 hard problems. Both were analysed with mixed-effect logistic regression; the agents' copy of the fractions tutor differed in showing the conversion fields from the start, which the author reports agents rarely exploited. Because agents compute whole and fractional numbers equally easily yet showed the constrained-problem benefit, the author argues against the original authors' explanation (easier computation) and proposes lower procedural ambiguity instead, which the paper says needs further research.

## Discussion

The design reading is that a simulated learner may be useful for screening which of two task orders or item designs is likely to help, but its absolute predictions are off wherever learners bring prior knowledge the model lacks, and the agreement shown is for two experiments, both of whose outcomes were already known. The author's proposed design rule from Study 2 (write items so only one candidate procedure yields a plausible answer) is a hypothesis from the model, not a tested finding.

## Related Claims
- [Apprentice learner models act as a check against expert blind spots because they start without target skills](apprentice-learner-models-check-expert-blind-spots.md) — the same architecture used for tutor authoring
- [In SimStudent simulations across three math and science domains, interleaved-order curricula yielded as effective or more effective learning than blocked-order curricula](simstudent-interleaved-as-or-more-effective.md) — an earlier simulated-learner test of problem order
