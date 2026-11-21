---
type: strategy
id: holistic-free-form-evaluation-strategy
title: Move beyond MMLU to a holistic evaluation of free-form tutor responses
description: "The article argues the current metric, MMLU, \"falls short in capturing the nuanced performance required for fine-tuned or customized models in RAG pipelines\" and plans a more holistic framework in which the model gene..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: juan-segundo-hevia-2025
    resource: "https://arxiv.org/abs/2510.06255"
    title: "Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. https://arxiv.org/abs/2510.06255"
    author: Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar
---

# Move beyond MMLU to a holistic evaluation of free-form tutor responses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article argues the current metric, MMLU, "falls short in capturing the nuanced performance required for fine-tuned or customized models in RAG pipelines" and plans a more holistic framework in which the model generates free-form responses evaluated for factual accuracy, coherence, and relevance against larger models. Because the burden of domain-specific knowledge rests on the RAG component, this framework would evaluate the language model on what it is actually responsible for: taking the prompt and RAG chunks, identifying relevant information, and formulating a comprehensible response.

## Design Implications

### Context
#### Requirements
- Free-form responses must be judged against larger models for factual accuracy, coherence, and relevance
#### Constraints
- 

### Target Learners
- students interacting with the customized offline AI tutor

### Target Learning Goals
- accurate, coherent, relevant explanations of coursework topics

## Claims

- [Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model](../claims/rag-context-reduces-small-model-accuracy.md) [+W]
- [Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training](../claims/mmlu-hellaswag-winogrande-stable.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. https://arxiv.org/abs/2510.06255
