---
type: claim
title: KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching
description: KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching
id: small-tau-kl-mitigates-noisy-labels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: taehyeon-kim-2021
    resource: "https://doi.org/10.24963/ijcai.2021/362"
    title: "Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)"
    author: Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under symmetric label noise below 50%, LKL with τ ≤ 1.0 achieves the best generalization, acting like label smoothing; above 50% noise, logit matching fails. [→ Taehyeon Kim 2021](#taehyeon-kim-2021)

## Evidence

### Taehyeon Kim 2021

Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)

`q2 · i?` · `causal · r2`

Noisy-label simulation on CIFAR-100 (Figure 6) with (WRN-28-4, WRN-16-2), randomly flipping a fraction of training labels following a symmetric uniform distribution; panels show 40% and 80% noise as τ varies.

> "Interestingly, the best generalization performance is achieved when we useLKL withτ ≤ 1.0."

## Discussion


## Related Claims
- [MSE-trained students are better calibrated than KL(τ = ∞)-trained students, with ECE closer to the teacher's](mse-distillation-better-calibration-than-large-tau-kl.md) — related
- [With a poorly trained (noisy) teacher, label matching outperforms logit matching, and MSE loss performs worst](noisy-teacher-label-matching-better.md) — related
- [Surprisal-based model selection adds an Occam-factor penalty for superfluous fit-parameters on top of goodness of fit](kl-divergence-model-selection-occam-penalty.md) — related
