---
type: claim
title: Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation
description: Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation
id: per-exam-accuracy-fluctuates-validation-detects-deviations
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

# Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Accuracy on small randomly chosen subsets DM deviates by a few percent from the large dataset, with large and non-constant variance, but the proposed validation procedure detects strong deviations. [→ Johannes Schneider 2023](#johannes-schneider-2023)
`q2 i?` Accuracy on difficult samples is lower and more variable than on easy samples, with a performance gap of more than 10%. [→ Johannes Schneider 2023 (2)](#johannes-schneider-2023-2)

## Evidence

### Johannes Schneider 2023

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Simulation-based evaluation drawing random 5% samples DM from test data DV, including a degraded autograder with 20% of correct predictions flipped. The article reports large, heteroscedastic variance on subsets and that strong deviations from expected accuracy can be reliably detected; accuracy was roughly normal per a Shapiro-Wilk test.

> "We observe large variance in accuracy for individual, randomly chosen subsets DM ⊂ DV for both easy and difficult samples."

### Johannes Schneider 2023 (2)

Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z

`q2 · i?` · `design · r2`

Numerical analysis on DV showing accuracy depends on distance from the threshold T*: "The (average) performance gap between the grading of easy and difficult samples is more than 10%", and the accuracy improves faster than linear when moving away from T*.

> "The (average) performance gap between the grading of easy and difficult samples is more than 10%, showing that difficult samples are harder to grade for the autograder."

## Discussion


## Related Claims
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](deferring-difficult-answers-raises-accuracy-92-percent.md) — related
- [Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages](numeric-answers-most-accurate-language-variation-under-8.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
