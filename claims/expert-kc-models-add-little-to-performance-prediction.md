---
type: claim
title: Expert-designed knowledge-component models add little to the accuracy of logistic-regression learner models on most tutoring datasets
description: On seven of nine tutoring-system datasets, adding the datasets' expert-designed knowledge-component features to a logistic-regression learner model raised prediction accuracy by 0.01 AUC or less, which the authors read as a sign of low-quality knowledge-component models.
id: expert-kc-models-add-little-to-performance-prediction
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: gervet-et-al-2020
    resource: "https://doi.org/10.5281/zenodo.4143614"
    title: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614)"
    author: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T."
    q: 2
    i: "?"
    n: 9 tutoring-system datasets
    kind: design
    rigour: 2
---

# Expert-designed knowledge-component models add little to the accuracy of logistic-regression learner models on most tutoring datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=9 tutoring-system datasets
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

A knowledge-component (KC) model tags each question with the skills or concepts it exercises; adaptive systems use it to decide what a learner has mastered. The finding concerns the KC models that came with these datasets, not KC modelling in general.

## Subclaims
`q2 i?` On seven of nine datasets, the logistic regression model with KC features (Best-LR) gained +0.01 AUC or less over the same model without them (NoKC-LR); only the two KDD Cup 2010 datasets (algebra05, bridge06) gained about +0.03 AUC. [→ Gervet et al. 2020](#gervet-et-al-2020)

`q2 i?` On four of nine datasets, a model using only KC features (performance factors analysis) did not beat a model using only item difficulty (item response theory), the condition the authors expect a suitable KC model to meet. [→ Gervet et al. 2020](#gervet-et-al-2020)

`q2 i?` Counts of a learner's prior correct answers and attempts across all questions, a feature absent from earlier models, substantially improved prediction on all nine datasets, while time-window features added no predictive power to the logistic regression model. [→ Gervet et al. 2020](#gervet-et-al-2020)

## Evidence

### Gervet et al. 2020

Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614)

`q2 · ablation study of prediction models on existing datasets` · `i? · differences reported in AUC, not as a standardised effect size` · `n=9 tutoring-system datasets` · `design · r2`

In an ablation study within a comparison of learner performance models, the authors fitted logistic regression and two-layer feedforward network models with different sets of features (item, KC, total counts, KC counts, time windows) on nine tutoring and online-practice datasets (ASSISTments, KDD Cup 2010, an engineering statics course, Squirrel AI mathematics, Spanish vocabulary), with five-fold cross-validation across learners. They say the small contribution of KC features surprised them and is consistent with Lindsey et al. (2014). They did not cross-validate across items, which is where a KC model is what lets a model generalise to new items, so the test may understate what a good KC model contributes.

## Discussion

The authors suggest that the knowledge-component model, together with the adaptive instructional policy, is often a weaker link in tutoring systems than the performance prediction model. The result is about predicting the next answer; it does not test whether refining a KC model improves learning.

## Related Claims
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — the same study
- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — the same study
