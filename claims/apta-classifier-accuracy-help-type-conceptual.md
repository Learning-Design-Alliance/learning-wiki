---
type: claim
title: "APTA's machine classifiers reached training-data accuracy of .81 for help type and .66 for conceptual content under 10-fold cross validation"
description: "APTA's machine classifiers reached training-data accuracy of .81 for help type and .66 for conceptual content under 10-fold cross validation"
id: apta-classifier-accuracy-help-type-conceptual
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: walker-2014
    resource: "https://doi.org/10.1007/s40593-013-0001-9"
    title: "Walker, E., Rummel, N., & Koedinger, K. R. (2014). Adaptive Intelligent Support to Improve Peer Tutoring in Algebra. Int J Artif Intell Educ 24, 33–61. https://doi.org/10.1007/s40593-013-0001-9"
    author: "Walker, E., Rummel, N., & Koedinger, K. R."
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# APTA's machine classifiers reached training-data accuracy of .81 for help type and .66 for conceptual content under 10-fold cross validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly
> **Design limits** · Walker 2014: no comparison group (read from the study by two models, 2026-10-27)

## Subclaims
`q2 i?` A support vector machine classifier trained with chi-squared feature selection achieved .81 accuracy for help type and .66 for conceptual content on training data. [→ Walker 2014](#walker-2014)

## Evidence

### Walker 2014

Walker, E., Rummel, N., & Koedinger, K. R. (2014). Adaptive Intelligent Support to Improve Peer Tutoring in Algebra. Int J Artif Intell Educ 24, 33–61. https://doi.org/10.1007/s40593-013-0001-9

`q2 · i?` · `causal · r?`

Technical evaluation of APTA's dialogue classifiers built with Taghelper Tools, using unigrams, bigrams, line length, punctuation, and domain-context features. The article reports that "the classifier had an accuracy of .81 for help type and .66 for conceptual content" on training data.

> "We used a chi-squared feature selection algorithm to rank the most predictive features, and 10-fold cross validation to train a support vector machine classifier for help type and conceptual content. On training data, the classifier had an accuracy of .81 for help type and .66 for conceptual content."

## Discussion


## Related Claims
- A prior-study corpus of 84 peer tutoring sessions was coded for help type and conceptual content with kappa of 0.83 and 0.72 — related
