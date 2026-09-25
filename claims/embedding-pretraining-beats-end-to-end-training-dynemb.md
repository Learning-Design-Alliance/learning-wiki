---
type: claim
title: Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits
description: Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits
id: embedding-pretraining-beats-end-to-end-training-dynemb
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
    q: 2
    i: 2
---

# Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i?` On ASSISTment09 under the Most Recent evaluation, end-to-end training caused overfitting while the pretraining strategy's learning curve showed neither overfitting nor underfitting, and pretraining was also computationally more efficient. [→ Liangbei Xu and Mark A. Davenport 2020](#liangbei-xu-and-mark-a-davenport-2020)

## Evidence

### Liangbei Xu and Mark A. Davenport 2020

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q2 · i2`

Experiment 3 compared training strategies on ASSISTment09 using the Most Recent evaluation method, plotting training and testing log-loss in Figure 4; end-to-end training overfit while the pretraining strategy did not, and pretraining also improved computational efficiency.

> "In Figure 4, we can see that end-to-end (E2E for short) training (with/without pretraining the ques- tion embedding) will cause over-ﬁtting, while the learning curve of proposed pretraining strategy does not suﬀer from over-ﬁtting or under-ﬁtting."

## Discussion


## Related Claims
-
