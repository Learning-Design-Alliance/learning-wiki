---
type: research-method
id: layered-markov-chain-analysis-of-exam-attempt-logs
title: Layered Markov chain analysis of exam-attempt logs
description: "The article introduces \"the method - which transforms the student exam attempt log into a probabilistic graphical representation\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Layered Markov chain analysis of exam-attempt logs

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article introduces "the method - which transforms the student exam attempt log into a probabilistic graphical representation". Exam attempts are aggregated to six exam-period weeks, encoded as quaternary states over three courses (64 states per week, state space of 384), and used to build non-homogeneous layered Markov chains with absorbing final-week states. Graph complexity is measured with a polynomial-based average complexity measure, and graphs are compared with a normalized shortest-path kernel. Edges taken by more than 10% of a group are extracted to reveal predominant patterns.

## Accounts
<!-- How each source describes or uses the method -->
- **Layered Markov chain method transforming exam attempt logs into probabilistic graphs**: The article introduces "the method - which transforms the student exam attempt log into a probabilistic graphical representation". Exam attempts are aggregated to six exam-period weeks, encoded as quaternary states over three courses (64 states per week, state space of 384), and used to build non-homogeneous layered Markov chains with absorbing final-week states. Graph complexity is measured with a polynomial-based average complexity measure, and graphs are compared with a normalized shortest-path kernel. Edges taken by more than 10% of a group are extracted to reveal predominant patterns. (Jakub Kuzilek et al. (2023))

### Claims
- [Successful students' exam-period Markov chains show the lowest graph complexity, with failing students' chains the highest](../claims/successful-students-lowest-markov-complexity.md) [+M]
- [Graph similarity is highest between successful and passing students (0.997) and lowest between successful and failing students (0.954)](../claims/markov-similarity-group-ordering.md) [+M]

## Related Research Methods
-

## Key Sources
- Jakub Kuzilek, Zdenek Zdrahal, Jonas Vaclavek, Viktor Fuglik, Jan Skocilas, Annika Wolff. (2023). First-Year Engineering Students' Strategies for Taking Exams. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00303-4
