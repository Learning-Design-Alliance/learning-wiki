---
type: strategy
id: separate-models-prototypes-and-series
title: Use separate models for generating MCQ prototypes and MCQ series
description: "The article recommends splitting test-item production into two tasks with different models: prototype creation via the multi-step template-like model with cognitive modelling, and series expansion via a one-step examp..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: krushynska-2025
    resource: "https://arxiv.org/abs/2602.08383"
    title: "Krushynska, T., Ursin, J., & Heilala, V. (2025). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. https://arxiv.org/abs/2602.08383"
    author: "Krushynska, T., Ursin, J., & Heilala, V"
---

# Use separate models for generating MCQ prototypes and MCQ series

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 design, 1 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article recommends splitting test-item production into two tasks with different models: prototype creation via the multi-step template-like model with cognitive modelling, and series expansion via a one-step example-based prompt generating five items simultaneously that differ from the prototype and each other. The authors conclude that their observations "suggest that using separate models for generating MCQ prototypes and test-item series is preferable."

## Design Implications

### Context
#### Requirements
- A completed MCQ prototype meeting the nine quality criteria, and specification of learning discipline and education level in the series prompt
#### Constraints
- Series items must not be obvious rephrasings; concept-derived series had more serious weaknesses and only 3.33% of rejected items were fixable by minor correction

### Target Learners
- university students in natural science disciplines

### Target Learning Goals
- maintaining exam security and content coverage through conceptually identical but contextually distinct item series

### Affordances
- [Three Step Human Ai Mcq Prototype Model](../designs/three-step-human-ai-mcq-prototype-model.md)

## Claims

- [A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt](../claims/multi-step-prompt-model-mcq-prototypes.md) [+W]
- [Distributing the three prompts among four AIs, each assigned the step it performed best, raised MCQ prototype acceptance further](../claims/distributing-prompts-among-ais-mcq.md) [+W]
- [In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model](../claims/input-type-learning-objectives-vs-textbook.md) [+W]
- [The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%](../claims/mcq-series-example-based-acceptance.md) [+W]
- [Generative AI, when used under precise conditions, reduces the cost and time of producing high-quality MCQs without compromising quality](../claims/genai-reduces-mcq-cost-and-time.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Krushynska, T., Ursin, J., & Heilala, V. (2025). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. https://arxiv.org/abs/2602.08383
