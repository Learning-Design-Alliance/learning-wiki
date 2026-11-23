---
type: claim
title: SAINT achieved state-of-the-art knowledge tracing performance with a dramatic AUROC improvement when trained on EdNet-KT1
description: SAINT achieved state-of-the-art knowledge tracing performance with a dramatic AUROC improvement when trained on EdNet-KT1
id: saint-sota-on-ednet-kt1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: choi-2020
    resource: "https://doi.org/10.1007/978-3-030-52240-7_13"
    title: "Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. [doi:10.1007/978-3-030-52240-7_13](https://doi.org/10.1007/978-3-030-52240-7_13)"
    author: Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J.
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# SAINT achieved state-of-the-art knowledge tracing performance with a dramatic AUROC improvement when trained on EdNet-KT1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training SAINT on EdNet-KT1 yielded state-of-the-art performance with a dramatic AUROC improvement over previous knowledge tracing models. [→ Choi 2020](#choi-2020)

## Evidence

### Choi 2020

Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. [doi:10.1007/978-3-030-52240-7_13](https://doi.org/10.1007/978-3-030-52240-7_13)

`q2 · i?` · `design · r?`

The paper's Applications section reports that SAINT, a Transformer-based knowledge tracing model trained on EdNet-KT1, "achieved state-of-the-art performance with an dramatic improvement in" AUROC; the paper attributes the result to reference [3] and prints no numeric AUROC value or test statistics.

> "Compared to previous knowledge tracing models, SAINT achieved state-of-the-art performance with an dramatic improvement in Area Under receiver operating characteristic Curve (AUROC)."

## Discussion


## Related Claims
- [Assessment Modeling, pre-trained on EdNet-KT4, achieved state-of-the-art exam score and review correctness prediction](assessment-modeling-sota-pretraining-ednet.md) — related
- [COTUTOR outperforms BKT, DKT, and Code-DKT across all evaluation metrics on the EdNet KT1 benchmark](cotutor-outperforms-baselines-ednet-benchmark.md) — related
- [Injecting MBP-KT's global collaborative information consistently improves KT models across RNN, memory-network, Transformer and state-based backbones](mbp-kt-consistently-improves-kt-backbones.md) — related
- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
- [Collaborative representations from meta-behavioral sequences are far less sparse than KC-based representations, which reach up to 99.3% sparsity](meta-behavioral-representations-reduce-sparsity.md) — related
