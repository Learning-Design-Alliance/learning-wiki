---
type: claim
title: In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom
description: In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom
id: word-count-top-traditional-formulas-unimportant
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: kole-norberg-2025
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: kole-norberg-2025-2
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` After 'Lesson', word count had the highest variable importance (28.99), and traditional readability metrics were not important, with SMOG the highest of these but below most other features. [→ Kole Norberg 2025](#kole-norberg-2025)
`q2 i?` Custom LSA magnitude ranked above magnitudes from spaCy or Word2Vec and above distance-between-texts measures. [→ Kole Norberg 2025 (2)](#kole-norberg-2025-2)

## Evidence

### Kole Norberg 2025

Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274

`q2 · i?` · `associational · r2`

Permutation-based variable importance from the random forest (Table 2): Word Count 28.99, the top readability feature after Lesson (100.00); Flesch Reading Ease 2.18 and LIX 0.00 rank lowest. Importance scores are printed, but no standardized effect size.

> "First, traditional readability metrics were not important to the model's performance. The smog index was the highest ranking of these but fell below most other features."

### Kole Norberg 2025 (2)

Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274

`q2 · i?` · `associational · r2`

Variable importance comparison within the same random forest: Custom Magnitude 20.13 versus Word2Vec Magnitude 6.05 and spaCy Magnitude 3.99 in Table 2. The authors read this as highlighting specialized MWP-corpus embeddings.

> "Second, custom LSA magnitude emerged as more important to the model than magnitude calculated using SpaCy or Word2Vec and as more important than measures of distance between texts."

## Discussion


## Related Claims
- [4,446 of 9,421 MATHia word problems showed larger-than-expected error-rate gaps between less- and more-skilled readers and were flagged for potential readability concerns](mathia-word-problems-flagged-reading-gaps.md) — related
- [Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships](partial-dependence-nonlinear-relationships.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Flagged word problems were shorter (lower word count) but had more sentences than non-flagged problems in descriptive statistics](flagged-problems-shorter-more-sentences-descriptives.md) — related
- [Rewriting MATHia word problems for struggling readers, by human experts or LLMs, sped completion by 30% and improved mastery rate](rewritten-word-problems-faster-completion-mastery.md) — related
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
