---
type: claim
title: The routine rule for selecting the graph threshold makes naive comparisons of β0 between two datasets invalid
description: The routine rule for selecting the graph threshold makes naive comparisons of β0 between two datasets invalid
id: rule-selected-thresholds-make-cross-dataset-beta0-comparison-invalid
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: inoue-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)"
    author: "Inoue, H., & Yasutake, K."
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: inoue-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)"
    author: "Inoue, H., & Yasutake, K."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The routine rule for selecting the graph threshold makes naive comparisons of β0 between two datasets invalid

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` Because the selection rule fixes the ratio of β0 to N at approximately one quarter by construction in every dataset, two datasets analysed each under its own rule-selected ε are not comparable. [→ Inoue 2026](#inoue-2026)
`q1 i?` The authors' own earlier analysis put each side at its own threshold and the contrast reversed once quantities were recomputed at a common threshold. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q1 · i?` · `design · r2`

Analytical point about the standard working-point rule (grid search taking the ε whose mean weekly β0 is closest to a quarter of cohort size): it forces β0/N toward one quarter in any dataset, so cross-dataset comparisons at rule-selected thresholds are invalid.

> "the rule makes the ratio of β 0 to N approximately one quarter by construction in every dataset to which it is applied. Two datasets analysed each under its own rule-selected ε are therefore not comparable, however natural the comparison looks."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q1 · i?` · `design · r2`

The authors illustrate the rule's hazard with an error of their own: contrasts computed at per-dataset thresholds (0.68 vs 0.70; 0.36 vs 0.68) reversed when recomputed at a single common threshold.

> "an earlier round of our own analysis put each side at its own threshold, 0.68 against 0.70 in one year but 0.36 against 0.68 in another, and the contrast reversed once the quantities were recomputed at a common threshold."

## Discussion


## Related Claims
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) — related
