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
- [In an empirical comparison on a testlet-based English assessment test, the bifactor model is preferred over the second-order and unidimensional 2PL models by both AIC and BIC](bifactor-model-preferred-aic-bic-testlet-test.md) — related
- [Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy](spectral-bkt-beats-standard-bkt-accuracy-kdd2010.md) — related
- [Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+](spectral-bkt-advantage-varies-by-opportunity.md) — related
- [Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration](spectral-bkt-alternative-configurations-no-improvement.md) — related
