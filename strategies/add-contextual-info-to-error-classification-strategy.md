---
type: strategy
id: add-contextual-info-to-error-classification-strategy
title: Feed additional contextual information about student intent (ITS-recorded actions, knowledge levels) into LLM error classifiers, and extend toward feedback generation
description: The authors recommend exploiting the flexible string input of LLM-based classifiers by including information beyond equations.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: mcnichols-2023
    resource: "https://arxiv.org/abs/2305.06163"
    title: "McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. https://arxiv.org/abs/2305.06163"
    author: "McNichols, H., Zhang, M., & Lan, A"
---

# Feed additional contextual information about student intent (ITS-recorded actions, knowledge levels) into LLM error classifiers, and extend toward feedback generation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors recommend exploiting the flexible string input of LLM-based classifiers by including information beyond equations. They showed that student action context from Cognitive Tutor logs gives "a signiﬁcant performance improvement", and hypothesize that "providing further contextual information, such as student knowledge levels, will continue to improve performance". They also propose an avenue where the method is "extend[ed] ... to generate feedback, rather than classify errors", since most mis-classifications stem from ambiguous labels.

## Design Implications

### Context
#### Requirements
- An ITS or similar system that records interaction data (e.g. student-selected actions) that can be tokenized into the model input.
#### Constraints
- The hypothesis about knowledge-level context is untested in this article; GPT-2 degraded slightly with programmatic log-text input, so model choice matters.

### Target Learners
- Middle- and secondary-school algebra students in ITS environments

### Target Learning Goals
- Improving accuracy of automated error classification so appropriate feedback can be delivered to students

## Claims

- [Adding ITS-recorded student action context to the input significantly improves MLM-based error classifiers, though GPT-2 declines slightly](../claims/action-context-improves-error-classification.md) [+W]
- [Most frequent mis-classifications by the BERT + Action method involve ambiguous or overlapping error classes, suggesting an upper limit on dataset performance](../claims/misclassification-ambiguous-error-classes.md) [~W]
- [Among tested LLMs, only BERT beats the baseline; GPT-2, MathBERT and XLM-RoBERTa underperform both baselines](../claims/only-bert-beats-error-classification-baseline.md) [~W]

## Related Strategies

- [Use hybrid architectures in which KG-grounded classifiers handle diagnosis while LLMs provide open-ended scaffolding and dialogue](hybrid-kg-diagnosis-llm-scaffolding-architecture.md)

## Examples
-

## Key Sources
- McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. https://arxiv.org/abs/2305.06163. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)
