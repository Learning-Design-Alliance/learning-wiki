---
type: claim
title: Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)
description: Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)
id: qwk-discretized-difficulty-agreement-0835
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When difficulty is discretized into the five-band VH/H/M/E/VE label scheme, the fine-tuned model's predicted labels agree with calibrated labels at QWK 0.835, above both baselines. [→ Christopher Ormerod and YoungKoung Kim 2026](#christopher-ormerod-and-youngkoung-kim-2026)

## Evidence

### Christopher Ormerod and YoungKoung Kim 2026

Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154 [doi:10.48550/arxiv.2608.10154](https://doi.org/10.48550/arxiv.2608.10154)

`q2 · i?` · `design · r2`

Results-section evaluation using the article's proposed agreement-under-discretization metric, motivated because descriptive difficulty labels are what is conveyed to educators; the QWK values for all three models are printed in the quoted sentence.

> "When difficulty is discretized into the five-band scheme of Table 4, the model reaches a QWK of 0.835 against the calibrated labels, whereas MetaMath has a QWK of 0.692 and MathBERT has a QWK of0.625."

## Discussion


## Related Claims
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](weak-discrimination-parameter-recovery.md) — related
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](simulated-respondents-recover-guessing-parameter-048.md) — related
- [Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction](soft-target-finetuning-beats-standard-loss-vocabulary-difficulty.md) — related
