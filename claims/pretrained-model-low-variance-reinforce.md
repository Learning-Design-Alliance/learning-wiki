---
type: claim
title: The pre-trained model showed relatively low variance despite using REINFORCE, which typically suffers from high variance
description: The pre-trained model showed relatively low variance despite using REINFORCE, which typically suffers from high variance
id: pretrained-model-low-variance-reinforce
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jean-vassoyan-2024
    resource: "https://doi.org/10.48550/arXiv.2411.11520"
    title: "Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). [doi:10.48550/arXiv.2411.11520](https://doi.org/10.48550/arXiv.2411.11520)"
    author: Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The pre-trained model showed relatively low variance despite using REINFORCE, which typically suffers from high variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Despite being trained with REINFORCE, which usually suffers from high variance compared to PPO, the pre-trained model showed relatively low variance, much lower than its non-pre-trained counterpart. [→ Jean Vassoyan 2024](#jean-vassoyan-2024)

## Evidence

### Jean Vassoyan 2024

Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). [doi:10.48550/arXiv.2411.11520](https://doi.org/10.48550/arXiv.2411.11520)

`q2 · i?` · `design · r2`

Observation from Table 1 confidence intervals: the model "showed a relatively low variance (much lower than its non-pre-trained counterpart)" despite using REINFORCE rather than PPO.

> "despite being trained with the REINFORCE algorithm, which, in comparison to PPO, usually suffers from high variance, our model showed a relatively low variance (much lower than its non-pre-trained counterpart)."

## Discussion


## Related Claims
- [ALPN-EPPO achieves the highest cumulative reward during training among the ALPN variants using EPPO, PPO and A2C](alpn-eppo-highest-cumulative-reward.md) — related
