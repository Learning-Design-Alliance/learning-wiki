---
type: product
id: select-algorithm-and-open-source-trial-dataset
title: SELECT algorithm and open-source trial dataset
description: An open-source release by Upadhyay et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
---

# SELECT algorithm and open-source trial dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
An open-source release by Upadhyay et al. containing the SELECT algorithm implementation and randomized-trial learning data for studying machine-learning-based instruction sequencing and memorization.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **SELECT algorithm and open-source trial dataset released for research at the intersection of cognitive science and machine learning**: The authors released an open-source implementation of their algorithm and all data gathered during the randomized controlled trial, "to facilitate research at the intersection of cognitive science and machine learning". The data and code are available at the GitHub repository Networks-Learning/spaced-selection. The trial data comprise more than ~16.75 million answers to ~1900 questions by ~50,700 learners in ~628,000 study sessions. (Utkarsh Upadhyay et al. (2021))
- **Select: optimal item selection probabilities derived via stochastic optimal control of memory models**: Select casts study-session design as optimizing the selection probability p_i(t) of each question rather than the rate of study, using exponential or power-law forgetting curve models with binary recalls and half-life regression to estimate forgetting rates. Via stochastic optimal control of jump SDEs, the article derives the closed-form "optimal selection probability" p*_i(t) = 1/√q (1−m_i(t)), which depends only on the estimated recall probability. The parameter q trades off recall probability and session size: "the higher its value, the shorter the study sessions". (Utkarsh Upadhyay et al. (2020))
- **Open-source release of the Select algorithm and the randomized trial data**: The authors release an open-source implementation of the Select algorithm together with all data gathered during the randomized controlled trial. The article states: "we are releasing open-source implementation of our algorithm and all the data gathered during our randomized control trial at https://github.com/Networks-Learning/spaced-selection/". This artifact supports research connecting cognitive science and machine learning. (Utkarsh Upadhyay et al. (2020))

### Claims
- [The selection algorithm affects engagement: select and difficulty groups were more likely to return within 4–7 days than the random group, but select-group learners were more likely to stop using the app in the initial 2 days](../claims/select-algorithm-engagement-effects.md) [~M]
- [ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews](../claims/select-algorithm-lower-forgetting-rate-rct.md) [+M]
- [Algorithm-selected learners remember content over ~69% longer, with median half-life increases of ~92% vs random and ~40% vs difficulty groups](../claims/select-group-longer-retention-half-life.md) [+M]
- [Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews](../claims/spacing-effect-and-advantage-grows-with-reviews.md) [+M]
- [ML-optimized item selection helps learners retain content 67% longer than a difficulty-based selection heuristic after controlling for study length and frequency](../claims/select-ml-item-selection-67-percent-longer-retention.md) [+M]
- [Select reduces median empirical forgetting rate 48% below random selection and 40% below difficulty-based selection, with significant differences in 75% of comparisons](../claims/select-lower-forgetting-rate-than-difficulty-and-random.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8
- Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2020). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. https://arxiv.org/abs/2010.04430
