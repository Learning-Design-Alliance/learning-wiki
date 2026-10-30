---
type: claim
title: In 5-fold cross-validation, multi-bin time-variant model fits outperform single-bin fits, with diminishing returns beyond a 5-bin split and further gains from differentiating by learner and amount of practice
description: In 5-fold cross-validation, multi-bin time-variant model fits outperform single-bin fits, with diminishing returns beyond a 5-bin split and further gains from differentiating by learner and amount of practice
id: cross-validation-favors-time-variant-fits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: maarten-van-der-velde-2026
    resource: "https://doi.org/10.1038/s41539-026-00447-1"
    title: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1"
    author: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: maarten-van-der-velde-2026-2
    resource: "https://doi.org/10.1038/s41539-026-00447-1"
    title: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1"
    author: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In 5-fold cross-validation, multi-bin time-variant model fits outperform single-bin fits, with diminishing returns beyond a 5-bin split and further gains from differentiating by learner and amount of practice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Dividing the interval range into multiple time bins generally produced better out-of-sample predictive performance than single-bin variants, with diminishing returns beyond a 5-bin split. [→ Maarten van der Velde 2026](#maarten-van-der-velde-2026)
`q2 i?` Differentiating fits by learner and by number of practice trials in the first session further improved predictive performance. [→ Maarten van der Velde 2026 (2)](#maarten-van-der-velde-2026-2)

## Evidence

### Maarten van der Velde 2026

Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1

`q2 · i?` · `associational · r2`

5-fold cross-validation with stratification by learner and interval bin, comparing summed log-likelihood on held-out folds; 3,650 sequences (14.1%) were excluded, leaving 22,193 sequences for evaluation. "a division into multiple time bins generally resulted in a better-performing model than the single-bin variants."

> "As Fig.2 shows, a division into multiple time bins generally resulted in a better-performing model than the single-bin variants, albeit with diminishing returns beyond a 5-bin split."

### Maarten van der Velde 2026 (2)

Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1

`q2 · i?` · `associational · r2`

Same cross-validated comparison at the group, by-learner, and by-practice-trial level. The article reports that "differentiating between learners, as well as differentiating between different amounts of practice prior to the between-session interval, produces a further improvement in predictive performance."

> "As Fig. 2a shows, differentiating between learners, as well as differentiating between different amounts of practice prior to the between-session interval, produces a further improvement in predictive performance."

## Discussion


## Related Claims
- [Allowing ACT-R memory parameters to vary with the between-session interval produces a strong fit between model and recall data across timescales](time-variant-parameters-capture-retention-across-timescales.md) — related
- [Extrapolating from parameters fitted to a restricted range of between-session intervals produces worse predictions than time-variant fits](restricted-range-fits-extrapolate-poorly.md) — related
- [Optimal ACT-R parameter values change systematically and predictably with the length of the between-session interval](parameters-vary-systematically-with-interval.md) — related
- [Split-half stability analysis shows fitted learning-rate parameters are meaningful, with Spearman correlations between 0.5 and 0.7 across independent data halves](split-half-learning-rate-stability.md) — related
