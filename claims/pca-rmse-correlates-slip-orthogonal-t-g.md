---
type: claim
title: In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE
description: In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE
id: pca-rmse-correlates-slip-orthogonal-t-g
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
---

# In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` PCA of RMSE and the four BKT parameters shows RMSE highly correlated with slip (S), G and T highly inversely correlated with each other, and T and G orthogonal to RMSE, suggesting T and G may have little or no effect on RMSE variation. [→ Martori 2015](#martori-2015)

## Evidence

### Martori 2015

Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

`q2 · i?`

Exploratory PCA on minimum-RMSE values and BKT parameters from BKT-BF grid results; first two components explain 71.4% of variance. Authors report "RMSE is highly correlated with the slip parameter" and orthogonality between T, G and RMSE.

> "In the chart, we can see how the RMSE is highly correlated with the slip parameter. At the same time, the parameters G and T seem to be highly inversely correlated, which is something that one can expect"

## Discussion


## Related Claims
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G](high-pc-bkt-little-room-t-g.md) — related
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](linear-regression-predicts-minimum-rss-bkt-bf.md) — related
- [BKT learning-rate parameters estimated from simulated student data correlate positively with those estimated from human data](simulated-data-initializes-bkt-parameters.md) — related
