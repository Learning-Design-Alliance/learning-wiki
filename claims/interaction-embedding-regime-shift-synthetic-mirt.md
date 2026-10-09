---
type: claim
title: On synthetic MIRT data, mean embeddings perform best at two knowledge components per question while MHSA embeddings perform best at four
description: On synthetic MIRT data, mean embeddings perform best at two knowledge components per question while MHSA embeddings perform best at four
id: interaction-embedding-regime-shift-synthetic-mirt
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: kai-neubauer-2026
    resource: "https://github.com/kainbr/kt_set_transformers"
    title: "Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers"
    author: Kai Neubauer, Yannick Rudolph, and Ulf Brefeld
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# On synthetic MIRT data, mean embeddings perform best at two knowledge components per question while MHSA embeddings perform best at four

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Experiments on synthetic MIRT data indicate a regime shift in which the best interaction embedding depends on the number of knowledge components per question and training-sample size. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q1 · i?` · `design · r2`

Simulation study using synthetic data from a compensatory multidimensional 3PL model, with 1,000 questions, 50 components, 100 interactions per student, and 10 trained models per configuration. Unique set embeddings performed worst throughout; at three components MHSA won on smaller samples while mean embeddings were better for 5,000 training sequences.

> "the experiments indicate a regime shift, where mean embeddings perform best on data with two knowledge components per question, while MHSA embeddings perform best on four knowledge components per question."

## Discussion


## Related Claims
- [The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work](expanded-representation-label-leakage-distribution-shift.md) — related
- [DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities](dynemb-performance-stable-across-embedding-dimensionality.md) — related
