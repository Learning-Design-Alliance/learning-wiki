---
type: design
id: transparency-framework-explainable-ai-simulation-training
title: Transparency framework for explainable artificial intelligence in simulation-based training
description: The article introduces a framework in which a simulated task generates raw data, metrics of performance are created and selected for their ability to differentiate groups, and a machine learning algorithm is trained a...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: mirchi-n-2020
    resource: "https://doi.org/10.1371/journal.pone.0229596"
    title: "Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596"
    author: Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF
---

# Transparency framework for explainable artificial intelligence in simulation-based training

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article introduces a framework in which a simulated task generates raw data, metrics of performance are created and selected for their ability to differentiate groups, and a machine learning algorithm is trained and tested to build an educational feedback platform. New users' normalized metrics yield both a group classification and "an individual breakdown of metric performance", so the learner sees how each metric contributes to the model's decision. The framework is presented as flexible: it "can be employed to teach any form of complex task where a multivariate dataset can be obtained from experts and non-experts".

## Design Implications

### Context
#### Requirements
- A labelled dataset containing a relatively large number of users, normalized metrics, and a trained predictive model whose weights can be exposed to the learner
#### Constraints
- The validated implementation uses a linear SVM distinguishing only two groups of expertise; the model bias is a weight without a corresponding metric and is left out of metric-wise assessment

### Target Learners
- Surgical and medical trainees (residents, fellows, medical students)

### Learning Goals
- Complex psychomotor technical skills, e.g. neurosurgical tumor resection

### Claims
- [Svm Classifies Skilled Novice Vr Neurosurgery 92 Accuracy](../claims/svm-classifies-skilled-novice-vr-neurosurgery-92-accuracy.md) [+M]
- [Four Metrics Selected From 270 Negative Weights](../claims/four-metrics-selected-from-270-negative-weights.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596
