---
type: claim
title: Hidden Markov modeling of practice latencies favors a three-learning-state model with within-state speedup
description: Hidden Markov modeling of practice latencies favors a three-learning-state model with within-state speedup
id: hmm-three-learning-states-best-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2015
recheck_by: 2018
sources:
  - id: tenison-2015
    resource: "https://dx.doi.org/10.1037/xlm0000204"
    title: "Tenison, C., & Anderson, J. R. (2015). Modeling the distinct phases of skill acquisition. https://dx.doi.org/10.1037/xlm0000204"
    author: "Tenison, C., & Anderson, J. R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Hidden Markov modeling of practice latencies favors a three-learning-state model with within-state speedup

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2018**: tool and model accuracy changes quickly
> **Design limits** · Tenison 2015: no comparison group (read from the study by two models, 2026-11-23)

## Subclaims
`q2 i?` Across 20 HMMs varying states and speedup functions, the three-state three-parameter power function model provided the best fit by BIC. [→ Tenison 2015](#tenison-2015)

## Evidence

### Tenison 2015

Tenison, C., & Anderson, J. R. (2015). Modeling the distinct phases of skill acquisition. https://dx.doi.org/10.1037/xlm0000204

`q2 · i?` · `causal · r1`

Model comparison of 20 HMMs (one to five states, four within-state speedup options) fit to each practiced problem's latency history for each participant, assessed by BIC (Table 2). Within-state speedup always beat no-speedup models; the APEX function fit substantially worse.

> "While the four-‐learning states power function HMM has the best BIC scores, the improvement from three-‐to four-‐learning states is negligible (Kass & Raftery, 1995). Thus, we conclude that the three-‐learning state, three-‐parameter power function provides the best fit to our data."

## Discussion


## Related Claims
- [Simulation analysis supports recovery of three states with within-state speedup but cannot discriminate power from exponential functions](hmm-simulation-sensitivity-three-states.md) — a broader claim this one bears on
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- [The three HMM learning states differ substantially in latency, accuracy, and reported strategy use](three-states-differ-latency-accuracy-strategy.md) — related
