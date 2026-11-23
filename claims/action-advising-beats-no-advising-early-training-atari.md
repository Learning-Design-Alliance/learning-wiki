---
type: claim
title: "Advised deep RL students outperform a no-advising student during early training in Atari domains, except Q*bert where advising benefits appear later"
description: "Advised deep RL students outperform a no-advising student during early training in Atari domains, except Q*bert where advising benefits appear later"
id: action-advising-beats-no-advising-early-training-atari
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# Advised deep RL students outperform a no-advising student during early training in Atari domains, except Q*bert where advising benefits appear later

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` All advised agents except RA performed better than the no-advising agent during early training with statistically significant differences in all domains except Q*bert, where advising benefits appear in later training stages. [→ Sahir 2022](#sahir-2022)

## Evidence

### Sahir 2022

Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)

`q2 · i?` · `causal · r2`

Simulation experiments on five Atari domains (Pong, Freeway, Seaquest, Enduro, Q*bert) with agents trained 5 million frames over 10 independent runs, comparing advised agents against the NA baseline. The article reports statistically significant early-training differences "in all domains except Q*bert"; no effect size is printed.

> "All advised agents (except RA) performed better than no advising agent (NA) during the early training phases, with statistically significant differences as they are more than twice the standard error in the respective means (for 95% confidence), in all domains except Q*bert, where the benefits of advising appear in later stages of training."

## Discussion


## Related Claims
- Advice reuse (SUA-AIR and AIR) yields a statistically significant performance boost over non-reuse advising agents in Freeway and Pong, and late-training gains in Q*bert — related
- [Uncertainty-driven advice collection changes when advice is requested from the teacher, spreading requests across training rather than consuming the budget early](uncertainty-driven-advising-changes-advice-schedule.md) — related
- [SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement](sua-air-not-significantly-better-than-air.md) — related
