---
type: claim
title: Across all three domains, trained StudentSim simulators outperform every baseline on guidance responsiveness (R), with the largest gap on open-ended guidance modes
description: Across all three domains, trained StudentSim simulators outperform every baseline on guidance responsiveness (R), with the largest gap on open-ended guidance modes
id: studentsim-outperforms-baselines-guidance-responsiveness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Across all three domains, trained StudentSim simulators outperform every baseline on guidance responsiveness (R), with the largest gap on open-ended guidance modes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Across chess, L2, and math, the trained simulators outperform every baseline on aggregate R, and the gap is largest on open-ended guidance modes. [→ Ke Yang 2026](#ke-yang-2026)
`q2 i?` On the chess guidance-following test set, StudentSim reaches R=0.91 versus GPT-4o 0.77, GPT-5.4 0.72, and Maia2 0.27. [→ Ke Yang 2026 (2)](#ke-yang-2026-2)

## Evidence

### Ke Yang 2026

Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591 [doi:10.48550/arxiv.2609.01591](https://doi.org/10.48550/arxiv.2609.01591)

`q2 · i?` · `design · r2`

Guidance responsiveness results across the three domains: "the trained simulators outperform every baseline on aggregateR", with the authors noting the gap is largest where the tutor prompts reasoning through questions or principles rather than stating the correction.

> "Across all three domains, the trained simulators outperform every baseline on aggregateR (Table 3); the gap is largest
on the open-ended guidance modes, where the tutor prompts the student to reason toward the fix through questions or
principles."

### Ke Yang 2026 (2)

Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao. (2026). StudentSim: Training LLM-based Student Simulators. https://arxiv.org/abs/2609.01591

`q2 · i?` · `design · r2`

Chess guidance-following evaluation on held-out positions: "STUDENTSIMreachesR=0.91" versus GPT-4o, GPT-5.4, and Maia2; Maia2's score is a zero-guidance lower bound because it has no natural-language input pathway. No effect size is printed.

> "Across the full
guidance-following test set, STUDENTSIMreachesR=0.91, vs. GPT-4oR= 0.77, GPT-5.4R= 0.72, and Maia2R= 0.27."

## Discussion


## Related Claims
- [Across chess, L2 writing, and math, trained StudentSim simulators outperform every reference baseline on behavioral fidelity (F)](studentsim-outperforms-baselines-behavioral-fidelity.md) — related
- [Using a trained StudentSim as the reward for chess tutor RL yields a tutor that expert human raters score best on accuracy, guidance quality, and personalization among the rewards studied](studentsim-reward-yields-best-rated-chess-tutor.md) — related
- [A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying](studentsim-socratic-case-beats-prompted-frontier-llm.md) — a narrower finding that bears on this claim
- [ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors](profilerl-outperforms-student-simulation-baselines.md) — related
