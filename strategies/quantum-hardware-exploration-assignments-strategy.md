---
type: strategy
id: quantum-hardware-exploration-assignments-strategy
title: Quantum hardware exploration assignments balancing authentic device access with simulator substitutes
description: Hardware exploration assignments let students run programs on real quantum devices via Azure Quantum, which students find exciting, but the article notes devices are a scarce resource requiring advance planning, and t...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: mariia-mykhailova-2022
    resource: "https://arxiv.org/abs/2211.16347"
    title: "Mariia Mykhailova. (2022). Developing Programming Assignments for Teaching Quantum Computing and Quantum Programming. arXiv. https://arxiv.org/abs/2211.16347"
    author: Mariia Mykhailova
---

# Quantum hardware exploration assignments balancing authentic device access with simulator substitutes

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 mixed, 1 against) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Hardware exploration assignments let students run programs on real quantum devices via Azure Quantum, which students find exciting, but the article notes devices are a scarce resource requiring advance planning, and that much of the pedagogical value can be delivered by local or cloud simulators. Suggested tasks include comparing noiseless-simulator and real-device results, observing how the probability of a correct answer changes as problem size grows, and comparing device target profiles that restrict control flow.

## Design Implications

### Context
#### Requirements
- Students must plan their work ahead because quantum devices are a scarce resource and job results must return in time to complete the assignment
#### Constraints
- A lot of the pedagogical value of running programs on a quantum device can be delivered by local or cloud simulators

### Target Learners
- students in a general introductory quantum computing course

### Target Learning Goals
- understanding noise impacts on computation
- understanding size and control-flow limitations of quantum hardware

## Claims

- [The article argues classical simulators are better suited than real quantum hardware for teaching, citing error rates, incomplete measurement output, and limited hardware access.](../claims/classical-simulators-preferred-for-teaching-quantum-computing.md) [-W]
- [Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data](../claims/hardware-execution-did-not-eliminate-llm-assistance.md) [~W]

## Related Strategies

- [Noise exploration assignments using a noise simulator to teach quantum noise concepts](noise-exploration-assignments-strategy.md)
- [Alternate pen-and-paper predictions with IBM Q runs so students test their own circuit calculations](predict-then-test-pen-paper-ibm-q.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Sequence learning from literature, through simulation, to authentication via real remote experiments](simulate-then-authenticate-with-remote-experiment.md)
- [Resource estimation assignments comparing the resources of alternative quantum algorithm implementations](resource-estimation-assignments-strategy.md)
- [Use real-hardware experiment results that deviate from theory to motivate a discussion of quantum error correction](real-hardware-error-observation-strategy.md)
- [Use cloud-accessible quantum computing platforms so students run circuits on real quantum hardware](cloud-quantum-platforms-school-use.md)
- [Design quantum courses around cloud-based platforms and simulators where hardware access is limited](cloud-based-quantum-platforms-course-design.md)
- [Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs](ocean-sdk-dwave-teaching-sequence.md)

## Examples
-

## Key Sources
- Mariia Mykhailova. (2022). Developing Programming Assignments for Teaching Quantum Computing and Quantum Programming. arXiv. https://arxiv.org/abs/2211.16347
