---
type: claim
title: Uncertainty sampling performs similarly to random sampling on real AS models but approaches reward-sampling performance on a pseudo model with randomly generated predictions
description: Uncertainty sampling performs similarly to random sampling on real AS models but approaches reward-sampling performance on a pseudo model with randomly generated predictions
id: uncertainty-sampling-gains-depend-on-model-error-structure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yaman-kumar-singla-2022
    resource: "https://doi.org/10.1609/aaai.v36i11.21563"
    title: "Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)"
    author: Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Uncertainty sampling performs similarly to random sampling on real AS models but approaches reward-sampling performance on a pseudo model with randomly generated predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Uncertainty sampling shows gains similar to random sampling in all models except the pseudo model, where its performance is more in line with reward sampling. [→ Yaman Kumar Singla 2022](#yaman-kumar-singla-2022)

## Evidence

### Yaman Kumar Singla 2022

Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)

`q2 · i?` · `causal · r2`

Results section comparison across the five models in Table 1 and Fig 4; the article attributes the difference to the pseudo model's randomly generated predictions, where "local gains translate well to global gains".

> "Interestingly, Uncertainty Sampling shows similar gains to random sam- pling in all models except the pseudo model, where its per- formance is more in line with reward sampling."

## Discussion


## Related Claims
- [Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines](reward-sampling-improves-automated-scoring-accuracy-qwk.md) — related
