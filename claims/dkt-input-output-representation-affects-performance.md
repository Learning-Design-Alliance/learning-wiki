---
type: claim
title: "DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets"
description: "DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets"
id: dkt-input-output-representation-affects-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: theophile-gervet-2020
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 2
  - id: theophile-gervet-2020-2
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 1
---

# DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i1`–`i2`

## Subclaims
`q2 i?` The choice of items versus KCs as DKT inputs and outputs considerably impacts performance, and KC inputs with item outputs work best on most datasets. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` DKT, although initially advertised as independent of expert-designed structure, relies on the KC model to perform optimally. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

DKT ablation (Table 14) across nine datasets comparing KC/item inputs and outputs; hyperparameter results were sensitive to dropout probability and input/output representation but not embedding dimension or layer count.

> "Table 14 shows this choice considerably impacts performance, and the KC inputs and item outputs combination works best on most datasets (when the number of items is small enough for this combination to be tractable)."

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Authors' interpretation of the Table 14 ablation: KC inputs reduce available information but help generalization because datasets contain many more learners per KC than per item.

> "This finding means that DKT – although initially advertised as independent from any expert-designed structure (Piech et al., 2015) – relies on the KC model to perform optimally."

## Discussion


## Related Claims
-
