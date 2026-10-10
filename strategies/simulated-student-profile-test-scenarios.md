---
type: strategy
id: simulated-student-profile-test-scenarios
title: Use simulated student profiles (expected path, struggling learner, off-topic input) as test scenarios for AI tutor QA
description: "PromptDecipher directs teachers to a test environment consisting of \"a simulated student chat\" in which they \"select a student profile (e.g., 'expected path,' 'struggling learner,' 'off-topic input'), read the bot's r..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: miina-koyama-2026
    resource: "https://arxiv.org/abs/2605.16605"
    title: "Miina Koyama, Ruiwei Xiao, and John Stamper. (2026). PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions. https://arxiv.org/abs/2605.16605"
    author: Miina Koyama, Ruiwei Xiao, and John Stamper
---

# Use simulated student profiles (expected path, struggling learner, off-topic input) as test scenarios for AI tutor QA

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
PromptDecipher directs teachers to a test environment consisting of "a simulated student chat" in which they "select a student profile (e.g., 'expected path,' 'struggling learner,' 'off-topic input'), read the bot's response, and either mark it as passing or edit it to reflect the desired behavior." Each profile represents a distinct interaction scenario the bot must handle, giving teachers a concrete, low-effort way to probe bot behavior across learner types before publication.

## Design Implications

### Context
#### Requirements
- A bot under authoring and a set of selectable student profiles representing anticipated interaction scenarios
#### Constraints
- The article lists these profiles as examples; future work may include auto-generation of additional edge-case scenarios

### Target Learners
- teachers authoring AI tutors for K-12 and higher-education students

### Target Learning Goals
- evaluating AI tutor responses across expected, struggling, and off-topic student behaviors

## Related Strategies

- Publication Gated Qa Workflow
- [Future directions: auto-generate edge-case test scenarios and integrate learning-science guidance into AI tutor authoring](future-ai-tutor-authoring-edge-cases-and-learning-science-guidance.md)

## Examples
-

## Key Sources
- Miina Koyama, Ruiwei Xiao, and John Stamper. (2026). PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions. https://arxiv.org/abs/2605.16605
