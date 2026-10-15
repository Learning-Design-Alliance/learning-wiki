---
type: design
id: special-r1-framework
title: "Special-R1: disability-aware pedagogical RL coupling a two-dimensional adaptive prompt with a persona-aware Thinking Reward"
description: Special-R1 is a framework extending pedagogical multi-turn RL to special education.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: unggi-lee-2026
    resource: "https://arxiv.org/abs/2605.30670"
    title: "Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670"
    author: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
---

# Special-R1: disability-aware pedagogical RL coupling a two-dimensional adaptive prompt with a persona-aware Thinking Reward

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Special-R1 is a framework extending pedagogical multi-turn RL to special education. It factors pedagogical support into two orthogonal dimensions: a support level (amount) mapped from the learner's baseline accuracy to Maximum, Moderate, or Minimum support following the I-Do / We-Do / You-Do progression, and a support style (manner) drawn from the learner's disability profile, so that "thewhatcomes from the support level, thehowcomes from the disability profile." Its second component is a persona-aware Thinking Reward whose judge is prompted with the learner's disability profile and scores whether the thinking trace reflects disability-appropriate reasoning, which the authors describe as "the first reward we are aware of that explicitly scoresdisability-appropriatereasoning."

## Design Implications

### Context
#### Requirements
- Requires a pre-measured baseline accuracy of the student simulator on the given problem type to select the support level, and a structured disability rubric with learning characteristics, communication patterns, and recommended tutor strategies.
#### Constraints
- Every student in the framework is a disability-conditioned LLM simulator; improvements on judge-based metrics have not been validated with real learners with disabilities.
- Experiments use 7-8B tutors; behavior at larger scales remains to be studied.

### Target Learners
- Learners with disabilities across five profiles: intellectual disability, specific learning disability, autism spectrum disorder, ADHD, and emotional/behavioral disorder

### Learning Goals
- Multi-domain tutoring covering mathematics, reading comprehension, social reasoning, and life skills

### Claims
- [Special R1 Raises Persona Fit And Sped Helpfulness](../claims/special-r1-raises-persona-fit-and-sped-helpfulness.md) [+M]
- [Thinking Reward Effective Only With Adaptive Prompting](../claims/thinking-reward-effective-only-with-adaptive-prompting.md) [+M]
- [Sped Adaptive Shifts Tutor Behavior Codebooks](../claims/sped-adaptive-shifts-tutor-behavior-codebooks.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670
