---
type: design
id: hitl-student-feedback-framework
title: Human-in-the-Loop framework centering student feedback as a generative signal for AI adaptation
description: "The framework positions students as active contributors who \"critique and modify AI responses using predefined feedback tags\", transforming passive consumption into an interactive feedback-driven loop."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: bhavishya-tarun-2025
    resource: "https://arxiv.org/abs/2508.11062"
    title: "Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. https://arxiv.org/abs/2508.11062"
    author: Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer
---

# Human-in-the-Loop framework centering student feedback as a generative signal for AI adaptation

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework positions students as active contributors who "critique and modify AI responses using predefined feedback tags", transforming passive consumption into an interactive feedback-driven loop. Structured tags serve both evaluation and as "a generative signal", combined with RAG to "personalize content iteratively and responsively". The system aims to promote student agency, iterative learning, and scalable personalization in STEM education.

## Design Implications

### Context
#### Requirements
- Students must engage with feedback tagging; the system uses "a tagging technique and prompt engineering to personalize content"
#### Constraints
- Live feedback was used sparingly (about 9.5% of turns), and the five-tag end-of-turn schema "may lack the granularity and immediacy needed to meaningfully steer the model’s next output"

### Target Learners
- STEM students learning Object-Oriented Design

### Learning Goals
- Deeper cognitive engagement
- self-regulated learning
- critical evaluation of AI-generated content

### Claims
- [Live Feedback Tags Modest Gains](../claims/live-feedback-tags-modest-gains.md) [+M]
- [Static Onboarding Metadata Highest Adaptability](../claims/static-onboarding-metadata-highest-adaptability.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. https://arxiv.org/abs/2508.11062
