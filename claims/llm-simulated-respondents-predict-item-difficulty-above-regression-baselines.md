---
type: claim
title: A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines
description: A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines
id: llm-simulated-respondents-predict-item-difficulty-above-regression-baselines
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: christopher-ormerod-and-youngkoung-kim-2026
    resource: "https://arxiv.org/abs/2608.10154"
    title: "Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154"
    author: Christopher Ormerod and YoungKoung Kim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On a held-out test set of mathematics items, the fine-tuned Qwen3.5-9B model attains a Pearson correlation of 0.85 on the difficulty parameter b, with RMSE 0.55 after a linear development-set correction, exceeding both regression baselines. [→ Christopher Ormerod and YoungKoung Kim 2026](#christopher-ormerod-and-youngkoung-kim-2026)

## Evidence

### Christopher Ormerod and YoungKoung Kim 2026

Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154

`q2 · i?` · `design · r2`

Numerical results on a held-out test set (Table 5) comparing the proposed simulated-respondent fine-tuned LLM against encoder-only regression baselines; the article reports "a relative improvement of roughly 15% over the stronger baseline, obtained with an RMSE of0.55".

> "The fine-tuned Qwen3.5-9B model attains a Pearson correlation of0.85 on the difficulty parameterb, exceeding both regression baselines—MathBERT (0.68) and MetaMath ( 0.75)—by a clear margin."

## Discussion


## Related Claims
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](weak-discrimination-parameter-recovery.md) — related
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](simulated-respondents-recover-guessing-parameter-048.md) — related
- [Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)](qwk-discretized-difficulty-agreement-0835.md) — related
