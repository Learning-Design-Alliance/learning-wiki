---
type: claim
title: "The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection"
description: "The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection"
id: dnn-benchmark-low-accuracy-false-prevention
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

# The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The DNN approach showed low accuracy (82.74% mid-term, 52.68% final-term), with error rates of 2.23% and 7.14% attributed to false prevention caused by students being extremely slow to select answers. [→ Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021](#leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021)

## Evidence

### Leslie Ching Ow Tiong and HeeJeong Jasmine Lee 2021

Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. [doi:10.48550/arXiv.2101.09841](https://doi.org/10.48550/arXiv.2101.09841)

`q2 · i?` · `design · r2`

Benchmarking analysis of the DNN network on the two examination datasets. The article reports DNN error rates "of 2.23% and 7.14% for mid-term and final-term examinations, respectively", associated with false prevention from extremely slow answer selection; its accuracies were 82.74% and 52.68%.

> "our investigations of the DNN system revealed error rates of 2.23% and 7.14% for mid-term and final-term examinations, respectively, which was associated with false prevention that occurred as a result of several students being extremely slow to select their answers."

## Discussion


## Related Claims
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](denselstm-highest-overall-accuracy-95-32.md) — related
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](denselstm-midterm-finalterm-accuracies.md) — related
