---
type: strategy
id: corresponding-reference-solution-grading-strategy
title: Select reference solutions that correspond to the submitted solution when grading with LLM error detectors
description: "This strategy operationalizes the article's finding that reference choice is decisive when using LLM-powered error detectors: \"introducing corresponding reference solutions effectively mitigates bias\", whereas uniform..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: hang-li-2024
    resource: "https://arxiv.org/abs/2412.16838"
    title: "Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2024). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. https://arxiv.org/abs/2412.16838"
    author: Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu
---

# Select reference solutions that correspond to the submitted solution when grading with LLM error detectors

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This strategy operationalizes the article's finding that reference choice is decisive when using LLM-powered error detectors: "introducing corresponding reference solutions effectively mitigates bias", whereas uniformly supplying the conventional solution as reference tends to amplify it. In practice, a grader should generate or retrieve a reference aligned with the submitted solution's reasoning path — for example via the AskBD pipeline — rather than defaulting to the textbook solution. The article presents this as the motivation for adaptive reference generation during grading.

## Design Implications

### Context
#### Requirements
- A reference solution whose reasoning aligns with the submitted solution; misalignment between the reasoning behind different solutions and the reference can degrade final detection performance
#### Constraints
- Reference answers are not always available in real-world error detection scenarios, and conventional solutions are more commonly provided when they are

### Target Learners
- Students submitting math word problem solutions for automated grading

### Target Learning Goals
- Fair, accurate error detection that accepts diverse valid problem-solving approaches

### Affordances
- Askbd Framework

## Claims

- [Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it](../claims/reference-solution-choice-mitigates-or-amplifies-bias.md) [+W]
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](../claims/llm-conformity-bias-mwp-error-detection.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2024). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. https://arxiv.org/abs/2412.16838
