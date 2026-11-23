---
type: claim
title: The model of the teacher shows similar action-prediction accuracy for SUA-AIR and AIR across training in Pong
description: The model of the teacher shows similar action-prediction accuracy for SUA-AIR and AIR across training in Pong
id: teacher-model-accuracy-similar-sua-air-air
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: sahir-2022
    resource: "https://doi.org/10.48550/arXiv.2204.07254"
    title: "Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)"
    author: Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The model of the teacher shows similar action-prediction accuracy for SUA-AIR and AIR across training in Pong

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The model of the teacher for SUA-AIR and AIR shows similar accuracies across training, with AIR's model slightly more accurate because it uses the model to collect advice. [→ Sahir 2022](#sahir-2022)

## Evidence

### Sahir 2022

Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)

`q2 · i?` · `causal · r2`

Secondary evaluation comparing teacher and model actions for states the student visits, in Pong averaged over 3 independent runs (Figure 5). The article reports similar accuracies; no effect size is printed.

> "It is evident from Figure 5 that the model of the teacher for SUA-AIR and AIR show similar accuracies across training. Since AIR uses the model of the teacher to collect advice, it is natural to see it slightly more accurate than the model of SUA-AIR."

## Discussion


## Related Claims
- [SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement](sua-air-not-significantly-better-than-air.md) — related
- Advice reuse (SUA-AIR and AIR) yields a statistically significant performance boost over non-reuse advising agents in Freeway and Pong, and late-training gains in Q*bert — related
