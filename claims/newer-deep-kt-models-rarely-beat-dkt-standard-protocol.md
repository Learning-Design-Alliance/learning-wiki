---
type: claim
title: Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy
description: A benchmark of ten deep knowledge-tracing models on seven datasets with shared preprocessing and five-fold cross-validation found that most models proposed after deep knowledge tracing (DKT) did not outperform it, that only AKT led on almost every dataset, and that evaluating expanded knowledge-component sequences one by one leaks answers and inflates AUC.
id: newer-deep-kt-models-rarely-beat-dkt-standard-protocol
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: liu-et-al-2022
    resource: "https://doi.org/10.52202/068431-1347"
    title: "Liu, Z., Liu, Q., Chen, J., Huang, S., Tang, J., & Luo, W. (2022). pyKT: A Python library to benchmark deep learning based knowledge tracing models. In *Advances in Neural Information Processing Systems 35* (Datasets and Benchmarks Track), 18542–18555. [doi:10.52202/068431-1347](https://doi.org/10.52202/068431-1347)"
    author: "Liu, Z., Liu, Q., Chen, J., Huang, S., Tang, J., & Luo, W."
    q: 2
    i: "?"
    n: 7 datasets, 10 models
    kind: design
    rigour: 2
---

# Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=7 datasets, 10 models
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

Knowledge tracing predicts whether a learner will answer the next question correctly from their history, and adaptive systems use it to decide what a learner has mastered. This claim concerns how far published accuracy gains for deep learning knowledge-tracing models hold up when every model is run on the same data splits and preprocessing; it does not test any model's effect on learning.

## Subclaims
`q2 i?` With shared preprocessing, five-fold cross-validation and Bayesian hyper-parameter search, the majority of recently proposed models did not beat the original deep knowledge tracing model (DKT); AKT outperformed almost all other models on all seven datasets, by 3.06%, 1.50%, 1.62% and 1.60% AUC over the second-best model on AS2009, AL2005, BD2006 and NIPS34, and by only 0.30% and 1.08% on Statics2011 and POJ. [→ Liu et al. 2022](#liu-et-al-2022)

`q2 i?` Predicting a question's expanded knowledge-component (KC) sequence one KC at a time lets the model see the answer to the same question, and inflated AUC by a mean of 8.38% on ASSISTments 2009 and 13.09% on Algebra 2005, the datasets where questions carry more KCs (1.1970 and 1.3634 per question); the authors recommend against this evaluation and say it may explain why they could not reproduce several published results. [→ Liu et al. 2022](#liu-et-al-2022)

`q2 i?` The original implementation of one model (ATKT) used the future ground truth to predict the current question, and its published results could not be reproduced once this was fixed. [→ Liu et al. 2022](#liu-et-al-2022)

`q2 i?` Prediction on programming exercises was much harder than on mathematics: models reached AUCs around 0.8 on the mathematics datasets but around 0.6 on the POJ programming dataset. [→ Liu et al. 2022](#liu-et-al-2022)

## Evidence

### Liu et al. 2022

Liu, Z., Liu, Q., Chen, J., Huang, S., Tang, J., & Luo, W. (2022). pyKT: A Python library to benchmark deep learning based knowledge tracing models. In *Advances in Neural Information Processing Systems 35* (Datasets and Benchmarks Track), 18542–18555. [doi:10.52202/068431-1347](https://doi.org/10.52202/068431-1347)

`q2 · benchmark comparison of prediction models on existing datasets` · `i? · differences reported in AUC, not as a standardised effect size` · `n=7 datasets, 10 models` · `design · r2`

The authors built an open-source library (pyKT) with standard preprocessing for seven public datasets (ASSISTments 2009 and 2015, Algebra 2005 and Bridge to Algebra 2006 from the KDD Cup 2010, NIPS 2020 Education Challenge task 3 and 4, Statics 2011 and the POJ programming dataset) and implementations of ten deep learning knowledge-tracing models chosen from those most often compared in AI and machine-learning venues from 2015 to 2021 (DKT, DKT+, DKT-F, KQN, DKVMN, ATKT, GKT, SAKT, SAINT, AKT). Every model was tuned and tested with five-fold cross-validation and AUC compared with paired t-tests at the 0.01 level. Self-attention models (SAKT, SAINT) did worse than the recurrent ones in most cases, which the authors attribute to distant past interactions mattering little for predicting the next answer. They note that all the datasets and models assume binary correct/incorrect responses and that none of the baselines uses side information such as time spent. The numbers above were checked against both the proceedings version and the arXiv version (v5), which reports re-run results differing from the original by less than 0.005 AUC.

## Discussion

The benchmark compares models from the deep learning family only; it does not include logistic regression or Bayesian knowledge tracing baselines. For an adaptive course the practical reading is that a reported accuracy gain for a newer knowledge-tracing model should be checked against DKT under the same protocol, and that a KC-level evaluation done question by question overstates accuracy.

## Related Claims
- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — qualifies it
