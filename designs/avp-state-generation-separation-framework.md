---
type: design
id: avp-state-generation-separation-framework
title: "Adaptive Virtual Patient framework: separating behavioral state transitions from language generation"
description: "The AVP framework inserts an explicit behavioral-state module between the trainee's turn and the virtual patient's reply: LLM evaluators score empathy and exploration each turn, a dynamics module accumulates the score..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: angela-chen-2026
    resource: "https://arxiv.org/abs/2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
---

# Adaptive Virtual Patient framework: separating behavioral state transitions from language generation

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The AVP framework inserts an explicit behavioral-state module between the trainee's turn and the virtual patient's reply: LLM evaluators score empathy and exploration each turn, a dynamics module accumulates the scores into an ordinal disclosure level (G/M/H) using weights derived from a psychotherapy-data SEM, and an LLM generates the next utterance conditioned on that level. The article argues that "Keeping the behavioral logic separate from generation makes the VP’s adaptation inspectable, controllable, and fixed across experimental conditions in a way a prompt-only system cannot achieve." The level determines what the patient may reveal; the LLM determines how they say it.

## Design Implications

### Context
#### Requirements
- Requires an external data-driven model of interaction dynamics (the SEM of Chen et al., 2026) to parameterize the state-update weights
- Requires validated skill detectors scoring user behaviors each turn
#### Constraints
- The dynamics module is parameterized from psychotherapy data and encodes assumptions specific to therapeutic communication; broader-domain claims are not yet validated
- The deployed 3:1 weight is an integer approximation, not an empirically optimized parameter

### Target Learners
- clinicians and clinical trainees practicing psychotherapy micro-skills

### Learning Goals
- empathic responding
- exploratory probing
- recognizing contingent patient disclosure

### Claims
- [Avp Climbing Disclosure Vs Static Flat](../claims/avp-climbing-disclosure-vs-static-flat.md) [+M]
- [Avp Faithful Realization Alignment](../claims/avp-faithful-realization-alignment.md) [+M]
- [Avp Weight Ablation Exploration Dominant](../claims/avp-weight-ablation-exploration-dominant.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051
