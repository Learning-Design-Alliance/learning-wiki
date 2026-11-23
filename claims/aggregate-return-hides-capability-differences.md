---
type: claim
title: "Aggregate return can be inconclusive between curriculum variants while capability profiles separate completely: base15 and longStack returns do not differ detectably, yet base15 exceeds longStack on deep-skill success rates"
description: "Aggregate return can be inconclusive between curriculum variants while capability profiles separate completely: base15 and longStack returns do not differ detectably, yet base15 exceeds longStack on deep-skill success..."
id: aggregate-return-hides-capability-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: zhu-2026
    resource: "https://doi.org/10.48550/arXiv.2610.15328"
    title: "Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)"
    author: Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zhu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2610.15328"
    title: "Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)"
    author: Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Aggregate return can be inconclusive between curriculum variants while capability profiles separate completely: base15 and longStack returns do not differ detectably, yet base15 exceeds longStack on deep-skill success rates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The base15-minus-longStack aggregate return difference is inconclusive under both the last-ten-checkpoints and checkpoint-15300 readings, with Welch intervals including zero. [→ Zhu 2026](#zhu-2026)
`q2 i?` Over the last ten checkpoints, every base15 run has a higher success rate than every longStack run on each of the four reported deep-skill outcomes, a complete three-versus-three separation. [→ Zhu 2026 (2)](#zhu-2026-2)

## Evidence

### Zhu 2026

Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)

`q2 · i?` · `causal · r2`

Welch comparison of three base15 versus three longStack 14B-teacher diagnostic runs under two readings of the same evaluation summaries (Table 4); the article states the aggregate comparison is inconclusive under either reading.

> "The base15-minus-longStack difference is−0.084362, with standard error0.883950, Welch degrees of freedom 3.2982, and 95% interval[−2.75893, 2.59020]; at checkpoint 15300 it is−0.079, with 95% interval[−3.77, 3.61]."

### Zhu 2026 (2)

Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)

`q2 · i?` · `causal · r2`

Capability profiles (Table 5) show, for example, defeat_gnome_warrior at 15.12±3.64 for base15 versus 1.55±2.59 for longStack in the tail window; at checkpoint 15300 one cross-arm pair does not follow the ordering for mine entry.

> "By contrast, over the last ten checkpoints every base15 run has a higher success rate than every longStack run on each of the four reported deep-skill outcomes; at checkpoint 15300 this complete separation persists for warrior, archer, and bat, while one"

## Discussion


## Related Claims
- [Within General Capability, model spread concentrates in competition mathematics (AIME), which dominates the aggregate score](aime-dominates-general-capability-spread.md) — related
- [A rule-based non-LLM curriculum (AHC) achieves higher native-task return than fresh native PPO-GTrXL at matched PPO rollout budgets in Craftax-Full, with all 43 actions unmasked](ahc-beats-native-ppo-craftax.md) — related
- [In an LLM-generated curriculum for Craftax, prerequisite mastery rules leave 27 downstream achievement targets ineligible for direct scheduling when mine entry tops out below the 0.30 threshold](prerequisite-rules-lock-downstream-targets.md) — related
