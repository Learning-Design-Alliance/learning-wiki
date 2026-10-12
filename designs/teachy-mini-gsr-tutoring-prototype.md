---
type: design
id: teachy-mini-gsr-tutoring-prototype
title: "Teachy Mini: a knowledge-based generative social robot tutoring prototype on the Reachy Mini platform"
description: Teachy Mini is a generative social robot tutoring prototype built on the open-source Reachy Mini desktop platform, supporting spoken dialogue and head/antenna social cues via the OpenAI Realtime API.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: stephan-vonschallen-2026
    resource: "https://arxiv.org/abs/2607.22345"
    title: "Stephan Vonschallen, Karim Kaufmann, Dominique Oberle, Friederike Eyssel, Theresa Schmiedel. (2026). Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education. arXiv. https://arxiv.org/abs/2607.22345"
    author: Stephan Vonschallen, Karim Kaufmann, Dominique Oberle, Friederike Eyssel, Theresa Schmiedel
---

# Teachy Mini: a knowledge-based generative social robot tutoring prototype on the Reachy Mini platform

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
Teachy Mini is a generative social robot tutoring prototype built on the open-source Reachy Mini desktop platform, supporting spoken dialogue and head/antenna social cues via the OpenAI Realtime API. The authors "usedthreemainmethodstoprovidetherobotwiththerequiredknowledge:Dynamic system prompting, retrieval-augmented generation, andstateful prompt orchestration". It personalizes through a seven-question onboarding profile, retrieves uploaded PDF lecture slides for grounded explanations, detects conversational states (frustration, confusion, requests for depth) via regex, and injects state-specific instructions such as rephrasing explanations with a concrete analogy. Implementation code is on GitHub and materials on researchbox.org (ID: #8129).

## Design Implications

### Context
#### Requirements
- Requires an external knowledge source for RAG grounding, an onboarding conversation to build the learner profile, and predefined verbal patterns for state detection.
#### Constraints
- Designed as an experimental single-session implementation, not a fully deployable educational system; learning progress was only partly accounted for and only the study-buddy role profile was evaluated.

### Target Learners
- university students and recent graduates in single-session tutoring interactions

### Learning Goals
- learning lecture content (research methodologies) through slide-grounded explanation, Socratic questioning, and personalized scaffolding

### Claims
- [Kbd Robot Perceived More Responsible Tutoring Behavior](../claims/kbd-robot-perceived-more-responsible-tutoring-behavior.md) [+M]
- [Kbd Manipulation Check Behavioral Differences Transcripts](../claims/kbd-manipulation-check-behavioral-differences-transcripts.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Stephan Vonschallen, Karim Kaufmann, Dominique Oberle, Friederike Eyssel, Theresa Schmiedel. (2026). Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education. arXiv. https://arxiv.org/abs/2607.22345
