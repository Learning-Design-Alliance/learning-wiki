---
type: claim
title: "DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database"
description: "DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database"
id: denselstm-highest-accuracy-90-72-overall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: leslie-ching-ow-tiong-2022
    resource: "https://doi.org/10.48550/arXiv.2201.13226"
    title: "Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)"
    author: Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six test sets drawn from three semesters, DenseLSTM achieved the highest overall accuracy (90.72%) among the tested networks, followed by LSTM (88.22%), RNN (85.64%) and DNN (65.74%). [→ Leslie Ching Ow Tiong 2022](#leslie-ching-ow-tiong-2022)

## Evidence

### Leslie Ching Ow Tiong 2022

Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)

`q2 · i?` · `design · r2`

Numerical evaluation on the PT Behavioural Database across six test sets (Spring 2020, Fall 2020, Spring 2021) comparing DenseLSTM against DNN, RNN and LSTM benchmarks; Table III reports DenseLSTM at 90.72% overall and DNN at 65.74% overall.

> "From Table III, of the different networks tested, the DenseLSTM network achieved the highest accuracy (90.72%) for overall performance, followed by the LSTM network with an accuracy of 88.22%."

## Discussion


## Related Claims
- [DenseLSTM exceeded 90% accuracy on the majority of the six test sets, with per-test accuracies of 97.77%, 91.92%, 91.96% and 90.18%](denselstm-above-90-percent-majority-test-sets.md) — related
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](denselstm-highest-overall-accuracy-95-32.md) — related
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](denselstm-midterm-finalterm-accuracies.md) — related
- [DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour](denselstm-highest-auc-values.md) — related
- [The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection](dnn-benchmark-low-accuracy-false-prevention.md) — related
- [DenseLSTM achieved the highest AUC values among the tested networks, up to 0.9972, for classifying normal versus suspected candidate behaviour](denselstm-highest-auc-values-up-to-0-9972.md) — related
