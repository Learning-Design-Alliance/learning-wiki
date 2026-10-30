---
type: claim
title: "Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%"
description: "Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%"
id: zero-false-negative-target-yields-10-percent-workload-reduction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: johannes-schneider-2023
    resource: "https://doi.org/10.1007/s40593-022-00289-z"
    title: "Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z"
    author: Johannes Schneider, Robin Richner, Micha Riser
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Setting a maximum false-negative rate of 0% and minimum accuracy of 98% still allows the autograder to grade slightly above 10% of answers at accuracy slightly above 98%. [→ Johannes Schneider 2023](#johannes-schneider-2023)

## Evidence

### Johannes Schneider 2023

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Numerical evaluation on test data simulating a teaching-assistant accuracy level, using thresholds derived from the accuracy constraint. The article reports "a possible workload reduction of slightly above 10% and overall accuracy of slightly above 98%" under these constraints.

> "If we use C c min = 0.98 and we do not allow the autograder to fail any students, we get a possible workload reduction of slightly above 10% and overall accuracy of slightly above 98%."

## Discussion


## Related Claims
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](deferring-difficult-answers-raises-accuracy-92-percent.md) — related
- [Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages](numeric-answers-most-accurate-language-variation-under-8.md) — related
- [Two attempted workload-reduction refinements—stopword-based question demoting and supplementing training data with answers labeled incorrect from other questions—did not improve classification results overall](question-demotion-and-cross-question-training-data-null-results.md) — related
