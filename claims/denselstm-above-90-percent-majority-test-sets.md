---
type: claim
title: "DenseLSTM exceeded 90% accuracy on the majority of the six test sets, with per-test accuracies of 97.77%, 91.92%, 91.96% and 90.18%"
description: "DenseLSTM exceeded 90% accuracy on the majority of the six test sets, with per-test accuracies of 97.77%, 91.92%, 91.96% and 90.18%"
id: denselstm-above-90-percent-majority-test-sets
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

# DenseLSTM exceeded 90% accuracy on the majority of the six test sets, with per-test accuracies of 97.77%, 91.92%, 91.96% and 90.18%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DenseLSTM's accuracy was higher than 90% for the majority of test sets: 97.77% for Test 1, 91.92% for Test 2, 91.96% for Test 3 and 90.18% for Test 5. [→ Leslie Ching Ow Tiong 2022](#leslie-ching-ow-tiong-2022)

## Evidence

### Leslie Ching Ow Tiong 2022

Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)

`q2 · i?` · `design · r2`

Numerical results across the six test sets of the PT Behavioural Database; the quoted sentence reports the per-test accuracies for Tests 1, 2, 3 and 5 as printed in the results section.

> "we observed that the accuracy of our network was higher than 90% when analysing the behaviour of candidates for the majority of test sets, with values of 97.77% for Test 1, 91.92% for Test 2, 91.96% for Test 3 and 90.18% for Test 5"

## Discussion


## Related Claims
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](denselstm-midterm-finalterm-accuracies.md) — related
- [DenseLSTM achieves the highest classification accuracy of the tested networks, 90.72% overall, outperforming LSTM, RNN and DNN benchmarks on the PT Behavioural Database](denselstm-highest-accuracy-90-72-overall.md) — related
