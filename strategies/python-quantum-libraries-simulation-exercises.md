---
type: strategy
id: python-quantum-libraries-simulation-exercises
title: Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning
description: "Given the early maturity of quantum communications systems, the article recommends code libraries as \"a very useful resource to simulate or interact with quantum technologies\", supporting lecture-based examples and ex..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: alberto-sebastián-lombraña-2023
    resource: "https://arxiv.org/abs/2303.01251"
    title: "Alberto Sebastián-Lombraña, Laura Ortiz, Juan P. Brito, Jaime Sáez de Buruaga, Rafael J. Vicente, Ruben B. Mendez, Rafael Artiñano, Vicente Martín. (2023). Teaching quantum communications through a hands-on laboratory. https://arxiv.org/abs/2303.01251"
    author: Alberto Sebastián-Lombraña, Laura Ortiz, Juan P. Brito, Jaime Sáez de Buruaga, Rafael J. Vicente, Ruben B. Mendez, Rafael Artiñano, Vicente Martín
---

# Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (3 for, 1 mixed, 1 against) · 4 studies (4 design), `q1`–`q2` · 0 of 4 report an effect size · 5 claims rest on one study

## Description
Given the early maturity of quantum communications systems, the article recommends code libraries as "a very useful resource to simulate or interact with quantum technologies", supporting lecture-based examples and experiential resources such as collaborative activities or self-evaluation exercises. Python is highlighted because it is "a widespread language in academic domains and highly probable to be known by a technical audience" and is cross-platform.

## Design Implications

### Context
#### Requirements
- Libraries with available resources around them and active communities that generate enough support
- Selection of exercises or libraries depends on the intention, such as whether they are a means of evaluation or promoting adoption
#### Constraints
- Demonstrations and simulations are commonly based on cryptographic applications of quantum communications, due to the high degree of maturity of techniques such as QKD

### Target Learners
- technical audience students
- engineering profiles

### Target Learning Goals
- first-hand experience of new quantum features
- developing students' own designs adapted to their specific domain

## Claims

- [Student feedback on the Quantum Communications Lab workshop was assessed as very positive, with attendees of diverse profiles showing interest in different fundamentals of quantum communication](../claims/quantum-comm-lab-positive-student-feedback.md) [+W]
- [Qiskit-based exercises agree with theoretical predictions and support introducing quantum computing to undergraduates](../claims/qiskit-agrees-with-theory-classroom-effectiveness.md) [+W]
- [Module 3 code execution success dropped to approximately 60% before a missing-dependency infrastructure fix, recovering to match the 86–87% rates of Modules 1 and 2](../claims/itas-module3-success-rate-infrastructure-fix.md) [~W]
- [Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data](../claims/hardware-execution-did-not-eliminate-llm-assistance.md) [-W]
- [In archived sessions, no operator code changes or quantum-logic corrections were needed; eight of nine notebook executions only required one permitted fix of a missing visualization dependency](../claims/archived-qiskit-sessions-needed-only-environment-fixes.md) [+W]

## Related Strategies

- Quantum Communications Lab Infieri Workshop
- [Noise exploration assignments using a noise simulator to teach quantum noise concepts](noise-exploration-assignments-strategy.md)
- [Extend the quantum communication teaching approach to other technical profiles and explore other delivery formats](extend-quantum-teaching-other-profiles.md)
- [Task-based quantum programming notebooks that withhold support libraries so participants compute matrix operations by hand](task-based-quantum-programming-notebooks.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Pair traditional quantum computation lecture topics with hands-on activities on real quantum systems](pair-lectures-with-hands-on-quantum-activities.md)
- [Present interactive code in self-contained logical blocks with stable function definitions to shorten the hypothesis–experiment–result feedback loop](self-contained-interactive-code-blocks.md)
- [Use reactive notebooks integrating explanatory text and code to support engagement and exploration](reactive-notebooks-integrated-text-code-strategy.md)

## Examples
-

## Key Sources
- Alberto Sebastián-Lombraña, Laura Ortiz, Juan P. Brito, Jaime Sáez de Buruaga, Rafael J. Vicente, Ruben B. Mendez, Rafael Artiñano, Vicente Martín. (2023). Teaching quantum communications through a hands-on laboratory. https://arxiv.org/abs/2303.01251
