---
type: claim
title: "An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy."
description: "An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy."
id: svm-tfidf-ngram-arabic-readability-87-14
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

# An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SVM with TF-IDF unigram+bigram features achieved the best accuracy of 87.14% over four Arabic complexity classes. [→ Sadik Bessou 2021](#sadik-bessou-2021)

## Evidence

### Sadik Bessou 2021

Sadik Bessou, Ghozlane Chenni. (2021). Efficient Measuring of Readability to Improve Documents Accessibility for Arabic Language Learners. Journal of Digital Information Management. https://doi.org/10.6025/jdim/2021/19/3/75-82

`q2 · i?` · `design · r2`

Experimental evaluation (type b) in the Results section: five classifiers were compared on the test split of the Arabic corpus. The article reports that "SVM achieved the highest scores overall experiments with the best accuracy of 87.14%" and that all SVM accuracies were above 74%.

> "We notice that SVM achieved the highest scores overall experiments with the best accuracy of 87.14%. All accuracies of SVM are above 74%."

## Discussion


## Related Claims
- [Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.](bernoulli-nb-worst-arabic-readability-classifier.md) — related
- [In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams.](mnb-best-with-count-vectors-86-47.md) — related
- [Classifier performance depends on the match between data representation and algorithm: SVM does better with TF-IDF, Multinomial Naïve Bayes with Count Vectors.](representation-algorithm-match-readability-classification.md) — related
- [Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.](unigram-bigram-combination-beats-single-grams.md) — related
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](roberta-svm-most-accurate-scoring-pisa.md) — related
