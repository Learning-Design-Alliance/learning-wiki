---
type: element
id: transformer-ieu-iiu-kt-framework
title: Transformer-encoder knowledge tracing framework with IEU/IIU input vectors and released code, models, and predictions
description: "A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: lu-2024
    resource: "https://osf.io/mdpzc/"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/"
    author: "Lu, Y., Tong, L., & Cheng, Y"
---

# Transformer-encoder knowledge tracing framework with IEU/IIU input vectors and released code, models, and predictions

> **Element** · [All elements](index.md)

## Description
A deep knowledge tracing framework for the ASSISTments dataset that predicts students' responses to end-of-unit test problems from action logs of in-unit assignments. It constructs IEU vectors (problem, sequence, student, and class information) as queries and IIU vectors (adding action-type embeddings and action features with positional encoding) as keys and values for a Transformer Encoder. The article states it is "a novel Transformer-based framework for the ASSISTments dataset which integrates several data-preprocessing techniques with a Transformer-based predictive model". Code, saved models, and predictions are released on OSF.

## Design Implications

### Context
#### Requirements
- Auxiliary information on problems, sequences, students, and classes (e.g., BERT+PCA problem text embeddings, curriculum folder paths, class memberships for SVD embeddings) is available in the training data.
#### Constraints
- The framework is designed for the distinction between in-unit assignments and end-of-unit tests; some dataset items lack features beyond their IDs, introducing missing or incomplete data the model must account for.

### Target Learners
- K-12 mathematics students using the ASSISTments online learning platform

### Target Learning Goals
- Predicting student performance on end-of-unit mathematics test problems from clickstream process data

## Related Elements
- 

## Examples
-

## Key Sources
- Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/
