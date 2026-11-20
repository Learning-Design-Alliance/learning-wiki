---
type: strategy
id: bert-semantic-matching-curriculum-alignment-strategy
title: Use BERT semantic matching of learning outcomes to reduce manual curriculum-alignment effort and surface cross-curricular connections
description: The article proposes an AI-based methodology in which learning outcomes are embedded with a sentence transformer (all-MiniLM-L12-v2, 384-dimensional vectors), stop words and numbers are removed, and a BERTopic wrapper...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: tamador-alkhidir-2024
    resource: "https://arxiv.org/abs/2403.05553"
    title: "Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi. (2024). Understanding the Progression of Educational Topics via Semantic Matching. arXiv preprint. https://arxiv.org/abs/2403.05553"
    author: Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi
---

# Use BERT semantic matching of learning outcomes to reduce manual curriculum-alignment effort and surface cross-curricular connections

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article proposes an AI-based methodology in which learning outcomes are embedded with a sentence transformer (all-MiniLM-L12-v2, 384-dimensional vectors), stop words and numbers are removed, and a BERTopic wrapper assigns primary topics, with a match established when two outcomes share the same generated topic. This lets specialists compare massive numbers of learning outcomes without manual search, discover similar LOs not already identified, and check spirality and common interconnected topics across grade levels.

## Design Implications

### Context
#### Requirements
- Learning outcomes structured within a dataset; the framework hierarchy (domains, strands, standards, learning outcomes) used to partially verify efficacy
#### Constraints
- The method addresses only the semantic aspect of learning outcomes; unmatched similarities may reflect method limitations or previously unaddressed similarity

### Target Learners
- curriculum specialists and educators revising taught subjects

### Target Learning Goals
- identifying gaps, introducing new learning topics, and enhancing learning outcomes across grades

## Claims

- [BERT-based topic matching paired learning outcomes in agreement with the curriculum framework's existing standard groupings for 95% of them (7,072 of 7,431).](../claims/bert-matching-95-percent-standard-agreement.md) [+W]
- [Semantic matching reveals high cross-subject overlap, including 76% between Visual Arts and Computing and 34% between Health Science and Biology.](../claims/cross-subject-overlap-percentages.md) [+W]
- [Subject-matter experts correctly labeled 400 of 570 learning-outcome pairs (70%), supporting the use of large language models in curriculum mapping.](../claims/expert-validation-70-percent-pairs.md) [+W]
- [Topic modeling exposes progression imbalances across grades, e.g. nutrition is extensively covered in Health Science but receives minimal attention in Physical Science.](../claims/topic-progression-imbalances.md) [+W]
- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](../claims/sentence-similarity-benchmark-correlations.md) [+W]

## Related Strategies

- [Future extensions: link lessons via summarization transformers, connect outcomes through Bloom taxonomy levels, and infer prerequisites from assessment performance](future-extensions-bloom-prerequisites-lessons.md)

## Examples
-

## Key Sources
- Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi. (2024). Understanding the Progression of Educational Topics via Semantic Matching. arXiv preprint. https://arxiv.org/abs/2403.05553
