---
type: claim
title: Semi-Markov models fit the writing-process data better than continuous-time Markov chain models
description: Semi-Markov models fit the writing-process data better than continuous-time Markov chain models
id: semimarkov-preferred-over-ctmc
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: hongwen-guo-2020
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/443"
    title: "Hongwen Guo, Mo Zhang, Paul Deane, Randy E. Bennett. (2020). Effects of Scenario-Based Assessment on Students’ Writing Processes. Journal of Educational Data Mining, Volume 12, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/443"
    author: Hongwen Guo, Mo Zhang, Paul Deane, Randy E. Bennett
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Semi-Markov models fit the writing-process data better than continuous-time Markov chain models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Most estimated Weibull shape parameters for state duration differed significantly from 1, indicating the semi-Markov model is preferable to a CTMC model. [→ Hongwen Guo 2020](#hongwen-guo-2020)

## Evidence

### Hongwen Guo 2020

Hongwen Guo, Mo Zhang, Paul Deane, Randy E. Bennett. (2020). Effects of Scenario-Based Assessment on Students’ Writing Processes. Journal of Educational Data Mining, Volume 12, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/443

`q2 · i?` · `causal · r2`

Model-fit evaluation for Form 1 (Table 6) with Bonferroni-corrected tests of shape parameters against 1; the article concludes “a semi-Markov model may be preferable to a continuous time Markov model.” Results across all four groups reportedly showed the same pattern.

> "Most of the values estimated for the shape parameterν of the state duration time are statistically signiﬁcantly different from 1 after applying Bonferroni correction (except forν21,ν 32,ν 42, andν43). Therefore, a semi-Markov model may be preferable to a continuous time Markov model."

## Discussion


## Related Claims
- [A four-state semi-Markov model distinguishing jump editing from local editing fits keystroke-log writing data significantly better than a three-state model](four-state-semimarkov-beats-three-state.md) — a narrower finding that bears on this claim
- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
