---
type: claim
title: "Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy"
description: "Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy"
id: deferring-difficult-answers-raises-accuracy-92-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
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

# Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When samples near the similarity threshold are excluded from autograding and graded manually, accuracy on autograded samples rises above the single-threshold accuracy. [→ Johannes Schneider 2023](#johannes-schneider-2023)

## Evidence

### Johannes Schneider 2023

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Numerical evaluation on test data using teacher-specified minimum accuracy constraints C_i min and C_c min to derive thresholds T_i and T_c. With these constraints, "62% of all samples are classified" at "accuracy of classified samples is 92%". The article also reports for C_c min of 0.9 about 49% of samples get classified, and for accuracy C_i min of 95% only 13%.

> "Overall, 62% of all samples are classified and the over - all accuracy of classified samples is 92%."

## Discussion


## Related Claims
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](finetuned-labse-86-5-percent-autograding-accuracy.md) — related
- [Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation](per-exam-accuracy-fluctuates-validation-detects-deviations.md) — related
- [Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%](zero-false-negative-target-yields-10-percent-workload-reduction.md) — related
- [Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages](numeric-answers-most-accurate-language-variation-under-8.md) — related
