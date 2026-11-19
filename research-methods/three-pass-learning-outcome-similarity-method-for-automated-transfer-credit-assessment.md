---
type: research-method
id: three-pass-learning-outcome-similarity-method-for-automated-transfer-credit-assessment
title: Three-pass learning-outcome similarity method for automated transfer-credit assessment
description: The article proposes a model that determines similarity between courses based on their learning outcomes in three passes.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Three-pass learning-outcome similarity method for automated transfer-credit assessment

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes a model that determines similarity between courses based on their learning outcomes in three passes. The article describes it as "a clustering-inspired methodology based on knowledge-based semantic similarity measures to assess the taxonomic similarity of LOs and a transformer-based semantic similarity model to assess the semantic similarity of the LOs." Pass 1 assigns learning outcomes to Bloom's taxonomy clusters via verbs detected with spaCy and WordNet, producing a taxonomic similarity grid; Pass 2 uses SRoBERTa embeddings and cosine similarity to build a semantic similarity grid; Pass 3 aggregates both into a final course-level similarity and credit decision.

## Accounts
<!-- How each source describes or uses the method -->
- **Three-pass model for automated transfer credit assessment via learning outcome similarity**: The article proposes a model that determines similarity between courses based on their learning outcomes in three passes. The article describes it as "a clustering-inspired methodology based on knowledge-based semantic similarity measures to assess the taxonomic similarity of LOs and a transformer-based semantic similarity model to assess the semantic similarity of the LOs." Pass 1 assigns learning outcomes to Bloom's taxonomy clusters via verbs detected with spaCy and WordNet, producing a taxonomic similarity grid; Pass 2 uses SRoBERTa embeddings and cosine similarity to build a semantic similarity grid; Pass 3 aggregates both into a final course-level similarity and credit decision. (Dhivya Chandrasekaran et al. (2021))

### Claims
- [Combining taxonomic and semantic similarity of learning outcomes yields higher agreement with human transfer-credit decisions than semantic similarity alone](../claims/nlp-transfer-credit-model-outperforms-semantic-only.md) [+M]

## Related Research Methods
-

## Key Sources
- Dhivya Chandrasekaran and Vijay Mago. (2021). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. https://arxiv.org/abs/2104.01955
