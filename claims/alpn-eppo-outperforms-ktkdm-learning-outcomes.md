---
type: claim
title: "The ALPN-EPPO system outperforms the KT-KDM baseline in maximizing students' learning outcomes, by 8.2% on average"
description: "The ALPN-EPPO system outperforms the KT-KDM baseline in maximizing students' learning outcomes, by 8.2% on average"
id: alpn-eppo-outperforms-ktkdm-learning-outcomes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: jyun-yi-chen-2023
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: jyun-yi-chen-2023-2
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The ALPN-EPPO system outperforms the KT-KDM baseline in maximizing students' learning outcomes, by 8.2% on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` During training, the ALPN-EPPO system was the most effective and robust in helping students achieve their learning goals, while the ALPN systems using general PPO or A2C and KT-KDM exhibited weaker performance. [→ Jyun-Yi Chen 2023](#jyun-yi-chen-2023)
`q1 i?` The authors report that ALPN outperformed KT-KDM by 8.2% on average in maximizing students' learning outcomes. [→ Jyun-Yi Chen 2023 (2)](#jyun-yi-chen-2023-2)

## Evidence

### Jyun-Yi Chen 2023

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

Simulation training comparing ALPN-EPPO, ALPN-PPO, ALPN-A2C and KT-KDM on learning outcome (APR) across the training process, plotted in Figure 3. The article reports ALPN-EPPO as "the most eﬀective and robust in helping students achieve their learning goals" while the other systems "exhibit weaker performance". No test statistic is printed.

> "The ﬁgure shows that the ALPN-EPPO system is the most eﬀective and robust in helping students achieve their learning goals. In comparison, the ALPN systems using general PPO or A2C and KT-KDM exhibit weaker performance."

### Jyun-Yi Chen 2023 (2)

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

The authors' concluding summary of the same simulation comparison states the system "demonstrated signiﬁcant improv ements, outperforming the KT-KDM method by 8.2% on average"; this percentage difference is not a standardized effect size.

> "Our system demonstrated signiﬁcant improv ements, outperforming the KT-KDM method by 8.2% on average to maximize students’ learning outcomes."

## Discussion


## Related Claims
- [ALPN-EPPO enables students to achieve their learning goals with the fewest number of learning activities among the compared systems](alpn-eppo-fewest-learning-activities.md) — related
- [ALPN systems generate more diverse learning paths than KT-KDM, with ALPN-EPPO the most diverse (10.5% higher rate)](alpn-eppo-higher-learning-path-diversity.md) — related
- [ALPN-EPPO achieves the highest cumulative reward during training among the ALPN variants using EPPO, PPO and A2C](alpn-eppo-highest-cumulative-reward.md) — related
