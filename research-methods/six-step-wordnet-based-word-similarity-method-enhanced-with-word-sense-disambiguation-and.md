---
type: research-method
id: six-step-wordnet-based-word-similarity-method-enhanced-with-word-sense-disambiguation-and
title: Six-step WordNet-based word similarity method enhanced with word-sense disambiguation and sense-frequency weighting
description: "The proposed method computes word similarity using the WordNet lexical database plus the Bloom's taxonomy hierarchy for LO complexity."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Six-step WordNet-based word similarity method enhanced with word-sense disambiguation and sense-frequency weighting

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The proposed method computes word similarity using the WordNet lexical database plus the Bloom's taxonomy hierarchy for LO complexity. It proceeds in six steps: tokenizing and part-of-speech tagging with NLTK; identifying word sense via Pywsd disambiguation; computing shortest path distance between synsets via f(l) = e^(−αl); computing hierarchical level information via g(h), a monotonically decreasing function of depth; combining word-sense frequency so "the sense with maximum frequency is compared with its counter part"; and averaging the disambiguated-pair and most-frequent-sense-pair similarities. It enhances the Li et al. sentence similarity algorithm by first identifying the meaning of the word in sentence context.

## Accounts
<!-- How each source describes or uses the method -->
- **Six-step WordNet-based word similarity method enhanced with word-sense disambiguation and sense-frequency weighting**: The proposed method computes word similarity using the WordNet lexical database plus the Bloom's taxonomy hierarchy for LO complexity. It proceeds in six steps: tokenizing and part-of-speech tagging with NLTK; identifying word sense via Pywsd disambiguation; computing shortest path distance between synsets via f(l) = e^(−αl); computing hierarchical level information via g(h), a monotonically decreasing function of depth; combining word-sense frequency so "the sense with maximum frequency is compared with its counter part"; and averaging the disambiguated-pair and most-frequent-sense-pair similarities. It enhances the Li et al. sentence similarity algorithm by first identifying the meaning of the word in sentence context. (Atish Pawar et al. (2018))

### Claims

- [Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate](../claims/corpus-disambiguation-inaccuracies.md) [~W]
- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](../claims/sentence-similarity-benchmark-correlations.md) [+W]
- [The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise](../claims/disambiguation-word-similarity-better-for-synonyms.md) [+W]

## Related Research Methods

- [Corpus-statistics word-sense disambiguation method for learning-objective comparison](corpus-statistics-word-sense-disambiguation-method-for-learning-objective-comparison.md)
- [Bloom Index: a hierarchical verb-based index of the learning gap between two learning outcomes](bloom-index-a-hierarchical-verb-based-index-of-the-learning-gap-between-two-learning-outco.md)
- [Verb-only Bloom taxonomy module for learning-objective similarity](verb-only-bloom-taxonomy-module-for-learning-objective-similarity.md)

## Key Sources
- Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago. (2018). Are we on the same learning curve: Visualization of Semantic Similarity of Course Objectives. arXiv preprint. https://arxiv.org/abs/1804.06339
