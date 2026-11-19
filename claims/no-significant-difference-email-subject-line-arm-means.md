---
type: claim
title: "No statistically significant difference exists among the three email subject-line arms' mean open rates under any of the three allocation policies"
description: "No statistically significant difference exists among the three email subject-line arms' mean open rates under any of the three allocation policies"
id: no-significant-difference-email-subject-line-arm-means
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: yanez-2022
    resource: "https://doi.org/10.48550/arXiv.2208.05090"
    title: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. [doi:10.48550/arXiv.2208.05090](https://doi.org/10.48550/arXiv.2208.05090)"
    author: "Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# No statistically significant difference exists among the three email subject-line arms' mean open rates under any of the three allocation policies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Post-experiment Wald z-tests with a Bonferroni-corrected family-wise false positive rate of 0.05 found all pairwise arm comparisons within each policy had p-values above the adjusted threshold of 0.017, failing to reject the null hypothesis of equal means. [→ Yanez 2022](#yanez-2022)

## Evidence

### Yanez 2022

Yanez, F. J., Zavaleta-Bernuy, A., Han, Z., Liut, M., Rafferty, A., & Williams, J. J. (2022). Increasing Students’ Engagement to Reminder Emails Through Multi-Armed Bandits. [doi:10.48550/arXiv.2208.05090](https://doi.org/10.48550/arXiv.2208.05090)

`q2 · i?` · `causal · r2`

Post-experiment Wald z-tests compared arm means within each policy under a Bonferroni-corrected family-wise rate of 0.05; all p-values were "greater than the adjusted-threshold of 0.017, failing to reject the null hypothesis of all real means being equal."

> "Table 2 also shows the p-value for such tests, where we can see that all of them are greater than the adjusted-threshold of 0.017, failing to reject the null hypothesis of all real means being equal."

## Discussion


## Related Claims
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](bandit-exploitation-without-significant-arm-difference.md) — related
- [Four homework reminder email versions showed no statistically significant difference in click rate over three weeks](homework-email-versions-no-click-rate-difference.md) — related
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — a broader claim this one bears on
- [Weekly open-rate estimates hinted at non-stationary arm means, meaning the optimal subject line could change each week](non-stationary-weekly-email-open-rates.md) — related
