---
type: claim
title: A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability
description: A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability
id: linear-regression-predicts-minimum-rss-bkt-bf
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L."
    q: 2
    i: "?"
---

# A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` A linear regression using n, dim, and percent_correct (with a second-degree polynomial on pc) predicts the minimum RSS value obtained from BKT-BF for a skill, achieving adjusted R² of 0.978 on a random validation set. [→ Martori 2015](#martori-2015)

## Evidence

### Martori 2015

Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

`q2 · i?`

Numerical modeling study using the Psychology MOOC GT Spring 2013 dataset (5615 students, ~2 million first attempts, 226 skills; 103 skills with dim≥4 retained). Best-subset linear regression on RMSE yielded "adjusted R 2 of 0.978" on validation.

> "Finally, using a random validation set (75 skills to train the model and 28 to test it), we have obtained an adjusted R 2 of 0.978, that shows a very good predictive ability for the adjusted model."

## Discussion


## Related Claims
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G](high-pc-bkt-little-room-t-g.md) — related
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](pca-rmse-correlates-slip-orthogonal-t-g.md) — related
