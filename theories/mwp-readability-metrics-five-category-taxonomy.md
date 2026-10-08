---
type: theory
title: Five-category taxonomy of readability metrics for math word problems
description: "The article organizes candidate readability measures for math word problems into five types: traditional readability formulas, basic text structure metrics, vocabulary metrics, syntactic and coherence metrics, and sem..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: kole-norberg-2025
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
---

# Five-category taxonomy of readability metrics for math word problems

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article organizes candidate readability measures for math word problems into five types: traditional readability formulas, basic text structure metrics, vocabulary metrics, syntactic and coherence metrics, and semantic analysis metrics. It states that "Features in the models included 32 indices representing five types of readability metrics". After dropping nearly perfectly correlated variables (r > 0.90), 28 metrics remained for modeling. Semantic metrics were computed from three vector representations (spaCy, Word2Vec, and custom LSA embeddings built from a corpus of 31,008 MATHia problems), each yielding cosine similarity, magnitude, and neighbor similarity.

## Design Implications

### Context
#### Requirements
- Texts must be calculable with the stated tools (textstat, NLTK, spaCy, gensim, TF-IDF/Truncated SVD), and nearly perfectly correlated variables (r > 0.90) must be dropped before modeling
#### Constraints
- The printed list of metric types in the introduction names four of the five types; the fifth (traditional formulas) is treated in Section 2.2.1
- MWPs are typically shorter than the texts traditional readability formulas were designed to analyze

### Target Learners
- middle and high school math students, particularly less-skilled readers

### Target Learning Objectives
- accessing mathematical content of word problems despite lower reading comprehension

### Claims

- [Random Forest Best Auc Flagged Problems](../claims/random-forest-best-auc-flagged-problems.md) [+M]
- [Word Count Top Traditional Formulas Unimportant](../claims/word-count-top-traditional-formulas-unimportant.md) [+M]
- [Flagged word problems were shorter (lower word count) but had more sentences than non-flagged problems in descriptive statistics](../claims/flagged-problems-shorter-more-sentences-descriptives.md) [+W]
- [4,446 of 9,421 MATHia word problems showed larger-than-expected error-rate gaps between less- and more-skilled readers and were flagged for potential readability concerns](../claims/mathia-word-problems-flagged-reading-gaps.md) [+W]
- [Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships](../claims/partial-dependence-nonlinear-relationships.md) [+W]

## Related Theories
- 

## Examples
-

## Key Sources
- Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274
