---
type: claim
title: Assessment Modeling, pre-trained on EdNet-KT4, achieved state-of-the-art exam score and review correctness prediction
description: Assessment Modeling, pre-trained on EdNet-KT4, achieved state-of-the-art exam score and review correctness prediction
id: assessment-modeling-sota-pretraining-ednet
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

# Assessment Modeling, pre-trained on EdNet-KT4, achieved state-of-the-art exam score and review correctness prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using EdNet-KT4 as training data, Assessment Modeling showed state-of-the-art results in both exam score and review correctness prediction, outperforming NLP pre-training methods. [→ Choi 2020](#choi-2020)

## Evidence

### Choi 2020

Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. [doi:10.1007/978-3-030-52240-7_13](https://doi.org/10.1007/978-3-030-52240-7_13)

`q2 · i?` · `design · r?`

The Applications section reports, attributing the method to reference [4], that Assessment Modeling defines assessments as a specific type of educational interactive feature and uses assessment prediction as a pre-training task for label-scarce AIEd tasks, "outperforming pre-training methods developed in the natural language processing community."

> "Using EdNet-KT4 as the training dataset, Assessment Modeling showed state-of-the-art results in both exam score and review correctness prediction, outperforming pre-training methods developed in the natural language processing community"

## Discussion


## Related Claims
- [The DAS model outperformed existing models for study session dropout prediction in mobile learning environments on EdNet-KT4](das-outperforms-on-ednet-kt4-dropout.md) — related
- [SAINT achieved state-of-the-art knowledge tracing performance with a dramatic AUROC improvement when trained on EdNet-KT1](saint-sota-on-ednet-kt1.md) — related
- [COTUTOR outperforms BKT, DKT, and Code-DKT across all evaluation metrics on the EdNet KT1 benchmark](cotutor-outperforms-baselines-ednet-benchmark.md) — related
