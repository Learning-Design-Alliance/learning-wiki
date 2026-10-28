---
type: theory
title: "Simulated student approach: using computational models of learning (Apprentice agents) to evaluate knowledge tracing online before classroom deployment"
description: "The article introduces \"a novel way of using machine-learning models to generate simulated students\" for evaluating knowledge tracing in online mastery learning settings."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: qiao-zhang-and-christopher-maclellan
    resource: "https://educationaldatamining.org/edm2021/"
    title: "Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/"
---

# Simulated student approach: using computational models of learning (Apprentice agents) to evaluate knowledge tracing online before classroom deployment

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
The article introduces "a novel way of using machine-learning models to generate simulated students" for evaluating knowledge tracing in online mastery learning settings. Unlike statistical predictive models, Apprentice agents "actually perform the task (not just predict performance)" and "do not require prior human data to operate." The authors ran 30 agents per condition in a fraction arithmetic tutor and argue the approach "provide[s] a practical means of evaluating knowledge tracing models prior to more costly classroom testing."

## Design Implications

### Context
#### Requirements
- Requires a computational model of learning that can perform the tutor task, such as the Apprentice Learner Architecture, plus a tutor environment to interact with
#### Constraints
- The authors note more work is needed to explore and generalize the parameter-initialization idea, and future work should test whether simulated students predict which approaches yield the best learning for human students

### Target Learners
- K-12 students learning fraction arithmetic in intelligent tutoring systems

### Target Learning Objectives
- Skill mastery estimation and problem selection in online knowledge tracing

### Claims

## Related Theories
- 

## Examples

- [Initialize BKT parameters from simulated student data when no human data is available](../strategies/initialize-bkt-parameters-from-simulated-data.md)
- [Use data-grounded simulation as a pre-deployment close-the-loop tool for ITS design decisions](../strategies/simulation-close-the-loop-its-redesign.md)
- [Simulation-based pre-validation of adaptive coaching systems before classroom deployment](../strategies/simulation-prevalidation-before-classroom-deployment.md)
- [Test an apprentice learner agent on previously unseen problems to determine when it has correctly learned target skills](../strategies/test-agent-on-unseen-problems.md)

## Key Sources
- Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/
