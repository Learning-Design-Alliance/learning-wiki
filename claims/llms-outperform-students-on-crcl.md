---
type: claim
title: "Frontier LLMs outperform the student average on most CRCI items, with mean accuracies of 97.0% (Gemini 3 Flash), 88.6% (Gemini 3 Pro) and 73.3% (GPT-5.2) versus 61.5% for students"
description: "Frontier LLMs outperform the student average on most CRCI items, with mean accuracies of 97.0% (Gemini 3 Flash), 88.6% (Gemini 3 Pro) and 73.3% (GPT-5.2) versus 61.5% for students"
id: llms-outperform-students-on-crcl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-21
recheck_by: 2029
sources:
  - id: eugenio-tufino-2026
    resource: "https://doi.org/10.1088/1361-6404/ae8c90"
    title: "Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)"
    author: Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Frontier LLMs outperform the student average on most CRCI items, with mean accuracies of 97.0% (Gemini 3 Flash), 88.6% (Gemini 3 Pro) and 73.3% (GPT-5.2) versus 61.5% for students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-21 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On a novel 21-item concept inventory administered 30 times per item per model, all three frontier LLMs achieved higher mean accuracy than the 267-student sample, though each had low accuracy on a few items (on Q16, 56.7%, 33.3% and 3.3%), and only GPT-5.2 failed an item completely (0% on Q4). [→ Eugenio Tufino 2026](#eugenio-tufino-2026)

## Evidence

### Eugenio Tufino 2026

Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)

`q2 · i?` · `associational · r2`

Repeated-trial evaluation of three LLMs on the CRCI (30 iterations per item, T=0.7) compared with N = 267 first-year physics students; Table 1 reports mean accuracies of "97.0% and 88.6%" for the Gemini models, 73.3% for GPT-5.2 (reasoning disabled) and 61.5% for students.

> "Across the 21 items, Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro, with mean accuracies of 97.0% and 88.6%, respectively (see Table 1)."

## Discussion


## Related Claims
- [The lighter Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro across temperature configurations, an inverse-scaling pattern](inverse-scaling-flash-beats-pro-crci.md) — related
- [All three models show severe, item-specific failures, with Q16 (fluid on inclined plane with friction) difficult for every model and GPT-5.2 scoring 0% on Q4](item-specific-complete-llm-failures.md) — a narrower finding that bears on this claim
