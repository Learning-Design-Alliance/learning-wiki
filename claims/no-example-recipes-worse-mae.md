---
type: claim
title: Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK
description: Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK
id: no-example-recipes-worse-mae
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

# Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Single-step NoEx showed MAE of approximately 1.45 and Multi-step NoEx the highest at 1.55, yet Multi-step NoEx performed second-best in QWK (around 0.35). [→ Olga Manakina 2026](#olga-manakina-2026)

## Evidence

### Olga Manakina 2026

Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814

`q2 · i?` · `causal · r1`

MAE analysis across the four grading recipes in the MAB experiment on IELTS Task 2 essays. The article reports the no-example recipes performed worse on MAE, while noting "Multi-step NoEx performed second-best in QWK (around 0.35), despite its poor MAE."

> "The approaches without examples performed substantially worse, with Single-step NoEx showing an MAE of approximately 1.45 and Multi-step NoEx demonstrating the highest error rate at 1.55."

## Discussion


## Related Claims
- [The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative](aes-accuracy-cost-tradeoff-recipes.md) — related
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](mab-prompt-selection-reduces-aes-costs.md) — related
- [The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls](multi-step-examples-highest-aes-accuracy.md) — related
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
