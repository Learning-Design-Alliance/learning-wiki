---
type: claim
title: All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions
description: All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions
id: llm-scores-decline-with-cogtax-level
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across all models and variants, assigned score proportions decrease monotonically from L1 to L4, mirroring the human pattern of declining performance with cognitive complexity. [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432

`q2 · i?` · `causal · r2`

Per-taxonomy-level analysis of LLM assigned grades under both variants (Section 4.2.2, Figure 6). The article reports L1 questions receive the highest proportions and L4 the lowest for every model, with GPT V2 (50.80%) and Gemini V2 (50.64%) highest at L4.

> "A consistent pattern emerges across all four models: the proportion of the available mark assignedtoquestionsdecreasesmonotonicallyascognitivecomplexityincreases."

## Discussion


## Related Claims
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
