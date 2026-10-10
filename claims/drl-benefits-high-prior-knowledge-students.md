---
type: claim
title: DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant
description: DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant
id: drl-benefits-high-prior-knowledge-students
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: tithi-2026
    resource: "https://arxiv.org/abs/2602.07308"
    title: "Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308"
    author: Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: tithi-2026-2
    resource: "https://arxiv.org/abs/2602.07308"
    title: "Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308"
    author: Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` High-DRL students achieved a significantly higher posttest score than High-Control students (β= 6.81, p= 0.008), while High-BKT did not (p=.16). [→ Tithi 2026](#tithi-2026)
`q3 i?` The condition-by-prior-knowledge interaction terms were not statistically significant, indicating the adaptive advantage did not differ significantly by prior knowledge level. [→ Tithi 2026 (2)](#tithi-2026-2)

## Evidence

### Tithi 2026

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Follow-up pairwise comparisons within the High prior knowledge subgroup of the N=113 mixed-effects regression (High-Control n=18, High-BKT n=20, High-DRL n=20), examining condition differences within the High subgroup.

> "studentsinHigh-DRLachievedasignificantlyhigherposttestscorethanstudents in High-Control (β= 6.81,SE= 2.6,z= 2.6,p= 0.008), while students in High-BKT did not (β= 4.09,SE= 2.9,z= 1.4,p=.16)."

### Tithi 2026 (2)

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Interaction terms from the same mixed-effects regression model on posttest problem scores testing whether the adaptive advantage over Control varied by prior knowledge level; neither interaction reached significance.

> "Theinteractiontermswerenotstatisticallysignificant(High-BKT:β=−5.3, SE= 3.9,z=−1.4,p=.18; High-DRL:β= 2.0,SE= 3.8,z= 0.6,p= 0.59), indicating that the advantage of adaptive conditions overControldid not differ significantly by prior knowledge level."

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — a broader claim this one bears on
- [BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls](bkt-benefits-low-prior-knowledge-students.md) — related
- [All training policies narrowed the prior-knowledge achievement gap from pretest to posttest, with BKT achieving the largest reduction (77.1%)](bkt-largest-achievement-gap-reduction.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
- [No significant differences in posttest rule accuracy across scaffolding conditions](no-rule-accuracy-difference-across-conditions.md) — reports the opposite
- [Critical thinking improvement differed by proficiency level: high-level students gained 18%, intermediate 12%, and low-level 8%, with asymmetric feedback adaptation](wise-agent-differential-proficiency-trajectories.md) — related
