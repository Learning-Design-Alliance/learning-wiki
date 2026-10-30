---
type: claim
title: A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.
description: A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.
id: multitask-matrix-factorization-outperforms-single-task-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
evidence_strength: moderate
newest_evidence: 2018
source_checked: 2026-10-30
recheck_by: 2021
sources:
  - id: luaces-2018
    resource: "https://doi.org/10.1016/j.compedu.2018.07.016"
    title: "Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.07.016"
    author: "Luaces, O., Díez, J., & Bahamonde, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · checked against its sources 2026-10-30 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task baseline that learns each label separately. [→ Luaces 2018](#luaces-2018)

## Evidence

### Luaces 2018

Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.07.016

`q2 · i?` · `design · r2`

In experiments across three courses, the multitask approach, which learns grading patterns for all labels simultaneously, achieved better accuracy than a binary relevance baseline that learns a separate model per label.

> "We have presented a method that uses a multitask approach to search for grading patterns in all labels at the same time. Multitask leverages the accuracy of a baseline that successively focuses on each label separately."

## Discussion


## Related Claims
- [A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.](matrix-factorization-predicts-grades-for-nongrading-students.md) — related
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — a broader claim this one bears on
- [Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models](mtl-multi-topic-beats-topic-specific-scoring.md) — a broader claim this one bears on
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
