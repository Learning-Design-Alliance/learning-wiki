---
type: claim
title: L1 predicts L2 in cross-validated machine-learning models of English proficiency
description: L1 predicts L2 in cross-validated machine-learning models of English proficiency
id: svr-l2-prediction-driven-by-l1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: xin-kang-2021
    resource: "https://doi.org/10.1038/s41539-021-00104-9"
    title: "Xin Kang, Stephen Matthews, Virginia Yip and Patrick C. M. Wong. (2021). Language and nonlanguage factors in foreign language learning: evidence for the learning condition hypothesis. npj Science of Learning 6:28. https://doi.org/10.1038/s41539-021-00104-9"
    author: Xin Kang, Stephen Matthews, Virginia Yip and Patrick C. M. Wong
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# L1 predicts L2 in cross-validated machine-learning models of English proficiency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In tenfold cross-validated SVR, L1 (Chinese) HKDSE grades alone significantly predicted L2 (English) HKDSE grades (mean cc = 0.257, p < 0.001, Cohen's d = 7.17). [→ Xin Kang 2021](#xin-kang-2021)

## Evidence

### Xin Kang 2021

Xin Kang, Stephen Matthews, Virginia Yip and Patrick C. M. Wong. (2021). Language and nonlanguage factors in foreign language learning: evidence for the learning condition hypothesis. npj Science of Learning 6:28. https://doi.org/10.1038/s41539-021-00104-9

`q2 · i?` · `associational · r2`

Support vector regression with tenfold cross-validation and 10,000 iterations predicted L2 (English) HKDSE grades. The L1-only model's predicted cc distribution differed significantly from null, with the article reporting "Cohen ’s d = 7.17".

> "When only L1 (Chinese) HKDSE grades were used as the predictor of L2 (English) HKDSE grades, the distribution of predicted cc (mean = 0.257, SD = 0.037) was also signi ﬁcantly different from the null distribution (mean = −0.0004, SD = 0.062, p < 0.001, Cohen ’s d = 7.17)."

## Discussion


## Related Claims
- [L1 and L2 proficiency are significantly associated in L3 learners](l1-l2-proficiency-significantly-correlated.md) — related
- [After controlling for nonlanguage factors, L1 predicts L2 and L2 predicts L3, but L1 does not predict L3](regression-language-associations-nonlanguage-controls.md) — a broader claim this one bears on
- [Machine-learning prediction of L3 proficiency is driven mainly by L2, not L1](svr-l3-prediction-driven-by-l2.md) — related
