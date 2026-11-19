---
type: claim
title: Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.
description: Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.
id: bernoulli-nb-worst-arabic-readability-classifier
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: sadik-bessou-2021
    resource: "https://doi.org/10.6025/jdim/2021/19/3/75-82"
    title: "Sadik Bessou, Ghozlane Chenni. (2021). Efficient Measuring of Readability to Improve Documents Accessibility for Arabic Language Learners. Journal of Digital Information Management. https://doi.org/10.6025/jdim/2021/19/3/75-82"
    author: Sadik Bessou, Ghozlane Chenni
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Bernoulli Naïve Bayes had the lowest accuracy (56.46% with Count Vectors; 55.63% with TF-IDF) in the combined unigram+bigram runs. [→ Sadik Bessou 2021](#sadik-bessou-2021)

## Evidence

### Sadik Bessou 2021

Sadik Bessou, Ghozlane Chenni. (2021). Efficient Measuring of Readability to Improve Documents Accessibility for Arabic Language Learners. Journal of Digital Information Management. https://doi.org/10.6025/jdim/2021/19/3/75-82

`q2 · i?` · `design · r2`

Results section, TF-IDF unigram+bigram experiment (type b, Table 7): the quote names the worst classifier and its printed accuracy; the corresponding Count-Vector experiment printed 56.46% for the same classifier.

> "The accuracy decreased to 72.58% for Random forest and the worst classifier was Bernoulli Naïve Bayes which has an accuracy of 55.63 %."

## Discussion


## Related Claims
- [In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams.](mnb-best-with-count-vectors-86-47.md) — related
- [An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy.](svm-tfidf-ngram-arabic-readability-87-14.md) — related
- [Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.](unigram-bigram-combination-beats-single-grams.md) — related
