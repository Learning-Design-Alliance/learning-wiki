---
type: research-method
id: pdtb-discourse-feature-analysis-for-instructor-intervention-prediction
title: PDTB discourse-feature analysis for instructor-intervention prediction
description: "The article introduces a set of 25 discourse features derived from a pre-trained PDTB-based discourse parser applied to student forum posts: total relation-sense frequency, absolute and relative frequency of each Level-1 sense, and normalized frequencies of sense sequences of length 2."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
---

# PDTB discourse-feature analysis for instructor-intervention prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article introduces a set of 25 discourse features derived from a pre-trained PDTB-based discourse parser applied to student forum posts: total relation-sense frequency, absolute and relative frequency of each Level-1 sense, and normalized frequencies of sense sequences of length 2. The article states "We derive 25 features from the PDTB relation senses output by the parser", using only explicit connectives and Level-1 senses to avoid sparsity, since implicit-connective extraction had low F1 (39.6%) versus explicit (86.7%). The implementations of the baseline and discourse-based systems are publicly released on GitHub.

## Accounts
<!-- How each source describes or uses the method -->
- **PDTB discourse feature set and released implementations for instructor intervention prediction**: The article introduces a set of 25 discourse features derived from a pre-trained PDTB-based discourse parser applied to student forum posts: total relation-sense frequency, absolute and relative frequency of each Level-1 sense, and normalized frequencies of sense sequences of length 2. The article states "We derive 25 features from the PDTB relation senses output by the parser", using only explicit connectives and Level-1 senses to avoid sparsity, since implicit-connective extraction had low F1 (39.6%) versus explicit (86.7%). The implementations of the baseline and discourse-based systems are publicly released on GitHub. (Muthu Kumar Chandrasekaran et al. (2017))

### Claims

- [Augmenting a state-of-the-art intervention predictor with PDTB discourse features improves out-of-domain prediction of instructor intervention by 3.4% F1 on average across 14 MOOCs](../claims/pdtb-features-improve-out-of-domain-intervention-prediction.md) [+M]
- [PDTB discourse features are more robust than vocabulary-based features across MOOC domains, gaining 11.6% out-of-domain versus 2.7% for the vocabulary baseline](../claims/pdtb-features-robust-to-domain-differences.md) [+M]
- [PDTB discourse features boost intervention prediction most when courses have low intervention ratios and fewer positive instances to learn from](../claims/pdtb-features-help-low-intervention-ratio-courses.md) [+W]
- [Contingency and Expansion discourse relations contribute most among the PDTB features for predicting instructor intervention](../claims/contingency-expansion-relations-contribute-most.md) [+W]
- [With PDTB discourse features added, the combined model outperforms the EDM'15 baseline on average in the in-domain setting across 14 MOOC offerings](../claims/pdtb-features-improve-in-domain-intervention-prediction.md) [+W]

## Related Research Methods
-

## Key Sources
- Muthu Kumar Chandrasekaran, Carrie Demmans Epp, Min-Yen Kan, Diane Litman. (2017). Using Discourse Signals for Robust Instructor Intervention Prediction. Association for the Advancement of Artificial Intelligence. https://github.com/WING-NUS/lib4moocdata
