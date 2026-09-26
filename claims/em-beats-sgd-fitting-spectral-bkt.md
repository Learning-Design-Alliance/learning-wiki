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
- [The AFM+S model, which explicitly models non-zero tail error, fits simulated student data better than the standard AFM](afm-plus-slip-fits-simulated-learning-curves.md) — related
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](bkt-sequence-recommendation-students-solved-harder-exercises.md) — related
- [OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets](optimnn-lower-rmse-than-em-cgd-sgd.md) — related
- [OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT](optimnn-hyperparameter-insensitivity.md) — related
- [Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration](spectral-bkt-alternative-configurations-no-improvement.md) — related
