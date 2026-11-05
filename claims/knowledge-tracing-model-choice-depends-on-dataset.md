---
type: claim
title: Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones
description: In a comparison on nine tutoring-system datasets, a logistic regression model with well-chosen features predicted best on four and deep knowledge tracing on five, depending mainly on how many learners attempted each item, how sequentially learners moved through the material and how long each learner's history was.
id: knowledge-tracing-model-choice-depends-on-dataset
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
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

# Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=9 tutoring-system datasets
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

This is about the accuracy of the learner model an adaptive system relies on to estimate what a learner knows and predict the next answer. Accuracy was measured by area under the ROC curve (AUC) and root mean squared error on learners held out of training.

## Subclaims
`q2 i?` A logistic regression model with the authors' best features (Best-LR) predicted best on four of nine datasets (algebra05, bridge06, assistments09, spanish) and deep knowledge tracing (DKT) on the other five (assistments12, assistments17, statics, squirrel, assistments15); Bayesian Knowledge Tracing lagged behind both, and a self-attention model (SAKT) did worse than DKT on every dataset. [→ Gervet et al. 2020](#gervet-et-al-2020)

`q2 i?` When the training data on one dataset (squirrel) were subsampled, Best-LR led below about one million interactions and DKT above it; the authors found the number of learners per item and per knowledge component a better measure of a dataset's effective size than its number of interactions. [→ Gervet et al. 2020](#gervet-et-al-2020)

`q2 i?` DKT led where learners worked through the material most sequentially, and kept its lead on two of them (assistments17, statics) when restricted to one model per knowledge component; where DKT led, its AUC margin over Best-LR was +0.007 to +0.029, and +0.056 on assistments17, a dataset that records repeated attempts (+0.016 when restricted to first attempts). [→ Gervet et al. 2020](#gervet-et-al-2020)

`q2 i?` On datasets with thousands of interactions per learner (spanish, bridge06), DKT stopped improving after about 1,000 interactions on a student while Best-LR kept improving; on a new student, DKT came close to its peak accuracy after 10 interactions where Best-LR needed 60 (squirrel). [→ Gervet et al. 2020](#gervet-et-al-2020)

## Evidence

### Gervet et al. 2020

Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614)

`q2 · empirical comparison of prediction models on existing datasets` · `i? · differences reported in AUC, not as a standardised effect size` · `n=9 tutoring-system datasets` · `design · r2`

The authors compared Markov-process models (Bayesian Knowledge Tracing and a variant), logistic regression models (item response theory, performance factors analysis, DAS3H and their own feature sets) and deep learning models (DKT, SAKT, feedforward networks) on nine datasets from tutoring systems and online practice: three ASSISTments datasets plus ASSISTments 2015, the two KDD Cup 2010 datasets, an engineering statics course, a middle-school mathematics tutor (Squirrel AI) and a Spanish vocabulary course, ranging from 189,297 to 6,003,641 interactions and from 182 to 29,018 learners. Models were trained and tested with five-fold cross-validation across learners, with hyper-parameters chosen by grid search. The authors note that they did not cross-validate across items, so the results show how models generalise to new learners but not to new items, and that this setup does not do justice to item response theory, whose learner ability parameter is never fitted. They conclude that in their view the weakest links of tutoring systems today are often the adaptive instructional policy and the knowledge-component model rather than the performance prediction model.

## Discussion

The study compares prediction accuracy only; it does not test whether a more accurate learner model produces more learning when it drives an adaptive system. The datasets were chosen to cover a range of properties, and the dataset characteristics the authors link to each model's lead (learners per item, sequential progression, history length) were identified across nine datasets, with the size explanation tested by subsampling one of them.

## Related Claims
- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — the same study
- [Expert-designed knowledge-component models add little to the accuracy of logistic-regression learner models on most tutoring datasets](expert-kc-models-add-little-to-performance-prediction.md) — the same study
- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — related
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — related
