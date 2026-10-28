---
type: claim
title: The stopping algorithm reduces average assessment duration by about 23.5 minutes
description: The stopping algorithm reduces average assessment duration by about 23.5 minutes
id: stopping-algorithm-reduces-assessment-duration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: matayoshi-2021
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: matayoshi-2021-2
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The stopping algorithm reduces average assessment duration by about 23.5 minutes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` After applying the stopping algorithm, mean duration drops from 93.6 to 70.1 minutes and median from 82.5 to 59.7 minutes. [→ Matayoshi 2021](#matayoshi-2021)
`q2 i?` Students taking longer than three hours show an even more pronounced reduction, with mean duration dropping by over 71 minutes. [→ Matayoshi 2021 (2)](#matayoshi-2021-2)

## Evidence

### Matayoshi 2021

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Analysis of 45,470 assessments with timing data from the held-out test set. Full-length assessments had mean 93.6 minutes and median 82.5 minutes; after the stopping algorithm (GRU, α = 0.99), the distribution shifts left with mean 70.1 and median 59.7 minutes.

> "the mean and median durations now being 70.1 minutes and 59.7 minutes, respectively. Thus, after applying the stopping algorithm, over half of the students are able to finish the assessment in less than an hour, with the average assessment duration being reduced by about 23.5 minutes."

### Matayoshi 2021 (2)

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Analysis of the right tail of the duration distribution. The number of assessments longer than three hours drops from 3483 to 1299, a reduction by a factor of approximately 2.7, with mean questions dropping to 19.4.

> "There are 3483 students who took longer than three hours to complete the assessment; these students have a mean duration of approximately 221.1 minutes. After applying the stopping algorithm, the mean duration for these students drops to 149.8 minutes"

## Discussion


## Related Claims
- [An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy](rnn-stopping-reduces-aleks-assessment-length.md) — possibly the same claim (merge candidate)
