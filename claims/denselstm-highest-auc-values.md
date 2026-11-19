---
type: claim
title: DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour
description: DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour
id: denselstm-highest-auc-values
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

# DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using ROC analysis, the proposed DenseLSTM achieved the highest AUC values of 0.9972 and 0.9760 for the mid-term and final-term examinations respectively. [→ Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021](#leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021)

## Evidence

### Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021

Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. [doi:10.48550/arXiv.2101.09841](https://doi.org/10.48550/arXiv.2101.09841)

`q2 · i?` · `design · r2`

Sensitivity and specificity characterisation using ROC and AUC on the mid-term and final-term examination data. The article reports DenseLSTM "achieved the highest AUC values of 0.9972 and 0.9760", while LSTM and RNN reached 0.9870 and 0.9810 on the mid-term and below 0.94 on the final-term.

> "our network (DenseLSTM) achieved the highest AUC values of 0.9972 and 0.9760, for the mid-term and final-term examinations, respectively."

## Discussion


## Related Claims
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](denselstm-highest-overall-accuracy-95-32.md) — related
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](denselstm-midterm-finalterm-accuracies.md) — related
- [DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database](denselstm-highest-accuracy-90-72-overall.md) — related
- [DenseLSTM achieved the highest AUC values among the tested networks, up to 0.9972, for classifying normal versus suspected candidate behaviour](denselstm-highest-auc-values-up-to-0-9972.md) — possibly the same claim (merge candidate)
