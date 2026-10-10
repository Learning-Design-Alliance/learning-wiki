---
type: claim
title: Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators
description: Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators
id: prompt-engineering-adaptation-transparency-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: yizhou-zhou-2026
    resource: "https://arxiv.org/abs/2605.08040"
    title: "Yizhou Zhou, Jiayin Li, and Zhi Zhang. (2026). ECNUClaw: A Learner-Profiled Intelligent Study Companion Framework for K-12 Personalized Education. arXiv preprint. https://arxiv.org/abs/2605.08040"
    author: Yizhou Zhou, Jiayin Li, and Zhi Zhang
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` Achieving adaptation through prompt injection rather than fine-tuning removes the need for GPU resources or training data and makes the adaptation logic inspectable, at the cost of instruction-following fidelity. [→ Yizhou Zhou 2026](#yizhou-zhou-2026)

## Evidence

### Yizhou Zhou 2026

Yizhou Zhou, Jiayin Li, and Zhi Zhang. (2026). ECNUClaw: A Learner-Profiled Intelligent Study Companion Framework for K-12 Personalized Education. arXiv preprint. https://arxiv.org/abs/2605.08040

`q1 · i?` · `design · r1`

Theoretical design argument from the paper's discussion section (§9.2), not an empirical test. The authors argue prompt-injection adaptation offers transparency and portability, with the stated trade-off that "the LLM may not always follow the injected instructions faithfully."

> "This means the system works with any OpenAI-compatible LLM without requiring GPU resources or training data. It also means the adaptation logic is transparent—educators can inspect the strategy block in the system prompt and understand what the companion is doing and why."

## Discussion


## Related Claims
- [Three LLMs fine-tuned on teacher-validated feedback reach reported training losses with qualitative teacher validation](aicofe-llm-finetuning-training-results.md) — related
- [Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05](clst-finetuning-compute-cost.md) — related
- [Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students](fine-tuning-improves-clst-auc.md) — related
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
