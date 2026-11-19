---
type: claim
title: "The EPPO agent adjusts exercise recommendations after a student answers multiple exercises incorrectly, better matching the student's current level"
description: "The EPPO agent adjusts exercise recommendations after a student answers multiple exercises incorrectly, better matching the student's current level"
id: eppo-adapts-after-incorrect-responses
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: jyun-yi-chen-2023
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The EPPO agent adjusts exercise recommendations after a student answers multiple exercises incorrectly, better matching the student's current level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` When students frequently answer incorrectly their knowledge state does not improve, and EPPO adjusts by recommending exercises that better match the student's current level. [→ Jyun-Yi Chen 2023](#jyun-yi-chen-2023)

## Evidence

### Jyun-Yi Chen 2023

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

Case analysis of three sampled students' knowledge-level trajectories under ALPN-EPPO (Figure 8), where not every student's level consistently increased; the article reports EPPO "adjusts after a student answers multiple exercises incorre ctly, recommending exercises that better match the student ’s current level".

> "When students frequently answer incorrectly, their knowle dge state naturally does not improve. However, our EPPO adjusts after a student answers multiple exercises incorre ctly, recommending exercises that better match the student ’s current level."

## Discussion


## Related Claims
- [ALPN-EPPO enables students to achieve their learning goals with the fewest number of learning activities among the compared systems](alpn-eppo-fewest-learning-activities.md) — related
- [ALPN systems generate more diverse learning paths than KT-KDM, with ALPN-EPPO the most diverse (10.5% higher rate)](alpn-eppo-higher-learning-path-diversity.md) — related
