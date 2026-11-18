---
type: research-method
id: active-grade-estimator-age
title: Active Grade Estimator (AGE)
description: AGE is a pool-based active learning model for automated grading systems (AGSs) that integrates LLMs and regression models.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Active Grade Estimator (AGE)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 5 claims rest on one study

## Description
AGE is a pool-based active learning model for automated grading systems (AGSs) that integrates LLMs and regression models. It consists of three major modules: "two-stage sampling, assessment voting, and grading estimation modules". The two-stage query first selects the most contextually similar student answer via cosine similarity, then rewrites it via LLM canonicalization and simplification before teacher annotation. A voting mechanism based on minimum error grading estimation reduces annotation bias from multiple teachers, and a regression model estimates grades for remaining ungraded answers.

## Accounts
<!-- How each source describes or uses the method -->
- **Active Grade Estimator (AGE): a pool-based active learning model for automated short answer grading with two-stage sampling, assessment voting, and grading estimation modules**: AGE is a pool-based active learning model for automated grading systems (AGSs) that integrates LLMs and regression models. It consists of three major modules: "two-stage sampling, assessment voting, and grading estimation modules". The two-stage query first selects the most contextually similar student answer via cosine similarity, then rewrites it via LLM canonicalization and simplification before teacher annotation. A voting mechanism based on minimum error grading estimation reduces annotation bias from multiple teachers, and a regression model estimates grades for remaining ungraded answers. (Mohammad Iqbal et al. (2024))
- **Ability estimation based on acquisition distribution**: The article proposes a statistical method that estimates an examinee's ability as a grade level by connecting test performance to knowledge-acquisition age distributions: the method 'draws a connection b e- tween students' abilities and the acquisition age distrib u- tions'. An examinee has ability theta if s percent of items in a test have been correctly answered, each by r percent of the population. It aggregates item quantile functions via a normal approximation of order statistics and combines current with historical estimates using an Exponential Moving Average, avoiding pre-calibrated item parameters. (Yi-Ting Huang et al. (2012))

### Claims
- [On the mismatch-grade dataset, all models without the voting mechanism diverge, while AGE with VM estimates student answers increasingly precisely](../claims/vm-prevents-divergence-mmg.md) [+M]
- [AGE reduces teacher grading burden by requiring only 1% of student answers in the UNT dataset to be graded](../claims/age-grades-only-one-percent-unt.md) [+W]
- [Instead of cutting answers, the proposed model converges faster than conventional AL and elevates grading up to 30% at the very beginning on the JRL dataset](../claims/age-converges-faster-jrl-30-percent.md) [+W]
- [In simulation the proposed estimation produced more accurate estimated abilities than MLE and Lee's method, with error ranges mostly within two grades](../claims/acquisition-estimation-more-accurate-than-mle-lee-simulation.md) [+W]
- [Estimated abilities correlate positively with post-test scores, with most experimental-group (history-informed) correlation values higher than control-group values](../claims/estimated-ability-posttest-correlation-history.md) [+M]

## Related Research Methods
-

## Key Sources
- Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1
- Yi-Ting Huang, Meng Chang Chen, and Yeali S. Sun. (2012). Bringing personalized learning into computer-aided question generation. https://scholar.google.com/scholar?q=Bringing+personalized+learning+into+computer-aided+question+generation
