---
type: claim
title: The lighter Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro across temperature configurations, an inverse-scaling pattern
description: The lighter Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro across temperature configurations, an inverse-scaling pattern
id: inverse-scaling-flash-beats-pro-crci
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eugenio-tufino-2026
    resource: "https://doi.org/10.1088/1361-6404/ae8c90"
    title: "Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)"
    author: Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The lighter Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro across temperature configurations, an inverse-scaling pattern

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Gemini 3 Flash outperformed the larger Gemini 3 Pro on the CRCI, with no item on which Pro performed better, and the gap persisted at T=1.0. [→ Eugenio Tufino 2026](#eugenio-tufino-2026)

## Evidence

### Eugenio Tufino 2026

Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)

`q2 · i?` · `design · r2`

Item-level comparison across 21 CRCI items at T=0.7 shows Flash ahead on every item; a robustness replication at T=1.0 "reduces the gap but does not eliminate it", indicating the difference is not a temperature artifact.

> "There is no item on which Pro performs better than Flash (see Table S1). This is consistent with an inverse-scaling pattern previously reported in the AI benchmarks literature (14)."

## Discussion


## Related Claims
- [Frontier LLMs outperform the student average on most CRCI items, with mean accuracies of 97.0% (Gemini 3 Flash), 88.6% (Gemini 3 Pro) and 73.3% (GPT-5.2) versus 61.5% for students](llms-outperform-students-on-crcl.md) — related
