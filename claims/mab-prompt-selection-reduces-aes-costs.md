---
type: claim
title: "A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%"
description: "A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%"
id: mab-prompt-selection-reduces-aes-costs
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

# A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` On IELTS Task 2 essays, the MAB framework achieved comparable QWK to grid search while reducing LLM calls by 78.4% and tokens by 72.8%. [→ Olga Manakina 2026](#olga-manakina-2026)

## Evidence

### Olga Manakina 2026

Olga Manakina, Igor Bogdanov. (2026). Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring. https://arxiv.org/abs/2608.23814

`q2 · i?` · `causal · r1`

Simulation-style experiment on the IELTS Task 2 subset using Google Gemini 2.5, comparing an epsilon-greedy MAB controller against exhaustive grid search. The article reports "MAB reduced total experimental costs by approximately 70%" ($0.4 vs $1.4) with comparable accuracy; Table 1 prints 78.4% call and 72.8% token reductions.

> "Grid Search had consumed approximately 9 million tokens compared to MAB's 1.8 million for similar coverage. This efficiency translated directly to cost savings, as shown in Figure 7, where MAB reduced total experimental costs by approximately 70% compared to Grid Search ($0.4 versus $1.4) while maintaining comparable accuracy outcomes."

## Discussion


## Related Claims
- [The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls](multi-step-examples-highest-aes-accuracy.md) — related
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
- [Grading recipes without calibration examples perform substantially worse on MAE, though multi-step without examples ranks second on QWK](no-example-recipes-worse-mae.md) — related
- [An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits](optimistic-prior-mitigates-mab-power-loss.md) — related
- [Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition](mab-fewer-students-in-worse-condition-long-horizon.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
