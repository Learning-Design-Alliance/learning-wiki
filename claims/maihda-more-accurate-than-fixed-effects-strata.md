---
type: claim
title: MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows
description: MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows
id: maihda-more-accurate-than-fixed-effects-strata
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
    kind: causal
    rigour: 2
---

# MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across simulated datasets, MAIHDA had smaller mean absolute true errors in 56 of 60 strata-by-sample-size cases, outperforming fixed effects models most at a total sample size of 500 (31%, 1.7 points) and least at 5,000 (13%, 0.2 points). [→ Van Dusen 2024](#van-dusen-2024)

## Evidence

### Van Dusen 2024

Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A. (2024). Comparing the efficacy of fixed effect and MAIHDA models in predicting outcomes for intersectional social strata. Originally published 2023. [doi:10.1177/00380407241254092](https://doi.org/10.1177/00380407241254092)

`q2 · i?` · `causal · r2`

Simulation study comparing fixed effects and MAIHDA models on 2,956 simulated datasets grounded in real-world FCI data at total sample sizes of 500, 1,000, and 5,000. "The MAIHDA model had smaller mean absolute true errors in 56 of the 60 cases", with margins of 31% (1.7 points) at N=500 versus 13% (0.2 points) at N=5,000.

> "The MAIHDA model had smaller mean absolute true errors in 56 of the 60 cases (i.e., 20 strata in each of the three total sample sizes)."

## Discussion


## Related Claims
- [MAIHDA maintains prediction accuracy at smaller strata sample sizes than fixed effects models](maihda-accurate-smaller-strata-samples.md) — a narrower finding that bears on this claim
- [The MAIHDA accuracy advantage over fixed effects is largest for the smallest strata, such as FG Black women](maihda-advantage-largest-small-strata.md) — related
- [Precision-weighted shrinkage in MAIHDA yields reliable conservative estimates for small strata and helps solve the multiple-testing problem](maihda-shrinkage-small-strata-advantages.md) — related
- [MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals](maihda-negative-bias-tiny-strata.md) — related
- [Mean absolute error between the 19 subgroup means and the pan-Asian aggregate was 3.9 percentage points at pretest and 4.0 at posttest, roughly 4-5 weeks of learning](mae-subgroup-vs-pan-asian-four-weeks.md) — related
