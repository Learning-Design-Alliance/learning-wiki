---
type: claim
title: "DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks"
description: "DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks"
id: denselstm-highest-overall-accuracy-95-32
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

# DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of the tested approaches, the proposed DenseLSTM system achieved the highest overall accuracy of 95.32%, with the second-best LSTM reaching 91.89%. [→ Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021](#leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021)

## Evidence

### Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021

Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. [doi:10.48550/arXiv.2101.09841](https://doi.org/10.48550/arXiv.2101.09841)

`q2 · i?` · `design · r2`

Benchmarking evaluation on mid-term and final-term examination data from the authors' own dataset, comparing DenseLSTM against DNN, LSTM and RNN benchmark networks. The results report that "the highest accuracy, of 95.32%, was achieved by our system for overall performance", with the LSTM second-best at 91.89%. No effect size is printed.

> "of the different approaches tested, the highest accuracy, of 95.32%, was achieved by our system for overall performance, followed by the second-best, the LSTM system, which reached an accuracy of 91.89%."

## Discussion


## Related Claims
- [DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour](denselstm-highest-auc-values.md) — related
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](denselstm-midterm-finalterm-accuracies.md) — related
- [The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection](dnn-benchmark-low-accuracy-false-prevention.md) — related
