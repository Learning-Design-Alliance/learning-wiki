---
type: strategy
id: synthetic-error-datasets-for-tutors-teachable-agents-teacher-pd
title: Use synthetic LLM-generated error datasets for AI tutors, teachable agents, and teacher professional development
description: "The article recommends three deployments of large-scale synthetic error datasets: training and evaluating automated tutoring systems so they can \"better diagnose and provide feedback on diverse, realistic student misc..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: ali-keramati-2026
    resource: "https://arxiv.org/abs/2606.14113"
    title: "Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113"
    author: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
---

# Use synthetic LLM-generated error datasets for AI tutors, teachable agents, and teacher professional development

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends three deployments of large-scale synthetic error datasets: training and evaluating automated tutoring systems so they can "better diagnose and provide feedback on diverse, realistic student misconceptions" without being constrained by limited human data; integrating generated errors into teachable agent environments where learners diagnose and correct mistakes made by an AI proxy, fostering vicarious learning and metacognitive debugging; and curating subsets of LLM-generated errors for teacher professional development so teachers practice formulating pedagogical responses before instruction.

## Design Implications

### Context
#### Requirements
- Curated subsets are needed for teacher professional development, since manually reviewing thousands of synthetic snippets is impractical
#### Constraints
- The diversity-fidelity trade-off means synthetic errors may diverge from authentic learner misconceptions, especially on higher-struggling tasks

### Target Learners
- introductory Java programming students
- novice educators and teachers

### Target Learning Goals
- diagnosing and giving feedback on student misconceptions
- metacognitive debugging skills through vicarious learning

### Affordances
- [Diversity Alignment Tradeoff Llm Error Simulation](../research-methods/multi-dimensional-fidelity-framework-for-llm-student-simulation.md)

## Related Strategies

- [Use knowledge distillation with deliberately limited synthetic data to expand scarce labeled evaluation datasets](limited-distillation-for-scarce-evaluation-labels.md)
- [Use unlearning-based simulated students as scalable practice environments for teacher professional development](unlearning-simulation-teacher-professional-development.md)
- [Use MEDS as baseline data for fine-tuning and moderation of AI mathematics tutoring content](use-meds-for-tutor-calibration-and-moderation.md)
- [Error-injection exercises: diagnosing subtly wrong simulations as graded practice](error-injection-diagnosis-exercises.md)

## Examples
-

## Key Sources
- Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113
