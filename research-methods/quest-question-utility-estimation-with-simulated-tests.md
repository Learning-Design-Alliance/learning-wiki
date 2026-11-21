---
type: research-method
id: quest-question-utility-estimation-with-simulated-tests
title: QUEST (Question Utility Estimation with Simulated Tests)
description: "QUEST (Question Utility Estimation with Simulated Tests) quantifies a question's utility as its marginal contribution to a simulated learner's exam score."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# QUEST (Question Utility Estimation with Simulated Tests)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
QUEST (Question Utility Estimation with Simulated Tests) quantifies a question's utility as its marginal contribution to a simulated learner's exam score. An LM question generator produces questions grounded in document sections, an answer generator answers them, a learner simulator attempts the exam using only the QA pairs, and a utility estimator compares scores with and without each pair. The authors define question utility as "the direct impact of a question-answer (QA) pair on a learner's understanding, measured by simulated exam performance improvement", and retain pairs with utility above a threshold to refine the generator via rejection sampling.

## Accounts
<!-- How each source describes or uses the method -->
- **QUEST: an outcome-driven framework estimating question utility via LM-simulated learner exam performance**: QUEST (Question Utility Estimation with Simulated Tests) quantifies a question's utility as its marginal contribution to a simulated learner's exam score. An LM question generator produces questions grounded in document sections, an answer generator answers them, a learner simulator attempts the exam using only the QA pairs, and a utility estimator compares scores with and without each pair. The authors define question utility as "the direct impact of a question-answer (QA) pair on a learner's understanding, measured by simulated exam performance improvement", and retain pairs with utility above a threshold to refine the generator via rejection sampling. (Dong-Ho Lee et al. (2025))

### Claims
- [QUEST-trained question generators raise simulated exam scores by 18.5% over the next strongest baseline across five subjects](../claims/quest-trained-generators-18-5-percent-exam-gain.md) [+M]
- [Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness](../claims/utility-moderately-correlates-human-perceived-usefulness.md) [+M]

## Related Research Methods
-

## Key Sources
- Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2025). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. https://arxiv.org/abs/2502.17383
