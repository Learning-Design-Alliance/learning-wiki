---
type: claim
title: In PERCS, prior-week activity moderated email effects, with the moderation sign switching between week one (better for active users) and week three (better for inactive users, potentially harmful for active users)
description: In PERCS, prior-week activity moderated email effects, with the moderation sign switching between week one (better for active users) and week three (better for inactive users, potentially harmful for active users)
id: percs-activity-moderation-sign-switch
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
---

# In PERCS, prior-week activity moderated email effects, with the moderation sign switching between week one (better for active users) and week three (better for inactive users, potentially harmful for active users)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In week one, emails of all types performed better for active users than inactive users for both US and Indian learners; in week three the moderation switched, favoring inactive users, more strongly for Indian learners. [→ Timothy NeCamp 2019](#timothy-necamp-2019)
`q2 i?` Week-three log odds ratios were positive for inactive users and negative for active users, suggesting emails helped bring back inactive users but potentially harmed active learners; differences were not significant, only suggestive. [→ Timothy NeCamp 2019 (2)](#timothy-necamp-2019-2)

## Evidence

### Timothy NeCamp 2019

Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)

`q2 · i?` · `causal · r2`

PERCS personalization analysis (Section 5.3.4, Figure 5): log odds ratios of returning the subsequent week by email type, split by prior-week activity (active = one or more clicks). No effect size printed.

> "In week one, for both US and Indian learners, reminder emails of all types performed better for active users than inactive users (higher log odds for blue than magenta, Fig- ure 5). In week three, the sign of the moderation switched, as emails performed better for inactive users compared to active users."

### Timothy NeCamp 2019 (2)

Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. [doi:10.1145/3303772.3303812](https://doi.org/10.1145/3303772.3303812)

`q2 · i?` · `causal · r2`

PERCS moderation result (Section 5.3.4). The authors note confidence intervals are mostly overlapping, so differences are "not signiﬁcant but only suggestive"; the harmful-to-active-learners reading is hedged as potential.

> "Also, the log odds ratios for inactive users were positive, while the log odds ratios for active users were negative, suggesting that emails were beneﬁcial for bringing back inactive users, but potentially harmful to active learners."

## Discussion


## Related Claims
- [In PERCS, email effects on return differed by country and week: positive for Indian learners in weeks 2–3 with no-problem emails as good or better, but non-significant for US learners except cultural problem emails in week 3](percs-timing-email-effects-country-week.md) — related
