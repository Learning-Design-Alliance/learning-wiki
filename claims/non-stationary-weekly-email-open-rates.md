---
type: claim
title: Weekly open-rate estimates hinted at non-stationary arm means, meaning the optimal subject line could change each week
description: Weekly open-rate estimates hinted at non-stationary arm means, meaning the optimal subject line could change each week
id: non-stationary-weekly-email-open-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: yanez-2022
    resource: "https://doi.org/10.48550/arXiv.2208.05090"
    title: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. [doi:10.48550/arXiv.2208.05090](https://doi.org/10.48550/arXiv.2208.05090)"
    author: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Weekly open-rate estimates hinted at non-stationary arm means, meaning the optimal subject line could change each week

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Sample estimates in Figure 1 hinted at non-stationary behaviour across weeks, so the optimal arm could change each week, while bandit allocations such as TS assume constant arm means. [→ Yanez 2022](#yanez-2022)

## Evidence

### Yanez 2022

Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. [doi:10.48550/arXiv.2208.05090](https://doi.org/10.48550/arXiv.2208.05090)

`q1 · i?` · `causal · r2`

Authors' interpretation of the deployment's weekly open-rate estimates plotted in Figure 1: sample estimates "hint at a non-stationary behaviour across weeks, meaning the optimal arm could change each week."

> "Furthermore, sample estimates in Figure 1 hint at a non-stationary behaviour across weeks, meaning the optimal arm could change each week."

## Discussion


## Related Claims
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](bandit-exploitation-without-significant-arm-difference.md) — related
- [No statistically significant difference exists among the three email subject-line arms' mean open rates under any of the three allocation policies](no-significant-difference-email-subject-line-arm-means.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — related
