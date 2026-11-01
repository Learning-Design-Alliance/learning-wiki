---
type: claim
title: Quantile regression revealed larger intervention effects on GMRT reading comprehension at the .25–.30 quantiles (g = .35, ~9 points) and the .50 quantile (g = 0.22, ~5 points), but not at other quantiles or on WJ-III Passage Comprehension
description: Quantile regression revealed larger intervention effects on GMRT reading comprehension at the .25–.30 quantiles (g = .35, ~9 points) and the .50 quantile (g = 0.22, ~5 points), but not at other quantiles or on WJ-III...
id: quantile-regression-larger-effects-25-50-quantiles
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: al-otaiba-2018
    resource: "https://doi.org/10.1111/ldrp.12179"
    title: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179"
    author: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B."
    q: 3
    i: 1
    kind: causal
    rigour: 2
  - id: al-otaiba-2018-2
    resource: "https://doi.org/10.1111/ldrp.12179"
    title: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179"
    author: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B."
    q: 3
    i: 1
    kind: causal
    rigour: 2
  - id: al-otaiba-2018-3
    resource: "https://doi.org/10.1111/ldrp.12179"
    title: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179"
    author: "Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B."
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Quantile regression revealed larger intervention effects on GMRT reading comprehension at the .25–.30 quantiles (g = .35, ~9 points) and the .50 quantile (g = 0.22, ~5 points), but not at other quantiles or on WJ-III Passage Comprehension

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q3` · `i1` small
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i1` At the .50 quantile of GMRT reading comprehension, the treatment group outperformed the comparison group by approximately 5 points (g = 0.22), controlling for baseline. [→ Al Otaiba 2018](#al-otaiba-2018)
`q3 i1` At the .25 to .30 quantiles of GMRT reading comprehension, the treatment group outperformed the comparison group by approximately 9 points (g = .35). [→ Al Otaiba 2018 (2)](#al-otaiba-2018-2)
`q3 i?` No significant differences were observed at other estimated quantiles of the GMRT, nor on the WJ-III Passage Comprehension outcomes at any quantile. [→ Al Otaiba 2018 (3)](#al-otaiba-2018-3)

## Evidence

### Al Otaiba 2018

Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179

`q3 · i1` · `causal · r2`

Exploratory post-hoc multilevel quantile regression on GMRT reading comprehension post-test, estimated with the lqmm package in R with student-within-school nesting. The article reports "an effect size of g = 0.22" at the .50 quantile.

> "Specifically, at the .50 quantile, there was an effect size of g = 0.22, and the treatment group outperformed the comparison group by approximately 5 points, controlling for baseline."

### Al Otaiba 2018 (2)

Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179

`q3 · i1` · `causal · r2`

Same exploratory quantile regression analysis. The article reports "a larger effect of Passport" at the .25 to .30 quantiles, with the treatment group ahead by ~9 points (g = .35).

> "At lower levels of the GMRT Reading post-test (e.g., .25 to .30 quantiles), there was a larger effect of Passport, where the treatment group outperformed the comparison group by ~9 points (g = .35)."

### Al Otaiba 2018 (3)

Al Otaiba, S., Petscher, Y., Wanzek, J., Lan, P., & Rivas, B. (2018). I'm not throwing away my shot: What Alexander Hamilton can tell us about standard reading interventions. Learning Disabilities Research & Practice, 33(3), 156–167. https://doi.org/10.1111/ldrp.12179

`q3 · i?` · `causal · r2`

Same quantile regression analysis of both comprehension measures. The article reports no significant differences at other GMRT quantiles and none at any quantile on WJ-III Passage Comprehension; equivalence was not tested.

> "No significant differences were observed at other estimated quantiles of the GMRT, nor on the WJ-III PC outcomes at any quantile."

## Discussion


## Related Claims
- [Students' relative rank order in reading remained stable across fourth grade on most measures, with GMRT reading comprehension the exception (r = .16)](rank-order-stability-reading-measures-fourth-grade.md) — related
- [Effect sizes for the intervention were less than g = .03 on most outcomes, with small comprehension effects of g = 0.15 and g = 0.19](small-comprehension-effect-sizes-g-015-019.md) — related
- [GAMLSS is preferred over quantile regression when the total outcome distribution is of interest, while quantile regression suits specific quantile regions](gamlss-preferred-over-quantile-regression-total-distribution.md) — related
