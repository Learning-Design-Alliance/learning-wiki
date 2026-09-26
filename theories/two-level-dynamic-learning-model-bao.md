---
type: theory
title: Two-level measurement-based dynamic model of learning with α, β, and γ transition processes
description: "The article models a student's measured knowledge as a two-level system in which the measured-correct level holds the score and the measured-wrong level holds its complement."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: lei-bao-2006
    resource: "https://arxiv.org/abs/physics/0606141"
    title: "Lei Bao. (2006). Dynamic Models of Learning and Education Measurement. https://arxiv.org/abs/physics/0606141"
    author: Lei Bao
---

# Two-level measurement-based dynamic model of learning with α, β, and γ transition processes

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (6 for) · 1 study, `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article models a student's measured knowledge as a two-level system in which the measured-correct level holds the score and the measured-wrong level holds its complement. Learning incidents cause transitions between levels, with three processes: α-type changes driven by instruction acting on wrong knowledge, β-type changes acting on correct knowledge, and γ-type associative changes from internal interactions between correct and incorrect knowledge. The dynamics are expressed as differential equations, e.g. the overall form ds_k/dt = α_k s_k(1−s_k) + β_k s_k + γ_k s_k(1−s_k). The article states it is a measurement-based probabilistic model that 'doesn't model any cognitive processes of how the learning occurs'.

## Design Implications

### Context
#### Requirements
- Scores scaled to 0–1 with a fixed measurement window defining the instrument's coverage of the knowledge domain
#### Constraints
- The model treats guessing and general mistakes as random errors not included in the transition processes
- The β-process is assumed to have a very small success rate in current education settings and is not analyzed in detail
- The model does not describe actual cognitive processes of learning, only probabilistic relations between measured states

### Target Learners
- physics students in pre-post assessed courses

### Target Learning Objectives
- conceptual knowledge gains measured by pre-post testing

### Claims

- [FCI change-score versus pretest-score data from three classes show linear relations at high pretest scores and curving-down at low scores, diagnosable as α- versus γ-process dominance](../claims/fci-change-score-curves-diagnose-processes.md) [+M]
- [When the γ-process (associative interaction of correct and incorrect knowledge) is considered, the normalized gain correlates positively with pretest score](../claims/gamma-process-positive-gain-pretest-correlation.md) [+M]
- [Hake's survey found interactive-engagement courses achieved average normalized gains about two standard deviations greater than traditional courses, with overall gain–pretest correlation of +0.02](../claims/hake-ie-gains-two-sd-greater.md) [+M]
- [High-ability students' learning behaves as a dominant α-process even at low pretest scores, while average-ability students show more γ-process behavior](../claims/high-ability-alpha-dominant-low-pretest.md) [+W]
- [Random measurement noise in pretest scores produces a negative contribution to the correlation between normalized gain and pretest score](../claims/measurement-noise-negative-gain-pretest-correlation.md) [+W]
- [Under a dominant α-process, the normalized gain contains no pretest-score term and is uncorrelated with pretest score if α is uncorrelated with pretest score](../claims/normalized-gain-pretest-uncorrelated-alpha-process.md) [+M]

## Related Theories

- [Generalized non-constant α model framing learning as an error-reduction process](non-constant-alpha-error-reduction-model.md)

## Examples

- [Fit change-score versus pretest-score data with α and γ process models to diagnose learning processes and distinguish student ability from instruction impact](../strategies/fit-change-score-curves-to-diagnose-learning.md)

## Key Sources
- Lei Bao. (2006). Dynamic Models of Learning and Education Measurement. https://arxiv.org/abs/physics/0606141
