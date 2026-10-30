---
type: claim
title: Bayes factors on Gaussian-process trajectories show each behavioural cluster is statistically distinct from the others
description: Bayes factors on Gaussian-process trajectories show each behavioural cluster is statistically distinct from the others
id: gpr-bayes-factors-cluster-distinctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: peach-2019
    resource: "https://doi.org/10.1038/s41539-019-0054-0"
    title: "Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M. (2019). Data-driven unsupervised clustering of online learner behaviour. npj Science of Learning 4:14. https://doi.org/10.1038/s41539-019-0054-0"
    author: Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Bayes factors on Gaussian-process trajectories show each behavioural cluster is statistically distinct from the others

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPR Bayes factors confirm that cluster trajectories derive from separate processes (overall K = 3.37×10^10), with pairwise factors between neighbouring clusters of 0.38, 1.52 and 0.17×10^10. [→ Peach 2019](#peach-2019)

## Evidence

### Peach 2019

Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M. (2019). Data-driven unsupervised clustering of online learner behaviour. npj Science of Learning 4:14. https://doi.org/10.1038/s41539-019-0054-0

`q2 · i?` · `associational · r2`

Gaussian Process Regression analysis of the 6-cluster partition of the 81-learner cohort. Comparing separate cluster log-likelihoods against the whole set, "The Bayes Factor ... was found to be large ( K = 3.37 × 1010)", with pairwise factors between neighbouring clusters also reported.

> "The Bayes Factor, calculated as the sum of log likelihoods of each separate cluster minus the log-likelihood of the entire set of trajectories 12 was found to be large ( K = 3.37 × 1010)."

## Discussion


## Related Claims
- [In pairwise WD analyses, learner trajectory similarity dominates variation in percentage-overlap values (57.90% of variation) while remaining design factors are essentially zero](trajectory-similarity-dominates-wd-pair-overlap.md) — related
- [Type 2 groups showed a communication–behaviour-synergistic transition, Type 1 a behaviour-oriented, and Type 3 a communication-oriented transition in hidden Markov models](hmm-transitional-regularities-pattern-types.md) — related
- [In simulated epistemic games, the weighted density statistic distinguishes simulated learner types with distinct mastery trajectories, with the expert trajectory showing the largest WD values](wd-detects-simulated-learner-trajectory-differences.md) — related
