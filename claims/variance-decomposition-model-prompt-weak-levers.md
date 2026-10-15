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
    resource: "https://doi.org/10.48550/arxiv.2603.00883"
    title: "Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883 [doi:10.48550/arxiv.2603.00883](https://doi.org/10.48550/arxiv.2603.00883)"
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

Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883 [doi:10.48550/arxiv.2603.00883](https://doi.org/10.48550/arxiv.2603.00883)

`q2 · i?` · `associational · r3`

Fully crossed random-effects variance decomposition (Table 1) of squared misalignment error over OBS, ITEM, LLM, PROMPT facets. The abstract states model and/or prompting strategy "only reliably accounts for 15% of all measured misalignment error."

> "the main effects of LLM and PROMPTexplain only a small portion of the squared-error landscape (median shares 0.07 and 0.02)"

## Discussion


## Related Claims
- Zero-shot prompt type has minimal impact on LLM-human coding concordance — related
- Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing — related
- Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots — related
- LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness — related
- [In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment](raw-agreement-kappa-paradox-classroom-video.md) — related
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
- [Off-the-shelf LLMs are systematically misaligned with human item-difficulty judgments and struggle to simulate lower-proficiency states](off-the-shelf-llms-misaligned-human-difficulty-judgments.md) — related
