---
type: claim
title: A rule-based non-LLM curriculum (AHC) achieves higher native-task return than fresh native PPO-GTrXL at matched PPO rollout budgets in Craftax-Full, with all 43 actions unmasked
description: A rule-based non-LLM curriculum (AHC) achieves higher native-task return than fresh native PPO-GTrXL at matched PPO rollout budgets in Craftax-Full, with all 43 actions unmasked
id: ahc-beats-native-ppo-craftax
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
---

# A rule-based non-LLM curriculum (AHC) achieves higher native-task return than fresh native PPO-GTrXL at matched PPO rollout budgets in Craftax-Full, with all 43 actions unmasked

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` At the lower 0.9961472B budget, primary AHC reaches 38.69±2.26 versus 36.63±1.42 for fresh native PPO, though the primary cohort's interval at this budget includes zero. [→ Zhu 2026](#zhu-2026)

## Evidence

### Zhu 2026

Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)

`q2 · i?` · `causal · r2`

Same repeated-world protocol at the below-1B checkpoint (update 7600). The article notes that at update 7600 the primary-cohort interval includes zero, while at update 15300 both AHC intervals exclude zero.

> "At the same 0.9961472B rollout budget, mean return is38.69± 2.26for primary AHC,40 .38± 1.69for additional AHC, and36.63± 1.42for fresh native PPO. The AHC means are 2.06 and 3.76 points above fresh native PPO, respectively."

## Discussion


## Related Claims
- [In an LLM-generated curriculum for Craftax, prerequisite mastery rules leave 27 downstream achievement targets ineligible for direct scheduling when mine entry tops out below the 0.30 threshold](prerequisite-rules-lock-downstream-targets.md) — related
- [Aggregate return can be inconclusive between curriculum variants while capability profiles separate completely: base15 and longStack returns do not differ detectably, yet base15 exceeds longStack on deep-skill success rates](aggregate-return-hides-capability-differences.md) — related
