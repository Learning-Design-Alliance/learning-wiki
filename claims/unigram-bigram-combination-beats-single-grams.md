---
type: claim
title: Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.
description: Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.
id: unigram-bigram-combination-beats-single-grams
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

# Combining unigram and bigram features gives better classification accuracy than either n-gram length alone for all classifiers.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across the experiments, accuracy was better with combined unigrams and bigrams than with each feature type alone. [→ Sadik Bessou 2021](#sadik-bessou-2021)

## Evidence

### Sadik Bessou 2021

Sadik Bessou, Ghozlane Chenni. (2021). Efficient Measuring of Readability to Improve Documents Accessibility for Arabic Language Learners. Journal of Digital Information Management. https://doi.org/10.6025/jdim/2021/19/3/75-82

`q2 · i?` · `design · r2`

Comparison across the six experiments reported in the Results section (type b): bigram-only runs dropped accuracy (e.g., SVM 74.41% with TF-IDF) while unigram+bigram runs were highest, which the authors attribute to the importance of n-gram features in detecting text difficulty.

> "For all classifiers, the accu- racy is better using a combination of unigrams and bigrams features than using each one alone."

## Discussion


## Related Claims
- [Bernoulli Naïve Bayes was consistently the worst-performing classifier for Arabic readability classification in both representations.](bernoulli-nb-worst-arabic-readability-classifier.md) — related
- [In Count Vector experiments, Multinomial Naïve Bayes outperformed the other classifiers, reaching 86.47% with combined unigrams and bigrams.](mnb-best-with-count-vectors-86-47.md) — a narrower finding that bears on this claim
- [An SVM classifier using TF-IDF word unigram-and-bigram features identifies Arabic text complexity across four levels with 87.14% accuracy.](svm-tfidf-ngram-arabic-readability-87-14.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
