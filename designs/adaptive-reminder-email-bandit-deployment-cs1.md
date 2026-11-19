---
type: design
id: adaptive-reminder-email-bandit-deployment-cs1
title: Adaptive multi-armed bandit deployment of weekly reminder emails in a first-year CS1 course
description: A 13-week field deployment in a first-year CS1 course, where weekly reminder emails nudged students to start homework early and three subject-line arms were assigned by uniform random, Thompson Sampling, and TS† algor...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: yanez-2022
    resource: "https://arxiv.org/abs/2208.05090"
    title: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. https://arxiv.org/abs/2208.05090"
    author: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J"
---

# Adaptive multi-armed bandit deployment of weekly reminder emails in a first-year CS1 course

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A 13-week field deployment in a first-year CS1 course, where weekly reminder emails nudged students to start homework early and three subject-line arms were assigned by uniform random, Thompson Sampling, and TS† algorithms. The article reports "There were initially 1119 students enrolled in the course, with a ﬁnal count of 1025 by the end of the term." Email open rate served as the engagement measure.

## Design Implications

### Context
#### Requirements
- Weekly emails sent on the same day and time every week, with data from the previous week used to allocate subject lines for the coming week.
#### Constraints
- Conducted on a single CS1 course; the authors note it may not be representative across domains.

### Target Learners
- first-year university CS1 students

### Learning Goals
- building time management habits
- starting weekly homework early
- engaging with instructor reminder emails

### Claims
- [No Significant Difference Email Subject Line Arm Means](../claims/no-significant-difference-email-subject-line-arm-means.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. https://arxiv.org/abs/2208.05090
