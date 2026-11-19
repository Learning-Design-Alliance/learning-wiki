---
type: claim
title: "In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams."
description: "In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams."
id: mnb-best-with-count-vectors-86-47
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

# In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Multinomial Naïve Bayes achieved the highest Count-Vector accuracy (86.47%), ahead of Logistic Regression (84.81%) and SVM (83.89%). [→ Sadik Bessou 2021](#sadik-bessou-2021)

## Evidence

### Sadik Bessou 2021

Sadik Bessou, Ghozlane Chenni. (2021). Efficient Measuring of Readability to Improve Documents Accessibility for Arabic Language Learners. Journal of Digital Information Management. https://doi.org/10.6025/jdim/2021/19/3/75-82

`q2 · i?` · `design · r2`

Results section (type b), Count Vectors with unigrams+bigrams (Table 4): the quoted ranking names MNB, Logistic Regression and SVM with their printed accuracies; Random Forest fell to 72.97% and Bernoulli Naïve Bayes was the worst classifier at 56.46%.

> "Multinomial Naïve Bayes outperformed other algorithms, achieving the highest accuracy rate of 86.47%, followed by Logistic Regression with 84.81%, then Support Vector Machine with 83.89%."

## Discussion


## Related Claims
- [Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.](bernoulli-nb-worst-arabic-readability-classifier.md) — related
- [Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.](unigram-bigram-combination-beats-single-grams.md) — a broader claim this one bears on
- [Classifier performance depends on the match between data representation and algorithm: SVM does better with TF-IDF, Multinomial Naïve Bayes with Count Vectors.](representation-algorithm-match-readability-classification.md) — a broader claim this one bears on
- [An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy.](svm-tfidf-ngram-arabic-readability-87-14.md) — related
