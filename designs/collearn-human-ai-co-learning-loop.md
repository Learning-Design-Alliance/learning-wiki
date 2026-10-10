---
type: design
id: collearn-human-ai-co-learning-loop
title: "Human–AI co-learning loop: persistent learner-state memory, adaptive question generation, and a transparent evidence view"
description: "CoLearn operationalises the ideal tutor as a loop in which the learner practises while the agent refines a persistent memory of the learner's mastery and misconceptions."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: kailai-he-2026
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
---

# Human–AI co-learning loop: persistent learner-state memory, adaptive question generation, and a transparent evidence view

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CoLearn operationalises the ideal tutor as a loop in which the learner practises while the agent refines a persistent memory of the learner's mastery and misconceptions. It has "three components: (i) a persistent learner-state memory that updates per-topic mastery with a soft-evidence variant of Bayesian Knowledge Tracing, where a large language model acts as a continuous observation function", (ii) adaptive question generation targeting the weakest topic and recurring misconceptions, and (iii) an evidence view making personalisation visible and testable. Co-learning here is deliberately modest: the question strategy stays fixed while only the agent's memory adapts.

## Design Implications

### Context
#### Requirements
- A persistent per-(learner, subject) memory record so evidence accumulates across sessions rather than per-session logs
- An LLM grader emitting continuous mastery_evidence and evidence_strength values in [0,1] as the observation function
#### Constraints
- The strategy guideline is a fixed text consulted on every generation; automatic revision from accumulated outcomes is planned but not yet implemented
- A rising mastery estimate is evidence that the agent's belief has changed, not proof that the learner has mastered the skill

### Target Learners
- secondary-school science learners (evaluated on Biology and Chemistry curricula)

### Learning Goals
- topic-level mastery diagnosis
- misconception identification and remediation through targeted practice

### Claims
- [Collearn Ab Personalised Question Preference](../claims/collearn-ab-personalised-question-preference.md) [+M]
- [Collearn Adaptive Mastery Mae Convergence](../claims/collearn-adaptive-mastery-mae-convergence.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154
