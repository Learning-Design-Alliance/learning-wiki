---
type: claim
title: "Personalized meta-learning federated models achieve at least 10% higher AUC than local and global baselines on the FOC and QDS datasets"
description: "Personalized meta-learning federated models achieve at least 10% higher AUC than local and global baselines on the FOC and QDS datasets"
id: meta-learning-personalization-10pt-auc-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: yun-wei-chu-2018
    resource: "https://doi.org/10.1145/1122445.1122456"
    title: "Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456"
    author: Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Personalized meta-learning federated models achieve at least 10% higher AUC than local and global baselines on the FOC and QDS datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Most local- and global-based models have at least 10% lower AUC than the personalized models on the FOC and QDS datasets. [→ Yun-Wei Chu 2018](#yun-wei-chu-2018)

## Evidence

### Yun-Wei Chu 2018

Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456

`q2 · i?` · `design · r2`

Comparative evaluation across three edX course datasets (Tables 3-5) grouping students by gender, continent, and age; the article reports the personalized models' AUC advantage, noting the performance of personalized models is possibly limited in the MOSFETs dataset by its overall smaller size.

> "Across Tables 3, 4, and 5, we see that most local- and global-based models have at least 10% lower AUC than the personalized models on the FOC and QDS datasets."

## Discussion


## Related Claims
- [A centralized global model performs better on larger subgroups, indicating it may ignore minorities](centralized-model-favors-majority-subgroups.md) — related
- [The personalized method outperforms the data-quality-weighted FedIRT baseline by at least 5% in most cases](meta-learning-beats-fedirt-by-5pt.md) — related
