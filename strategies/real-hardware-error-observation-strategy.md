---
type: strategy
id: real-hardware-error-observation-strategy
title: Use real-hardware experiment results that deviate from theory to motivate a discussion of quantum error correction
description: "Because experiments run on real quantum hardware, \"students could easily observe that the results of the experiments differ from the theoretical predictions, as shown in Figure 6.\" The strategy turns this observation..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: qihong-sun-2024
    resource: "https://arxiv.org/abs/2403.17485"
    title: "Qihong Sun, Shuangxiang Zhou, Ronghang Chen, Guanru Feng, Shi-Yao Hou, and Bei Zeng. (2024). From Computing to Quantum Mechanics: Accessible and Hands-On Quantum Computing Education for High School Students. arXiv:2403.17485. https://arxiv.org/abs/2403.17485"
    author: Qihong Sun, Shuangxiang Zhou, Ronghang Chen, Guanru Feng, Shi-Yao Hou, and Bei Zeng
---

# Use real-hardware experiment results that deviate from theory to motivate a discussion of quantum error correction

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Because experiments run on real quantum hardware, "students could easily observe that the results of the experiments differ from the theoretical predictions, as shown in Figure 6." The strategy turns this observation into a teaching moment: the article states errors "can occur in quantum computing, and to correct these errors, quantum error correction was invented". Informing students about errors and correction is presented as helping them "develop a better understanding of the subject matter".

## Design Implications

### Context
#### Requirements
- Experiments must be run on a real quantum computer so that deviations between experimental results and theoretical predictions are visible to students.
#### Constraints
- Detailed knowledge of quantum error correction is explicitly beyond the scope of the course; only an informational discussion is recommended.

### Target Learners
- high school students performing quantum computing experiments on real hardware

### Target Learning Goals
- understand that errors occur in quantum computing and that quantum error correction addresses them
- develop a better understanding of quantum computing through observation of real experimental results

## Claims

- [Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data](../claims/hardware-execution-did-not-eliminate-llm-assistance.md) [+W]
- [The article argues classical simulators are better suited than real quantum hardware for teaching, citing error rates, incomplete measurement output, and limited hardware access.](../claims/classical-simulators-preferred-for-teaching-quantum-computing.md) [-W]

## Related Strategies

- [Alternate pen-and-paper predictions with IBM Q runs so students test their own circuit calculations](predict-then-test-pen-paper-ibm-q.md)
- [Quantum hardware exploration assignments balancing authentic device access with simulator substitutes](quantum-hardware-exploration-assignments-strategy.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Use cloud-accessible quantum computing platforms so students run circuits on real quantum hardware](cloud-quantum-platforms-school-use.md)
- [Classroom discussion of statistical error versus hardware noise when simulating on quantum devices](statistics-versus-noise-classroom-discussion.md)

## Examples
-

## Key Sources
- Qihong Sun, Shuangxiang Zhou, Ronghang Chen, Guanru Feng, Shi-Yao Hou, and Bei Zeng. (2024). From Computing to Quantum Mechanics: Accessible and Hands-On Quantum Computing Education for High School Students. arXiv:2403.17485. https://arxiv.org/abs/2403.17485
