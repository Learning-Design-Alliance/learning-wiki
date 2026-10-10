---
type: claim
title: "L2C coaching significantly reduces learners' lap times and failure counts from pre- to post-coaching in FPV drone racing"
description: "L2C coaching significantly reduces learners' lap times and failure counts from pre- to post-coaching in FPV drone racing"
id: l2c-within-subject-lap-time-failure-gains
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
  - id: wei-wang-2026-2
    resource: "https://arxiv.org/abs/2606.25337"
    title: "Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337"
    author: Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# L2C coaching significantly reduces learners' lap times and failure counts from pre- to post-coaching in FPV drone racing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i2`–`i3`

## Subclaims
`q3 i2` After about 40 minutes of L2C coaching, learners' lap times dropped by 27.9% on average (dz = -1.08, p = 0.005). [→ Wei Wang 2026](#wei-wang-2026)
`q3 i3` L2C coaching reduced per-lap failure count by a mean of 3.52 failures (dz = -2.13, p < 0.001). [→ Wei Wang 2026 (2)](#wei-wang-2026-2)

## Evidence

### Wei Wang 2026

Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337

`q3 · i2` · `causal · r2`

Within-subject paired t-test in the N=33 user study, L2C group, comparing pre- and post-coaching unassisted test laps. The article reports "a mean reduction of 27.9%" with Cohen's dz = -1.08 (large) and p = 0.005.

> "a paired-samplest-test comparing pre- and post-coaching lap times yielded a mean reduction of 27.9% withp= 0.005and Cohen’sd z =−1.08(large)"

### Wei Wang 2026 (2)

Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337

`q3 · i3` · `causal · r2`

Paired t-test on per-lap failure count (collisions and timeouts) for the L2C group in the same user study, pre- versus post-coaching. The article reports "a mean reduction of 3.52 failures per lap" with Cohen's dz = -2.13 (very large), p < 0.001.

> "a paired t-test on per-lap failure count yielded a mean reduction of 3.52 failures per lap withp<0.001and Cohen’sd z =−2.13(very large)"

## Discussion


## Related Claims
- [Baseline coaches produced weaker or absent learning gains: RBF improved only failure count, MIA neither outcome](baselines-weak-or-absent-skill-gains.md) — related
- [Learners rated the L2C coach higher than both baselines on safety, performance, agency, and satisfaction](l2c-higher-subjective-ratings.md) — related
- [L2C outperformed both the Rule-based Fading and Minimally-invasive Assistance baselines on lap time and failure count](l2c-outperforms-rbf-mia-baselines.md) — related
- [The L2C coach adaptively modulates assistance by estimated learner skill and physical context, concentrating intervention around gates](l2c-adaptive-assistance-by-skill-and-context.md) — related
