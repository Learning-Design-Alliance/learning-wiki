---
type: claim
title: "In a re-analysis of PBL tutor-background data, neither a meta-regression nor subgroup comparisons found that tutor expertise predicts student learning"
description: "In a re-analysis of PBL tutor-background data, neither a meta-regression nor subgroup comparisons found that tutor expertise predicts student learning"
id: tutor-background-meta-regression-not-predictive
aliases: [tutor-background-subgroup-differences-nonsignificant]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-02
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: walker-2023
    resource: "https://doi.org/10.14434/ijpbl.v17i2.35844"
    title: "Walker, A., & Leary, H. (2023). Conducting Problem-Based Learning Meta-Analysis: Complexities, Implications, and Best Practices. The Interdisciplinary Journal of Problem-based Learning. https://doi.org/10.14434/ijpbl.v17i2.35844"
    author: "Walker, A., & Leary, H."
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# In a re-analysis of PBL tutor-background data, neither a meta-regression nor subgroup comparisons found that tutor expertise predicts student learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person
<!-- deprecated title (2026-10-05, covered only one of the two findings after the fold): In a dummy-coded meta-regression of PBL tutor background, no tutor expertise category significantly predicts student learning -->

## Subclaims

`q2 i?` A random-effects dummy-coded meta-regression with content novices as reference found no significant predictors of student learning (R2 = .01, Wald X2(4, 348) = 6.86, p = 0.14). [→ Walker 2023](#walker-2023)

`q2 i?` The largest mean difference between mixed (d = 0.34) and content expert (d = 0.22) tutors was not statistically significant, so tutor background alone does not explain variation in PBL effect sizes. [→ Walker 2023](#walker-2023)

## Evidence

### Walker 2023

Walker, A., & Leary, H. (2023). Conducting Problem-Based Learning Meta-Analysis: Complexities, Implications, and Best Practices. The Interdisciplinary Journal of Problem-based Learning. https://doi.org/10.14434/ijpbl.v17i2.35844

`q2 · i?` · `quant-synthesis · r2`

New meta-regression analysis of the Leary et al. (2013) tutor-background data using a random effects model with a restricted maximum likelihood estimator. The article reports that "no significant predictors of student learning were found, R2 = .01, Wald X2(4, 348) = 6.86, p = 0.14."

> "no significant predictors of student learning were found, R2 = .01, Wald X2(4, 348) = 6.86, p = 0.14."

The same article also compares tutor-background subgroups with a z test (carried over from the folded page `tutor-background-subgroup-differences-nonsignificant`, which recorded this entry separately as `r1`): the "largest mean difference between mixed (d = 0.34) and content experts (d = 0.22) failed to achieve statistical significance, z(213) = 1.80, p = 0.07." No effect size for the contrast itself is printed.

> "even the largest mean difference between mixed (d = 0.34) and content experts (d = 0.22) failed to achieve statistical significance, z(213) = 1.80, p = 0.07."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does the helper's domain expertise, by itself, predict how much the learner gains or how good the help is?* This table gathers the studies behind this claim and the 2 narrower claims that bear on it: **4 distinct studies** (3 associational, 1 quant-synthesis), `q2`, 0 of 4 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Walker 2023](https://doi.org/10.14434/ijpbl.v17i2.35844) | q2 · quant-synthesis · r2 | i? | this claim |
| [Wu & Schunn 2023](https://doi.org/10.1037/edu0000768) | q2 · associational · r? | i? | [In two secondary-school writing studies, peer reviewers' own performance predicted how hel](peer-feedback-accuracy-depends-on-expertise.md) (qualifies) |
| [Schunn et al. 2016](https://doi.org/10.1002/jaal.525) | q2 · associational · r2 | i? | [In two secondary-school writing studies, peer reviewers' own performance predicted how hel](peer-feedback-accuracy-depends-on-expertise.md) (qualifies) |
| Gordon 2018 | q2 · associational · r2 | i? | [CPS mentor teachers were more qualified than other teachers, but their qualifications were](cps-mentor-teachers-more-qualified-qualifications-unrelated-to-outcomes.md) (supports) |
<!-- synthesis:end -->

## Discussion

Both findings come from one source, Walker & Leary's (2023) re-analysis of the Leary et al. (2013) PBL meta-analysis data: a dummy-coded meta-regression with content novices as reference (no significant predictors, R² = .01) and a subgroup comparison whose largest difference (mixed against content-expert tutors) was not significant (p = 0.07). Both are null results without a powered equivalence test, so they show that tutor background did not detectably explain variation in PBL effect sizes in these data, not that it has no effect.

## Related Claims

- [The overall effect of PBL in the tutor-background meta-analysis is modest (g = 0.27) with large, statistically significant heterogeneity](pbl-overall-effect-modest-large-heterogeneity.md) — related
- Robust variance estimation shows study of origin does not impact the final effect size in the PBL tutor-background data — related
- [Individual PBL outcome effect sizes in the tutor-background meta-analysis span a massive range, from g = -1.26 to g = 1.91](massive-range-pbl-outcome-effect-sizes.md) — related
- [Problem-based learning shows null or negative effects on basic knowledge acquisition but positive effects on conceptual understanding and transfer relative to direct instruction](pbl-null-basic-knowledge-positive-transfer.md) — related
