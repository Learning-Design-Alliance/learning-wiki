---
type: strategy
id: scenario-guided-conversation-level-ai-tutor-evaluation
title: Scenario-guided, conversation-level expert evaluation of AI tutors in three stages
description: "The report describes a reusable evaluation strategy: curate a bank of 49 structured learning scenarios specifying subject, setting, learning goal, grounding material, learner persona, conversation plan, initial query,..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: learnlm-team-2024
    resource: "https://arxiv.org/abs/2412.16429"
    title: "LearnLM Team, Google. (2024). LearnLM: Improving Gemini for Learning. arXiv. https://arxiv.org/abs/2412.16429"
    author: LearnLM Team, Google
---

# Scenario-guided, conversation-level expert evaluation of AI tutors in three stages

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The report describes a reusable evaluation strategy: curate a bank of 49 structured learning scenarios specifying subject, setting, learning goal, grounding material, learner persona, conversation plan, initial query, and system instructions; have educators role-play learners in paired conversations with two unlabeled systems (minimum 10 turns); then have separate pedagogy experts assess transcripts and comparative preference. The authors argue "scenario-based approaches support relatively repeatable, controlled comparisons of the capabilities of different conversational AI systems" and help ensure evaluation coverage across diverse use cases.

## Design Implications

### Context
#### Requirements
- Scenarios must be ecologically representative and cover diverse learning goals, personas, and subject areas; without scenarios, unconstrained human-AI interactions lead to meandering conversations that offer a poor basis for comparison.
#### Constraints
- Role-playing experts are imperfect proxies for students, providing only preliminary insight into user experience; the design measures intrinsic pedagogy quality, not learning outcomes.

### Target Learners
- role-played learners spanning classroom students and independent EdTech users

### Target Learning Goals
- comparative assessment of pedagogical quality of conversational AI tutors across subjects and learning goals

## Claims

- [Role-playing learners report weaker experiences with GPT-4o than with LearnLM, Gemini 1.5 Pro, and Claude 3.5 Sonnet](../claims/learnlm-roleplayer-weaker-gpt4o-experience.md) [~W]

## Related Strategies

- [Use simulated student profiles (expected path, struggling learner, off-topic input) as test scenarios for AI tutor QA](simulated-student-profile-test-scenarios.md)
- [Evaluate chatbot-based digital tutors in real field settings rather than only laboratory experiments](field-evaluation-of-digital-tutors.md)

## Examples
-

## Key Sources
- LearnLM Team, Google. (2024). LearnLM: Improving Gemini for Learning. arXiv. https://arxiv.org/abs/2412.16429
