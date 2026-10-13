---
type: research-method
id: multi-turn-synthetic-dialogue-evaluation-protocol-for-ai-tutors
title: Multi-turn synthetic-dialogue evaluation protocol for AI tutors
description: A novel evaluation protocol in which a fine-tuned student model and a candidate tutor model generate synthetic multi-turn dialogues that are scored by conversational statistics and a reasoning LLM judge, with results aggregated.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# Multi-turn synthetic-dialogue evaluation protocol for AI tutors

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A novel evaluation protocol in which a fine-tuned student model and a candidate tutor model generate synthetic multi-turn dialogues that are scored by conversational statistics and a reasoning LLM judge, with results aggregated. The article introduces "a novel multi-turn evaluation protocol that combines a fine-tuned student model and a fine-tuned tutor model to generate a large number of synthetic dialogues." Each evaluation point corresponds to 100 simulated conversations (10 repetitions across 10 student models) to limit variability and ensure reproducibility.

## Accounts
<!-- How each source describes or uses the method -->
- **Multi-turn evaluation protocol combining a fine-tuned student model with single-shot LLM judging**: A novel evaluation protocol in which a fine-tuned student model and a candidate tutor model generate synthetic multi-turn dialogues that are scored by conversational statistics and a reasoning LLM judge, with results aggregated. The article introduces "a novel multi-turn evaluation protocol that combines a fine-tuned student model and a fine-tuned tutor model to generate a large number of synthetic dialogues." Each evaluation point corresponds to 100 simulated conversations (10 repetitions across 10 student models) to limit variability and ensure reproducibility. (Janos Perczel et al. (2025))

### Claims

- [The v2 synthetic generator was tuned for stricter trace-data realism with more incorrect code, retries, and longer dialogues](../claims/astra-v2-generator-stricter-realism.md) [+W]
- [Off-the-shelf LLM tutors are more verbose than human tutors, leaving students only 5-15% of talk time versus close to 30% in human tutoring](../claims/off-the-shelf-llms-verbose-low-student-talk-time.md) [+W]
- [A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models](../claims/fine-tuned-student-model-approximates-human-ai-dialogue.md) [+W]

## Related Research Methods

- [History-conditioned student simulation: two-component profile-generator-plus-simulator framework](history-conditioned-student-simulation-two-component-profile-generator-plus-simulator-fram.md)
- [Offline evaluation with calibrated LLM judges for tutoring behaviors](offline-evaluation-with-calibrated-llm-judges-for-tutoring-behaviors.md)

## Key Sources
- Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087
