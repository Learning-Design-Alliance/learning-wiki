---
type: strategy
id: automated-credit-transfer-lo-comparison-strategy
title: Automating credit-transfer course comparison by extracting and semantically comparing learning outcomes
description: "A strategy for institutions developing Transfer Agreements: instead of a panel of reviewers manually comparing course outlines, extract LOs from the two outlines and compute their semantic similarity with the proposed..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: atish-pawar-2018
    resource: "https://arxiv.org/abs/1804.06339"
    title: "Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago. (2018). Are we on the same learning curve: Visualization of Semantic Similarity of Course Objectives. arXiv preprint. https://arxiv.org/abs/1804.06339"
    author: Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago
---

# Automating credit-transfer course comparison by extracting and semantically comparing learning outcomes

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A strategy for institutions developing Transfer Agreements: instead of a panel of reviewers manually comparing course outlines, extract LOs from the two outlines and compute their semantic similarity with the proposed algorithms, then present results in a visualization that assists domain experts. The article motivates this by the current process raising "the subjectivity of experts, their availability and their self motives", and reports that the tools are "helpful in supporting the project managers who are assigned the tasks of preparing transfer programs".

## Design Implications

### Context
#### Requirements
- Course outline documents from which LOs can be extracted; experts remain involved to interpret the similarity visualizations.
#### Constraints
- Extraction is inaccurate for very generic outlines and the similarity results are not education-domain accurate with the general-purpose lexical database.

### Target Learners
- transfer students
- program managers
- domain expert reviewers

### Target Learning Goals
- deciding course equivalence for credit transfer

## Claims

- [The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise](../claims/disambiguation-word-similarity-better-for-synonyms.md) [+W]
- [The heading-based extraction algorithm correctly tagged learning outcomes in 78 of 86 course outline documents (90.69% accuracy)](../claims/lo-extraction-90-69-percent-86-documents.md) [+W]
- [A small survey of users judged the system's semantic and Bloom similarity results useful for deciding between real learning objectives](../claims/lo-similarity-user-survey-usefulness.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago. (2018). Are we on the same learning curve: Visualization of Semantic Similarity of Course Objectives. arXiv preprint. https://arxiv.org/abs/1804.06339
