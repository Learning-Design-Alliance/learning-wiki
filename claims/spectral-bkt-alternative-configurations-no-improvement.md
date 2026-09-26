---
type: claim
title: Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration
description: Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration
id: spectral-bkt-alternative-configurations-no-improvement
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

# Alternative Spectral BKT configurations (2 states with 4 bigrams; 8 states with 16 4-grams) did not improve over the 4-state, 3-gram configuration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i0` A 2-state configuration with 4 bigram spectral observations did not improve over standard BKT, and an 8-state configuration with 16 4-gram observations did not tangibly improve over the reported 4-state configuration. [→ Falakmasir 2015](#falakmasir-2015)

## Evidence

### Falakmasir 2015

Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup

`q2 · i1`

Empirical configuration search reported in the Discussion section: the authors tried smaller and larger Spectral BKT setups and report that neither "did not result in an improvement" case beat the chosen 4-state, 3-gram configuration. No statistics are printed for these trials.

> "We empirically tried configurations of Spectral BKT with 2 states and 4 bigram spectral observations that did not result in an improvement over standard BKT, as well as a configuration with 8 states and 16 4 -gram spectral observations that did not result in a tangible improvement over the configuration we discussed in this paper."

## Discussion


## Related Claims
- [Spectral BKT's accuracy advantage over standard BKT varies by skill opportunity: slightly worse at opportunity 1, but decisive at opportunities 2 and 3+](spectral-bkt-advantage-varies-by-opportunity.md) — related
- [Model-complexity penalties favor Spectral BKT under student-stratified cross-validation but not under item-stratified cross-validation](spectral-bkt-aic-bic-stratification-dependent.md) — related
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
- [Spectral BKT achieves higher prediction accuracy than standard BKT on the KDD Cup 2010 Bridge to Algebra data, reaching 92% accuracy](spectral-bkt-beats-standard-bkt-accuracy-kdd2010.md) — related
