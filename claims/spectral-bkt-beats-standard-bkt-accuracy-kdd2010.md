---
type: claim
title: "Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy"
description: "Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy"
id: spectral-bkt-beats-standard-bkt-accuracy-kdd2010
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

# Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i2` On the KDD Cup 2010 dataset, Spectral BKT reaches 92% overall accuracy, above what the authors report as never previously achieved for BKT or its variations on that dataset. [→ Falakmasir 2015](#falakmasir-2015)

## Evidence

### Falakmasir 2015

Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

`q2 · i2`

Cross-validation of standard BKT versus Spectral BKT on the KDD Cup 2010 Bridge to Algebra data, using 10-fold student-based and item-based cross-validations with the hmmsclbl tool. The paper reports Spectral BKT "hits an impressive 92%" accuracy, with standard BKT at 0.8609 (item) and 0.8659 (student) in Table 1.

> "To the best of our knowledge, the overall accuracy of BKT or its variations was never reported to be above 90%  on the dataset we used and Spectral BKT hits an impressive 92%."

## Discussion


## Related Claims
- [Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+](spectral-bkt-advantage-varies-by-opportunity.md) — related
- [Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation](spectral-bkt-aic-bic-stratification-dependent.md) — related
- [Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration](spectral-bkt-alternative-configurations-no-improvement.md) — related
