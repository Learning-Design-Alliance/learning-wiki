---
type: design
id: colab-gai-embedded-notebook-worksheets
title: Colab notebooks as active-learning worksheets with embedded GAI tutorial prompts and interactive plots
description: A lesson-level design in which Colab Python notebooks serve as in-class worksheets submitted at the end of active-learning sessions, combining markdown tutorial cells, suggested GAI chat prompts, pre-populated code wi...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: stubbs-2025
    resource: "https://github.com/astrostubbs/harvard-astro17-labs"
    title: "Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A. (2025). Lessons Learned from Integrating Generative AI into an Introductory Undergraduate Astronomy Course at Harvard. https://github.com/astrostubbs/harvard-astro17-labs"
    author: "Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A"
---

# Colab notebooks as active-learning worksheets with embedded GAI tutorial prompts and interactive plots

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lesson-level design in which Colab Python notebooks serve as in-class worksheets submitted at the end of active-learning sessions, combining markdown tutorial cells, suggested GAI chat prompts, pre-populated code with slider-controlled real-time plots, and empty cells for GAI-assisted code generation. Cells with "adjustable parameters using slider bars and associated real-time plots to reinforce concepts and build intuition" let students iteratively engage with GAI tutorial material linked to quantitative analysis tasks. Students worked in groups of 2-3 and submitted notebooks independently.

## Design Implications

### Context
#### Requirements
- A GAI-enabled notebook environment (Colab with embedded Gemini) accessible without API keys
- Data files loaded into each student's Google Drive folder
#### Constraints
- Non-default Python libraries do not persist and must be reinstalled each run; data-file interaction is slightly cumbersome and requires an authentication step

### Target Learners
- introductory undergraduate science students working in small groups

### Learning Goals
- fitting models to data
- building conceptual intuition through interactive visualization

### Claims
- [Gai Utility Ranked Task Focused Work Highest](../claims/gai-utility-ranked-task-focused-work-highest.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A. (2025). Lessons Learned from Integrating Generative AI into an Introductory Undergraduate Astronomy Course at Harvard. https://github.com/astrostubbs/harvard-astro17-labs
