---
type: claim
title: LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction
description: LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction
id: llm-judge-correlates-human-experts-medgame
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: qian-wu-2026
    resource: "https://arxiv.org/abs/2607.21570"
    title: "Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570"
    author: Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Average correlation between LLM judge and human ratings was r = 0.81 for Medical Narrative Generation and r = 0.61 for Story Direction. [→ Qian Wu 2026](#qian-wu-2026)

## Evidence

### Qian Wu 2026

Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570

`q2 · i3` · `design · r2`

Human validation of the LLM-as-a-Judge protocol: three medical Ph.D. holders rated 50 Medical Narrative Generation cases and two game developers rated 50 Story Direction cases using the same rubrics as GPT-5.2, blinded to model identities. Correlations r = 0.81 and r = 0.61.

> "LLM scores correlate with human judgments, with strong agreement for Medical Narrative Generation (avg.r= 0.81 ) and moderate agreement for Story Direction (avg.r= 0.61)."

## Discussion


## Related Claims
- [Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics](commercial-models-outperform-open-source-medgame-baseline.md) — related
- [Expert-in-the-loop revision substantially improves medical accuracy and educational quality of generated storylines](expert-revision-improves-generated-medical-storylines.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — a narrower finding that bears on this claim
- [A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)](gemini-autorater-creativity-real-students.md) — related
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
