---
type: design
id: joint-engineering-decision-campus-ai-tutor
title: Treat model choice, evidence selection, serving compatibility, and product design as a joint engineering decision when building a campus AI tutor
description: "The article argues that a tutoring system's quality cannot be improved by swapping one component in isolation: latency, memory, retrieval, and product surfaces interact."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-13
sources:
  - id: sidney-shapiro-and-joshua-lindemann-2026
    resource: "https://arxiv.org/abs/2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510"
    author: Sidney Shapiro and Joshua Lindemann
---

# Treat model choice, evidence selection, serving compatibility, and product design as a joint engineering decision when building a campus AI tutor

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article argues that a tutoring system's quality cannot be improved by swapping one component in isolation: latency, memory, retrieval, and product surfaces interact. As the abstract concludes, "The results support treating model choice, evidence selection, serving compatibility, and product design as a joint engineering decision." The bake-off held the retrieval stack fixed to make generator comparisons interpretable, and a separate experiment changed model and response contract together so its gains could not be attributed to scale alone.

## Design Implications

### Context
#### Requirements
- Keep the serving retrieval stack fixed during model comparisons so failures are traceable
- Promotion requires clearing a classroom speed gate plus a demonstrated quality improvement
#### Constraints
- The authors state they do not claim that 8B is universally optimal, and no controlled learning-outcome comparison is reported

### Target Learners
- undergraduate business education students

### Learning Goals
- grounded explanations of assigned course material
- reliable practice with course-scoped feedback

### Claims
- [Larger Generators Fail Classroom Speed Gate](../claims/larger-generators-fail-classroom-speed-gate.md) [+M]
- [Moe Candidate Mixed Fidelity Result](../claims/moe-candidate-mixed-fidelity-result.md) [+M]
- [Round2 Candidates Pass Speed Gate](../claims/round2-candidates-pass-speed-gate.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510
