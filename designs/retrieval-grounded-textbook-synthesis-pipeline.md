---
type: design
id: retrieval-grounded-textbook-synthesis-pipeline
title: Five-stage retrieval-grounded textbook synthesis pipeline producing 686K source-grounded books (32B tokens)
description: "A pipeline that transforms a pre-training corpus into textbook-form training data in two phases: knowledge extraction (query generation, retrieval, chunking, KMeans clustering with relevance filtering) and structured..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: jiawen-tao-2026
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
---

# Five-stage retrieval-grounded textbook synthesis pipeline producing 686K source-grounded books (32B tokens)

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A pipeline that transforms a pre-training corpus into textbook-form training data in two phases: knowledge extraction (query generation, retrieval, chunking, KMeans clustering with relevance filtering) and structured generation (hierarchical TOC planning with a quality gate, then source-grounded section generation and assembly). The article states it "retrieves and clusters source documents, plans hierarchical tables of contents (TOCs) with quality filtering, and assembles source-grounded sections into complete books." It produced 249K TOCs (91.8% passing the gate) and 686K books totaling 32B tokens across 15,387 disciplines, with up to 48 variants per discipline.

## Design Implications

### Context
#### Requirements
- A searchable pre-training corpus index for keyword retrieval, plus LLMs for query generation, TOC planning, quality gating, and section generation
#### Constraints
- The pipeline requires a searchable corpus index, which adds preprocessing and retrieval-infrastructure overhead, per the article's limitations

### Target Learners
- language models undergoing mid-training

### Learning Goals
- domain knowledge injection and improved downstream benchmark performance

### Claims
- [Structured Synthesis Beats Rephrasing](../claims/structured-synthesis-beats-rephrasing.md) [+M]
- [Synthetic Textbooks Replace Natural Books Gain](../claims/synthetic-textbooks-replace-natural-books-gain.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109
