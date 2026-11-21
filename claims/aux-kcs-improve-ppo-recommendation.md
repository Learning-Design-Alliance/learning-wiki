---
type: claim
title: Adding pretrained auxiliary KCs to a PPO-based recommendation policy consistently improves simulated student learning outcomes
description: Adding pretrained auxiliary KCs to a PPO-based recommendation policy consistently improves simulated student learning outcomes
id: aux-kcs-improve-ppo-recommendation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
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

# Adding pretrained auxiliary KCs to a PPO-based recommendation policy consistently improves simulated student learning outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a simulated student environment, adding pre-trained auxiliary KCs to the PPO-LSTM policy yields consistent improvement in normalized gain and mean reward over a 140-exercise plan. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)

`q2 · i?` · `design · r2`

Simulation study: 24 simulated students each receive 140 recommended exercises from a PPO-LSTM policy with and without auxiliary KCs, evaluated by average reward and normalized gain (Table 4). The article reports "consistent improvement" from adding the auxiliary KCs.

> "Our experiments shows consistent improvement of adding the pre-trained auxiliary KCs to the PPO based policy as seen in Table 4."

## Discussion


## Related Claims
- [Incorporating auxiliary KCs into the Expectimax algorithm improves recommendation performance in the simulated environment](aux-kcs-improve-expectimax-recommendation.md) — related
- [The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7](ppo-outperforms-random-baseline-reward.md) — related
- [The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns](pretrained-model-outperforms-baselines-all-scenarios.md) — related
