---
type: claim
title: The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative
description: The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative
id: aes-accuracy-cost-tradeoff-recipes
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

# The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Multi-step Ex was most accurate (MAE 0.85) at about $0.0011 per essay, while Single-step Ex offered moderate accuracy (MAE 1.0) at $0.0003 and Single-step NoEx was most economical at $0.0002 with MAE 1.45. [→ Olga Manakina 2026](#olga-manakina-2026)

## Evidence

### Olga Manakina 2026

Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814

`q2 · i?` · `causal · r1`

Cost analysis plotting MAE against average estimated API cost per grading attempt for the four recipes (Figure 5). The article reports the accuracy-cost tradeoff, with Single-step NoEx the most economical at $0.0002 (MAE 1.45) and Multi-step NoEx worst on both metrics (MAE 1.55 at $0.0004).

> "Multi-step Ex, while most accurate (MAE of 0.85), incurred a relatively high cost of approximately $0.0011 per essay. Single-step Ex offered a balanced alternative with moderate accuracy (MAE of 1.0) at a lower cost ($0.0003)."

## Discussion


## Related Claims
- [The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls](multi-step-examples-highest-aes-accuracy.md) — related
- [Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK](no-example-recipes-worse-mae.md) — related
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
