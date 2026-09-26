---
type: element
id: tf-idf-term-weighting-scheme
title: tf-idf term-weighting scheme from information retrieval
description: "tf-idf is a composite weighting scheme from information retrieval that combines a term's frequency within a document with its inverse document frequency across the collection, formalized as tf(t,d) times idf(t,D)."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: jones-2017
    resource: "https://doi.org/10.1016/bs.plm.2017.03.008"
    title: "Jones, M. N., Dye, M., & Johns, B. T. (2017). Context as an Organizing Principle of the Lexicon. Psychology of Learning and Motivation, Volume 67. https://doi.org/10.1016/bs.plm.2017.03.008"
    author: "Jones, M. N., Dye, M., & Johns, B. T"
---

# tf-idf term-weighting scheme from information retrieval

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
tf-idf is a composite weighting scheme from information retrieval that combines a term's frequency within a document with its inverse document frequency across the collection, formalized as tf(t,d) times idf(t,D). The chapter states that "tf-idf selects for terms that occur many times in a small number of documents, penalizing terms that occur only a few times in a document, or that occur in many documents." It is used to identify effective keywords and provides the feature space for distributional models such as latent semantic indexing and Bayesian topic models, illustrating that context-sensitive dispersion measures are useful for retrieval systems and, by analogy, for understanding human lexical organization.

## Design Implications

### Context
#### Requirements
- An indexed document collection over which document-level dispersion statistics can be computed
#### Constraints
- The chapter notes the best keywords have high variance over documents and low document entropy, prioritizing bursty terms over uniformly distributed ones

### Target Learners
- information seekers
- search system users

### Target Learning Goals
- information retrieval
- keyword selection

## Related Elements
- 

## Examples
-

## Key Sources
- Jones, M. N., Dye, M., & Johns, B. T. (2017). Context as an Organizing Principle of the Lexicon. Psychology of Learning and Motivation, Volume 67. https://doi.org/10.1016/bs.plm.2017.03.008
