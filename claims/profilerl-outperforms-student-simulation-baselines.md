---
type: claim
title: ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors
description: ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors
id: profilerl-outperforms-student-simulation-baselines
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: zhangqi-duan-2026
    resource: "https://arxiv.org/abs/2605.30051"
    title: "Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051"
    author: Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` ProfileRL improves Acts by 0.042, Corr. by 0.037, and Errors by 0.038 over History SFT, with statistically significant gains on these three metrics (p<0.05 under a paired t-test). [→ Zhangqi Duan 2026](#zhangqi-duan-2026)
`q2 i?` ProfileRL outperforms all baselines on every metric, and the gains hold with a smaller simulator (Llama-3.2-3B). [→ Zhangqi Duan 2026](#zhangqi-duan-2026)

## Evidence

### Zhangqi Duan 2026

Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051

`q2 · i?` · `causal · r2`

Quantitative comparison on 5-fold cross-validation over a real-world math platform dataset (1,775 dialogues, 66,705 QA records, 670 students), with a 80/10/10 split across students. ProfileRL reaches the best scores, e.g. Acts 0.644 vs History SFT 0.602, and the article reports "statistically significant gains on these three metrics".

> "Compared to History SFT, ProfileRL improves Acts by 0.042, Corr. by 0.037, and Errors by 0.038, with statistically significant gains on these three metrics (p<0.05under a pairedt-test)"

## Discussion


## Related Claims
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
