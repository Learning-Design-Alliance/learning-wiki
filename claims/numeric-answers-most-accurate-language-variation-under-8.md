---
type: claim
title: "Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages"
description: "Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages"
id: numeric-answers-most-accurate-language-variation-under-8
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
  - id: johannes-schneider-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00289-z"
    title: "Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z"
    author: Johannes Schneider, Robin Richner, Micha Riser
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Grading error rates for numeric answers are less than half those of other answer types. [→ Johannes Schneider 2023](#johannes-schneider-2023)
`q2 i?` Language-related differences in error rates tend to be less than 8% between the lowest and highest languages. [→ Johannes Schneider 2023 (2)](#johannes-schneider-2023-2)

## Evidence

### Johannes Schneider 2023

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Analysis of correctness depending on languages, answer length, question type and answers per question (Fig. 11). The article attributes this to limited semantic variation: "semantic variation in answers tends to be limited given a single number is expected".

> "Generally, grading is most accurate for numeric answers with error rates being less than half of other answer types."

### Johannes Schneider 2023 (2)

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Cross-language comparison in the data-characteristics analysis. The article cautions that drawing conclusions from language differences requires care since question types vary across languages, and it found no strong dependence on ground-truth length.

> "Overall differences tend to be less than 8% between the language with the lowest and highest error."

## Discussion


## Related Claims
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](finetuned-labse-86-5-percent-autograding-accuracy.md) — related
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](deferring-difficult-answers-raises-accuracy-92-percent.md) — related
- [Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation](per-exam-accuracy-fluctuates-validation-detects-deviations.md) — related
- [Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%](zero-false-negative-target-yields-10-percent-workload-reduction.md) — related
