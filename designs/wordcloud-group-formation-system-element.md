---
type: design
id: wordcloud-group-formation-system-element
title: Group formation system with automatic grouping panel, group composition visualization, and Wordcloud group-awareness tool
description: A group formation system embedded in the LEAF infrastructure that automates grouping from learning log data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-18
sources:
  - id: liang-2025
    resource: "https://doi.org/10.1007/s11412-025-09452-9"
    title: "Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9"
    author: "Liang, C., Toyokawa, Y., & Ogata, H"
---

# Group formation system with automatic grouping panel, group composition visualization, and Wordcloud group-awareness tool

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A group formation system embedded in the LEAF infrastructure that automates grouping from learning log data. Teachers configure groups through an automatic grouping panel with pre-configured inputs, view each group's input characteristics via colored bar graphs in a group composition panel, and monitor performance through an evaluation panel for formative feedback. A Wordcloud visualization module acts as a GAT for active reading, displaying key terms highlighted by group members in BookRoll so that, for example, a word "appears prominently among other red markers in the Wordcloud, indicating frequent highlights by multiple group members", supporting discussion initiation and peer learning while preserving privacy by not naming individual proficiency.

## Design Implications

### Context
#### Requirements
- LEAF infrastructure consolidating LMS and BookRoll xAPI interaction logs; marker data collected during an individual active reading phase before grouping
#### Constraints
- Logs must be cleaned of duplicated markers in the same area and markers on irrelevant pages, which the authors note calls for context-based data-cleaning methods
- Wordcloud comparisons between Used and Non-used students were exploratory post-hoc subgroup analyses

### Target Learners
- Senior high school EFL students and their classroom teacher

### Learning Goals
- Vocabulary learning, text comprehension, and group knowledge awareness in collaborative active reading

### Claims
- [Mixed Ga Grouping Greater Vocabulary Gain Efl](../claims/mixed-ga-grouping-greater-vocabulary-gain-efl.md) [+M]
- [Wordcloud Use Survey And Outcome Comparison](../claims/wordcloud-use-survey-and-outcome-comparison.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9
