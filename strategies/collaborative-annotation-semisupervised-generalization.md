---
type: strategy
id: collaborative-annotation-semisupervised-generalization
title: Direct generalization efforts toward collaborative annotation and semi-supervised learning to reduce annotation time across new problems
description: "To make the measurement scheme usable on unseen problems without per-problem manual annotation, the article recommends that \"initial efforts to improve generalization across problems while reducing required annotation..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: lb0
    title: Lb0
---

# Direct generalization efforts toward collaborative annotation and semi-supervised learning to reduce annotation time across new problems

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
To make the measurement scheme usable on unseen problems without per-problem manual annotation, the article recommends that "initial efforts to improve generalization across problems while reducing required annotation time should be directed towards collaborative annotation as well as semi-supervised learning methods." This strategy addresses the current dependence on problem-specific training: the shared classifier heads already reduce scaling from linear in the number of problems to constant, and the authors hypothesize more labeled data across many additional problems could enable performance on unseen problem instances in introductory mechanics.

## Design Implications

### Context
#### Requirements
- Labeled training data across many additional problems beyond the current four
#### Constraints
- The article states the amount of data needed to generalize to unseen problems is unclear

### Target Learners
- college students in introductory mechanics courses

### Target Learning Goals
- scaling measurement of mechanistic sensemaking to new problems and larger studies

### Affordances
- [Ausem Seven Domain Sensemaking Scheme](../theories/mechanistic-reasoning.md)

## Claims

- [A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems](../claims/bert-finetuned-best-auroc-sensemaking.md) [+W]
- [Once trained, the ML models annotate student responses far faster than manual application of the measurement scheme (under 1 minute versus about 5 hours per ~100 responses for one problem)](../claims/ml-annotation-faster-than-manual-coding.md) [+W]
- [Classification performance varies across the seven sensemaking domains, and no AUROC could be reported for the properties domain because its positive examples were too rare](../claims/per-domain-auroc-varies-properties-undefined.md) [~W]
- [Machine-learning-supported grading with complete manual review of all classifier output reduced total exam grading time by 74% (or 64% under a conservative estimate) compared with fully manual grading](../claims/ml-supported-grading-cuts-exam-workload-64-74-percent.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Lb0
