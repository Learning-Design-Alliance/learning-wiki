---
type: claim
title: "In PERCS, email effects on return differed by country and week: positive for Indian learners in weeks 2–3 with no-problem emails as good or better, but non-significant for US learners except cultural problem emails in week 3"
description: "In PERCS, email effects on return differed by country and week: positive for Indian learners in weeks 2–3 with no-problem emails as good or better, but non-significant for US learners except cultural problem emails in..."
id: percs-timing-email-effects-country-week
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2019
sources:
  - id: timothy-necamp-2019
    resource: "https://doi.org/10.1145/3303772.3303812"
    title: "Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)"
    author: Timothy NeCamp, Josh Gardner, Christopher Brooks
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: timothy-necamp-2019-2
    resource: "https://doi.org/10.1145/3303772.3303812"
    title: "Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)"
    author: Timothy NeCamp, Josh Gardner, Christopher Brooks
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: timothy-necamp-2019-3
    resource: "https://doi.org/10.1145/3303772.3303812"
    title: "Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)"
    author: Timothy NeCamp, Josh Gardner, Christopher Brooks
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# In PERCS, email effects on return differed by country and week: positive for Indian learners in weeks 2–3 with no-problem emails as good or better, but non-significant for US learners except cultural problem emails in week 3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For Indian learners, email impacts in weeks 2 and 3 were largely positive, and no-problem emails (P0) were as good or better than global or cultural problem emails. [→ Timothy NeCamp 2019](#timothy-necamp-2019)
`q2 i?` For US learners, effects were non-significant across all emails except the cultural problem email (P2) in week 3, and emails did not impact propensity to return and may deter it. [→ Timothy NeCamp 2019 (2)](#timothy-necamp-2019-2)
`q2 i?` Emails were more effective for Indian learners than US learners despite significantly higher open rates for US learners (41.7%) than Indian learners (27.0%). [→ Timothy NeCamp 2019 (3)](#timothy-necamp-2019-3)

## Evidence

### Timothy NeCamp 2019

Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)

`q2 · i?` · `causal · r2`

PERCS timing analysis (Section 5.2.4): weekly logistic regressions with a binary outcome of clicking anything in the course, log odds ratios versus no email shown in Figure 4. No effect size printed; the comparison names P0 versus P1 and P2.

> "The results in Figure 4 show that the impact of emails on Indian learners in weeks 2 and 3 is largely positive, but the impact of receiving a no problem email (P0) is as good or better than receiving either global or cultural problem emails"

### Timothy NeCamp 2019 (2)

Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)

`q2 · i?` · `causal · r2`

PERCS timing analysis for US learners (Section 5.2.4, Figure 4). The article reports non-significant effects and small, often negative log odds ratios; no standardized effect size is printed.

> "For US learners, the effects are non-signiﬁcant across all emails except for the cultural problem email (P2) in week 3, and the log odds ratios are small and in many cases negative."

### Timothy NeCamp 2019 (3)

Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)

`q2 · i?` · `associational · r1`

PERCS secondary analysis of email open rates by country (Section 5.2.4). The article reports the printed open rates and a p-value for the difference in proportions; the authors suggest Indian learners may benefit more if open rates increased.

> "Emails were more effective for Indian learners compared to US learners, despite email open rates being signiﬁcantly larger for US learners (41.7% open rate) than Indian learn- ers (27.0% open rate, p-value -0.001 for difference in pro- portions)."

## Discussion


## Related Claims
- [In PERCS, prior-week activity moderated email effects, with the moderation sign switching between week one (better for active users) and week three (better for inactive users, potentially harmful for active users)](percs-activity-moderation-sign-switch.md) — related
- [In PERCS, differences in effects of email sequences on week-4 return were mostly not significant, though sequences starting with an email tended to be slightly more beneficial for US learners but not Indian learners](percs-sequence-effects-suggestive-us-week1-email-benefit.md) — related
