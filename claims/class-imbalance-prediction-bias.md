---
type: claim
title: "The model's class imbalance biases predictions: faculty without experience teaching computation are classified almost at random"
description: "The model's class imbalance biases predictions: faculty without experience teaching computation are classified almost at random"
id: class-imbalance-prediction-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: nicholas-t-young-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The model's class imbalance biases predictions: faculty without experience teaching computation are classified almost at random

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Because about 60% of the sample had experience teaching computation, the model was better at classifying faculty with experience and appeared to classify those without almost at random, though the authors argue AUC-based importance is unaffected by class imbalance. [→ Nicholas T. Young 2019](#nicholas-t-young-2019)

## Evidence

### Nicholas T. Young 2019

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Limitations analysis of unbalanced classes; the authors report attempted corrections (up-sampling biased the cforest algorithm; down-sampling excluded nearly 20% of usable data and did not improve accuracy or AUC in their trials).

> "However, our model appears to be classifying faculty without experience teaching computation almost at random, suggesting that our results are biased."

## Discussion


## Related Claims
- [Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class](intermediate-skill-class-hardest-to-classify.md) — related
