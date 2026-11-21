---
type: design
id: uncertainty-threshold-supervisor-intervention-architecture
title: Uncertainty-based human-in-the-loop dialogue architecture in which a supervisor intervenes when model uncertainty thresholds are met
description: "The paper's conversational agent couples NLP modules (dialogue act classification, entity recognition, turn-taking) with an uncertainty quantification layer using Active Dropout."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: debajyoti-datta-2021
    resource: "https://arxiv.org/abs/2112.00985"
    title: "Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). https://arxiv.org/abs/2112.00985"
    author: Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown
---

# Uncertainty-based human-in-the-loop dialogue architecture in which a supervisor intervenes when model uncertainty thresholds are met

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The paper's conversational agent couples NLP modules (dialogue act classification, entity recognition, turn-taking) with an uncertainty quantification layer using Active Dropout. Each module has a threshold, and "If the uncertainty module gets triggered by the threshold, the supervisor intervenes and states the system's limitations or answers the question if it was because of a failure of one of the components." The expert user types the response as a student through a Supervisor Interface, which "prevents conversations from breaking because of the failure of ML pipelines and dialogue system components." The same interventions double as a mechanism for collecting additional training data during deployment.

## Design Implications

### Context
#### Requirements
- Requires expert supervisors available to respond when uncertainty thresholds are triggered
- Requires module-specific uncertainty thresholds to be set for the dialogue act, entity recognition and turn-taking modules
#### Constraints
- Evaluated only in a text-based mathematical questioning scenario about scale factor; the authors state they plan to incorporate other modalities like speech in the future

### Target Learners
- Pre-service teachers in teacher education programs

### Learning Goals
- Mathematical question-asking strategies
- Conducting mathematical discussion using visual aids such as an interactive widget on scale factor

### Claims
- [Eight User Evaluation Utterance Routing](../claims/eight-user-evaluation-utterance-routing.md) [+M]

## Related Designs

- [Three-module speech-to-sign-language translation architecture with a rule-based translation core](speech-to-sign-translation-three-module-architecture.md)

## Examples
-

## Key Sources
- Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). https://arxiv.org/abs/2112.00985
