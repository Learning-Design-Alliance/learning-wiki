---
type: research-method
id: corpus-statistics-word-sense-disambiguation-method-for-learning-objective-comparison
title: Corpus-statistics word-sense disambiguation method for learning-objective comparison
description: The methodology treats the domain corpus as a supervised learning model that disambiguates word senses before semantic similarity is computed.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Corpus-statistics word-sense disambiguation method for learning-objective comparison

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The methodology treats the domain corpus as a supervised learning model that disambiguates word senses before semantic similarity is computed. The article states: "This methodology simulates the use of corpus as a supervised learning model. The corpus is then 'disambiguated', i.e., we ﬁnd the appropriate sense for each word in the corpus." Using the 'max similarity' word sense disambiguation algorithm as implemented in Pywsd, each corpus word is stored with its chosen WordNet synset and meaning, then synset frequencies are computed; the meaning with the highest frequency is selected when a learning-objective word is compared, falling back to WordNet's predefined frequency distribution for rare failures of the disambiguation function.

## Accounts
<!-- How each source describes or uses the method -->
- **Corpus statistics as a disambiguated supervised-learning model for selecting word senses in learning objectives**: The methodology treats the domain corpus as a supervised learning model that disambiguates word senses before semantic similarity is computed. The article states: "This methodology simulates the use of corpus as a supervised learning model. The corpus is then 'disambiguated', i.e., we ﬁnd the appropriate sense for each word in the corpus." Using the 'max similarity' word sense disambiguation algorithm as implemented in Pywsd, each corpus word is stored with its chosen WordNet synset and meaning, then synset frequencies are computed; the meaning with the highest frequency is selected when a learning-objective word is compared, falling back to WordNet's predefined frequency distribution for rare failures of the disambiguation function. (Atish Pawar et al. (2018))

### Claims

- [Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate](../claims/corpus-disambiguation-inaccuracies.md) [~W]
- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](../claims/sentence-similarity-benchmark-correlations.md) [+W]
- [The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise](../claims/disambiguation-word-similarity-better-for-synonyms.md) [+W]

## Related Research Methods

- [Six-step WordNet-based word similarity method enhanced with word-sense disambiguation and sense-frequency weighting](six-step-wordnet-based-word-similarity-method-enhanced-with-word-sense-disambiguation-and.md)
- [Verb-only Bloom taxonomy module for learning-objective similarity](verb-only-bloom-taxonomy-module-for-learning-objective-similarity.md)

## Key Sources
- Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. https://arxiv.org/abs/1804.06333
