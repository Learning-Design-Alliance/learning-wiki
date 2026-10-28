---
type: claim
title: A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)
description: A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)
id: stacking-ensemble-best-finetuning-f1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: josmario-albuquerque-2026
    resource: "https://doi.org/10.18608/jla.2026.8905"
    title: "Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905"
    author: Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Among 120 evaluated stack configurations, the best-performing stack (LG, SVM, NB, KNN, XGB) achieved an F1-score of 0.88 during fine-tuning, exceeding SVM's second-highest 0.86. [→ Josmario Albuquerque 2026](#josmario-albuquerque-2026)

## Evidence

### Josmario Albuquerque 2026

Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905

`q2 · i?` · `design · r2`

Fine-tuning experiment evaluating 120 stacking combinations by F1-score during training/validation on the OER dataset; the stack "outperformed individual models such as SVM" at this stage, though on the test set STK's F1 was 0.69.

> "the best-performing stack achieved an F1-score of 0.88. This stack included LG, SVM, NB, KNN, and XGB models and outperformed individual models such as SVM, which achieved the second-highest F1-score of 0.86."

## Discussion


## Related Claims
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- [The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set](naive-bayes-highest-precision-bias-detection.md) — related
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — a narrower finding that bears on this claim
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — a broader claim this one bears on
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
- [k-nearest neighbours achieves the highest recall of the tested models, making it better suited when identifying which students know a topic matters](knn-highest-recall-for-identifying-students.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [On one graphical differentiation item, eye tracking data predicted students' specific difficulties as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
- [The generalised plait ensemble outperforms single classifiers, majority-vote and stacking ensembles, substantially improving perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%).](plait-ensemble-outperforms-single-and-standard-ensembles.md) — related
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](svm-best-single-classifier-task-difficulty.md) — related
- [SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764](svm-embeddings-classify-comments-f1-0914.md) — related
