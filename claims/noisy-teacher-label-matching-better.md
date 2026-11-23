---
type: claim
title: With a poorly trained (noisy) teacher, label matching outperforms logit matching, and MSE loss performs worst
description: With a poorly trained (noisy) teacher, label matching outperforms logit matching, and MSE loss performs worst
id: noisy-teacher-label-matching-better
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
  - id: taehyeon-kim-2021-2
    resource: "https://doi.org/10.24963/ijcai.2021/362"
    title: "Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)"
    author: Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# With a poorly trained (noisy) teacher, label matching outperforms logit matching, and MSE loss performs worst

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Distilling from a WRN-28-4 teacher with only 53.77% training accuracy, students using label matching (small τ) score highest and MSE-trained students lowest. [→ Taehyeon Kim 2021](#taehyeon-kim-2021)
`q2 i?` On ImageNet with a ResNet-152 teacher at 81.16% training accuracy, extreme logit matching again exhibits the worst performance. [→ Taehyeon Kim 2021 (2)](#taehyeon-kim-2021-2)

## Evidence

### Taehyeon Kim 2021

Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)

`q2 · i?` · `causal · r2`

CIFAR-100 experiment (Table 4) with an under-trained WRN-28-4 teacher (10 epochs, 53.77% training accuracy); accuracies fall monotonically from τ = 0.1 (51.64) to LMSE (49.20).

> "When poor knowledge is distilled, the students following the label matching scheme performed better than the students following the logit matching scheme, and the extreme logit matching throughLMSE has the worst performance."

### Taehyeon Kim 2021 (2)

Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)

`q2 · i?` · `causal · r2`

ImageNet experiment with (ResNet-152, ResNet-50): LCE baseline 76.28, standard LKL 77.15, LKL(τ=20) 77.52, LMSE 75.84; baseline and standard-LKL results taken from Heo et al.

> "Table 5 presents top-1 test accu- racies on ImageNet, where the used teacher network (ResNet-152) has a training accuracy of 81.16%, which is provided in PyTorch. Even in this case, the extreme logit matching exhibits the worst performance."

## Discussion


## Related Claims
- [MSE-trained students are better calibrated than KL(τ = ∞)-trained students, with ECE closer to the teacher's](mse-distillation-better-calibration-than-large-tau-kl.md) — related
- [KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching](small-tau-kl-mitigates-noisy-labels.md) — related
