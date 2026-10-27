---
type: strategy
id: per-exam-validation-via-difficult-samples
title: Validate the autograder on each exam by leveraging the difficult samples a teacher must grade anyway
description: The article recommends a per-usage validation mechanism rather than relying on average performance over large datasets.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: johannes-schneider-2023
    resource: "https://doi.org/10.1007/s40593-022-00289-z"
    title: "Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z"
    author: Johannes Schneider, Robin Richner, Micha Riser
---

# Validate the autograder on each exam by leveraging the difficult samples a teacher must grade anyway

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends a per-usage validation mechanism rather than relying on average performance over large datasets. "It relies on comparing the grading accuracy of a set of questions and answers that are manually and automatically graded": the teacher's marks on difficult samples, which require human grading regardless, serve as ground truth to estimate whether accuracy constraints hold on the autograded samples. The more negative the difference Δ between accuracy on difficult samples of the data to grade and of the validation data, the less the autograder should be trusted. A teacher can respond by raising the minimum accuracy thresholds.

## Design Implications

### Context
#### Requirements
- The teacher must manually grade the difficult samples within the uncertainty range
- The teacher's grading on difficult samples should contain few errors upon validation
#### Constraints
- The assumption linking difficult-sample accuracy to easy-sample accuracy is probabilistic, not guaranteed
- Correlation between deviations on difficult and easy samples is only weak
- Large deviations can stem from small dataset size or from the teacher's own grading errors

### Target Learners
- teachers and teaching assistants grading short free-text answers

### Target Learning Goals
- ensuring autograder accuracy on individual exams meets teacher-specified minimum accuracy constraints

### Affordances
- [Similarity Threshold Deferral Autograding Framework](../research-methods/confidence-aware-selective-automated-scoring-framework.md)

## Claims

- [Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation](../claims/per-exam-accuracy-fluctuates-validation-detects-deviations.md) [+W]
- [Deferring difficult question-answer pairs to humans raises grading accuracy, with 62% of samples classified at 92% accuracy](../claims/deferring-difficult-answers-raises-accuracy-92-percent.md) [+W]
- [Targeting zero false negatives and 98% accuracy leaves about a 10% teacher workload reduction with accuracy slightly above 98%](../claims/zero-false-negative-target-yields-10-percent-workload-reduction.md) [+W]
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](../claims/finetuned-labse-86-5-percent-autograding-accuracy.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Johannes Schneider, Robin Richner, Micha Riser. (2023). Towards Trustworthy AutoGrading of Short, Multi-lingual, Multi-type Answers. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00289-z
