---
type: claim
title: "Email nudges referencing personalized data about a teacher's own students outperform nudges without personalized data, boosting math progress by 2.26%"
description: "Email nudges referencing personalized data about a teacher's own students outperform nudges without personalized data, boosting math progress by 2.26%"
id: personalized-data-emails-outperform
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: duckworth-2025
    resource: "https://doi.org/10.1073/pnas.2418616122"
    title: "Duckworth, A. L., Ko, A., Milkman, K. L., et al. (2025). A national megastudy shows that email nudges to elementary school teachers boost student math achievement, particularly when personalized. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2418616122"
    author: Duckworth, A. L., Ko, A., Milkman, K. L., et al
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: duckworth-2025-2
    resource: "https://doi.org/10.1073/pnas.2418616122"
    title: "Duckworth, A. L., Ko, A., Milkman, K. L., et al. (2025). A national megastudy shows that email nudges to elementary school teachers boost student math achievement, particularly when personalized. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2418616122"
    author: Duckworth, A. L., Ko, A., Milkman, K. L., et al
    q: 2
    i: "?"
    kind: causal
    rigour: 3
---

# Email nudges referencing personalized data about a teacher's own students outperform nudges without personalized data, boosting math progress by 2.26%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2`–`r3` · `q2`–`q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Interventions referencing personalized data led students to complete 0.04 more lessons (2.26% increase; d = 0.02, P = 0.001) than interventions that did not reference personalized data. [→ Duckworth 2025](#duckworth-2025)
`q2 i?` The only objectively coded attribute significantly associated with a condition's effect was whether emails referenced personalized data [r(13) = 0.70, P = 0.004], and perceived specificity was the only subjective attribute significantly associated with effects [r(13) = 0.55, P = 0.03]. [→ Duckworth 2025 (2)](#duckworth-2025-2)

## Evidence

### Duckworth 2025

Duckworth, A. L., Ko, A., Milkman, K. L., et al. (2025). A national megastudy shows that email nudges to elementary school teachers boost student math achievement, particularly when personalized. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2418616122

`q3 · i?` · `causal · r2`

Exploratory (not preregistered) Model 3 in Table 2, a weighted OLS regression comparing interventions whose emails referenced personalized data (directly or via dashboard hyperlinks) against conditions without personalized data, among 140,461 randomized teachers. The article reports a "2.26% increase; d = 0.02, P = 0.001".

> "interventions that referenced personalized data led students to complete 0.04 more lessons (2.26% increase; d = 0.02, P = 0.001) during the 4-wk intervention period than interventions that did not"

### Duckworth 2025 (2)

Duckworth, A. L., Ko, A., Milkman, K. L., et al. (2025). A national megastudy shows that email nudges to elementary school teachers boost student math achievement, particularly when personalized. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2418616122

`q2 · i?` · `causal · r3`

Preregistered exploratory attribute analysis correlating 15 condition effects with 21 message attributes coded by trained raters (100% agreement) and 8 dimensions rated by 1,752 Prolific raters. The article reports r(13) = 0.70, P = 0.004 for personalized data and r(13) = 0.55, P = 0.03 for perceived specificity.

> "The only objectively coded attribute that showed a statistically significant association with a condition’s regression-estimated effect was whether emails referenced personalized data specific to a teacher’s students"

## Discussion


## Related Claims
- [Weekly behaviorally informed email nudges to elementary school teachers slightly improve students' math progress (1.89% increase) over a 4-week intervention](email-nudges-teachers-boost-math-progress.md) — related
- [Intervention effects on student math progress persisted without fadeout through the 8-week post-intervention period](nudge-effects-persist-8-weeks.md) — related
- [Intervention effects were larger for teachers with paid (vs. free) Zearn Math accounts, including a larger personalized-data effect and larger social-comparison gains](paid-account-moderator-nudge-effects.md) — related
- [Email nudges did not significantly increase teacher engagement (dashboard logins), though student engagement rose similarly to achievement](teacher-login-engagement-null.md) — related
- [The most effective intervention, Nudging Weekly Logins, increased students' math progress by 5.06% (3.30% after winner's-curse adjustment) and was the only intervention significant after multiple-comparison correction](weekly-login-nudge-best-intervention.md) — related
