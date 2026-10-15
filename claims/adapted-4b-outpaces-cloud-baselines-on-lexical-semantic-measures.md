---
type: claim
title: The adapted 4B model outperforms zero-shot cloud baselines on lexical and semantic measures despite lower raw accuracy
description: The adapted 4B model outperforms zero-shot cloud baselines on lexical and semantic measures despite lower raw accuracy
id: adapted-4b-outpaces-cloud-baselines-on-lexical-semantic-measures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rashid-azraf-jahin-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00664"
    title: "Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)"
    author: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The adapted 4B model outperforms zero-shot cloud baselines on lexical and semantic measures despite lower raw accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Cloud baselines (GPT-4o-mini 69.5%, Gemini-2.5-FL 82.9% accuracy) score lower Token F1 and BERTScore than the adapted 4B model, which reaches 50.9% accuracy. [→ Rashid Azraf Jahin 2026](#rashid-azraf-jahin-2026)

## Evidence

### Rashid Azraf Jahin 2026

Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)

`q2 · i?` · `causal · r1`

Results on the held-out test set (Table III): cloud baselines are zero-shot, edge models evaluated with and without LoRA. The authors explain cloud models generate longer, more explanatory responses than the shorter NCTB-standard phrases the lexical and semantic metrics reward.

> "Cloud baselines have greater raw accuracy, 69.5 and 82.9 percent respectively but lower Token F1 and BERTScore than the adapted 4B model."

## Discussion


## Related Claims
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
