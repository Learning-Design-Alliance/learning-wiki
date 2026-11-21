---
type: research-method
id: log-based-classwork-session-inference-using-inactivity-thresholds-and-active-student-count
title: Log-based classwork session inference using inactivity thresholds and active-student counts
description: "Algorithm 1 infers classwork sessions from DLP transaction logs along two dimensions: a minimum of five active students (to distinguish classwork from individual or small-group use) and a temporal inactivity threshold."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Log-based classwork session inference using inactivity thresholds and active-student counts

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Algorithm 1 infers classwork sessions from DLP transaction logs along two dimensions: a minimum of five active students (to distinguish classwork from individual or small-group use) and a temporal inactivity threshold. After a sensitivity analysis of thresholds between 2 and 30 minutes, the authors "select 7.5 minutes as the threshold to infer classwork sessions." The algorithm is deliberately simple, requiring minimal calibration, and the authors state it "can be applied to any system that logs student engagement data."

## Accounts
<!-- How each source describes or uses the method -->
- **Algorithm 1: log-based classwork session inference using inactivity threshold and active-student count**: Algorithm 1 infers classwork sessions from DLP transaction logs along two dimensions: a minimum of five active students (to distinguish classwork from individual or small-group use) and a temporal inactivity threshold. After a sensitivity analysis of thresholds between 2 and 30 minutes, the authors "select 7.5 minutes as the threshold to infer classwork sessions." The algorithm is deliberately simple, requiring minimal calibration, and the authors state it "can be applied to any system that logs student engagement data." (Ashish Gurung et al. (2025))

### Claims
- [Session-level time-based measures of classwork engagement show moderate-to-high month-to-month reliability, comparable to or exceeding gaming tendency](../claims/session-level-measures-moderate-high-reliability.md) [+M]

## Related Research Methods
-

## Key Sources
- Ashish Gurung, Jionghao Lin, Zhongtian Huang, Conrad Borchers, Ryan S. Baker, Vincent Aleven, Kenneth R. Koedinger. (2025). Starting Seatwork Earlier as a Valid Measure of Student Engagement. arXiv. https://arxiv.org/abs/2505.13341
