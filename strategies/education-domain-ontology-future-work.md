---
type: strategy
id: education-domain-ontology-future-work
title: "Future improvements: expand domains and corpus, restructure data files, and build education-domain WordNet-like ontologies"
description: "The authors' stated forward-looking agenda is to \"expand the domains and corpus, increasing eﬃciency of algorithms by using diﬀerent ﬁle structures and forming WordNet-like ontologies for speciﬁcally the education dom..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: atish-pawar-and-vijay-mago-2018
    resource: "https://arxiv.org/abs/1804.06333"
    title: "Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. https://arxiv.org/abs/1804.06333"
    author: Atish Pawar and Vijay Mago
---

# Future improvements: expand domains and corpus, restructure data files, and build education-domain WordNet-like ontologies

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The authors' stated forward-looking agenda is to "expand the domains and corpus, increasing eﬃciency of algorithms by using diﬀerent ﬁle structures and forming WordNet-like ontologies for speciﬁcally the education domain". Building education-domain ontologies would parallel the study's use of WordNet synsets plus corpus frequencies, replacing the general-purpose lexical database with education-specific meaning structures, while domain and corpus expansion would address the scarcity of domain-specific corpora that forced the authors to compile a small corpus themselves.

## Design Implications

### Context
#### Requirements
- Domain-specific corpora with sufficient apparent domain words for the disambiguation function to predict meaning via the max similarity algorithm.
#### Constraints
- The current study is limited to one compiled small Chemistry-domain corpus and reports that corpus disambiguation can misassign senses for words like structure and table.

### Target Learners
- program managers and coordinators developing transfer agreements across institutions and domains

### Target Learning Goals
- reliable automated semantic comparison of learning objectives across multiple academic domains

## Claims

- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](../claims/sentence-similarity-benchmark-correlations.md) [+W]
- [A small survey of users judged the system's semantic and Bloom similarity results useful for deciding between real learning objectives](../claims/lo-similarity-user-survey-usefulness.md) [+W]

## Related Strategies

- [Advance ontology development as an evidence-based engineering activity: validate quality parameters empirically, build an easy-to-use metrics toolbox, and change developer behaviour incrementally](evidence-based-ontology-development-research-agenda.md)
- [Develop ontologies for ITS interoperability incrementally (mappings, benchmark tasks, folksonomies) rather than a top-down super-ontology](incremental-ontology-standards-aied.md)

## Examples
-

## Key Sources
- Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. https://arxiv.org/abs/1804.06333
