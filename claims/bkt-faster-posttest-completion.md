---
type: claim
title: BKT students completed posttest problems significantly faster than Control students, with DRL showing marginal advantages in time and solution optimality
description: BKT students completed posttest problems significantly faster than Control students, with DRL showing marginal advantages in time and solution optimality
id: bkt-faster-posttest-completion
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
  - id: tithi-2026-2
    resource: "https://arxiv.org/abs/2602.07308"
    title: "Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308"
    author: Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# BKT students completed posttest problems significantly faster than Control students, with DRL showing marginal advantages in time and solution optimality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` BKT students completed posttest problems significantly faster than Control students (10.8 vs 11.8 minutes, p= 0.02, A=.58). [→ Tithi 2026](#tithi-2026)
`q3 i?` DRL students showed marginally lower posttest completion time and marginally fewer steps (more optimal solutions) than Control (both p= 0.06). [→ Tithi 2026 (2)](#tithi-2026-2)

## Evidence

### Tithi 2026

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Posttest problem completion time comparison across conditions in the N=113 study; BKT mean 10.8 minutes versus Control 11.8 minutes with A=.58. DRL's time difference was marginal (p= 0.06, A=.56).

> "students inBKTcompleted posttest problems signifi- cantly faster than students inControl(Control(mean) = 11.8 minutes per prob- lem,BKT(mean) = 10.8 minutes,p= 0.02,A=.58, 95% CI [.53, .63])"

### Tithi 2026 (2)

Tithi, S.D., Alam, N., Yasir, T., Shi, Y., Tian, X., Chi, M., Barnes, T. (2026). Adaptive Scaffolding for Cognitive Engagement in an Intelligent Tutoring System. arXiv. https://arxiv.org/abs/2602.07308

`q3 · i?` · `causal · r2`

Posttest solution optimality (steps) comparison; shorter solutions with fewer steps are more optimal in this domain. The DRL advantage over Control was marginal (p= 0.06) rather than significant.

> "TheDRLgroup had marginally more optimal solutions with fewer steps than theControlgroup in posttest problems (Control(mean) = 8.5 steps,DRL(mean) = 7.7 steps,p= 0.06,A=.56, 95% CI [.51, .61])"

## Discussion


## Related Claims
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — related
- [Adaptive-condition students complete the posttest in significantly less time than Control students](adaptive-proactive-hints-less-posttest-time.md) — a broader claim this one bears on
- [Students receiving Adaptive proactive hints based on HelpNeed predictions achieve significantly higher posttest optimality than Control students](adaptive-proactive-hints-higher-posttest-optimality.md) — related
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](drl-policy-favors-guided-examples-distribution.md) — related
- [No significant differences in posttest rule accuracy across scaffolding conditions](no-rule-accuracy-difference-across-conditions.md) — related
- [Both hint conditions took more time-on-task than control, but ChatGPT and human tutor conditions did not differ in session time](hint-conditions-time-on-task.md) — related
