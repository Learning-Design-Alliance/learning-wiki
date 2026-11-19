---
type: claim
title: "MathBERT outperforms the best prior methods on three mathematics-education NLP tasks by 1.18% to 22.01% across metrics"
description: "MathBERT outperforms the best prior methods on three mathematics-education NLP tasks by 1.18% to 22.01% across metrics"
id: mathbert-outperforms-prior-best-methods
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: jia-tracy-shen-2021
    resource: "https://doi.org/10.48550/arXiv.2106.07340"
    title: "Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee. (2021). MathBERT: A Pre-trained Language Model for General NLP Tasks in Mathematics Education. [doi:10.48550/arXiv.2106.07340](https://doi.org/10.48550/arXiv.2106.07340)"
    author: Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MathBERT outperforms the best prior methods on three mathematics-education NLP tasks by 1.18% to 22.01% across metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuned MathBERT-orig and MathBERT-custom beat the best prior methods on KC prediction, auto-grading, and knowledge tracing across all metrics. [→ Jia Tracy Shen 2021](#jia-tracy-shen-2021)

## Evidence

### Jia Tracy Shen 2021

Jia Tracy Shen, Michiharu Yamashita, Ethan Prihar, Neil Heffernan, Xintao Wu, Ben Graff, Dongwon Lee. (2021). MathBERT: A Pre-trained Language Model for General NLP Tasks in Mathematics Education. [doi:10.48550/arXiv.2106.07340](https://doi.org/10.48550/arXiv.2106.07340)

`q2 · i?` · `design · r2`

Evaluation section comparing fine-tuned MathBERT (five random seeds, t-tests) against prior best methods on three ASSISTments task datasets; the paper reports MathBERT-orig is "about 1.38% to 22.01% better" than prior best across all metrics and tasks. No effect sizes printed.

> "MathBERT-orig is about 1.38% to 22.01% better and MathBERT-custom is about 1.18% to 21.92% better than the best prior methods across all metrics and tasks."

## Discussion


## Related Claims
- [MathBERT outperforms BASE BERT by about 1.98% to 8.28% on the three tasks, with statistical significance](mathbert-outperforms-base-bert.md) — related
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)](qwk-discretized-difficulty-agreement-0835.md) — related
- [MathBERT+TAPT models outperform MathBERT alone on most metrics, significantly only for knowledge tracing](mathbert-plus-tapt-beats-mathbert.md) — related
