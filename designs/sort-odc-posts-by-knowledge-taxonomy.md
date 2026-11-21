---
type: design
id: sort-odc-posts-by-knowledge-taxonomy
title: Sort online community posts by a knowledge taxonomy of the UI components and visual elements their comments mention
description: "The article's first design goal is to \"Sort posts based on the knowledge taxonomy about the UI components and visual elements that their comments mention\", because existing ODCs classify posts by intention or example..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: xia-chen-2025
    resource: "https://arxiv.org/abs/2504.09827"
    title: "Xia Chen, Xinyue Chen, Weixian Hu, Haojia Zheng, Yujun Qian, and Zhenhui Peng. (2025). Redesign of Online Design Communities: Facilitating Personalized Visual Design Learning with Structured Comments. https://arxiv.org/abs/2504.09827"
    author: Xia Chen, Xinyue Chen, Weixian Hu, Haojia Zheng, Yujun Qian, and Zhenhui Peng
---

# Sort online community posts by a knowledge taxonomy of the UI components and visual elements their comments mention

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's first design goal is to "Sort posts based on the knowledge taxonomy about the UI components and visual elements that their comments mention", because existing ODCs classify posts by intention or example type but few provide a knowledge taxonomy for locating learning content. In DesignLearner, selecting a UI component sorts posts by keyword counts, and a visual element filter re-sorts them with a weighted score emphasizing visual elements. This addresses formative-study challenges of filtering posts and finding related content.

## Design Implications

### Context
#### Requirements
- A validated computational workflow that detects UI component and visual element keywords in comments
#### Constraints
- The keyword-count weighting (0.4 for UI component, 0.6 for visual element) was chosen for the study's focus and could be re-assigned for learners focused on applying given visual elements across components

### Target Learners
- novices browsing online design communities for learning

### Learning Goals
- finding design examples and comments relevant to interested knowledge points

### Claims
- [Odc Novice Learning Challenges Formative](../claims/odc-novice-learning-challenges-formative.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Xia Chen, Xinyue Chen, Weixian Hu, Haojia Zheng, Yujun Qian, and Zhenhui Peng. (2025). Redesign of Online Design Communities: Facilitating Personalized Visual Design Learning with Structured Comments. https://arxiv.org/abs/2504.09827
