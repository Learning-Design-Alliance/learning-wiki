---
type: strategy
id: weak-supervision-plus-failure-accounting-for-educational-cas
title: Build educational conversational agents for scenarios without large datasets by combining weak supervision with accounting for model failures
description: "The authors' forward-looking recommendation from their analysis is that scarce training data need not block scenario development: \"Our analysis showed that conversational agents could be built for mathematical scenari..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: debajyoti-datta-2021
    resource: "https://arxiv.org/abs/2112.00985"
    title: "Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). https://arxiv.org/abs/2112.00985"
    author: Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown
---

# Build educational conversational agents for scenarios without large datasets by combining weak supervision with accounting for model failures

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors' forward-looking recommendation from their analysis is that scarce training data need not block scenario development: "Our analysis showed that conversational agents could be built for mathematical scenarios that do not have large datasets by combining weak supervision and accounting for model failures." Weak supervision generates pre-filled labels via labeling functions, expert annotators then refine them through model-assisted labeling, and an uncertainty-based supervisor catches model failures during use. The authors add that "more robust training paradigms will help build newer scenarios with minimal data," which they call especially useful in educational research where data collection relies on video and audio transcriptions of classroom recordings.

## Design Implications

### Context
#### Requirements
- Expert annotators to develop nuanced labeling functions and to verify weakly supervised labels
- An uncertainty quantification mechanism to detect and route model failures to a human supervisor
#### Constraints
- When dataset sizes are large, weak supervision alone achieves similar accuracies to supervised labels, but with small datasets it is used as part of the pipeline rather than by itself

### Target Learners
- Pre-service teachers
- Educational researchers developing new training scenarios

### Target Learning Goals
- Developing domain-specific questioning skills in scenarios that lack large labeled datasets

### Affordances
- [Uncertainty Threshold Supervisor Intervention Architecture](../designs/uncertainty-threshold-supervisor-intervention-architecture.md)

## Claims

- [A BERT-representation logistic regression entity recognizer reached precision 0.84, recall 0.82 and F1 0.83 on the mathematical questioning dataset](../claims/bert-logistic-regression-entity-recognition-performance.md) [+W]
- [A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario](../claims/distilbert-dialogue-act-f1-0-71-weak-supervision.md) [+W]
- [In an evaluation with eight experienced users, most utterances were correctly classified by the NLP components, with only certain utterance types always routed to the human supervisor](../claims/eight-user-evaluation-utterance-routing.md) [+W]
- [Weak supervision combined with model-assisted labeling cut expert annotators' labeling time by 70% while maintaining accuracy comparable to traditional labeling](../claims/weak-supervision-model-assisted-labeling-reduces-annotation-time.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). https://arxiv.org/abs/2112.00985
