---
type: design
id: mixed-genetic-algorithm-homogeneous-heterogeneous-fitness
title: Mixed genetic algorithm fitness function balancing homogeneous and heterogeneous grouping components
description: The article adapts a mixed genetic algorithm (inspired by Revelo Sanchez et al., 2021) for data-driven group formation.
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

# Mixed genetic algorithm fitness function balancing homogeneous and heterogeneous grouping components

> **Design** · [All designs](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article adapts a mixed genetic algorithm (inspired by Revelo Sanchez et al., 2021) for data-driven group formation. Input characteristics are divided into homogeneous and heterogeneous components, and the group fitness score F′(gk) is "calculated by subtracting the F(gk) score for the homogeneous component from that of the heterogeneous component" (Eq. 2), so desirable groups minimize variance on homogeneous features while maximizing it on heterogeneous ones. The score is interpreted relatively among candidates generated from the same input feature set, and negative values occur when homogeneous-feature variance exceeds heterogeneous-feature variance.

## Design Implications

### Context
#### Requirements
- A student characteristic matrix (e.g., active reading marker clusters vectorized via Jaro–Winkler similarity with a threshold of 0.8) plus explicit decisions on which features are treated as homogeneous versus heterogeneous
#### Constraints
- The authors state the fitness value distribution revealed imbalances across groups, "raising important considerations about the trade-off between promoting internal group cohesion and ensuring equity across groups"
- The score is interpretable in relative terms, not as an absolute indicator

### Target Learners
- K-12 / senior high school EFL students in classroom collaborative learning

### Learning Goals
- Vocabulary learning and text comprehension through collaborative active reading

### Claims

- [Marker Feature Distributions Differ Across Groups](../claims/marker-feature-distributions-differ-across-groups.md) [+M]
- [Mixed Ga Grouping Greater Vocabulary Gain Efl](../claims/mixed-ga-grouping-greater-vocabulary-gain-efl.md) [+M]
- [Group summary scores did not differ significantly between algorithm-formed and randomly formed groups on content, vocabulary, or grammar rubrics](../claims/group-summary-scores-no-significant-difference.md) [~W]
- [Process mining of two fitness-typical groups suggests the group with more heterogeneous yellow markers and shared red markers worked more efficiently while both achieved the same summary outcome](../claims/process-mining-heterogeneous-yellow-group-more-efficient.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9
