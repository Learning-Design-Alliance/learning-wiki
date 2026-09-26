---
type: claim
title: The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G
description: The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G
id: high-pc-bkt-little-room-t-g
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

# The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` The authors interpret the model's very high adjusted R² as possibly indicating that BKT works better when the percentage of correct answers is very high, in which case there may not be much room for the T and G parameters in the model. [→ Martori 2015](#martori-2015)

## Evidence

### Martori 2015

Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

`q2 · i?`

Authors' interpretation (type e) of the regression result in the discussion section; no additional test is reported for this hypothesis. The article states this "may be indicating" and flags it as a suspicion requiring a different dataset.

> "The very high performance of the model, in terms of adjusted R 2, may be indicating that BKT works better when the percentage of correct answers is very high, as the RSS decreases."

## Discussion


## Related Claims
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](linear-regression-predicts-minimum-rss-bkt-bf.md) — related
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](pca-rmse-correlates-slip-orthogonal-t-g.md) — related
- [The percentage of hints taken on a question is negatively correlated with the percentage of correct responses](hint-taking-negatively-correlated-with-correct-responses.md) — related
- [BKT learning-rate parameters estimated from simulated student data correlate positively with those estimated from human data](simulated-data-initializes-bkt-parameters.md) — related
