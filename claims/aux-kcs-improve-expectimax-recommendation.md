---
type: claim
title: Incorporating auxiliary KCs into the Expectimax algorithm improves recommendation performance in the simulated environment
description: Incorporating auxiliary KCs into the Expectimax algorithm improves recommendation performance in the simulated environment
id: aux-kcs-improve-expectimax-recommendation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yahya-badran-and-christine-preisach-2026
    resource: "https://doi.org/10.1007/978-3-032-39106-3_8"
    title: "Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)"
    author: Yahya Badran and Christine Preisach
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Incorporating auxiliary KCs into the Expectimax algorithm improves recommendation performance in the simulated environment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A dual-filtering Expectimax variant that plans over human-defined and learned auxiliary KC sets and intersects the associated exercises shows improved performance over the base Expectimax algorithm. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)

`q2 · i?` · `design · r2`

Simulation evaluation on the ASSISTments2009-trained simulator with 24 random students each receiving 140 exercises (Table 4). The Expectimax variant performs Expectimax planning independently over each KC set and intersects the exercises, which the article reports "can show improvements".

> "Moreover, incorporating auxiliary KCs into the Expectimax algorithm can show improvements as seen in Table 4."

## Discussion


## Related Claims
- [Adding pretrained auxiliary KCs to a PPO-based recommendation policy consistently improves simulated student learning outcomes](aux-kcs-improve-ppo-recommendation.md) — related
- [The quantization layer is important to SBRKT: removing it (dense variant) underperforms significantly, and auxiliary KCs from quantized variants transfer better](quantization-layer-ablation.md) — related
