---
type: claim
title: The mixed algorithm produced groups differing significantly in marker-feature distributions, with shared (overlapping) yellow markers significantly lower than unique yellow markers
description: The mixed algorithm produced groups differing significantly in marker-feature distributions, with shared (overlapping) yellow markers significantly lower than unique yellow markers
id: marker-feature-distributions-differ-across-groups
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
sources:
  - id: liang-2025
    resource: "https://doi.org/10.1007/s11412-025-09452-9"
    title: "Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9"
    author: "Liang, C., Toyokawa, Y., & Ogata, H."
    q: 2
    i: 3
    kind: design
    rigour: 2
  - id: liang-2025-2
    resource: "https://doi.org/10.1007/s11412-025-09452-9"
    title: "Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9"
    author: "Liang, C., Toyokawa, Y., & Ogata, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The mixed algorithm produced groups differing significantly in marker-feature distributions, with shared (overlapping) yellow markers significantly lower than unique yellow markers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` A one-way ANOVA on the four group marker features showed a statistically significant difference among groups (F(3, 36) = 7.0755, p = .0007), with η² = 0.371. [→ Liang 2025](#liang-2025)
`q2 i?` Shared Yellow Markers were significantly lower than Unique Yellow Markers (p = .002), while the Unique Red vs Shared Red comparison showed no significant difference (p = .149). [→ Liang 2025 (2)](#liang-2025-2)

## Evidence

### Liang 2025

Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9

`q2 · i3` · `design · r2`

Descriptive analysis of the 10 algorithm-formed groups' marker features (unique/shared red and yellow markers) followed by one-way ANOVA after normality and variance checks. The test reached significance with η² = 0.371 ("37.1% of the variance explained by marker features").

> "The ANOV A results indicated a statistically signiﬁcant difference among the groups ( F(3, 36) = 7.0755, p = .0007). The effect size, measured as Eta Squared (η2), was 0.371, indicating a medium-to-large effect size, with 37.1% of the variance explained by marker features."

### Liang 2025 (2)

Liang, C., Toyokawa, Y., & Ogata, H. (2025). Optimizing group formation with a mixed genetic algorithm: an empirical study in active reading using marker data. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09452-9

`q2 · i?` · `design · r2`

Tukey's HSD pairwise comparisons of marker features. Shared Yellow was significantly lower than Unique Yellow (p = .002); Unique Red vs Shared Red was non-significant (p = .149), as were the remaining red-yellow pairs.

> "The Shared Yellow Marker exhibited signiﬁcantly lower values compared to the Unique Yellow Marker ( p = .002 <. 05). When comparing the Unique Red Marker and the Shared Red Marker , although there were more unique markers for the red marker, no signiﬁcant difference was found ( p = .149 >. 05)."

## Discussion


## Related Claims

- [Process mining of two fitness-typical groups suggests the group with more heterogeneous yellow markers and shared red markers worked more efficiently while both achieved the same summary outcome](process-mining-heterogeneous-yellow-group-more-efficient.md)
- [In a high school EFL active-reading setting, mixed genetic algorithm group formation with Wordcloud awareness produced significantly greater vocabulary learning gains than random grouping](mixed-ga-grouping-greater-vocabulary-gain-efl.md)
- [A text-mining group and representation tool scaffolds students' learning processes and improves outcomes under specific conditions](grt-text-mining-group-formation-scaffolds-learning.md) — a broader claim this one bears on
