---
type: element
id: comta-and-mathdial-tutoring-dialogue-datasets
title: CoMTA and MathDial Math Tutoring Dialogue Datasets
description: The article evaluates dialogueKT on two existing math tutoring dialogue datasets.
canonical: true
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# CoMTA and MathDial Math Tutoring Dialogue Datasets

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article evaluates dialogueKT on two existing math tutoring dialogue datasets. "The CoMTA dataset [39] contains 188 dialogues between human students and Khanmigo, Khan Academy’s GPT-4- powered tutor"; after removing Calculus dialogues, 153 remain, with 623 labeled turn pairs and 164 unique KCs. MathDial contains 2,848 dialogues between GPT-3.5-simulated students and crowd workers role-playing tutors; the article uses 2,823 with 13,200 labels and 145 KCs.

## Design Implications

### Context
#### Requirements
- CoMTA has no defined train/test split, so the article uses 5-fold cross-validation; MathDial uses the original train/test split of 2,235/588 dialogues.
#### Constraints
- Calculus dialogues are removed from CoMTA because Common Core does not contain Calculus standards.
- CoMTA contains partial dialogues that are cut short for LLM evaluation purposes.
- MathDial students are simulated by an LLM; the authors state it is unlikely for simulated students to behave like real ones.

### Target Learners
- Human students tutored by Khanmigo (CoMTA) and GPT-3.5-simulated students tutored by crowd workers (MathDial)

### Target Learning Goals
- Estimating student knowledge of math knowledge components (Common Core standards) and predicting student response correctness across dialogue turns

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](../claims/dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) [+W]
- [LLMKT's predicted knowledge change curves on CoMTA are mixed across the 15 most frequent KCs, though overall they mostly resemble the power law of practice when dialogues have sufficient turns.](../claims/llmkt-knowledge-change-curves-show-mixed-trends-resembling-power-law-of-practice.md) [+W]
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](../claims/existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) [+W]
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](../claims/expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
