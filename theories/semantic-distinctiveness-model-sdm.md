---
type: theory
title: Semantic Distinctiveness Model (SDM)
description: "The SDM is a distributional model of lexical semantics that incorporates an attention-weighting mechanism when encoding a new context entry in a word's vector."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: johns-2016
    resource: "https://doi.org/10.3758/s13423-015-0980-7"
    title: "Johns, B. T., Dye, M., & Jones, M. N. (2016). The influence of contextual diversity on word learning. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0980-7"
    author: "Johns, B. T., Dye, M., & Jones, M. N"
---

# Semantic Distinctiveness Model (SDM)

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (3 for) · 1 study, `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The SDM is a distributional model of lexical semantics that incorporates an attention-weighting mechanism when encoding a new context entry in a word's vector. As the article states, "If the new context is congruent with the expected meaning in memory, it is encoded at a weaker intensity than if the new context is surprising." Vector magnitude indexes lexical availability and vector phase indexes semantic similarity, allowing one model to explain both lexical access and semantic similarity behavior. In this study the SDM was trained on the same passages the subjects read, predicting stronger memory for diverse-context items and more stable representations for uniform-context items.

## Design Implications

### Context
#### Requirements
- Training on the same materials as learners to generate task-specific predictions
- A corpus (e.g., a 200-k document Wikipedia corpus) to build representations for associate words
#### Constraints
- The article states the SDM "is only a representational model" and does not itself implement predictive processing, though its predictions align with predictive accounts of language processing

### Target Learners
- adult readers learning novel vocabulary incidentally from text

### Target Learning Objectives
- word recognition
- semantic representation of novel words

### Claims
- [Diverse Contexts Improve Pseudoword Recognition Accuracy](../claims/diverse-contexts-improve-pseudoword-recognition-accuracy.md) [+M]
- [Redundant Contexts Improve Semantic Representations](../claims/redundant-contexts-improve-semantic-representations.md) [+M]
- [Diversity Dissociation Processing Versus Semantics](../claims/diversity-dissociation-processing-versus-semantics.md) [+M]

## Related Theories

- [Semantic diversity as a graded measure of contextual diversity based on document content overlap](semantic-diversity-graded-measure.md)
- [Expectancy-congruency learning mechanism updating lexical representations from context fit](expectancy-congruency-learning-mechanism.md)

## Examples
-

## Key Sources
- Johns, B. T., Dye, M., & Jones, M. N. (2016). The influence of contextual diversity on word learning. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0980-7
