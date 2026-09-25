---
type: element
id: dynemb-skill-tag-concatenation-integration
title: "Skill tag integration scheme: concatenating matrix-factorization question embeddings with one-hot skill tag embeddings, with l1-regularized tag-based initialization"
description: "When manually labeled skill tags are available, DynEmb incorporates them by concatenating the latent question embedding learned via matrix factorization with a one-hot encoding of the question's skill tag, initializin..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
---

# Skill tag integration scheme: concatenating matrix-factorization question embeddings with one-hot skill tag embeddings, with l1-regularized tag-based initialization

> **Element** · [All elements](index.md)

## Description
When manually labeled skill tags are available, DynEmb incorporates them by concatenating the latent question embedding learned via matrix factorization with a one-hot encoding of the question's skill tag, initializing the question embedding from its skill tag's one-hot encoding and adding an l1 regularization to promote sparsity; a fully connected ReLU layer controls the dimensionality of the concatenated embedding. The article says this scheme "enables easy incorporation of additional embeddings/ﬁelds, e.g., semantic embedding from question text", and the StudentDyn component then uses this modified question embedding as before.

## Design Implications

### Context
#### Requirements
- Manually-labeled skill tag information for each question must be available for this integration scheme to apply.
#### Constraints
- The latent space learned via matrix factorization may differ from the latent space constructed by manual labeling, which the concatenation scheme is designed to bridge.

### Target Learners
- students in intelligent tutoring systems with tagged question banks

### Target Learning Goals
- predicting student responses by fusing question-level and skill-level information

## Related Elements
- 

## Examples
-

## Key Sources
- Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org
