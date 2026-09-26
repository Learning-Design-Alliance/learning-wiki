---
type: claim
title: "Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+"
description: "Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+"
id: spectral-bkt-advantage-varies-by-opportunity
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
    i: 2
---

# Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i2` On the second skill opportunity, Spectral BKT outperforms standard BKT by almost 9% accuracy and 0.08 RMSE, and by around 5% accuracy and 0.09 RMSE from the third opportunity onward. [→ Falakmasir 2015](#falakmasir-2015)

## Evidence

### Falakmasir 2015

Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

`q2 · i2`

Per-opportunity breakdown of the same 10-fold cross-validation, reported in the text accompanying Table 1. Because 3-gram observations delay predictions, the paper reports opportunity 1 (7% of data), opportunity 2 (6%), and opportunity 3+ (87%) separately; Spectral BKT shows "a decisive edge" from opportunity 2 onward.

> "On the second opportunity prediction, Spectral BKT has a decisive edge of a lmost 9% and 0.08 in RMSE. On the third opportunity and further, Spectral BKT has a comfortable advantage of around 5% in accuracy and 0.09 in RMSE."

## Discussion


## Related Claims
- [Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy](spectral-bkt-beats-standard-bkt-accuracy-kdd2010.md) — related
- [Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration](spectral-bkt-alternative-configurations-no-improvement.md) — related
- [Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation](spectral-bkt-aic-bic-stratification-dependent.md) — related
