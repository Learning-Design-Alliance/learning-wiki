---
type: claim
title: Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics
description: Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics
id: commercial-models-outperform-open-source-medgame-baseline
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: qian-wu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.21570"
    title: "Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570 [doi:10.48550/arxiv.2607.21570](https://doi.org/10.48550/arxiv.2607.21570)"
    author: Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Prompted open-source models lag commercial frontier models across structure and content metrics on Medical Narrative Generation and Story Direction. [→ Qian Wu 2026](#qian-wu-2026)

## Evidence

### Qian Wu 2026

Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570 [doi:10.48550/arxiv.2607.21570](https://doi.org/10.48550/arxiv.2607.21570)

`q2 · i?` · `design · r2`

RQ1 benchmark evaluation of prompted baselines (2-shot for narrative generation, zero-shot for story direction). Claude-Sonnet-4.5 and Gemini-3-Pro reached 99.5% and 100.0% Strict validation; open-source Story Direction Sample-wise validation reached only 56.50–80.30% versus over 99% for commercial models.

> "Open-source models lag across both structure and content metrics: Qwen3-32B reaches only 79.4% Strict validation, Gemma-3-27B and MedGemma-27B remain below 60%, and their medical accuracy scores are consistently lower than commercial frontier models."

## Discussion


## Related Claims
- [Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models](fine-tuning-improves-open-source-llms-medgame-bench.md) — related
- [LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction](llm-judge-correlates-human-experts-medgame.md) — related
- [In a pilot with eight medical students, multimodal MedGame was perceived as more engaging and useful than text-only MedGame and original case material](multimodal-medgame-higher-perceived-engagement-pilot.md) — related
- [Related-case overlap between MedGame Bench train and test splits shows no significant performance difference](no-related-case-overlap-inflation-medgame-bench.md) — related
- [Supervised fine-tuning was less effective than direct prompting of SOTA LLMs for generating deep-level feedback, a task with non-deterministic output](sft-less-effective-than-prompting-for-feedback-generation.md) — related
