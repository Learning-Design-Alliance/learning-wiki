---
type: claim
title: In an LLM-generated curriculum for Craftax, prerequisite mastery rules leave 27 downstream achievement targets ineligible for direct scheduling when mine entry tops out below the 0.30 threshold
description: In an LLM-generated curriculum for Craftax, prerequisite mastery rules leave 27 downstream achievement targets ineligible for direct scheduling when mine entry tops out below the 0.30 threshold
id: prerequisite-rules-lock-downstream-targets
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

# In an LLM-generated curriculum for Craftax, prerequisite mastery rules leave 27 downstream achievement targets ineligible for direct scheduling when mine entry tops out below the 0.30 threshold

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Altered-graph configurations (repairF, shufGraph) recover the four-skill boundary in all three runs under either tail-window or checkpoint-15300 readings. [→ Zhu 2026](#zhu-2026)

## Evidence

### Zhu 2026

Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. [doi:10.48550/arXiv.2610.15328](https://doi.org/10.48550/arXiv.2610.15328)

`q2 · i?` · `causal · r2`

Recovery counts over three training runs against the four-skill boundary (Table 2): repairF and shufGraph each recover 3/3 under both tail-window and checkpoint-15300 readings, while longStack recovers 0/3.

> "Altered-graph configurations recover the skill boundary in all runs under either reading."

## Discussion


## Related Claims
- [A rule-based non-LLM curriculum (AHC) achieves higher native-task return than fresh native PPO-GTrXL at matched PPO rollout budgets in Craftax-Full, with all 43 actions unmasked](ahc-beats-native-ppo-craftax.md) — related
- [Removing the scaffold gate's floor clause changes direct deep-floor practice access and recovers the skill boundary in all three Surgical runs](floor-clause-removal-restores-practice-access.md) — related
- [Aggregate return can be inconclusive between curriculum variants while capability profiles separate completely: base15 and longStack returns do not differ detectably, yet base15 exceeds longStack on deep-skill success rates](aggregate-return-hides-capability-differences.md) — related
