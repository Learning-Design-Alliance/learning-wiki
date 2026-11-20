---
type: claim
title: MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals
description: MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals
id: maihda-negative-bias-tiny-strata
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
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

# MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When strata sample sizes fell below ten, MAIHDA mean true errors showed a small but consistent negative bias, driven by shrinkage pulling the least-represented strata's predictions toward the additive score. [→ Van Dusen 2024](#van-dusen-2024)

## Evidence

### Van Dusen 2024

Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A. (2024). Comparing the efficacy of fixed effect and MAIHDA models in predicting outcomes for intersectional social strata. Originally published 2023. [doi:10.1177/00380407241254092](https://doi.org/10.1177/00380407241254092)

`q2 · i?` · `design · r2`

Simulation analysis of mean true error by strata sample size (Table 5). "In our MAIHDA models, when strata sample sizes fell below ten individuals, we began to have a small but consistent negative bias in the mean true error scores", attributed to shrinkage regressing predictions toward the additive score for the least represented strata.

> "In our MAIHDA models, when strata sample sizes fell below ten individuals, we began to have a small but consistent negative bias in the mean true error scores (see Table 5)."

## Discussion


## Related Claims
- [MAIHDA maintains prediction accuracy at smaller strata sample sizes than fixed effects models](maihda-accurate-smaller-strata-samples.md) — related
- [The MAIHDA accuracy advantage over fixed effects is largest for the smallest strata, such as FG Black women](maihda-advantage-largest-small-strata.md) — related
- [MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows](maihda-more-accurate-than-fixed-effects-strata.md) — related
- [Precision-weighted shrinkage in MAIHDA yields reliable conservative estimates for small strata and helps solve the multiple-testing problem](maihda-shrinkage-small-strata-advantages.md) — a broader claim this one bears on
