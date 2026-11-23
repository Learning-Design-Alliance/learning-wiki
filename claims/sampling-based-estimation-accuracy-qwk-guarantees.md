---
type: claim
title: "A confidence-based secondary sampling procedure estimates post-sampling accuracy and QWK with a 95% statistical guarantee using a sample of 200 candidates"
description: "A confidence-based secondary sampling procedure estimates post-sampling accuracy and QWK with a 95% statistical guarantee using a sample of 200 candidates"
id: sampling-based-estimation-accuracy-qwk-guarantees
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yaman-kumar-singla-2022
    resource: "https://doi.org/10.1609/aaai.v36i11.21563"
    title: "Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)"
    author: Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A confidence-based secondary sampling procedure estimates post-sampling accuracy and QWK with a 95% statistical guarantee using a sample of 200 candidates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A secondary sample of 200 candidates drawn from a confidence distribution yields stable 95% confidence intervals, and taking the lower bound guarantees accuracy/QWK falls below the estimate only 5% of runs. [→ Yaman Kumar Singla 2022](#yaman-kumar-singla-2022)

## Evidence

### Yaman Kumar Singla 2022

Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)

`q2 · i?` · `design · r2`

Estimation experiments reported in §5.2 and Fig 5 for two models (BERT-TwoStage and LSTM-Baseline), where after reward sampling a confidence-distribution sample is drawn and "the 95% conﬁdence interval for both accuracy and kappa is calculated".

> "Empirically, we observed that a sample size of 200 was sufﬁcient for stable estimations of a 95% conﬁdence interval."

## Discussion


## Related Claims
- [Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines](reward-sampling-improves-automated-scoring-accuracy-qwk.md) — related
- [MC-dropout uncertainty estimates separate reliable from unreliable pseudo-labels, and balanced low-uncertainty sampling best matches the target score distribution](ust-uncertainty-filtering-pseudo-labels.md) — related
