---
type: strategy
id: multiagent-vp-alternative-to-standardized-patients
title: Use multiagent virtual patient frameworks as scalable, customizable alternatives to standardized patients in clinical communication training
description: "The article recommends multiagent virtual patient (VP) frameworks as a \"customizable and scalable solution for medical communication training, without compromising patient confidentiality\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: qu-yufei-2026
    resource: "https://doi.org/10.2196/84747"
    title: "Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747"
    author: Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong
---

# Use multiagent virtual patient frameworks as scalable, customizable alternatives to standardized patients in clinical communication training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (6 for, 2 against) · 2 studies (1 quant-synthesis, 1 design), `q2` · 0 of 2 report an effect size · 8 claims rest on one study

## Description
The article recommends multiagent virtual patient (VP) frameworks as a "customizable and scalable solution for medical communication training, without compromising patient confidentiality". Teachers can specify patient attributes including age, personality, and communication barriers to generate customized VPs, addressing the high resource requirements, anxiety, and fatigue associated with SP-based training. The framework supports scalable simulation across multiple clinical departments.

## Design Implications

### Context
#### Requirements
- Requires clinical case reports, natural language queries, and instructional requirements from medical teachers as inputs
- Requires selection of an appropriate base LLM balancing response quality and latency
#### Constraints
- Limited discriminative power against leading questions requires further adaptation for authentic student interactions
- Pediatric case simulation requires role definition adjustments such as simulating a guardian

### Target Learners
- medical students

### Target Learning Goals
- clinical communication skills
- medical history taking
- physician-patient communication

### Affordances
- [Cerebral Cortex Inspired Multiagent Vp Framework](../products/meduai-sp.md)

## Claims

- [All methods achieved accuracy rates exceeding 94 percent on dental case dialogues](../claims/all-methods-accuracy-exceeding-94-percent.md) [+W]
- [DeepSeek-V3 and Qwen3-32B multiagent frameworks received full perceived educational utility scores from physicians](../claims/full-perceived-educational-utility-scores.md) [+W]
- [GPT-4o–based multiagent framework achieved the highest factual consistency score of 0.769](../claims/gpt4o-highest-factual-consistency-0-769.md) [+W]
- [Multiagent framework showed limited discriminative power against leading questions in low-quality inquiry analysis](../claims/limited-discriminative-power-leading-questions.md) [-W]
- [Multiagent framework demonstrated stable cross-specialty scalability with lower variability than single-LLM baseline](../claims/multiagent-stable-cross-specialty-scalability.md) [+W]
- [Qwen3-32B–based framework achieved the highest role-playing competency score of 39.67](../claims/qwen3-32b-highest-role-playing-score-39-67.md) [+W]
- [Qwen3-32B–based VP achieved approximately 3 s latency and highest multiturn engagement averaging 13 turns](../claims/qwen3-32b-latency-3s-13-turns.md) [+W]
- [Reported barriers to immersive and VP-based communication training include limited authenticity of non-verbal interaction, unrealistic student perceptions, high institutional resource requirements, technical challenges, and scalability constraints](../claims/vp-communication-implementation-barriers-authenticity-resources.md) [-W]

## Related Strategies

- [Deploy LLM-driven virtual patients for scalable, standardized deliberate practice of psychiatric interviews](llm-virtual-patients-scalable-deliberate-practice.md)
- [Use rubric-guided multiagent LLM simulation workflows for scalable, auditable psychotherapy practice and formative feedback](multiagent-llm-simulation-psychotherapy-training-strategy.md)
- [Position immersive technologies and virtual patients as supplementary components within blended learning rather than stand-alone replacements for established clinical communication training](immersive-tech-adjunctive-blended-not-replacement.md)
- [Use virtual patients to replace passive instruction and train clinical reasoning before bedside learning, without diminishing bedside teaching hours](vp-replace-passive-before-bedside-strategy.md)
- [Use blended learning—combining lectures, digital modules, and limited in-person simulation—as a scalable compromise for communication training](blended-learning-scalable-communication-training.md)
- [Deploy DeepSeek in medical education as a virtual mentor, PBL case tool, and adaptive question bank](deepseek-medical-education-integration-strategies.md)

## Examples
-

## Key Sources
- Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747
