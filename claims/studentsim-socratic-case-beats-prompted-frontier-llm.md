---
type: claim
title: A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying
description: A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying
id: studentsim-socratic-case-beats-prompted-frontier-llm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: ke-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.01591"
    title: "Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591 [doi:10.48550/arxiv.2609.01591](https://doi.org/10.48550/arxiv.2609.01591)"
    author: Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On a held-out Socratic chess case where the guidance never names the destination square, the trained 4B simulator outputs the engine best move while prompted GPT-5.4 outputs a different wrong move. [→ Ke Yang 2026](#ke-yang-2026)

## Evidence

### Ke Yang 2026

Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591 [doi:10.48550/arxiv.2609.01591](https://doi.org/10.48550/arxiv.2609.01591)

`q2 · i?` · `causal · r2`

Single held-out case study in the guidance responsiveness results: the Socratic prompt never names the destination square, the player's actual move was a blunder, and the per-player simulator "outputs the engine best move f8b4" while GPT-5.4 answers a different wrong square. This is a qualitative case, not an aggregate statistic.

> "That a 4B trained simulator solves the Socratic case where
prompted access to a much larger closed-source model fails is direct evidence that the multi-turn training stage adds a
guidance-following capability, not merely a hint-copying shortcut on the easy modes where the prompt already contains
the answer."

## Discussion


## Related Claims
- [Across chess, L2 writing, and math, trained StudentSim simulators outperform every reference baseline on behavioral fidelity (F)](studentsim-outperforms-baselines-behavioral-fidelity.md) — related
- [Across all three domains, trained StudentSim simulators outperform every baseline on guidance responsiveness (R), with the largest gap on open-ended guidance modes](studentsim-outperforms-baselines-guidance-responsiveness.md) — a broader claim this one bears on
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [Using a trained StudentSim as the reward for chess tutor RL yields a tutor that expert human raters score best on accuracy, guidance quality, and personalization among the rewards studied](studentsim-reward-yields-best-rated-chess-tutor.md) — related
- [Prompt-literacy guidance was associated with higher transcript-coded rule-following compliance than unrestricted LLM access, mainly in process-over-answer and stepwise-hint behaviors](guided-llm-training-raises-rule-following-compliance.md) — related
