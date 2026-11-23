---
type: claim
title: SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement
description: SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement
id: sua-air-not-significantly-better-than-air
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
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

# SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The performance differences between SUA-AIR and AIR are not statistically significant, so the answer to whether dual uncertainties improve student learning is inconclusive. [→ Sahir 2022](#sahir-2022)

## Evidence

### Sahir 2022

Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)

`q2 · i?` · `causal · r2`

Results section comparison of the proposed SUA-AIR against the state-of-the-art AIR baseline across the five Atari domains. The article reports no statistically significant difference; equivalence was not tested and no effect size is printed.

> "In general, SUA-AIR and AIR performed in a similar fashion. The differences in performance between SUA-AIR and AIR are not statistically significant. Thus, the answer to RQ1 is inconclusive."

## Discussion


## Related Claims
- [Advised deep RL students outperform a no-advising student during early training in Atari domains, except Q*bert where advising benefits appear later](action-advising-beats-no-advising-early-training-atari.md) — related
- Advice reuse (SUA-AIR and AIR) yields a statistically significant performance boost over non-reuse advising agents in Freeway and Pong, and late-training gains in Q*bert — related
- [Uncertainty-driven advice collection changes when advice is requested from the teacher, spreading requests across training rather than consuming the budget early](uncertainty-driven-advising-changes-advice-schedule.md) — related
- [The model of the teacher shows similar action-prediction accuracy for SUA-AIR and AIR across training in Pong](teacher-model-accuracy-similar-sua-air-air.md) — related
