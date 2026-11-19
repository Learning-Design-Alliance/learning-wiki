---
type: claim
title: DenseLSTM achieved the highest AUC values among the tested networks, up to 0.9972, for classifying normal versus suspected candidate behaviour
description: DenseLSTM achieved the highest AUC values among the tested networks, up to 0.9972, for classifying normal versus suspected candidate behaviour
id: denselstm-highest-auc-values-up-to-0-9972
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

# DenseLSTM achieved the highest AUC values among the tested networks, up to 0.9972, for classifying normal versus suspected candidate behaviour

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using ROC and AUC characterisation, DenseLSTM achieved the highest AUC values of 0.9972, 0.9760, 0.9593, 0.9043, 0.8867 and 0.8921 for Test 1 to Test 5, excluding Test 6. [→ Leslie Ching Ow Tiong 2022](#leslie-ching-ow-tiong-2022)

## Evidence

### Leslie Ching Ow Tiong 2022

Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)

`q2 · i?` · `design · r2`

ROC/AUC analysis reported in the results section and plotted in Fig. 5 across the six test sets; the quoted sentence lists the printed AUC values for DenseLSTM, with Test 6 excluded.

> "In Fig. 5, DenseLSTM achieved the highest AUC values of 0.9972, 0.9760, 0.9593, 0.9043, 0.8867 and 0.8921 for Test 1 to Test 5, respectively, excluding Test 6."

## Discussion


## Related Claims
- [DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database](denselstm-highest-accuracy-90-72-overall.md) — related
- [DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour](denselstm-highest-auc-values.md) — possibly the same claim (merge candidate)
