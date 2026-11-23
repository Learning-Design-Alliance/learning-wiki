---
type: claim
title: Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines
description: Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines
id: reward-sampling-improves-automated-scoring-accuracy-qwk
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
  - id: yaman-kumar-singla-2022-2
    resource: "https://doi.org/10.1609/aaai.v36i11.21563"
    title: "Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)"
    author: Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across five AS models, reward sampling with a 30% human budget yields average gains of 19.80% accuracy and 25.60% QWK, versus 8.6% and 12.2% for random and uncertainty sampling. [→ Yaman Kumar Singla 2022](#yaman-kumar-singla-2022)
`q2 i?` On the BERT-Baseline model at 10% human budget, reward sampling shows an 8% accuracy gain, more than twice the gains achieved by random sampling. [→ Yaman Kumar Singla 2022 (2)](#yaman-kumar-singla-2022-2)

## Evidence

### Yaman Kumar Singla 2022

Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)

`q2 · i?` · `causal · r2`

Experiments on the SLTI SOPI speech-scoring dataset across BERT, two-stage BERT, LSTM-attention and pseudo models, with sampled predictions replaced by ground truth and global metrics recomputed; the article reports "19.80% increase in accuracy and 25.60% increase in QWK" versus baseline gains.

> "Averaging over these models, we observe 19.80% increase in accuracy and 25.60% increase in QWK when using reward sampling with 30% of the dataset as a human budget. The random sampling and uncertainty sampling baselines achieve 8.6% and 12.2% gains in accuracy, respectively."

### Yaman Kumar Singla 2022 (2)

Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)

`q2 · i?` · `causal · r2`

Results section analysis of the BERT-Baseline model when 10% of the dataset is sampled for human scoring; reward sampling's "8% gain in accuracy" is more than twice random sampling's gain, with random sampling showing only 3% improvement.

> "Reward Sampling, on the other hand, shows an 8% gain in accuracy, more than twice the gains achieved by random sampling."

## Discussion


## Related Claims
- [Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows](reward-sampling-gains-largest-below-30-percent-budget.md) — related
- [A confidence-based secondary sampling procedure estimates post-sampling accuracy and QWK with a 95% statistical guarantee using a sample of 200 candidates](sampling-based-estimation-accuracy-qwk-guarantees.md) — related
- [Uncertainty sampling performs similarly to random sampling on real AS models but approaches reward-sampling performance on a pseudo model with randomly generated predictions](uncertainty-sampling-gains-depend-on-model-error-structure.md) — related
