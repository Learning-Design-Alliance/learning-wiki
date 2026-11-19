---
type: claim
title: A behavior-cloned policy distilled from online RL data was estimated to outperform the online policy in the majority of offline evaluation splits and was deployed in study 2
description: A behavior-cloned policy distilled from online RL data was estimated to outperform the online policy in the majority of offline evaluation splits and was deployed in study 2
id: behavior-cloned-policy-outperformed-online-policy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: sherry-ruan-2024
    resource: "https://doi.org/10.1007/s10994-023-06423-9"
    title: "Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)"
    author: Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A behavior-cloned policy distilled from online RL data was estimated to outperform the online policy in the majority of offline evaluation splits and was deployed in study 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In offline policy evaluation over 10 random train/validation splits, the behavior-cloned policy was estimated to outperform the online policy in the majority of splits, and a small 1-layer network performed best. [→ Sherry Ruan 2024](#sherry-ruan-2024)

## Evidence

### Sherry Ruan 2024

Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)

`q2 · i?` · `causal · r2`

Offline reinforcement learning policy selection using weighted importance sampling on study 1 data, with 108 hyperparameter combinations and 10 repeated 50/50 splits. This is a numerical/simulation-style evaluation of estimated policy value, not a human-outcome result; the distilled policy was then deployed in study 2.

> "In our evaluation, the behavior cloned policy was estimated to outperform the online policy in the majority of splits. Also, a small 1-layer fully connected neural network with 4-dimensional hidden state and Gaussian error linear unit [26] activation function outperformed other model architectures."

## Discussion


## Related Claims
- [Among RL-in-education papers testing statistical significance, 18 of 35 report at least one RL policy significantly outperforming all baselines, while over half of all reviewed papers report no statistical analysis](rl-education-significance-18-of-35-outperform.md) — related
- [Reinforcement-learning sequencing policies beat baseline sequencing in about half of controlled studies, mostly in constrained tasks and against weak baselines](rl-sequencing-policies-beat-baselines-in-constrained-tasks.md) — related
