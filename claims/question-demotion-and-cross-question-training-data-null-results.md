---
type: claim
title: Two attempted workload-reduction refinements—stopword-based question demoting and supplementing training data with answers labeled incorrect from other questions—did not improve classification results overall
description: Two attempted workload-reduction refinements—stopword-based question demoting and supplementing training data with answers labeled incorrect from other questions—did not improve classification results overall
id: question-demotion-and-cross-question-training-data-null-results
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: rebecka-weegar-peter-idestam-almquist-2024
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
    q: 2
    i: 0
    kind: design
    rigour: 2
  - id: rebecka-weegar-peter-idestam-almquist-2024-2
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Two attempted workload-reduction refinements—stopword-based question demoting and supplementing training data with answers labeled incorrect from other questions—did not improve classification results overall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i0` Stopword-based question demoting produced no improvement in classification results for this data set. [→ Rebecka Weegar · Peter Idestam-Almquist 2024](#rebecka-weegar-peter-idestam-almquist-2024)
`q2 i?` Adding answers from other questions labeled as incorrect to a question's training data improved a few questions but not overall. [→ Rebecka Weegar · Peter Idestam-Almquist 2024 (2)](#rebecka-weegar-peter-idestam-almquist-2024-2)

## Evidence

### Rebecka Weegar · Peter Idestam-Almquist 2024

Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1

`q2 · i0` · `design · r2`

Null result from the Other Results section: the authors evaluated stopword-based question demoting, a method introduced by Mohler et al. (2011) for removing question text from student answers, and observed no improvement in classification results.

> "We evaluated stop- word-based question demoting for our data set, but did not observe any improve- ment in the classification results."

### Rebecka Weegar · Peter Idestam-Almquist 2024 (2)

Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1

`q2 · i?` · `design · r2`

Null result from the Other Results section: supplementing the training data for one question with answers to other questions labeled as incorrect helped a few questions but not overall.

> "This approach did improve classification results for a few questions but did not improve classification results overall."

## Discussion


## Related Claims
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](random-forest-slightly-better-for-answer-classification.md) — related
