---
type: design
id: bloom-classification-ui-selected-questions-verbs
title: Lightweight UI for instructor-driven Bloom classification built on the selected-questions-verbs prompt
description: "A lightweight tool built on the article's best-performing prompting strategy."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: abdolali-faraji-2026
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
---

# Lightweight UI for instructor-driven Bloom classification built on the selected-questions-verbs prompt

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lightweight tool built on the article's best-performing prompting strategy. Instructors provide a small set of example questions per Bloom level for their context; the tool "extracts key action verbs from these examples" and uses them with the examples to construct the classification prompt. Users upload question sets in CSV/Excel and receive Bloom-level predictions in structured output. A user study with N=50 Prolific participants reported low workload (NASA-TLX means: mental demand 2.32, effort 2.46, frustration 1.68) and mean SUS of 78.2 (SD 14.07).

## Design Implications

### Context
#### Requirements
- Instructors must supply example questions per Bloom level for their specific course, topic, or learning objectives
#### Constraints
- The article notes feedback from real instructors would provide more precise insights for practical deployment, as the UI was tested with pilot users

### Target Learners
- instructors classifying large question banks

### Learning Goals
- automatic Bloom-level classification of assessment questions

### Claims
- [Selected Questions Verbs Best Prompt](../claims/selected-questions-verbs-best-prompt.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684
