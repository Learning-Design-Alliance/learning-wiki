---
type: claim
title: The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin
description: The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin
id: em-beats-sgd-fitting-spectral-bkt
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: weak
sources:
  - id: falakmasir-2015
    resource: "http://pslcdatashop.web.cmu.edu/KDDCup"
    title: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup"
    author: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K."
    q: 2
    i: 1
---

# The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` Among the solver algorithms tested, EM gave consistently better performance than stochastic gradient descent, with the margin within 1% in accuracy and 0.03 in RMSE. [→ Falakmasir 2015](#falakmasir-2015)

## Evidence

### Falakmasir 2015

Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

`q2 · i1`

Solver comparison within the Model Validation section, using the hmmsclbl C/C++ utility on the transformed 3-gram dataset. The paper reports EM "gave a consistently better per formance" with a small margin; no per-solver table is printed.

> "We tested several solver algorithms hmmsclbl supports, including EM and stochastic gradient descent. EM gave a consistently better per formance, but the margin was small: within 1% in accuracy and 0.03 in RMSE."

## Discussion


## Related Claims
-
