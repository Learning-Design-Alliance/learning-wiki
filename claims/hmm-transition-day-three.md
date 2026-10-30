---
type: claim
title: Hidden Markov model of individual training curves shows task-specific improvement plateaued on average on the third day of training
description: Hidden Markov model of individual training curves shows task-specific improvement plateaued on average on the third day of training
id: hmm-transition-day-three
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2028
sources:
  - id: julia-ericson-and-torkel-klingberg-2023
    resource: "https://doi.org/10.1038/s41539-023-00161-2"
    title: "Julia Ericson and Torkel Klingberg. (2023). A dual-process model for cognitive training. npj Science of Learning. https://doi.org/10.1038/s41539-023-00161-2"
    author: Julia Ericson and Torkel Klingberg
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Hidden Markov model of individual training curves shows task-specific improvement plateaued on average on the third day of training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2028: baselines and conditions change

## Subclaims
`q3 i?` Fitting the piecewise linear HMM to individual learning curves revealed the task-specific improvement plateaued on the third day of training on average (median transition day 3.05, quartiles 2.13 and 5.18). [→ Julia Ericson and Torkel Klingberg 2023](#julia-ericson-and-torkel-klingberg-2023)

## Evidence

### Julia Ericson and Torkel Klingberg 2023

Julia Ericson and Torkel Klingberg. (2023). A dual-process model for cognitive training. npj Science of Learning. https://doi.org/10.1038/s41539-023-00161-2

`q3 · i?` · `associational · r2`

HMM fitted to one learning curve per each of the 1300 subjects using daily Grid performance, with parameters optimized by expectation maximization. The article reports "the median day for transitioning was day 3.05, with quartiles of 2.13 and 5.18."

> "the median day for transitioning was day 3.05, with quartiles of 2.13 and 5.18 (Fig. 6b)."

## Discussion


## Related Claims
- [HMM-derived task-specific and capacity parameters correlate with the corresponding CFA estimates, validating the daily-data model](hmm-parameters-correlate-cfa-estimates.md) — related
- [Simulation study shows the HMM recovers the true transition day within one day in 88% of cases](hmm-simulation-reliability-transition-day.md) — related
- [Task-specific improvement was identified only in individual learning curves and was not apparent in averaged performance data](individual-curves-needed-to-identify-task-specific-phase.md) — related
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
