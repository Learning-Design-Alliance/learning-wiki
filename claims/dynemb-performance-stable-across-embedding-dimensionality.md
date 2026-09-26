---
type: claim
title: "DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities"
description: "DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities"
id: dynemb-performance-stable-across-embedding-dimensionality
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
    i: 1
---

# DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` Across embedding dimensionalities tested on ASSISTment09 and CT05, DynEmb's AUC showed little variation, indicating robustness to this hyperparameter. [→ Liangbei Xu and Mark A. Davenport 2020](#liangbei-xu-and-mark-a-davenport-2020)

## Evidence

### Liangbei Xu and Mark A. Davenport 2020

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q2 · i1`

Experiment 2 varied the dynamic embedding dimensionality on the ASSISTment09 and Cognitive Tutor 'Algebra I 2005' (CT05) datasets, the two with the smallest numbers of interactions, and evaluated on the response prediction task; Figure 3 shows AUC varying little across dimensionalities.

> "As we can see from Figure 3, the performance by AUC of DynEmb is quite stable over a wide range of embedding dimensionalities. This robustness is an additional attractive feature of our approach."

## Discussion


## Related Claims
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
