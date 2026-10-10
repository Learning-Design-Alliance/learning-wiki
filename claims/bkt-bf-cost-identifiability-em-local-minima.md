---
type: claim
title: "BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima"
description: "BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima"
id: bkt-bf-cost-identifiability-em-local-minima
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: weak
sources:
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` BKT-BF is very expensive in computational cost and does not help the identifiability problem of BKT, whereas EM is less computationally demanding but suffers from local minima issues. [→ Martori 2015](#martori-2015)

## Evidence

### Martori 2015

Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

`q2 · i?` · `associational · r1`

Definitional/interpretive statement in the introduction about the two main BKT training approaches, citing prior work on identifiability and EM. The article presents this as established background motivating the study.

> "BKT-BF is, however, is very expensive in computational cost, as all brute force algorithms are, and does not help the identifiability [3] problem from BKT"

## Discussion


## Related Claims
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](linear-regression-predicts-minimum-rss-bkt-bf.md) — related
- [OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets](optimnn-lower-rmse-than-em-cgd-sgd.md) — related
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](pca-rmse-correlates-slip-orthogonal-t-g.md) — related
- [The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G](high-pc-bkt-little-room-t-g.md) — related
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](bkt-identifiability-explained-by-parameter-a.md) — related
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](bkt-sequence-recommendation-students-solved-harder-exercises.md) — related
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
- [BKT implemented as an RNN layer in PyTorch recovers generating parameters comparably to brute-force grid-search BKT while scaling to large datasets](bkt-rnn-matches-brute-force-parameter-recovery.md) — related
- [Algorithmically inferred measurement functions may intensify, rather than resolve, the problem of nomic measurement in analyzing student learning](ai-intensifies-nomic-measurement-problem.md) — related
- [A Bayesian DINA model converges successfully on educational response data with 91.3% sparsity where the EM algorithm failed](bayesian-dina-converges-sparse-data.md) — related
- [Group-level marginal inferences identify population propensity and autonomy but are nearly vacuous for higher algorithmic skill levels](group-marginal-inferences-cat-skills-propensity.md) — related
