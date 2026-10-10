---
type: claim
title: "The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)"
description: "The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)"
id: drl-policy-favors-guided-examples-distribution
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

# The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` The DRL group's training problem-type distribution differed significantly from both Control and BKT, with 35% PS, 4% Buggy, and 60% Guided examples. [→ Tithi 2026](#tithi-2026)

## Evidence

### Tithi 2026

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Chi-square tests of training problem-type distributions across the three conditions in the N=113 study (RQ1). The DRL group's distribution "encountered significantly different distribution from bothControl" and BKT, whereas Control and BKT did not differ significantly (χ2(2) = 1.77, p= 1.00).

> "students inDRLgroup en- countered significantly different distribution from bothControl(χ2(2) = 131.2,p < .001), andBKT(χ 2(2) = 143.1,p < .001), with 35% PS, only 4% Buggy, and 60% Guided."

## Discussion


## Related Claims
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — related
- [BKT students completed posttest problems significantly faster than Control students, with DRL showing marginal advantages in time and solution optimality](bkt-faster-posttest-completion.md) — related
- [BKT scaffolding significantly benefits low prior knowledge students, who outperformed low prior knowledge controls](bkt-benefits-low-prior-knowledge-students.md) — related
- [DRL scaffolding significantly benefits high prior knowledge students while BKT does not, and condition-by-prior-knowledge interactions are not significant](drl-benefits-high-prior-knowledge-students.md) — related
- [No significant differences in posttest rule accuracy across scaffolding conditions](no-rule-accuracy-difference-across-conditions.md) — related
- [All training policies narrowed the prior-knowledge achievement gap from pretest to posttest, with BKT achieving the largest reduction (77.1%)](bkt-largest-achievement-gap-reduction.md) — related
