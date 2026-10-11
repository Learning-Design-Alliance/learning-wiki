---
type: claim
title: "Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other"
description: "Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other"
id: knowledge-behavior-profile-complementary-signals
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

# Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Removing the behavior sections lowers Corr. and Errors despite retaining the full knowledge profile, and removing the knowledge sections causes the largest drops on Corr. and Errors while also hurting Acts and Cos. Sim. [→ Zhangqi Duan 2026](#zhangqi-duan-2026)

## Evidence

### Zhangqi Duan 2026

Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051

`q2 · i?` · `causal · r2`

Profile-content ablation (Table 2) splitting the profile into knowledge sections (knowledge state, acquisition, misconceptions) and behavior sections (dialogue acts, linguistic style). The article reports these "cross-metric drops show that knowledge and behavior provide complementary signals".

> "Removing the behavior sections primarily hurts behavior-sensitive metrics, decreas- ing Acts, Cos. Sim., and ROUGE-L, but it also lowers Corr. and Errors despite retaining the full knowledge profile."

## Discussion


## Related Claims
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Question-answering and dialogue histories are complementary views of the same student, with signals transferring across metric categories](qa-dialogue-histories-complementary-views.md) — related
