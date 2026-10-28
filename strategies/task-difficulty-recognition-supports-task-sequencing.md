---
type: strategy
id: task-difficulty-recognition-supports-task-sequencing
title: "Use perceived task-difficulty recognition output in three ways to support Vygotsky-based task sequencing: personalised adaptive threshold, threshold correction, and misconception detection"
description: The authors propose feeding perceived task-difficulty recognition into the Schatten and Schmidt-Thieme (2014) task sequencer, which uses matrix-factorization performance prediction and a Vygotsky Policy to keep studen...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: ruth-janning-2016
    resource: "https://doi.org/10.1007/s40593-016-0097-9"
    title: "Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9"
    author: Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme
---

# Use perceived task-difficulty recognition output in three ways to support Vygotsky-based task sequencing: personalised adaptive threshold, threshold correction, and misconception detection

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors propose feeding perceived task-difficulty recognition into the Schatten and Schmidt-Thieme (2014) task sequencer, which uses matrix-factorization performance prediction and a Vygotsky Policy to keep students in the Zone of Proximal Development. "We aim to support this approach by perceived task-difficulty recognition in three different ways: • providing a personalised and adaptive threshold for the Vygotsky Policy, • correcting the Vygotsky Policy threshold value, • detecting misconceptions." The personalised threshold is computed from the average performance of the k most similar students when they felt appropriately challenged, optionally including the considered student's own averages.

## Design Implications

### Context
#### Requirements
- A performance-prediction sequencer with a Vygotsky Policy threshold; identification of students with similar task performance, e.g., by k-Nearest-Neighbour; perceived task-difficulty recognition running on log-file features.
#### Constraints
- These are proposals for future integration, not yet evaluated: the article states "Future steps will be to integrate the presented perceived task-difficulty recognition into an intelligent tutoring system and evaluate the proposed approaches".

### Target Learners
- students using adaptive intelligent tutoring systems for mathematics

### Target Learning Goals
- keeping students within their Zone of Proximal Development; neither boring nor frustrating them; detecting misconceptions

## Claims

- [A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session.](../claims/log-feature-combination-significant-accumulated-difficulty.md) [+W]
- [Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking](../claims/plait-ensemble-outperforms-single-and-standard-ensembles.md) [+W]
- [Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.](../claims/single-per-task-features-weak-fit.md) [~W]
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](../claims/svm-best-single-classifier-task-difficulty.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9
