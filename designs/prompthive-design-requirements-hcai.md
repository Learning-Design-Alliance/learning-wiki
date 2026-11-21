---
type: design
id: prompthive-design-requirements-hcai
title: Six design requirements for expert-driven prompt-authoring interfaces grounded in the Human-Centered AI framework
description: "The authors derive one overarching requirement and five supporting requirements for integrating subject matter expertise into prompt engineering: Control (R0), Integration (R1), Simplicity (R2), Trust (R3), Iteration..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: mohi-reza-2024
    resource: "https://arxiv.org/abs/2410.16547"
    title: "Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2024). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. https://arxiv.org/abs/2410.16547"
    author: Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos
---

# Six design requirements for expert-driven prompt-authoring interfaces grounded in the Human-Centered AI framework

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies (1 associational, 1 qualitative), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors derive one overarching requirement and five supporting requirements for integrating subject matter expertise into prompt engineering: Control (R0), Integration (R1), Simplicity (R2), Trust (R3), Iteration (R4), and Collaboration (R5). They adopt Shneiderman's two-dimensional Human-Centered AI framework rather than a unidimensional automation spectrum, aiming to "automate the content generation process as much as possible without diminishing SMEs' sense of control". Each requirement maps to concrete interface features: randomization buttons for iteration, the shared library for collaboration, and evaluation tools for trust.

## Design Implications

### Context
#### Requirements
- Interface support must scaffold prompt writing to minimize the high metacognitive demands of prompting
- Experimentation on multiple prompt variations is required because LLM outputs are inherently unpredictable
#### Constraints
- Derived from the OATutor expert workflow and validated with math experts authoring hints; the article does not claim the requirements generalize to all domains

### Target Learners
- subject matter experts without AI specialization

### Learning Goals
- effective, expert-guided prompt engineering for educational content generation

### Claims

- [Experts Perceived Consistency And Control](../claims/experts-perceived-consistency-and-control.md) [+M]
- [Attachment to LLMs exhibits cruel optimism: desired efficiency collides with the vigilance and expertise students do not yet possess](../claims/cruel-optimism-of-llms-in-education.md) [-W]

## Related Designs

- [A design-oriented pedagogical framework for integrating LLMs to scaffold critical thinking in higher education](llm-critical-thinking-pedagogical-framework.md)
- [Instructional Model for Human-Centered Generative AI Engagement: five recursive phases for LLM-integrated learning](instructional-model-human-centered-generative-ai-engagement.md)

## Examples
-

## Key Sources
- Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2024). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. https://arxiv.org/abs/2410.16547
