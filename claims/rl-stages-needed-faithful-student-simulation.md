---
type: claim
title: "Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation"
description: "Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation"
id: rl-stages-needed-faithful-student-simulation
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

# Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Removing both DPO for the simulator and GRPO for the profile generator decreases Acts from 0.605 to 0.589, Corr. from 0.466 to 0.436, and Errors from 0.150 to 0.115. [→ Zhangqi Duan 2026](#zhangqi-duan-2026)
`q2 i?` History SFT, which removes all three components of the method, performs poorly, and prompting-only use of the profile performs worst. [→ Zhangqi Duan 2026](#zhangqi-duan-2026)

## Evidence

### Zhangqi Duan 2026

Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051

`q2 · i?` · `causal · r2`

Ablation study on one data split (Table 2) varying training stages and profile inputs. The article concludes "SFT alone is not sufficient for faithful student simulation" and that the two optimization stages are complementary.

> "Removing both DPO for dialogue simulator training and GRPO for profile generator training leads to the largest drop in performance, decreasing Acts from 0.605 to 0.589, Corr. from 0.466 to 0.436, and Errors from 0.150 to 0.115."

## Discussion


## Related Claims
- [GRPO training shifts profiles from broad summaries toward diagnostic, behaviorally grounded representations that better support simulation](grpo-refines-profiles-toward-diagnostic-representations.md) — related
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
- [ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors](profilerl-outperforms-student-simulation-baselines.md) — related
- [Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality](dpo-training-contributes-accuracy-and-pedagogical-tone.md) — related
