---
type: strategy
id: future-extensions-bloom-prerequisites-lessons
title: "Future extensions: link lessons via summarization transformers, connect outcomes through Bloom taxonomy levels, and infer prerequisites from assessment performance"
description: "The authors outline future implementations: deducing learning outcomes and keywords from textbook lessons using a predefined summarization sentence transformer to link lessons across subjects automatically; additional..."
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

# Future extensions: link lessons via summarization transformers, connect outcomes through Bloom taxonomy levels, and infer prerequisites from assessment performance

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors outline future implementations: deducing learning outcomes and keywords from textbook lessons using a predefined summarization sentence transformer to link lessons across subjects automatically; additionally linking learning outcomes through cognitive skills (Bloom taxonomy levels) to address their complexity; and deducing prerequisites by combining semantic matching results with students' performance in outcomes-based assessments to pinpoint how not understanding one learning outcome can affect others.

## Design Implications

### Context
#### Requirements
- Semantic matching results plus students' performance data from outcomes-based assessments for prerequisite inference
#### Constraints
- The current paper focuses only on the semantic aspect of the learning outcomes

### Target Learners
- curriculum specialists and education systems using outcomes-based assessment

### Target Learning Goals
- tracking topic progression, addressing outcome complexity, and inferring dependencies between learning outcomes

## Claims

- [BERT-based topic matching paired learning outcomes in agreement with the curriculum framework's existing standard groupings for 95% of them (7,072 of 7,431).](../claims/bert-matching-95-percent-standard-agreement.md) [+W]
- [Semantic matching reveals high cross-subject overlap, including 76% between Visual Arts and Computing and 34% between Health Science and Biology.](../claims/cross-subject-overlap-percentages.md) [+W]
- [Subject-matter experts correctly labeled 400 of 570 learning-outcome pairs (70%), supporting the use of large language models in curriculum mapping.](../claims/expert-validation-70-percent-pairs.md) [+W]

## Related Strategies

- [Use BERT semantic matching of learning outcomes to reduce manual curriculum-alignment effort and surface cross-curricular connections](bert-semantic-matching-curriculum-alignment-strategy.md)
- [Future directions: cross-component comparisons and multilingual embeddings for course overlap](coursegraph-future-cross-component-multilingual.md)

## Examples
-

## Key Sources
- Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi. (2024). Understanding the Progression of Educational Topics via Semantic Matching. arXiv preprint. https://arxiv.org/abs/2403.05553
