---
type: claim
title: A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.
description: A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.
id: matrix-factorization-predicts-grades-for-nongrading-students
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

# A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · checked against its sources 2026-10-30 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students. [→ Luaces 2018](#luaces-2018)

## Evidence

### Luaces 2018

Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.07.016

`q2 · i?` · `design · r2`

The authors report that their multitask matrix factorization model, trained on peer assessment data from a subset of students, generalizes to grade answers from students outside the peer assessment loop, relieving part of the student body of grading work.

> "models learned using the multitask approach can be extended to answers not at all involved in peer assessment. The consequence is that a part of the students can be relieved of the assessment task, thereby reducing the burden on students in processes of this kind."

## Discussion


## Related Claims
- [A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.](multitask-matrix-factorization-outperforms-single-task-baseline.md) — related
- [Peer assessment systems can generate explanatory feedback for students by having graders assess multiple labeled aspects of an answer, not just an overall grade.](peer-assessment-multi-label-feedback.md) — related
- [AGE reduces teacher grading burden by requiring only 1% of student answers in the UNT dataset to be graded](age-grades-only-one-percent-unt.md) — related
