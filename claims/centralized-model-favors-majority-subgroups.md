---
type: claim
title: A centralized global model performs better on larger subgroups, indicating it may ignore minorities
description: A centralized global model performs better on larger subgroups, indicating it may ignore minorities
id: centralized-model-favors-majority-subgroups
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

# A centralized global model performs better on larger subgroups, indicating it may ignore minorities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` AttnGRU-G performs better on the male than the female subgroup for QDS and MOSFETs, and better on Asian and North American subgroups than others on FOC and QDS, which the authors flag as an ethical concern. [→ Yun-Wei Chu 2018](#yun-wei-chu-2018)

## Evidence

### Yun-Wei Chu 2018

Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456

`q2 · i?` · `design · r2`

Subgroup results in Tables 3 and 4 show the centralized AttnGRU-G model is more accurate on larger subgroups; the article states this indicates the model will ignore minorities and thus may have ethical concerns.

> "For example, the performance of AttnGRU-G on the male subgroup is better that on the female subgroup for QDS and MOSFETs (see Table 3); moreover, the model performs better on the Asian and North American subgroups than other subgroups on FOC and QDS (see Table 4)."

## Discussion


## Related Claims
- [Personalized meta-learning federated models achieve at least 10% higher AUC than local and global baselines on the FOC and QDS datasets](meta-learning-personalization-10pt-auc-gain.md) — related
- [Learned student embeddings are organized and sometimes well-clustered by demographic subgroup](subgroup-clustered-embeddings.md) — related
