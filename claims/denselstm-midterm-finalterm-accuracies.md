---
type: claim
title: "DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations"
description: "DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations"
id: denselstm-midterm-finalterm-accuracies
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021
    resource: "https://doi.org/10.48550/arXiv.2101.09841"
    title: "Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. [doi:10.48550/arXiv.2101.09841](https://doi.org/10.48550/arXiv.2101.09841)"
    author: Leslie Ching Ow Tiong and HeeJeong Jasmine Lee
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The proposed network's accuracy was higher than 92% for both mid-term and final-term examinations, at 97.77% and 92.86% respectively. [→ Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021](#leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021)

## Evidence

### Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021

Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. [doi:10.48550/arXiv.2101.09841](https://doi.org/10.48550/arXiv.2101.09841)

`q2 · i?` · `design · r2`

Benchmarking evaluation on the two examination datasets. The article reports the network's accuracy "was higher than 92%" on both exams, "with values of 97.77% and 92.86%, respectively". The second-best LSTM scored 94.49% and 89.29% on the same exams.

> "the accuracy of our network was higher than 92% in analysing the behaviour of students during online exams for both mid-term and final-term examinations, with values of 97.77% and 92.86%, respectively"

## Discussion


## Related Claims
- [DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour](denselstm-highest-auc-values.md) — related
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](denselstm-highest-overall-accuracy-95-32.md) — related
- [The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection](dnn-benchmark-low-accuracy-false-prevention.md) — related
- [DenseLSTM exceeded 90% accuracy on the majority of the six test sets, with per-test accuracies of 97.77%, 91.92%, 91.96% and 90.18%](denselstm-above-90-percent-majority-test-sets.md) — related
- [DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database](denselstm-highest-accuracy-90-72-overall.md) — related
