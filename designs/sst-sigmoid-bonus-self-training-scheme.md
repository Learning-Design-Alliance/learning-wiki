---
type: design
id: sst-sigmoid-bonus-self-training-scheme
title: Student Self-Training (SST) scheme with sigmoidally weighted homework bonus
description: The SST scheme motivates voluntary, unsupervised multiple-choice homework by adding homework points to the mid-term grade through a sigmoid weight C(Gm) = (1 + tanh(αGm))/2, so that Fm = Gm + C(Gm)×Gh.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: gl-lippi-2018
    resource: "https://arxiv.org/abs/1809.04968"
    title: "G.L. Lippi. (2018). Multiple choice homework as a cost-effective and efficient tool for student self-training. arXiv. https://arxiv.org/abs/1809.04968"
    author: G.L. Lippi
---

# Student Self-Training (SST) scheme with sigmoidally weighted homework bonus

> **Design** · [All designs](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The SST scheme motivates voluntary, unsupervised multiple-choice homework by adding homework points to the mid-term grade through a sigmoid weight C(Gm) = (1 + tanh(αGm))/2, so that Fm = Gm + C(Gm)×Gh. Because the weight is near zero for low mid-term grades and rises steeply between Gm = 0.25 and Gm = 0.75, copied homework yields no benefit (C ≈ 0 for weak exam performance), which the author describes as rendering cheating useless. The scheme targets technical and mathematical skills, not concept acquisition.

## Design Implications

### Context
#### Requirements
- Homework must be computer-gradable so instructor time stays low
- A supervised mid-term test must exist to weight the bonus against
- Exercises must match the calculations appearing in course-related problems
#### Constraints
- The homework is unsupervised and cheating cannot be detected; the scheme only makes it unprofitable
- SST is not a technique for presenting and acquiring concepts and does not compete with approaches such as the inverted classroom
- Developed for mathematical skills in Physics; extension to weekly course homework is only envisaged

### Target Learners
- undergraduate Physics students with insufficient mathematical background in non-selecting universities

### Learning Goals
- quantitative problem-solving and mathematical skills in fundamental sciences

### Claims

- Sst Training Gain 010 Bonus 003 [+M]
- [Sst Homework Participants Gain 013 Nonparticipants 002](../claims/sst-homework-participants-gain-013-nonparticipants-002.md) [+M]
- [Only 21 of 68 enrolled students chose to return the voluntary homework](../claims/sst-low-uptake-21-of-68.md) [~W]
- [Homework participants scored sensibly higher on the initial level test (0.39 vs 0.31), suggesting self-selection into the scheme](../claims/sst-level-test-self-selection-039-vs-031.md) [~W]
- [Class averages fluctuated little across the four cohorts 2014-15 to 2017-18, arguing against cohort or test-difficulty bias](../claims/sst-cohort-averages-stable-across-years.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- G.L. Lippi. (2018). Multiple choice homework as a cost-effective and efficient tool for student self-training. arXiv. https://arxiv.org/abs/1809.04968
