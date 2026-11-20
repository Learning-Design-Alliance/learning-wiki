---
type: claim
title: MAIHDA maintains prediction accuracy at smaller strata sample sizes than fixed effects models
description: MAIHDA maintains prediction accuracy at smaller strata sample sizes than fixed effects models
id: maihda-accurate-smaller-strata-samples
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: van-dusen-2024
    resource: "https://doi.org/10.1177/00380407241254092"
    title: "Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A. (2024). Comparing the efficacy of fixed effect and MAIHDA models in predicting outcomes for intersectional social strata. Originally published 2023. [doi:10.1177/00380407241254092](https://doi.org/10.1177/00380407241254092)"
    author: "Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MAIHDA maintains prediction accuracy at smaller strata sample sizes than fixed effects models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MAIHDA's mean absolute true error stayed below the fixed effects model's error at strata N=20 (4.4) until strata sample sizes fell to five or fewer. [→ Van Dusen 2024](#van-dusen-2024)

## Evidence

### Van Dusen 2024

Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A. (2024). Comparing the efficacy of fixed effect and MAIHDA models in predicting outcomes for intersectional social strata. Originally published 2023. [doi:10.1177/00380407241254092](https://doi.org/10.1177/00380407241254092)

`q2 · i?` · `design · r2`

Simulation analysis of mean absolute true error for strata sample sizes 1-20 (Table 5, Figure 6), benchmarked against the fixed effects error at strata N=20 with total N=500. "For the MAIHDA model, the mean absolute true error did not reach 4.4 until the strata sample sizes were reduced to five or fewer."

> "For the MAIHDA model, the mean absolute true error did not reach 4.4 until the strata sample sizes were reduced to five or fewer."

## Discussion


## Related Claims
- [MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows](maihda-more-accurate-than-fixed-effects-strata.md) — a broader claim this one bears on
- [MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals](maihda-negative-bias-tiny-strata.md) — related
- [The MAIHDA accuracy advantage over fixed effects is largest for the smallest strata, such as FG Black women](maihda-advantage-largest-small-strata.md) — related
- [Precision-weighted shrinkage in MAIHDA yields reliable conservative estimates for small strata and helps solve the multiple-testing problem](maihda-shrinkage-small-strata-advantages.md) — related
