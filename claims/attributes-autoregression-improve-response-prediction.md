---
type: claim
title: Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.
description: Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.
id: attributes-autoregression-improve-response-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: vasileios-lampos-2021-2
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Incorporating student attributes increases classification accuracy for all methods (RF accuracy up 4.37%, F1 up 1.64%), and combining attributes with autoregression in a GP yields the best performance (accuracy 0.711, F1 0.757). [→ Vasileios Lampos 2021](#vasileios-lampos-2021)
`q2 i?` In leave-one-student-out validation the best model performs worse than within-cohort cross-validation but still significantly outperforms the major class baseline. [→ Vasileios Lampos 2021 (2)](#vasileios-lampos-2021-2)

## Evidence

### Vasileios Lampos 2021

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r1`

10-fold cross-validation results over 5460 coded interactions (Tables 2–3). The article reports that performance "increases for all methods, when student attributes are incorporated", and that the combination of attributes and autoregression attains "an accuracy of 0.711 (SD = 0.015) and an F 1 score of 0.757 (SD = 0.014)". No effect size printed.

> "Overall, we see that the classification performance increases for all methods, when student attributes are incorporated. For the RF method, in particular, accuracy and F 1 score increase by 4.37% and 1.64%, respectively."

### Vasileios Lampos 2021 (2)

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r1`

Generalisation check on the same dataset using leave-one-student-out (7-fold) cross-validation with the GP-α (τ = 1) model. The article reports inferior performance "as expected given the increased difficulty of the task", yet it "still significantly outperforms the major class baseline"; detailed numbers are in the SI.

> "Deploying this best performing model in a leave-one-student-out validation setup (7-fold cross-validation) yields inferior performance as expected given the increased difficulty of the task. However, it still significantly outperforms the major class baseline; more details are provided in the Supple- mentary Information (SI)."

## Discussion


## Related Claims
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.](ml-predicts-student-response-autism-communication.md) — related
