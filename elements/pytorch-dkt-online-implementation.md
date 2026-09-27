---
type: element
id: pytorch-dkt-online-implementation
title: Open-source PyTorch DKT implementation supporting online knowledge tracing with DataShop-format data
description: "The authors created their own DKT implementation using PyTorch's LSTM module to support online mastery learning."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: qiao-zhang-and-christopher-maclellan
    resource: "https://educationaldatamining.org/edm2021/"
    title: "Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/"
---

# Open-source PyTorch DKT implementation supporting online knowledge tracing with DataShop-format data

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 mixed) · 3 studies, `q2` · 0 of 3 report an effect size · 1 claim rests on one study

## Description
The authors created their own DKT implementation using PyTorch's LSTM module to support online mastery learning. Based on prior work, "the model has 200 nodes in the hidden layer, uses a dropout of 0.4 during training, and uses a batch size of 5." It "supports the ability to ﬁt DKT to data presented in standard DataShop format" and provides "a simple interface for use in online knowledge tracing settings." Open-source code is available at the authors' GitLab repository.

## Design Implications

### Context
#### Requirements
- Trained models require fitting to log data (here, data from simulated students in the Random condition) before online use
#### Constraints
- The article identifies a fundamental issue with DKT for mastery learning on multi-step problems that this implementation inherits

### Target Learners
- K-12 students learning fraction arithmetic

### Target Learning Goals
- Predicting student step correctness for mastery learning and problem selection

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression](../claims/dkt-long-term-information-and-faster-burn-in.md) [~M]
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](../claims/bkt-most-efficient-online-mastery-learning.md) [~M]

## Related Elements
- 

## Examples
-

## Key Sources
- Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/
