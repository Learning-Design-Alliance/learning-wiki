---
type: claim
title: Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance
description: Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance
id: representation-gaps-model-specific-code-amplification
status: draft
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

# Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Per-model max-min representation gaps are nontrivial for all models, and some models (e.g., Meta Llama) exhibit increased representation gaps under executable reasoning. [→ Sagnik Nath 2026](#sagnik-nath-2026)

## Evidence

### Sagnik Nath 2026

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)

`q2 · i?` · `causal · r2`

Model-level decomposition of representation gaps (Fig. 2), computed as the difference between best and worst accuracy across story, symbolic, and word-equation variants. The article reports Meta Llama shows "increased representation gaps under executable reasoning".

> "Notably, some models (e.g., Meta Llama) exhibit increased representation gaps under executable reasoning, suggesting that code-based interaction can amplify representational specialization rather than uniformly stabilizing performance."

## Discussion


## Related Claims
- [LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions](llm-representational-sensitivity-equivalent-math-forms.md) — a broader claim this one bears on
- [Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations](executable-reasoning-failure-redistribution-layers.md) — related
- [Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes](interaction-condition-chi-square-representation-differences.md) — related
