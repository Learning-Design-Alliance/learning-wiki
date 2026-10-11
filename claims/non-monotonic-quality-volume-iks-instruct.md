---
type: claim
title: "Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality"
description: "Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality"
id: non-monotonic-quality-volume-iks-instruct
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: shwetha-singaravelu-2026
    resource: "https://arxiv.org/abs/2607.23322"
    title: "Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322"
    author: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Neither raw volume expansion nor aggressive curation improved model-level judge scores relative to the moderately sized v1.1 dataset. [→ Shwetha Singaravelu 2026](#shwetha-singaravelu-2026)

## Evidence

### Shwetha Singaravelu 2026

Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322

`q2 · i?` · `design · r3`

Version-level comparison in Section 5.3 (Table 6) of three LoRA models trained on successive IKS-Instruct versions, scored by the same five-judge panel. Median scores are 6.39 (v1.1), 6.33 (v1.7), and 6.12 (v2.1); no effect size is printed.

> "The moderately sized 13,882-pair v1.1 produced the best model (6.39); expanding to the 20,000-pair v1.7 slightly reduced quality (6.33), consistent with the noisy auto-generated Vedic-mathematics pairs added in that step; and aggressively curating down to the 7,130-pair v2.1 reduced quality further at the model level (6.12), even though curation improved several dataset-level quality metrics."

## Discussion


## Related Claims
- [IKS-Instruct fine-tuning is necessary for IKS pedagogical capability: a compact 7B fine-tune reaches a median judge score of 6.39, within 0.15 of a general-purpose reference, while the base model scores near zero on IKS-specific dimensions](iks-instruct-finetuning-necessary-for-iks-pedagogical-capability.md) — related
- [Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations](source-anchoring-reduces-hallucination-instruction-data.md) — related
