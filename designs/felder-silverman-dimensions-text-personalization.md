---
type: design
id: felder-silverman-dimensions-text-personalization
title: Felder-Silverman learning-preference dimensions as a text-personalization profile
description: "The study operationalizes learning preferences along the Felder-Silverman model, which \"consists of four dimensions assessing how students best perceive (sensing or intuitive), receive (visually or verbally), process..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: vaccaro-jr-2024
    resource: "https://github.com/m-vaccaro/LLMs-and-Personalized-Learning"
    title: "Vaccaro Jr., M., Friday, M., and Zaghi, A. (2024). Evaluating the capability of large language models to personalize science texts for diverse middle-school-age learners. https://github.com/m-vaccaro/LLMs-and-Personalized-Learning"
    author: Vaccaro Jr., M., Friday, M., and Zaghi, A
---

# Felder-Silverman learning-preference dimensions as a text-personalization profile

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The study operationalizes learning preferences along the Felder-Silverman model, which "consists of four dimensions assessing how students best perceive (sensing or intuitive), receive (visually or verbally), process (actively or reflectively), and understand (sequentially or globally) information". Because the study focused on text, the visual/verbal dimension was replaced with an imagery/no-imagery dimension. GPT-4 generated a short profile description along these dimensions from training-session choices, and the rewrite model aligned texts to the profile.

## Design Implications

### Context
#### Requirements
- A training session in which the student selects preferred paragraphs from pairs targeting the extremes of each dimension
#### Constraints
- The four dimensions do not explicitly account for a learner's preferred pace, specific interests, or existing knowledge; the profile remained static during the experiment

### Target Learners
- middle-school students in grades 7 and 8

### Learning Goals
- tailoring educational science text to individual learning preferences

### Claims
- [Gpt4 Aligned Texts Preferred Over Generic](../claims/gpt4-aligned-texts-preferred-over-generic.md) [+M]
- [Profile Recognition At Chance Group Difference](../claims/profile-recognition-at-chance-group-difference.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Vaccaro Jr., M., Friday, M., and Zaghi, A. (2024). Evaluating the capability of large language models to personalize science texts for diverse middle-school-age learners. https://github.com/m-vaccaro/LLMs-and-Personalized-Learning
