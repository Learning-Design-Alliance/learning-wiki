---
type: claim
title: Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.
description: Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.
id: ml-predicts-student-response-autism-communication
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Classifiers predict whether a student with ASC gives a full response better than random (0.500) and major-class (0.566) baselines, with the RF model reaching 0.664 accuracy without student attributes. [→ Vasileios Lampos 2021](#vasileios-lampos-2021)

## Evidence

### Vasileios Lampos 2021

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r1`

Discussion summary of the exploratory observational study: binary classification of full response versus otherwise on 5460 coded in-vivo interactions from seven students, evaluated by 10-fold cross-validation. The RF model achieved "an accuracy (0.664; RF model) greater than that expected from a random (0.500) or major class (0.566) baseline prediction". No effect size is printed for this finding.

> "A machine learning classifier was able to predict which type of teacher communication was more likely to generate a positive response by a student with ASC, indicating that the student responded to the communication in a way intended by the teacher, with an accuracy (0.664; RF model) greater than that expected from a random (0.500) or major class (0.566) baseline prediction."

## Discussion


## Related Claims
- [Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.](attributes-autoregression-improve-response-prediction.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Machine learning models can predict SRL-use categories early in students' interactions with accuracy significantly above baseline](ml-models-predict-srl-early.md) — related
