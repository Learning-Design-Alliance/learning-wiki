---
type: research-method
id: self-reflective-llm-annotation-agent-with-iterative-criteria-refinement-and-short-term-mem
title: Self-reflective LLM annotation agent with iterative criteria refinement and short-term memory
description: An LLM-based agent that labels each discourse sample, then reflects to identify weaknesses in the current coding framework and applies revision actions (modify, add, delete, hold, merge) before labeling the next sample.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Self-reflective LLM annotation agent with iterative criteria refinement and short-term memory

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An LLM-based agent that labels each discourse sample, then reflects to identify weaknesses in the current coding framework and applies revision actions (modify, add, delete, hold, merge) before labeling the next sample. It "retained short-term memory of the three most recently labeled samples and the three most recent versions of the criteria", enabling progressive self-refinement beyond single-prompt labeling. In experiments the agents consistently chose only to modify existing levels, preserving the seven-level structure. Code is released at https://github.com/HanlingJ/human-icl-llm-agent.

## Accounts
<!-- How each source describes or uses the method -->
- **Self-reflective LLM annotation agent with iterative criteria refinement and short-term memory**: An LLM-based agent that labels each discourse sample, then reflects to identify weaknesses in the current coding framework and applies revision actions (modify, add, delete, hold, merge) before labeling the next sample. It "retained short-term memory of the three most recently labeled samples and the three most recent versions of the criteria", enabling progressive self-refinement beyond single-prompt labeling. In experiments the agents consistently chose only to modify existing levels, preserving the seven-level structure. Code is released at https://github.com/HanlingJ/human-icl-llm-agent. (Lan Anh Do et al. (2026))

### Claims
- [Agent-refined frameworks improved cross-model agreement but remained below the human-refined framework and varied across foundation models](../claims/agent-refined-frameworks-below-human-refined.md) [+M]

## Related Research Methods
-

## Key Sources
- Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas. (2026). Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents. https://arxiv.org/abs/2607.28651
