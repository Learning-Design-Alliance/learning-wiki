---
type: strategy
id: embeddings-exploratory-human-in-the-loop-review
title: Use embeddings for exploratory organization and human-in-the-loop review of student solutions, with external validation before any grading use
description: The article recommends deploying text embeddings of student solutions for exploratory purposes — organizing responses, selecting examples, supporting human review — rather than as an unsupervised grading mechanism.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: maike-tauschhuber-and-gerd-kortemeyer-2026
    resource: "https://arxiv.org/abs/2606.28872"
    title: "Maike Tauschhuber and Gerd Kortemeyer. (2026). Testing the Validity of Embedding-Based Similarity and Clustering for Handwritten Physics Solutions. https://arxiv.org/abs/2606.28872"
    author: Maike Tauschhuber and Gerd Kortemeyer
---

# Use embeddings for exploratory organization and human-in-the-loop review of student solutions, with external validation before any grading use

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends deploying text embeddings of student solutions for exploratory purposes — organizing responses, selecting examples, supporting human review — rather than as an unsupervised grading mechanism. It states that "state-of-the-art embeddings can support exploratory organization and human-in-the-loop review of physics solutions, but they do not provide an unsupervised basis for grading without external validation against the assessment construct of interest." This aligns with the human-in-the-loop stance the article describes, in which confidence filters route trustworthy AI decisions forward and defer uncertain cases to human graders.

## Design Implications

### Context
#### Requirements
- External validation of embedding clusters against the assessment construct of interest before any grading-related interpretation
#### Constraints
- Embedding similarity showed only a modest relationship to score similarity, and clusters were score-enriched but not score-equivalent

### Target Learners
- undergraduate physics or engineering students in large-enrollment courses

### Target Learning Goals
- scalable formative feedback and organization of handwritten solution paths while preserving trustworthy assessment

### Affordances
- [Clustering Validity Criterion Embeddings](../research-methods/clustering-validity-criterion.md)

## Claims

- [Hierarchical clusters formed from embedding similarities are score-enriched but not score-equivalent to human-assigned score groups](../claims/embedding-clusters-score-enriched-not-score-equivalent.md) [+W]
- [Pairwise embedding similarity shows a consistent but modest relationship to human-assigned score similarity for handwritten physics solutions](../claims/embedding-similarity-modestly-predicts-score-similarity.md) [+W]
- [Synthetic-data experiments suggest embedding geometry of physics solutions is driven by surface features rather than conceptual structure, behaving like novices](../claims/embeddings-behave-like-novices-surface-features.md) [-W]
- [Embedding-based clustering of physics solutions does not provide an unsupervised basis for grading without external validation against the assessment construct](../claims/embeddings-insufficient-unsupervised-grading.md) [+W]

## Related Strategies

- [Apply human quality-check supervision before deploying LLM-generated hint content in tutoring systems](human-quality-checks-for-llm-hints.md)
- [Use independent expert physician review as a governance safeguard before deploying LLM-generated questions to learners](expert-physician-review-governance.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)

## Examples
-

## Key Sources
- Maike Tauschhuber and Gerd Kortemeyer. (2026). Testing the Validity of Embedding-Based Similarity and Clustering for Handwritten Physics Solutions. https://arxiv.org/abs/2606.28872
