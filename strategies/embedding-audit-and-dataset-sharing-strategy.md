---
type: strategy
id: embedding-audit-and-dataset-sharing-strategy
title: Use embedding-based semantic distance auditing and public dataset sharing to improve consistency in qualitative coding practice
description: The article recommends two practices for qualitative researchers.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: mjaaland-2025
    resource: "https://arxiv.org/abs/2508.19836"
    title: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. https://arxiv.org/abs/2508.19836"
    author: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B"
---

# Use embedding-based semantic distance auditing and public dataset sharing to improve consistency in qualitative coding practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends two practices for qualitative researchers. First, embeddings can audit both machine-coded and human-coded datasets, representing "a promising addition to the existing toolkit for identifying errors and inconsistencies in qualitative datasets". Second, the authors propose that "science education researchers should make a habit of publicly sharing their datasets", as done in this work, to enable testing the framework on previously coded datasets and benchmarking new analyses.

## Design Implications

### Context
#### Requirements
- Access to the raw response texts and existing codes; an embedding model runnable on local machines
#### Constraints
- Benchmarking a framework application on a new, uncoded dataset is significantly harder absent additional human coding

### Target Learners
- science education researchers conducting qualitative content analysis

### Target Learning Goals
- improved coding consistency and replicability in large-scale qualitative analysis

## Claims

- [DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples](../claims/desca-high-agreement-exhaustive-coding.md) [+W]
- [DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task](../claims/desca-lower-agreement-selective-coding.md) [-W]
- [Pairwise semantic distance between embedded responses can audit previously human-coded datasets, flagging near-identical responses that received different codes](../claims/embedding-audit-coding-inconsistencies.md) [+W]
- [Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task](../claims/fine-tuning-improves-selective-coding.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. https://arxiv.org/abs/2508.19836
