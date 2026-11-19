---
type: claim
title: "PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations"
description: "PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations"
id: pjsd-outperforms-repetition-baseline-uptake
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: dorottya-demszky-2021
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The PJSD model (ρ=.540) significantly outperforms the %-IN-T baseline (ρ=.523) in correlation with human uptake annotations. [→ Dorottya Demszky 2021](#dorottya-demszky-2021)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `associational · r2`

Correlation study on the released annotated dataset: model scores were correlated with averaged z-scored expert judgments via Spearman ρ with bootstrap confidence intervals. The PJSD model reached "ρ=.540" versus %-IN-T's .523, a difference the authors report as significant; the upper bound of rater agreement was estimated at ρ=.539.

> "Table 3 shows that the PJSD model (ρ=.540) signiﬁcantly outperforms %- IN-T. Our rough estimate on the upper bound of rater agreement (ρ=.539, obtained from a pilot annotation where all 13 raters rated 70 examples)"

## Discussion


## Related Claims
- [Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set](elaboration-prompts-pjsd-advantage.md) — related
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](pjsd-captures-uptake-phenomena-switchboard.md) — related
- [PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting](pjsd-correlates-educational-outcomes-three-datasets.md) — related
- [Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness](supervised-models-competitiveness-uptake.md) — related
- [Word-overlap measures outperform sentence-level similarity measures, including neural ones, at measuring uptake](token-overlap-outperforms-sentence-similarity-uptake.md) — related
