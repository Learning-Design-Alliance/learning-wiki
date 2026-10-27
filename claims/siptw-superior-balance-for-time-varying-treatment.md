---
type: claim
title: Stabilized IPTW achieved covariate balance on all variables, outperforming unstabilized IPTW, and was used for effect estimation
description: Stabilized IPTW achieved covariate balance on all variables, outperforming unstabilized IPTW, and was used for effect estimation
id: siptw-superior-balance-for-time-varying-treatment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: yue-huang-2024
    resource: "https://doi.org/10.1007/s40593-024-00443-9"
    title: "Yue Huang, Joshua Wilson, & Henry May. (2024). Exploring the Long-Term Effects of the Statewide Implementation of an Automated Writing Evaluation System on Students' State Test ELA Performance. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00443-9"
    author: "Yue Huang, Joshua Wilson, & Henry May"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Stabilized IPTW achieved covariate balance on all variables, outperforming unstabilized IPTW, and was used for effect estimation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` SIPTW limited standardized mean differences for all covariates to the 0.1 cutoff while IPTW left two variables above it, so SIPTW was chosen for the treatment effects models. [→ Yue Huang 2024](#yue-huang-2024)

## Evidence

### Yue Huang 2024

Yue Huang, Joshua Wilson, & Henry May. (2024). Exploring the Long-Term Effects of the Statewide Implementation of an Automated Writing Evaluation System on Students' State Test ELA Performance. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00443-9

`q3 · i?` · `causal · r2`

Covariate balance evaluation comparing IPTW and SIPTW weighting across 16 covariates in the 134,425-student sample, using the cobalt package in R with an average absolute SMD cutoff of 0.1. SIPTW "limited results for all variables to the cutoff point".

> "IPTW constrained the SMDs for 14 of the 16 variables to the cutoff point (i.e., 0.1). The school size variable still had a slightly higher SMD between treatment conditions, but the SMD of the cumulative treatment indicator was even larger using IPTW."

## Discussion


## Related Claims
- [Before matching, bilingual Spanish and monolingual English kindergarteners differ substantially on covariates related to executive function](pre-matching-covariate-imbalance-bilingual-monolingual.md) — related
- [Monolingual and bilingual kindergarteners differ in English oral proficiency screening performance even after meeting the same inclusion cutoff](prelas-proficiency-distribution-differs-language-groups.md) — related
- [The main dropout-contagion findings remained essentially unchanged across five robustness checks including unmatched samples, IPTW, and conditional regression](robustness-checks-support-dropout-contagion-findings.md) — related
