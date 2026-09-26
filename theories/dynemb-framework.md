---
type: theory
title: "DynEmb: a hybrid knowledge tracing framework combining static matrix-factorization question embeddings with an RNN that tracks dynamic student knowledge states"
description: "DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
---

# DynEmb: a hybrid knowledge tracing framework combining static matrix-factorization question embeddings with an RNN that tracks dynamic student knowledge states

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study, `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question interactions, and StudentDyn, an RNN (an LSTM by default) whose hidden state serves as a dynamic student embedding. The predicted probability of a correct response combines the question embedding and the dynamic student embedding through an inner product with a per-question bias and sigmoid activation. The article argues this hybrid "can harness the advantages from both static and sequential models in a way that outperforms both", and that the framework is flexible, accommodating various sequential models and optional tag or other feature information.

## Design Implications

### Context
#### Requirements
- A sequence of student-question-response interactions from an ensemble of students; the question embedding must be pretrained and held fixed while training the sequential component.
#### Constraints
- The paper focuses mainly on binary correct/incorrect responses, though the framework is stated to extend to numerical scores; online deployment requires additional algorithmic improvement.

### Target Learners
- students interacting with computer-based learning systems and intelligent tutoring systems

### Target Learning Objectives
- estimating and tracking student knowledge or proficiency over time to enable personalized learning

### Claims
- [Dynemb Outperforms Dkt And Bmf Baselines](../claims/dynemb-outperforms-dkt-and-bmf-baselines.md) [+M]
- [Dynemb Tracks Knowledge Without Skill Tags](../claims/dynemb-tracks-knowledge-without-skill-tags.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org
