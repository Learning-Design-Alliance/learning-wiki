---
type: strategy
id: escalate-explanation-level-repeated-requests
title: Escalate explanation scope and simplicity on repeated clarification requests
description: "The article recommends a two-tier escalation recipe: if the first explanation is insufficient, repeating the signal triggers a broader, simpler one."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: boris-ruf-2024
    resource: "https://arxiv.org/abs/2412.14201"
    title: "Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. https://arxiv.org/abs/2412.14201"
    author: Boris Ruf, Marcin Detyniecki
---

# Escalate explanation scope and simplicity on repeated clarification requests

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends a two-tier escalation recipe: if the first explanation is insufficient, repeating the signal triggers a broader, simpler one. First-level explanations cover the last sentence; second-level explanations take a broader perspective and use simple language. As printed: "In case the user continues to have comprehension problems, repeating the signal will trigger the system to simplify and expand the explanation further."

## Design Implications

### Context
#### Requirements
- The LLM prompt must define both scopes in advance, since second-level explanations "consider the last two sentences and thus take a broader perspective in its response" and are "explicitly asked to use simple language"
#### Constraints
- The article states the "methodological determination of the optimal text length as basis for the explanations remains a subject for future investigations"

### Target Learners
- viewers of recorded lectures who need a second, simpler clarification

### Target Learning Goals
- comprehension when an initial explanation is insufficient

### Affordances
- [Huh Button Method Llm Video Clarification](../designs/huh-button-method-llm-video-clarification.md)

## Related Strategies

- [Use impasse depth and type as real-time learning-analytics signals to trigger graduated escalation of tutor support](impasse-depth-type-analytics-escalation-signals.md)
- [Hybrid Socratic-to-sub-question tutoring with EEG-triggered fallback and progressively concrete hints](eeg-triggered-socratic-fallback-hybrid-tutoring.md)
- [Design chatbots that begin with guided inquiry and progressively provide explicit guidance when students remain stuck](chatbots-guided-inquiry-then-explicit-guidance.md)
- [Use a Plan-Do-Study-Act ramp to build simulation complexity stepwise, repeating a cycle when objectives are unmet before escalating.](pdsa-ramp-simulation-complexity-strategy.md)
- [Precision Requests](precision-requests.md)

## Examples
-

## Key Sources
- Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. https://arxiv.org/abs/2412.14201
