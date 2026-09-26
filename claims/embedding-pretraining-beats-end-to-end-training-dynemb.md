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
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related
- [DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities](dynemb-performance-stable-across-embedding-dimensionality.md) — related
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization](dynemb-question-embedding-clusters-by-skill.md) — related
- [Pretraining Improves Transfer](pretraining-improves-transfer.md) — related
