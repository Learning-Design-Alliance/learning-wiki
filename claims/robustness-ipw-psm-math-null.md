---
type: claim
title: Main findings were robust to inverse-probability weighting and propensity-score matching, but the mathematics effect lost significance in the lower-performing-half sample
description: Main findings were robust to inverse-probability weighting and propensity-score matching, but the mathematics effect lost significance in the lower-performing-half sample
id: robustness-ipw-psm-math-null
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: mixed
newest_evidence: 2025
sources:
  - id: jacobs-2025
    resource: "https://doi.org/10.1371/journal.pone.0323352"
    title: "Jacobs, M., Haelermans, C., & Meeter, M. (2025). Effective remediation programs for vulnerable students to overcome learning loss. PLoS One, 20(5). https://doi.org/10.1371/journal.pone.0323352"
    author: "Jacobs, M., Haelermans, C., & Meeter, M."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Main findings were robust to inverse-probability weighting and propensity-score matching, but the mathematics effect lost significance in the lower-performing-half sample

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` IPW-weighted and PSM-weighted DiD estimations confirmed the main findings. [→ Jacobs 2025](#jacobs-2025)
`q2 i?` When the sample was limited to lower-performing students, results remained consistent for composite and reading, but the mathematics effect was no longer significant. [→ Jacobs 2025](#jacobs-2025)

## Evidence

### Jacobs 2025

Jacobs, M., Haelermans, C., & Meeter, M. (2025). Effective remediation programs for vulnerable students to overcome learning loss. PLoS One, 20(5). https://doi.org/10.1371/journal.pone.0323352

`q2 · i?` · `causal · r2`

Robustness checks on the same DiD models: IPW weights aligning the sample with the national population (S9 Table), a lower-performing-half subsample (S10 Table), and Kernel propensity-score matching weights (S4 Appendix). The article states the IPW and PSM results confirm the main findings.

> "The results of limiting our sample to lower-performing students are consistent with the main finding for composite and reading. However, for mathematics, the effect is not significant anymore in this robustness check. Therefore, these results need to be treated with more caution"

## Discussion


## Related Claims
- [The main dropout-contagion findings remained essentially unchanged across five robustness checks including unmatched samples, IPTW, and conditional regression](robustness-checks-support-dropout-contagion-findings.md) — related
- [Propensity score matching produced baseline-equivalent treatment and comparison groups on all measured variables](psm-baseline-equivalence-mtss-study.md) — related
- [Post-COVID 15–17-year-old girls in India had 1.5–1.6% lower reading ability than matched pre-COVID girls](post-covid-girls-literacy-loss-india.md) — related
- [Inverse-probability weights for attrition, non-consent, and non-response improved validity only to the extent the missing-data assumptions held](attrition-nonresponse-weights-validity.md) — related
- [The main associations are not driven by children with high problem scores, by IQ adjustment, or by attrition selection bias](sensitivity-analyses-robust-associations.md) — related
