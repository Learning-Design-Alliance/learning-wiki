---
type: claim
title: LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness
description: LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness
id: coding-dimension-listing-easier-than-correct-defining
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
    kind: causal
    rigour: 2
---

# LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Coding dimension yielded distinct correlation levels with a large effect (partial η² = .39): listing surpassed defining, which exceeded correctly defining. [→ Keith 2026](#keith-2026)
`q2 i?` Error rates followed the same order: listing showed the lowest error rate and correctly defining the highest. [→ Keith 2026 (2)](#keith-2026-2)

## Evidence

### Keith 2026

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i3` · `causal · r1`

Pairwise contrasts on estimated marginal means from the correlation ANOVA (dimension partial η² = .39) show the ordering "Listing surpassed defining" and defining exceeded correctly defining, all p < .001.

> "Listing surpassed defining (Δz = 0.15, p < .001) and correctly defining (Δz = 0.33, p < .001); defining also exceeded correctly defining (Δz = 0.18, p < .001)."

### Keith 2026 (2)

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i?` · `causal · r2`

In the binomial mixed-effects error model (N = 8040 observations from 39 students), estimated marginal means show "Listing showed the lowest error rate" and correctly defining the highest, all Tukey-adjusted ps < .001.

> "Listing showed the lowest error rate (logit = -2.08, SE = 0.07, p̂  = .11), followed by defining (-1.48, 0.07, .19) and correctly defining (-0.99, 0.07, .27)."

## Discussion


## Related Claims
- [Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing](prompt-dimension-interaction-error-rates.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [LLMs align better with human coding on concise theories with discrete concepts than on more complex ones](theory-complexity-affects-llm-coding-agreement.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [LLM scoring performance is dimension-specific: Reasoning shows the strongest agreement and Terminology the weakest across all three strategies](dimension-specific-scoring-reasoning-strongest-terminology-weakest.md) — a narrower finding that bears on this claim
