---
type: claim
title: L2C outperformed both the Rule-based Fading and Minimally-invasive Assistance baselines on lap time and failure count
description: L2C outperformed both the Rule-based Fading and Minimally-invasive Assistance baselines on lap time and failure count
id: l2c-outperforms-rbf-mia-baselines
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: wei-wang-2026
    resource: "https://arxiv.org/abs/2606.25337"
    title: "Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337"
    author: Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam
    q: 3
    i: 2
    kind: causal
    rigour: 2
---

# L2C outperformed both the Rule-based Fading and Minimally-invasive Assistance baselines on lap time and failure count

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3` · `i2` medium

## Subclaims
`q3 i2` Between-group Welch tests with Holm correction showed L2C outperforming MIA and RBF on both lap time and failure count, with Hedges' g between 0.60 and 0.76. [→ Wei Wang 2026](#wei-wang-2026)

## Evidence

### Wei Wang 2026

Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337

`q3 · i2` · `causal · r2`

Welch two-sample t-tests with Holm correction across the three randomly assigned coach groups (N=33) in the drone-racing user study. All four contrasts favor L2C with Hedges' g = -0.63, -0.60, -0.76, and -0.67, described as "medium-to-large effect sizes between 0.60 and 0.76".

> "On lap time, L2C outperformed MIA (∆ =−21.7%, Hedges’g=−0.63) and RBF (∆ =−16.6%, g=−0.60); on failure count, L2C outperformed MIA (∆ =−2.41failures per lap,g=−0.76) and RBF (∆ =−1.52failures per lap,g=−0.67)"

## Discussion


## Related Claims
- [Baseline coaches produced weaker or absent learning gains: RBF improved only failure count, MIA neither outcome](baselines-weak-or-absent-skill-gains.md) — related
- [Learners rated the L2C coach higher than both baselines on safety, performance, agency, and satisfaction](l2c-higher-subjective-ratings.md) — related
- [L2C coaching significantly reduces learners' lap times and failure counts from pre- to post-coaching in FPV drone racing](l2c-within-subject-lap-time-failure-gains.md) — related
