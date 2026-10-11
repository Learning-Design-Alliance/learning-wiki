---
type: claim
title: Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models
description: Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models
id: fine-tuning-improves-open-source-llms-medgame-bench
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: qian-wu-2026
    resource: "https://arxiv.org/abs/2607.21570"
    title: "Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570"
    author: Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Fine-tuning open-source models on MedGame Bench training trajectories raises structural validity to near-commercial levels and improves content metrics on both generation tracks. [→ Qian Wu 2026](#qian-wu-2026)

## Evidence

### Qian Wu 2026

Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570

`q2 · i?` · `design · r2`

Benchmark experiments on MedGame Bench (LoRA fine-tuning on Gemini-3-Pro reference trajectories, 4,000-case training split). The article reports Qwen3.5-27B∗ reaching "99.5% Strict validation" and Qwen3-32B∗ improving CSU from 5.41 to 8.50; Qwen3.5-27B∗ slightly surpassed Claude-Sonnet-4.5 on summed content indicators (59.83 vs. 59.08).

> "Qwen3.5-27B∗ reaches 99.5% Strict validation on Medical Narrative Generation, while Qwen3-32B∗ improves CSU from 5.41 to 8.50, suggesting better use of curated personas and clinical locations."

## Discussion


## Related Claims
- [Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics](commercial-models-outperform-open-source-medgame-baseline.md) — related
- [Related-case overlap between MedGame Bench train and test splits shows no significant performance difference](no-related-case-overlap-inflation-medgame-bench.md) — related
