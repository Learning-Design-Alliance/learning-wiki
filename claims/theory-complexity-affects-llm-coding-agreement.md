---
type: claim
title: LLMs align better with human coding on concise theories with discrete concepts than on more complex ones
description: LLMs align better with human coding on concise theories with discrete concepts than on more complex ones
id: theory-complexity-affects-llm-coding-agreement
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

# LLMs align better with human coding on concise theories with discrete concepts than on more complex ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Correlations varied largely across the four criminological theories (partial η² = .39), with the largest contrast between Theory A Paper 3 (social control theory) and Theory A Paper 6. [→ Keith 2026](#keith-2026)
`q2 i?` Theory A Paper 3 (social control theory) yielded the lowest error rate of the four paper conditions. [→ Keith 2026 (2)](#keith-2026-2)

## Evidence

### Keith 2026

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i3` · `causal · r1`

In the correlation ANOVA, theory had a large effect (partial η² = .39); the printed contrast shows "The largest contrast was Theory A Paper 3 versus Theory A Paper 6" at Δz = 0.37, p < .001.

> "The largest contrast was Theory A Paper 3 versus Theory A Paper 6  (Δz = 0.37, p < .001). All remaining differences were significant (ps < .006)."

### Keith 2026 (2)

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i?` · `design · r2`

The binomial error model's estimated marginal means show "Theory A Paper 3 yielded the lowest error rate"; all pairwise differences were highly significant except Theory B Paper 6 vs Theory A Paper 6 (p = .156).

> "Theory A Paper 3 yielded the lowest error rate (logit = -2.21, SE = 0.07, p̂  =.10), less than Theory B Paper 6 (-1.46, 0.07, .19), Theory A Paper 6 (-1.39, 0.07, .20), and Theory B Paper 3 (-1.01, 0.07, .27)."

## Discussion


## Related Claims
- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](coding-dimension-listing-easier-than-correct-defining.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [AI-teacher diagnostic agreement was higher in the Diagnostic Review class and varied by issue type, with local language issues best diagnosed](ai-teacher-agreement-issue-type-variation.md) — related
