---
type: claim
title: LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions
description: LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions
id: llm-representational-sensitivity-equivalent-math-forms
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
---

# LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Aggregated across 5 LLMs, accuracy differs across story, symbolic, and word-equation representations of the same problems under both direct and code-augmented interaction conditions. [→ Sagnik Nath 2026](#sagnik-nath-2026)

## Evidence

### Sagnik Nath 2026

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)

`q2 · i?` · `causal · r2`

Evaluation of 5 LLMs on a curated dataset of mathematically equivalent problems, aggregated accuracy per representation shown in Fig. 1. The article reports that "performance varies across representations" under deterministic decoding, in both interaction conditions.

> "Despite deterministic decoding and identical underlying mathematical structure, performance varies across representations as seen in Fig. 1. This effect is present in both interaction conditions showing that representational sensitivity is not an artifact of sampling variability."

## Discussion


## Related Claims
- [Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations](executable-reasoning-failure-redistribution-layers.md) — related
- [Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes](interaction-condition-chi-square-representation-differences.md) — related
- [Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance](representation-gaps-model-specific-code-amplification.md) — a narrower finding that bears on this claim
- [Multiple representations improve learning](multiple-representations-improve-learning.md) — related
- [The Multimodal Interference Effect: mapping visual representations to physical concepts degrades LLM performance even on non-visual problem aspects](multimodal-interference-effect-llms.md) — related
