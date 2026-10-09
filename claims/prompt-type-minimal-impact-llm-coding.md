---
type: claim
title: Zero-shot prompt type has minimal impact on LLM-human coding concordance
description: Zero-shot prompt type has minimal impact on LLM-human coding concordance
id: prompt-type-minimal-impact-llm-coding
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
    i: 1
    kind: causal
    rigour: 1
---

# Zero-shot prompt type has minimal impact on LLM-human coding concordance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i1` small

## Subclaims
`q2 i1` Prompt type showed no overall main effect on LLM-human correlation (partial η² = .03), and no pairwise contrast was significant. [→ Keith 2026](#keith-2026)

## Evidence

### Keith 2026

Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

`q2 · i1` · `causal · r1`

In the four-factor ANOVA on Fisher Z-transformed correlations, prompt type (5 levels) showed only a small effect; the article reports "no overall main effect (partial η² = .03)" with no significant pairwise contrasts (largest |Δz| = 0.10, all ps > .077).

> "Prompt type showed no overall main effect (partial η² = .03)."

## Discussion


## Related Claims
- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](coding-dimension-listing-easier-than-correct-defining.md) — related
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — reports the opposite
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
