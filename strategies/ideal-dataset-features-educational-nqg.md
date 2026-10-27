---
type: strategy
id: ideal-dataset-features-educational-nqg
title: "Design educational QG datasets with six features: higher-level questions, diverse contexts, deep answers, key-content highlights, short verification contexts, and question-type annotations"
description: "The review enumerates six imperative dataset features for educational question generation model development: focusing on higher-level questions, including diverse educational contexts, optional answers with depth, hig..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: said-al-faraby-2024
    resource: "https://doi.org/10.1007/s40593-023-00374-x"
    title: "Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony. (2024). Review on Neural Question Generation for Education Purposes. Int J Artif Intell Educ 34:1008–1045. https://doi.org/10.1007/s40593-023-00374-x"
    author: Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony
---

# Design educational QG datasets with six features: higher-level questions, diverse contexts, deep answers, key-content highlights, short verification contexts, and question-type annotations

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The review enumerates six imperative dataset features for educational question generation model development: focusing on higher-level questions, including diverse educational contexts, optional answers with depth, highlights for key content selection, shorter context for human verification, and question type annotations. It argues these features align dataset design "with the overarching objectives of enhancing the educational question generation process" and enable controlled generation of specific question types.

## Design Implications

### Context
#### Requirements
- Annotation of question types relevant to educational purposes is needed for controlled question generation and systematic model training
- For longer contexts, highlights or specific portions contributing to corresponding questions must be incorporated
#### Constraints
- Existing datasets such as LearningQ lack keyword annotation or target answers, and OpenStax lacks reference questions, requiring additional processing

### Target Learners
- students in K-12 and higher education studying from textbook- and exam-derived materials

### Target Learning Goals
- generating higher-level questions that support comprehension, higher-order thinking, and active retrieval

## Claims

- [Multi-paragraph educational contexts require key content identification for useful NQG](../claims/key-content-identification-long-educational-contexts.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony. (2024). Review on Neural Question Generation for Education Purposes. Int J Artif Intell Educ 34:1008–1045. https://doi.org/10.1007/s40593-023-00374-x
