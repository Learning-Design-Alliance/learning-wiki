---
type: research-method
id: student-level-recency-weighted-proportional-correctness-feature-rkcspfa
title: Student-level recency-weighted proportional correctness feature (RKC,SPFA)
description: "This feature extends Galyardt and Goldin's KC-level proportional decay measure by tracking the recency-weighted proportion of correct responses at the level of the student across KCs."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Student-level recency-weighted proportional correctness feature (RKC,SPFA)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This feature extends Galyardt and Goldin's KC-level proportional decay measure by tracking the recency-weighted proportion of correct responses at the level of the student across KCs. The authors hypothesized this additional feature "could stand in for student learning differences as well as learning transfer across KCs". It requires two ghost attempts (one incorrect, one correct) to center the measure at .5 so it can adapt upward or downward, and the authors have implemented a version in a running system.

## Accounts
<!-- How each source describes or uses the method -->
- **Student-level recency-weighted proportional correctness feature (RKC,SPFA)**: This feature extends Galyardt and Goldin's KC-level proportional decay measure by tracking the recency-weighted proportion of correct responses at the level of the student across KCs. The authors hypothesized this additional feature "could stand in for student learning differences as well as learning transfer across KCs". It requires two ghost attempts (one incorrect, one correct) to center the measure at .5 so it can adapt upward or downward, and the authors have implemented a version in a running system. (Eglington et al. (2022))

### Claims
- [Adding PEV or student-level proportional correctness significantly reduces the absolute value of student-level signed error in all six datasets](../claims/pev-student-proportion-reduce-signed-error.md) [+M]

## Related Research Methods
-

## Key Sources
- Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0
