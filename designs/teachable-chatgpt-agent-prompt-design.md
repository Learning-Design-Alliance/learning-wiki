---
type: design
id: teachable-chatgpt-agent-prompt-design
title: Prompt-based teachable ChatGPT agent structured by a five-stage help-seeking model
description: The teachable ChatGPT agent is a prompt-based configuration of gpt-4 that role-plays a help-seeking student learning the eight queens puzzle.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: angxuan-chen-2024
    resource: "https://arxiv.org/abs/2412.15226"
    title: "Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226"
    author: Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang
---

# Prompt-based teachable ChatGPT agent structured by a five-stage help-seeking model

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The teachable ChatGPT agent is a prompt-based configuration of gpt-4 that role-plays a help-seeking student learning the eight queens puzzle. The authors "employed a prompt-based design approach that could modify the role of ChatGPT", structuring its responses around Gall's five-stage help-seeking process model, and deliberately "used the original ChatGPT without other augmented techniques" so that its mistakes resemble a beginner and create opportunities for students to teach.

## Design Implications

### Context
#### Requirements
- Learners first watch instructional videos covering the backtracking algorithm and the puzzle
- An online judging platform that automatically evaluates whether the generated code solves the puzzle
- Learners take an explicit teaching role, guiding the agent only in natural language
#### Constraints
- Accuracy of the agent's generated code was not controlled; the authors note ChatGPT may hallucinate wrong content without control

### Target Learners
- university students with a computer-science background and self-reported fundamental C++ coding ability

### Learning Goals
- knowledge of the backtracking algorithm and the eight queens puzzle
- C++ programming skill for solving the eight queens puzzle

### Claims
- [Chatgpt Teachable Agent Knowledge Gains](../claims/chatgpt-teachable-agent-knowledge-gains.md) [+M]
- [Chatgpt Teachable Agent No Correctness Gain](../claims/chatgpt-teachable-agent-no-correctness-gain.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226
