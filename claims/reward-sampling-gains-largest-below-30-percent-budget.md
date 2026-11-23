---
type: claim
title: "Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows"
description: "Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows"
id: reward-sampling-gains-largest-below-30-percent-budget
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
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

# Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Reward sampling outperforms other methods with large gains up to a sample size of about 30%, beyond which gains are no longer as significant and other methods catch up. [→ Yaman Kumar Singla 2022](#yaman-kumar-singla-2022)

## Evidence

### Yaman Kumar Singla 2022

Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. [doi:10.1609/aaai.v36i11.21563](https://doi.org/10.1609/aaai.v36i11.21563)

`q2 · i?` · `causal · r2`

Results analysis across all models in Fig 4, where accuracy and QWK are plotted against increasing human budget up to 80% of the dataset; the article reports the trend "upto a sam- ple size of∼30%" and states it holds across all models.

> "Initially, Reward Sampling outperforms the other sampling methods with large gains, upto a sam- ple size of∼30%. Beyond this mark, the gains are no longer as signiﬁcant and the other methods slowly catch up."

## Discussion


## Related Claims
- [Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines](reward-sampling-improves-automated-scoring-accuracy-qwk.md) — related
- [Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks](agenticmath-data-size-positive-correlation-accuracy.md) — related
