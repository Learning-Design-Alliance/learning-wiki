---
type: claim
title: Clustering practice behavior in an open-ended task yields five behavior types that differ significantly in normalized learning gain
description: Clustering practice behavior in an open-ended task yields five behavior types that differ significantly in normalized learning gain
id: five-practice-behavior-clusters-differ-learning-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: anan-schütt-2024
    resource: "https://doi.org/10.1145/3636555.3636876"
    title: "Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André. (2024). Does Difficulty even Matter? Investigating Difficulty Adjustment and Practice Behavior in an Open-Ended Learning Task. Originally published 2023. [doi:10.1145/3636555.3636876](https://doi.org/10.1145/3636555.3636876)"
    author: Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: anan-schütt-2024-2
    resource: "https://doi.org/10.1145/3636555.3636876"
    title: "Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André. (2024). Does Difficulty even Matter? Investigating Difficulty Adjustment and Practice Behavior in an Open-Ended Learning Task. Originally published 2023. [doi:10.1145/3636555.3636876](https://doi.org/10.1145/3636555.3636876)"
    author: Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Clustering practice behavior in an open-ended task yields five behavior types that differ significantly in normalized learning gain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` K-means clustering on clickstream features (set, unset, reset counts, time between clicks) identifies five practice behavior clusters that differ significantly in NLG (KW H-test, H(4) = 18.43, p = 0.0010, η² = 0.206). [→ Anan Schütt 2024](#anan-schutt-2024)
`q2 i?` Clusters also differ significantly in perceived difficulty (ANOVA, F = 5.21, p = 0.0010, η² = 0.229) but not in flow (ANOVA, F = 1.0378, p = 0.39). [→ Anan Schütt 2024 (2)](#anan-schutt-2024-2)

## Evidence

### Anan Schütt 2024

Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André. (2024). Does Difficulty even Matter? Investigating Difficulty Adjustment and Practice Behavior in an Open-Ended Learning Task. Originally published 2023. [doi:10.1145/3636555.3636876](https://doi.org/10.1145/3636555.3636876)

`q2 · i?` · `causal · r?`

Post-hoc clustering analysis of 75 participants' practice-phase clickstreams (after removing 6 non-clicking and 5 outlier participants). K-means with kneedle-selected k = 5 yields clusters differing significantly in normalized learning gain, with η² = 0.206 as printed.

> "For NLG, there is a significant difference between the clusters (KW H-test, H(4) = 18.43, p = 0.0010, 𝜂2 = 0.206)"

### Anan Schütt 2024 (2)

Anan Schütt, Tobias Huber, Jauwairia Nasir, Cristina Conati, Elisabeth André. (2024). Does Difficulty even Matter? Investigating Difficulty Adjustment and Practice Behavior in an Open-Ended Learning Task. Originally published 2023. [doi:10.1145/3636555.3636876](https://doi.org/10.1145/3636555.3636876)

`q2 · i?` · `causal · r2`

Same cluster-level omnibus tests for the subjective measures: no significant flow difference, but a significant perceived-difference difference across the five clusters with the printed ANOVA statistics.

> "For flow, there is no significant difference (ANOVA, F = 1.0378, p = 0.39, 𝜂2 = 0.056). Finally, there is also a significant difference in perceived difficulty (ANOVA, F = 5.21, p = 0.0010, 𝜂2 = 0.229)"

## Discussion


## Related Claims
- [No significant difference in learning gain, flow, or perceived difficulty between predefined, self-determined, and DDA difficulty adjustment in an open-ended reasoning task](difficulty-adjustment-methods-no-difference-open-ended-task.md) — related
- [Heavy use of resets instead of careful backtracking with unsets appears counterproductive for learning (board-clearers cluster)](resets-counterproductive-board-clearers.md) — a narrower finding that bears on this claim
- [Thoughtful searchers (many sets/unsets with moderate pacing) learn significantly better than few-shot rushers, strugglers, and board-clearers](thoughtful-searchers-high-learning-gain.md) — a narrower finding that bears on this claim
- [Latent representations cluster into interpretable behavior types at question level, with less distinguishable task-switching clusters at student level](process-bert-representations-cluster-behavior-types.md) — related
- [Difficulty adjustment method shows no statistically testable influence on practice behavior; only a descriptive trend links Self-det to the board-clearers cluster](difficulty-method-practice-behavior-no-testable-link.md) — related
