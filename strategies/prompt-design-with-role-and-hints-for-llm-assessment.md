---
type: strategy
id: prompt-design-with-role-and-hints-for-llm-assessment
title: Achieve high-precision automated constructive assessment through prompt design alone—explicit role assignment plus human-scored hint examples—without fine-tuning
description: "The article's method achieves automated problem generation, scoring, and feedback \"solely through prompt design without retraining.\" Prompts assign a professional role (e.g., \"You are a professional grader of case met..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: satoshi-takahashi-2026
    resource: "https://arxiv.org/abs/2609.25790"
    title: "Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790"
    author: Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada
---

# Achieve high-precision automated constructive assessment through prompt design alone—explicit role assignment plus human-scored hint examples—without fine-tuning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's method achieves automated problem generation, scoring, and feedback "solely through prompt design without retraining." Prompts assign a professional role (e.g., "You are a professional grader of case methods"), state scoring criteria explicitly, and—critically—include multiple correct and incorrect example answers from human scoring. The hint examples stabilized GPT-4o's judgments to match human scoring, whereas criteria-only prompts produced unstable, over-interpreting behavior. Scoring was repeated nine times with majority vote for robustness.

## Design Implications

### Context
#### Requirements
- Explicit role assignment and clear task statements in prompts
- Human-scored example answers (hints) included in scoring prompts
- Repeated scoring with majority vote to ensure output consistency
#### Constraints
- Accuracy "heavily depends on the ingenuity of prompt design and output control"; the structural characteristics of HDR alone do not guarantee LLM performance
- The study used OpenAI's GPT-4o, which may differ in behavior from other LLMs; robustness across models requires future validation

### Target Learners
- Working adults in business-skills assessment

### Target Learning Goals
- Automated scoring and feedback on descriptive answers explaining knowledge misuse

### Affordances
- [Hierarchical Diagnostic Reasoning Hdr](../products/hierarchical-diagnostic-reasoning-hdr.md)

## Claims

- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](../claims/task-specific-prompt-beats-pedcot-prompting.md) [~W]

## Related Strategies

- [Automated assessment outputs must retain human monitoring and never serve as official grades or sole decision bases](human-monitoring-automated-assessment.md)
- [Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)](rubric-enhanced-llm-grading-prompt.md)

## Examples
-

## Key Sources
- Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790
