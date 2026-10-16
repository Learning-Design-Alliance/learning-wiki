---
type: claim
title: Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes
description: Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes
id: interaction-condition-chi-square-representation-differences
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
    i: 0
    kind: causal
    rigour: 2
  - id: sagnik-nath-2026-2
    resource: "https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
    q: 2
    i: 0
    kind: causal
    rigour: 2
---

# Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i0` negligible

## Subclaims
`q2 i0` After Bonferroni correction, baseline versus code-augmented differences were significant for story problems (χ² = 13.14, p = 0.00029) and symbolic problems (χ² = 8.44, p = 0.0037) but not word-equation problems (χ² = 2.63, p = 0.105), with small Cramér's V effect sizes (Vstory = 0.073, Vsymbolic = 0.058, Vwordeq = 0.032). [→ Sagnik Nath 2026](#sagnik-nath-2026)
`q2 i0` Cramér's V effect sizes for the interaction-condition differences were small across all three shared representations, indicating modest practical shifts in accuracy. [→ Sagnik Nath 2026 (2)](#sagnik-nath-2026-2)

## Evidence

### Sagnik Nath 2026

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)

`q2 · i0` · `causal · r2`

Representation-specific chi-square tests comparing baseline and code-augmented performance on shared representations, with Bonferroni correction (α = 0.05/3 ≈ 0.0167). The article reports differences "statistically significant for story problems" and symbolic, but not word-equation.

> "differences between interaction conditions were statistically significant for story problems ( χ² = 13.14, p = 0.00029) and symbolic problems (χ² = 8.44, p = 0.0037), but not for word-equation problems (χ² = 2.63, p = 0.105)."

### Sagnik Nath 2026 (2)

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv

`q2 · i0` · `causal · r2`

Same analysis: Cramér's V effect sizes were "small across all representations", indicating statistically detectable differences correspond to "modest practical shifts in accuracy".

> "However, effect sizes measured by Cramér's V (φ for 2×2 tables [27]) were small across all representations of story, symbolic, and word-equation (Vstory = 0.073, Vsymbolic = 0.058, Vwordeq = 0.032), indicating that even statistically detectable differences correspond to modest practical shifts in accuracy."

## Discussion


## Related Claims
- [LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions](llm-representational-sensitivity-equivalent-math-forms.md) — related
- [Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance](representation-gaps-model-specific-code-amplification.md) — related
