---
type: claim
title: Standard BKT fits Raging Skies pilot process data with acceptable RMSE and good accuracy under 10-fold cross-validation
description: Standard BKT fits Raging Skies pilot process data with acceptable RMSE and good accuracy under 10-fold cross-validation
id: bkt-fits-raging-skies-process-data
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: ying-cui-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    title: "Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    author: Ying Cui, Man-Wai Chu, Fu Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Standard BKT fits Raging Skies pilot process data with acceptable RMSE and good accuracy under 10-fold cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The standard BKT model achieved an RMSE of 0.39 and accuracy of 0.77 averaged across 10 cross-validation folds on Grade 5 gameplay log data. [→ Ying Cui 2019](#ying-cui-2019)

## Evidence

### Ying Cui 2019

Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397

`q2 · i?` · `design · r2`

Cross-validated BKT analysis of log data from 460 Grade 5 students playing Raging Skies, trained with the hmm-scalable tool and Baum-Welch solver. The article reports "an acceptable RMSE of 0.39 and a good accuracy of 0.77"; no effect size is printed.

> "The 10-fold cross-validation results show that the standard BKT model fits the data with an acceptable RMSE of 0.39 and a good accuracy of 0.77."

## Discussion


## Related Claims
- [BKT tended to outperform DBN across skills, possibly because DBN's greater parameter complexity exceeded what the sample size could estimate](bkt-outperforms-dbn.md) — related
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
- [CCM showed adequate model-data fit for game log data, except for infrequent tasks 7 and 9](ccm-model-data-fit-adequate-except-tasks-7-9.md) — related
