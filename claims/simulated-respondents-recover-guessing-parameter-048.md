---
type: claim
title: The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior
description: The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior
id: simulated-respondents-recover-guessing-parameter-048
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: christopher-ormerod-and-youngkoung-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2608.10154"
    title: "Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154 [doi:10.48550/arxiv.2608.10154](https://doi.org/10.48550/arxiv.2608.10154)"
    author: Christopher Ormerod and YoungKoung Kim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The fine-tuned model recovers the guessing parameter at Pearson 0.48 (Qwen3.5-9B; 0.45 for 4B), where MathBERT reaches 0.25 and MetaMath 0.28, which the authors read as evidence the model captures genuine response behavior rather than surface stimulus features. [→ Christopher Ormerod and YoungKoung Kim 2026](#christopher-ormerod-and-youngkoung-kim-2026)

## Evidence

### Christopher Ormerod and YoungKoung Kim 2026

Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154 [doi:10.48550/arxiv.2608.10154](https://doi.org/10.48550/arxiv.2608.10154)

`q2 · i?` · `design · r2`

Discussion-section interpretation of the Table 5 results: a model that merely reads the question cannot infer how often low-ability students are drawn to a distractor, whereas a model trained to imitate those students can. Table 5 prints baseline c correlations of 0.25 and 0.28.

> "Recovering the guessing parameter c at a correlation of 0.48, where the regression baselines are very low by comparison, is arguably the clearest evidence that the approach captures genuine response behavior rather than surface features of the stimulus"

## Discussion


## Related Claims
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)](qwk-discretized-difficulty-agreement-0835.md) — related
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](weak-discrimination-parameter-recovery.md) — related
- [Test item construction, including avoidance of cognate L1 equivalents, often affects KVL difficulty scores beyond the genuine difficulty of the words](test-item-construction-affects-kvl-difficulty-scores.md) — related
