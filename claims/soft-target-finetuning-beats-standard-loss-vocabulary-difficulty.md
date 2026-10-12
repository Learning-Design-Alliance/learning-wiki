---
type: claim
title: Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction
description: Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction
id: soft-target-finetuning-beats-standard-loss-vocabulary-difficulty
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: adam-nohejl-2026
    resource: "https://arxiv.org/abs/2605.14257"
    title: "Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257"
    author: Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Ablation results show that fine-tuning with soft-target cross-entropy loss yields lower RMSE than standard cross-entropy loss with discretized scores for both LLMs and MLMs, and than a regression head with MSE loss for MLMs. [→ Adam Nohejl 2026](#adam-nohejl-2026)

## Evidence

### Adam Nohejl 2026

Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257

`q2 · i?` · `causal · r?`

Ablation analysis (Section 6.1, Tables 4 and 5) of the fine-tuned Ministral-3-14B LLM and mmBERT-base MLM used in the submissions, comparing the soft-target method against standard-loss and regression-head variants; the article reports a tangible performance drop for the standard loss ablations. The authors state the soft-target technique "is superior to common approaches for both LLMs and MLMs."

> "The standard loss ablation demonstrates that our technique of fine-tuning using cross-entropy loss with soft targets is superior to common approaches for both LLMs and MLMs."

## Discussion


## Related Claims
- [The team's open-track submissions with added features surpassed all other shared task submissions on all three languages, with RMSE near 0.7](open-track-submissions-surpassed-all-others.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)](qwk-discretized-difficulty-agreement-0835.md) — related
