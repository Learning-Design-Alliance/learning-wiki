---
type: claim
title: "With PDTB discourse features added, the combined model outperforms the EDM'15 baseline on average in the in-domain setting across 14 MOOC offerings"
description: "With PDTB discourse features added, the combined model outperforms the EDM'15 baseline on average in the in-domain setting across 14 MOOC offerings"
id: pdtb-features-improve-in-domain-intervention-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: muthu-kumar-chandrasekaran-2017
    resource: "https://doi.org/10.1609/aaai.v31i1.11015"
    title: "Muthu Kumar Chandrasekaran, Carrie Demmans Epp, Min-Yen Kan, Diane Litman. (2017). Using Discourse Signals for Robust Instructor Intervention Prediction. Association for the Advancement of Artificial Intelligence. [doi:10.1609/aaai.v31i1.11015](https://doi.org/10.1609/aaai.v31i1.11015)"
    author: Muthu Kumar Chandrasekaran, Carrie Demmans Epp, Min-Yen Kan, Diane Litman
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# With PDTB discourse features added, the combined model outperforms the EDM'15 baseline on average in the in-domain setting across 14 MOOC offerings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under stratified five-fold cross validation within each MOOC, the E+P model outperforms EDM'15 on average, though per-course results vary and two low-intervention-ratio courses yield zero F1 for both models. [→ Muthu Kumar Chandrasekaran 2017](#muthu-kumar-chandrasekaran-2017)

## Evidence

### Muthu Kumar Chandrasekaran 2017

Muthu Kumar Chandrasekaran, Carrie Demmans Epp, Min-Yen Kan, Diane Litman. (2017). Using Discourse Signals for Robust Instructor Intervention Prediction. Association for the Advancement of Artificial Intelligence. [doi:10.1609/aaai.v31i1.11015](https://doi.org/10.1609/aaai.v31i1.11015)

`q2 · i?` · `associational · r2`

In-domain evaluation with stratified five-fold cross validation per MOOC, comparing EDM'15 and E+P. The article reports that "the combined model E+P outperforms the baseline EDM’15 (Table 3), on average". Per-course F1 varies; no standardized effect size is printed.

> "We see that the combined model E+P outperforms the baseline EDM’15 (Table 3), on average."

## Discussion


## Related Claims
- [Contingency and Expansion discourse relations contribute most among the PDTB features for predicting instructor intervention](contingency-expansion-relations-contribute-most.md) — related
- [PDTB discourse features boost intervention prediction most when courses have low intervention ratios and fewer positive instances to learn from](pdtb-features-help-low-intervention-ratio-courses.md) — related
- [Augmenting a state-of-the-art intervention predictor with PDTB discourse features improves out-of-domain prediction of instructor intervention by 3.4% F1 on average across 14 MOOCs](pdtb-features-improve-out-of-domain-intervention-prediction.md) — related
- [PDTB discourse features are more robust than vocabulary-based features across MOOC domains, gaining 11.6% out-of-domain versus 2.7% for the vocabulary baseline](pdtb-features-robust-to-domain-differences.md) — related
- [A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations](roberta-discourse-classifier-pdtb-implicit-sota.md) — related
