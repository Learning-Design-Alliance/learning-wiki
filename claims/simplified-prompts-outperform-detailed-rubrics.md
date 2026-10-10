---
type: claim
title: Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study
description: Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study
id: simplified-prompts-outperform-detailed-rubrics
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

# Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` The Multi-Step with Examples recipe without explicit rubrics achieved MAE 0.862 and QWK 0.566, outperforming its rubric-enhanced counterpart (MAE 0.965, QWK 0.485) while consuming fewer tokens. [→ Olga Manakina 2026](#olga-manakina-2026)

## Evidence

### Olga Manakina 2026

Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814

`q2 · i?` · `causal · r1`

Ablation study comparing prompts with detailed IELTS Key Assessment Criteria descriptions against simplified prompts without them. The simplified version "outperform[ed] its rubric-enhanced counterpart" on both MAE and QWK with fewer tokens; the MAB allocated 70.8% of pulls to the simplified variant versus 66.4%.

> "The Multi-Step with Examples recipe without explicit rubrics achieved an MAE of 0.862 and QWK of 0.566, outperforming its rubric-enhanced counterpart (MAE 0.965, QWK 0.485) while consuming fewer tokens (7,402 vs. 7,862) and reducing costs."

## Discussion


## Related Claims
- [The four grading recipes exhibit an accuracy-cost tradeoff, with the most accurate recipe costing roughly five times the balanced alternative](aes-accuracy-cost-tradeoff-recipes.md) — related
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](mab-prompt-selection-reduces-aes-costs.md) — related
- [Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK](no-example-recipes-worse-mae.md) — related
- [The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls](multi-step-examples-highest-aes-accuracy.md) — related
- [Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign](rubric-structure-part-of-assessment-construct.md) — related
