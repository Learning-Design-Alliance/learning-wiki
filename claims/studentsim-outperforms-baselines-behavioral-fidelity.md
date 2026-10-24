---
type: claim
title: Across chess, L2 writing, and math, trained StudentSim simulators outperform every reference baseline on behavioral fidelity (F)
description: Across chess, L2 writing, and math, trained StudentSim simulators outperform every reference baseline on behavioral fidelity (F)
id: studentsim-outperforms-baselines-behavioral-fidelity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-17
recheck_by: 2029
sources:
  - id: ke-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.01591"
    title: "Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591 [doi:10.48550/arxiv.2609.01591](https://doi.org/10.48550/arxiv.2609.01591)"
    author: Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ke-yang-2026-2
    resource: "https://arxiv.org/abs/2609.01591"
    title: "Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591"
    author: Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Across chess, L2 writing, and math, trained StudentSim simulators outperform every reference baseline on behavioral fidelity (F)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-17 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the 30-player chess held-out set, StudentSim reaches per-player top-1 fidelity F=0.51, above Maia2 (0.45), GPT-5.4 (0.23), and GPT-4o (0.22). [→ Ke Yang 2026](#ke-yang-2026)
`q2 i?` The trained simulators outperform every reference baseline on F across all three domains (chess, L2, math). [→ Ke Yang 2026 (2)](#ke-yang-2026-2)

## Evidence

### Ke Yang 2026

Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591 [doi:10.48550/arxiv.2609.01591](https://doi.org/10.48550/arxiv.2609.01591)

`q2 · i?` · `design · r2`

Evaluation of per-student simulators on a held-out chess set of 30 real Lichess players, scoring top-1 move-prediction fidelity. The figure-reported result shows "STUDENTSIMreaches per-player top-1 fidelity F=0.51" versus Maia2, GPT-5.4, and GPT-4o; no effect size is printed.

> "On the full 30-player held-out set, STUDENTSIMreaches per-player top-1 fidelity
F=0.51vs. Maia2F= 0.45, GPT-5.4F= 0.23, and GPT-4oF= 0.22."

### Ke Yang 2026 (2)

Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591

`q2 · i?` · `design · r2`

Cross-domain comparison in the behavioral fidelity results section: "The trained simulators outperform every reference baseline onF across all three domains", covering chess, L2 English writing, and mathematics against LLM and state-tracking baselines scored on the same held-out records.

> "The trained simulators outperform every reference baseline onF across all three domains (Table 2)."

## Discussion


## Related Claims
- [Across all three domains, trained StudentSim simulators outperform every baseline on guidance responsiveness (R), with the largest gap on open-ended guidance modes](studentsim-outperforms-baselines-guidance-responsiveness.md) — related
- [A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying](studentsim-socratic-case-beats-prompted-frontier-llm.md) — related
- [Using a trained StudentSim as the reward for chess tutor RL yields a tutor that expert human raters score best on accuracy, guidance quality, and personalization among the rewards studied](studentsim-reward-yields-best-rated-chess-tutor.md) — related
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
