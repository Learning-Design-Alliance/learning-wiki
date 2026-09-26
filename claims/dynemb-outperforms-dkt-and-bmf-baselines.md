---
type: claim
title: "DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting"
description: "DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting"
id: dynemb-outperforms-dkt-and-bmf-baselines
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
  - id: liangbei-xu-and-mark-a-davenport-2020-2
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
    q: 2
    i: 2
---

# DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i2` In offline and online evaluations on ASSISTments and Cognitive Tutor datasets, DynEmb achieved higher AUC than the best baseline, with improvements up to 5.43%. [→ Liangbei Xu and Mark A. Davenport 2020](#liangbei-xu-and-mark-a-davenport-2020)

## Evidence

### Liangbei Xu and Mark A. Davenport 2020

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q2 · i2`

Experiment 1 (future response prediction) on five datasets from ASSISTments and Cognitive Tutor, comparing DynEmb against offline and online BMF and DKT using AUC under 'New User' and 'Most Recent' evaluation. The authors report that DynEmb "signiﬁcantly outper- forms the best baseline in all datasets in terms of AUC", with Table 2 showing improvements up to 5.43% (Algebra I 2005, New User).

> "We observe that DynEmb signiﬁcantly outper- forms the best baseline in all datasets in terms of AUC on the three datasets up to 5.43%."

### Liangbei Xu and Mark A. Davenport 2020 (2)

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q2 · i2`

Table 2 reports per-dataset AUC for BMF (offline and online), DKT, and DynEmb with question-only and concatenated embeddings; e.g., Algebra I 2005 New User AUC of 0.815 versus 0.773 for DKT, a 5.43% improvement.

> "Table 2: Future response prediction experiment: Table comparing the performance of DynEmb (concatenating question and skill embedding) with baselines, in terms of AUC. DynEmb outperforms the best baseline by up to 5.43%."

## Discussion


## Related Claims
- [DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities](dynemb-performance-stable-across-embedding-dimensionality.md) — related
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — related
