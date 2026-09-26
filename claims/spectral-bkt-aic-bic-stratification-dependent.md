---
type: claim
title: Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation
description: Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation
id: spectral-bkt-aic-bic-stratification-dependent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: falakmasir-2015
    resource: "http://pslcdatashop.web.cmu.edu/KDDCup"
    title: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup"
    author: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K."
    q: 2
    i: 1
---

# Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` With 37 parameters per skill versus 4 for standard BKT, AIC and BIC decrease by 21% and 13% under student-stratified cross-validation but increase by 3% and 9% under item-stratified cross-validation. [→ Falakmasir 2015](#falakmasir-2015)

## Evidence

### Falakmasir 2015

Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

`q2 · i1`

AIC/BIC comparison from the Model Validation section's cross-validation of the two models, which differ in parameters per skill (4 for standard BKT, 37 for Spectral BKT). The penalty metrics favor Spectral BKT only under student stratification; under item stratification they rise.

> "The n umber of parameters being an order of magnitude higher, the AIC and BIC metrics that penalize for that go up 3% and 9% (item-stratified cross -validation). In the case of student -stratified cross -validation, both AIC and BIC are decreaseв by 21% and 13%."

## Discussion


## Related Claims
-
