---
type: claim
title: Dialogue-shuffling augmentation improves evaluator performance while downsampling reduces it
description: Dialogue-shuffling augmentation improves evaluator performance while downsampling reduces it
id: dialogue-shuffling-augmentation-improves-evaluator
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tahmid-al-hannan-2026
    resource: "https://doi.org/10.48550/arxiv.2607.10647"
    title: "Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647 [doi:10.48550/arxiv.2607.10647](https://doi.org/10.48550/arxiv.2607.10647)"
    author: Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Dialogue-shuffling augmentation improves evaluator performance while downsampling reduces it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` For the Mistake Identification task, dialogue shuffling improved lenient F1 from 82.04 to 84.04 and strict F1 from 59.00 to 62.44, whereas downsampling reduced accuracy. [→ Tahmid Al Hannan 2026](#tahmid-al-hannan-2026)

## Evidence

### Tahmid Al Hannan 2026

Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647 [doi:10.48550/arxiv.2607.10647](https://doi.org/10.48550/arxiv.2607.10647)

`q2 · i?` · `causal · r1`

Training-strategy comparison for Llama 3.1 8B on the Mistake Identification task, reported in Table 2 with lenient and strict F1 and accuracy. The article states "dialogue shuffling consistently im- proved performance, whereas downsampling re- duced accuracy"; Table 2 prints lenient F1 of 84.04 for shuffling versus 82.04 baseline.

> "Table 2 shows that dialogue shuffling consistently im- proved performance, whereas downsampling re- duced accuracy."

## Discussion


## Related Claims
- [Knowledge distillation from a frontier LLM substantially improves lightweight AI-tutor evaluation across all four pedagogical dimensions](distillation-improves-ai-tutor-evaluation.md) — related
