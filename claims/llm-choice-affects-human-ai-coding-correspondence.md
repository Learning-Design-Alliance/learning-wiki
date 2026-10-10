---
type: claim
title: LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst
description: LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst
id: llm-choice-affects-human-ai-coding-correspondence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: keith-2026
    resource: "https://github.com/imrryr/LLM-queries"
    title: "Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries"
    author: Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: keith-2026-2
    resource: "https://github.com/imrryr/LLM-queries"
    title: "Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries"
    author: Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Agreement between LLM and human coding of theory concepts differed significantly across the four models, with a large model effect (partial η² = .19). [→ Keith 2026](#keith-2026)
`q2 i?` GPT 4.1 Mini correlated significantly worse with human coding than all other models, standing alone in the lowest tier. [→ Keith 2026 (2)](#keith-2026-2)

## Evidence

### Keith 2026

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i3` · `causal · r1`

Four-factor ANOVA on Fisher Z-transformed LLM-to-human Pearson correlations across 240 design cells (4 LLMs × 5 prompt types × 3 dimensions × 4 theories), R² = .63. The model effect was "differed across models (partial η² = .19)".

> "Agreement with human scores differed across models (partial η² = .19)."

### Keith 2026 (2)

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i?` · `design · r2`

Tukey-adjusted pairwise contrasts of estimated marginal means in the correlation regression showed GPT 4.1 Mini "significantly worse than all other models", while GPT 4.1 Full and Claude Sonnet 4 did not differ (Δz = 0.02, p = .88).

> "GPT4.1 Mini was significantly worse than all other models (all Δzs > 0.10, ps <.007), standing alone in the lowest tier."

## Discussion


## Related Claims
- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](coding-dimension-listing-easier-than-correct-defining.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related
- [LLMs align better with human coding on concise theories with discrete concepts than on more complex ones](theory-complexity-affects-llm-coding-agreement.md) — related
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](gpt-4o-mini-lowest-act-balance-mae.md) — related
