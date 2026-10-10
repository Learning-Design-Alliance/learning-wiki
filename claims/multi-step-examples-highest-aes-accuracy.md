---
type: claim
title: The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls
description: The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls
id: multi-step-examples-highest-aes-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: olga-manakina-2026
    resource: "https://arxiv.org/abs/2608.23814"
    title: "Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814"
    author: Olga Manakina, Igor Bogdanov
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Multi-step assessment with calibration examples achieved the lowest MAE (approximately 0.85) and highest QWK (approximately 0.55), and the MAB allocated over 70% of pulls to it. [→ Olga Manakina 2026](#olga-manakina-2026)

## Evidence

### Olga Manakina 2026

Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814

`q2 · i?` · `causal · r1`

Numerical results from the MAB experiment on 787 IELTS Task 2 essays scored with Gemini 2.5. The text reports "Multi-step Ex achieved the lowest error rate (approximately 0.85)"; QWK analysis showed approximately 0.55, and the bandit allocated approximately 350 pulls (over 70%) to this recipe.

> "Figure 3 displays the Mean Absolute Error (MAE) for each recipe, revealing that Multi-step Ex achieved the lowest error rate (approximately 0.85), followed by Single-step Ex (1.0)."

## Discussion


## Related Claims
- [The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative](aes-accuracy-cost-tradeoff-recipes.md) — related
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](mab-prompt-selection-reduces-aes-costs.md) — related
- [Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK](no-example-recipes-worse-mae.md) — related
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
