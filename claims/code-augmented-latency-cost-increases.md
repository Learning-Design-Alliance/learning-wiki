---
type: claim
title: Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier
description: Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier
id: code-augmented-latency-cost-increases
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sagnik-nath-2026
    resource: "https://doi.org/10.1007/978-3-032-30860-3_11"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: sagnik-nath-2026-2
    resource: "https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` The code-augmented condition consistently increases both median latency and tail latency relative to the baseline condition. [→ Sagnik Nath 2026](#sagnik-nath-2026)
`q2 i?` Economic cost per correct answer typically increases under the code-augmented condition, though Gemini 2.5 Pro is a notable outlier with reduced per-success cost despite increased overall failure rates. [→ Sagnik Nath 2026 (2)](#sagnik-nath-2026-2)

## Evidence

### Sagnik Nath 2026

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)

`q2 · i?` · `causal · r2`

Latency analysis per model under both interaction conditions (Fig. 7), reporting median latency with one-sided p90 tails. The article reports the code-augmented condition "consistently increases both median latency and tail latency".

> "The code-augmented condition consistently increases both median latency and tail latency indicating not only slower responses but also greater variability in response time with respect to the baseline condition."

### Sagnik Nath 2026 (2)

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv

`q2 · i?` · `causal · r2`

Economic cost per correct answer per model under both conditions (Fig. 8). The article reports "Costs typically increase under the code-augmented condition", with Gemini 2.5 Pro a "notable outlier".

> "Costs typically increase under the code-augmented condition, reflecting the cumulative expense of failed executions, retries and longer responses. Gemini 2.5 Pro constitutes a notable outlier, suggesting that for models with strong latent reasoning but brittle interface compliance, executable constraints can reduce per-success cost despite increasing overall failure rates."

## Discussion


## Related Claims
- [Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations](executable-reasoning-failure-redistribution-layers.md) — related
- [Asynchronous concurrent execution bounds overall latency to approximately the slowest individual model's inference time](async-concurrency-latency-bounded-by-slowest-model.md) — related
- [Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance](representation-gaps-model-specific-code-amplification.md) — related
