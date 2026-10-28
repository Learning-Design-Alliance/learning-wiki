---
type: product
id: self-labelling-tutoring-tool-dataset-7-students-40-fractionarithmetic-tasks-280-self-label
title: "Self-labelling tutoring tool dataset: 7 students, 40 fraction/arithmetic tasks, 280 self-labelled tasks with log-file recording"
description: A dataset created by Ruth Janning et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Self-labelling tutoring tool dataset: 7 students, 40 fraction/arithmetic tasks, 280 self-labelled tasks with log-file recording

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
A dataset created by Ruth Janning et al. containing timestamped interaction logs and student self-labels of perceived difficulty from 280 fraction and arithmetic practice tasks.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Self-labelling tutoring tool dataset: 7 students, 40 fraction/arithmetic tasks, 280 self-labelled tasks with log-file recording**: A dataset from a study in which "7 students in the age of 21 – 28 each had to solve 40 mathematical tasks and to label at the end of a task the perceived task-difficulty themselves by means of the small offline self-labelling tutoring java tool". "Each of the 7 students has seen all 40 tasks resulting in 280 labelled tasks", distributed as 40 too hard, 20 hard, 93 appropriate, 121 easy and 6 too easy. The tool is a drill-and-practice math system that does not model student knowledge but provides only the log-file data and labels; every action was written with a time stamp into a log file. (Ruth Janning et al. (2016))

### Claims

- [Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.](../claims/single-per-task-features-weak-fit.md) [+W]
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](../claims/svm-best-single-classifier-task-difficulty.md) [+W]
- [A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session.](../claims/log-feature-combination-significant-accumulated-difficulty.md) [+W]
- [Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking](../claims/plait-ensemble-outperforms-single-and-standard-ensembles.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9
