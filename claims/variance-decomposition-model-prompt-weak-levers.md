---
type: claim
title: Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions
description: Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions
id: variance-decomposition-model-prompt-weak-levers
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.00883"
    title: "Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883"
    author: Michael Hardy, Yunsung Kim
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2`

## Subclaims
`q2 i?` A fully crossed Generalizability Theory decomposition shows LLM and PROMPT main effects explain little squared error (median shares 0.07 and 0.02), while higher-order interactions conditioning on classroom text dominate. [→ Michael Hardy 2026](#michael-hardy-2026)
`q2 i?` The dominant variance shares occur in interactions such as LLM×ITEM×OBS (0.19) and LLM×PROMPT×OBS (0.14), with a cell-specific remainder of 0.24. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883

`q2 · i?` · `associational · r3`

Fully crossed random-effects variance decomposition (Table 1) of squared misalignment error over OBS, ITEM, LLM, PROMPT facets. The abstract states model and/or prompting strategy "only reliably accounts for 15% of all measured misalignment error."

> "the main effects of LLM and PROMPTexplain only a small portion of the squared-error landscape (median shares 0.07 and 0.02)"

## Discussion


## Related Claims
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
- [Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing](prompt-dimension-interaction-error-rates.md) — related
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](coding-dimension-listing-easier-than-correct-defining.md) — related
