---
type: claim
title: The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work
description: The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work
id: expanded-representation-label-leakage-distribution-shift
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

# The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Expanding interactions over multiple knowledge components without proper masking leaks the current response into preceding interaction features, and partial fixes create a distribution shift between training and testing. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q1 · i?` · `design · r2`

Analytical critique of the expanded representation used in prior work (e.g., Ghosh et al. 2020; Liu et al. 2022; Yin et al. 2023). The article argues the response appears in preceding expanded features, and that fixing leakage only for testing but not training creates a distribution shift; no empirical effect sizes accompany this argument.

> "Without proper masking regarding the original interaction sequence, this introduces label leakage, i.e., parts of the expanded interactions have information about the response (the label at the current time step)"

## Discussion


## Related Claims
- [KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios](ktst-gains-largest-high-kc-ratio-datasets.md) — related
- [Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation](mean-embeddings-beat-rasch-embeddings-as2009.md) — related
- [On synthetic MIRT data, mean embeddings perform best at two knowledge components per question while MHSA embeddings perform best at four](interaction-embedding-regime-shift-synthetic-mirt.md) — related
