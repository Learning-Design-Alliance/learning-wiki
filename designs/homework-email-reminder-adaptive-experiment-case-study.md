---
type: design
id: homework-email-reminder-adaptive-experiment-case-study
title: Three-week homework email reminder adaptive experiment with four email versions and daily batches
description: "A real-world field deployment in which \"For three consecutive weeks, we tested four diﬀerent versions of the emails\" to investigate which version led students to click the homework link appended to the email."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: zavaleta-bernuy-2022
    resource: "https://arxiv.org/abs/2208.05092"
    title: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2022). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. https://arxiv.org/abs/2208.05092"
    author: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J"
---

# Three-week homework email reminder adaptive experiment with four email versions and daily batches

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A real-world field deployment in which "For three consecutive weeks, we tested four diﬀerent versions of the emails" to investigate which version led students to click the homework link appended to the email. Messages were sent in four batches on consecutive days (Tuesday to Friday), with uniform random assignment and two TS variants: an epsilon[0.5]-TS hybrid in Weeks 1 and 2 and traditional TS in Week 3. The article presents this as a case study on how to conduct adaptive experiments in education.

## Design Implications

### Context
#### Requirements
- Digital educational environments that allow sending intervention messages in batches and recording click outcomes
#### Constraints
- The case study concerns a setting where no difference between arms was observed

### Target Learners
- students in a course receiving homework reminder emails

### Learning Goals
- prompting students to click the homework link and complete homework

### Claims
- [Homework Email Versions No Click Rate Difference](../claims/homework-email-versions-no-click-rate-difference.md) [+M]
- [Ts Drastic Shift Inconsistent Favoured Arm](../claims/ts-drastic-shift-inconsistent-favoured-arm.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2022). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. https://arxiv.org/abs/2208.05092
