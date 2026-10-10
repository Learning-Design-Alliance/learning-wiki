---
type: claim
title: BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls
description: BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls
id: bkt-benefits-low-prior-knowledge-students
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: tithi-2026
    resource: "https://arxiv.org/abs/2602.07308"
    title: "Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308"
    author: Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Low-BKT students significantly outperformed Low-Control students on posttest scores (β= 9.4, p=.001), while Low-DRL showed only a marginal increase (p=.08). [→ Tithi 2026](#tithi-2026)

## Evidence

### Tithi 2026

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Mixed-effects regression on posttest problem scores with Condition and Prior Knowledge as fixed effects and problem ID as random intercept, using median-split prior-knowledge subgroups (Low-Control n=18, Low-BKT n=15, Low-DRL n=22) with Low-Control as reference (mean= 60.4).

> "Students in Low-BKT significantly outperformed Low- Control (β= 9.4,SE= 2.7,z= 3.4,p=.001), while students in Low-DRL demonstrated marginal increase (β= 4.8,SE= 2.8,z= 1.7,p=.08)."

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — a broader claim this one bears on
- [DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant](drl-benefits-high-prior-knowledge-students.md) — related
- [All training policies narrowed the prior-knowledge achievement gap from pretest to posttest, with BKT achieving the largest reduction (77.1%)](bkt-largest-achievement-gap-reduction.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
- [No significant differences in posttest rule accuracy across scaffolding conditions](no-rule-accuracy-difference-across-conditions.md) — reports the opposite
- [Critical thinking improvement differed by proficiency level: high-level students gained 18%, intermediate 12%, and low-level 8%, with asymmetric feedback adaptation](wise-agent-differential-proficiency-trajectories.md) — related
