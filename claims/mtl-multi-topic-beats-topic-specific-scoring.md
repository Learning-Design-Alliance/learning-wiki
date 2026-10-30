---
type: claim
title: Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models
description: Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models
id: mtl-multi-topic-beats-topic-specific-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: xiaoyu-bai-manfred-stede-2023
    resource: "https://doi.org/10.1007/s40593-022-00323-0"
    title: "Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0"
    author: Xiaoyu Bai · Manfred Stede
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Xue et al. (2021) found that a single BERT-based MTL model trained jointly on essays from multiple topics outperformed separate models trained on smaller, topic-specific datasets. [→ Xiaoyu Bai · Manfred Stede 2023](#xiaoyu-bai-manfred-stede-2023)

## Evidence

### Xiaoyu Bai · Manfred Stede 2023

Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0

`q2 · i?` · `review · r2`

The survey describes Xue et al. (2021)'s BERT-based multi-task learning essay scoring model, which "jointly learned to score essays on all topics"; the comparison is reported as the survey states it, with no effect size printed.

> "They found in their experiments that training a single model on a large, multi-topic dataset outperformed separate models trained on smaller, topic-specific datasets."

## Discussion


## Related Claims
- [The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks](qbert-rr-comparable-or-better-than-single-task.md) — a broader claim this one bears on
- [Training NQG models on multiple datasets with different answer types improved performance over single-dataset training](multi-dataset-training-improves-nqg-answer-types.md) — a broader claim this one bears on
- [A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.](multitask-matrix-factorization-outperforms-single-task-baseline.md) — a narrower finding that bears on this claim
