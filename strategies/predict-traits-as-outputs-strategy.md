---
type: strategy
id: predict-traits-as-outputs-strategy
title: Use trait values as auxiliary prediction outputs rather than input scaffolds when supervising rubric-agnostic essay scoring
description: "The article finds that how traits enter fine-tuning matters: \"predicting trait values as outputs performs better than providing them as inputs, since generating trait-level abstractions encourages the model to learn a..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: nischal-ashok-kumar-2026
    resource: "https://github.com/umass-ml4ed/generalization-in-essay-scoring"
    title: "Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. https://github.com/umass-ml4ed/generalization-in-essay-scoring"
    author: Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan
---

# Use trait values as auxiliary prediction outputs rather than input scaffolds when supervising rubric-agnostic essay scoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article finds that how traits enter fine-tuning matters: "predicting trait values as outputs performs better than providing them as inputs, since generating trait-level abstractions encourages the model to learn a structured mapping from text to rubric-relevant features." Incorporating natural-language trait observations alongside values does not improve performance, reportedly because longer textual explanations introduce variability that makes consistent signals harder to extract. The strategy is to train models to jointly generate categorical trait values with the final rubric label.

## Design Implications

### Context
#### Requirements
- A fixed trait schema defined prior to experimentation and held fixed across train/test splits
- LLM-generated trait annotations (silver labels) for essays
#### Constraints
- Incorporating trait observations does not improve performance
- Trait benefit is concentrated in the No Labels setting and diminishes under stronger supervision

### Target Learners
- 6th-12th grade U.S. students writing argumentative essays

### Target Learning Goals
- Rubric-based scoring of critical thinking in student writing

## Claims

- [Predicting rubric-agnostic trait values as outputs improves cross-rubric essay scoring in the No Labels setting, improving macro F1 by 5.0% over a no-traits baseline](../claims/trait-output-supervision-improves-no-labels-cross-rubric-scoring.md) [+W]
- [The benefit of trait-based representations diminishes when target-essay supervision is available, with traits not consistently outperforming no-traits baselines under Pseudo or Gold Labels](../claims/trait-benefit-diminishes-with-target-essay-supervision.md) [-W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. https://github.com/umass-ml4ed/generalization-in-essay-scoring
