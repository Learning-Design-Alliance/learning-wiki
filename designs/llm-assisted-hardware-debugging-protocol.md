---
type: design
id: llm-assisted-hardware-debugging-protocol
title: LLM-assisted hardware debugging protocol mapped to the four-step troubleshooting model
description: "The paper proposes a protocol following Katz and Anderson's troubleshooting model, in which an LLM-assistant supports each of the four steps: \"understanding the system, testing the system, locating the bug, and ﬁxing..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: andrew-ash-and-john-hu-2026
    resource: "https://arxiv.org/abs/2608.02420"
    title: "Andrew Ash and John Hu. (2026). WIP: Chat-Debugging: Large Language Model as a Hardware Debugging Assistant. arXiv preprint. https://arxiv.org/abs/2608.02420"
    author: Andrew Ash and John Hu
---

# LLM-assisted hardware debugging protocol mapped to the four-step troubleshooting model

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The paper proposes a protocol following Katz and Anderson's troubleshooting model, in which an LLM-assistant supports each of the four steps: "understanding the system, testing the system, locating the bug, and ﬁxing the bug." The LLM summarizes datasheets and expected component functionality, helps draft test plans, generates multiple potential root causes, and reminds the student of hardware context while fixing and verifying the bug. The student must maintain control by validating the LLM's claims throughout.

## Design Implications

### Context
#### Requirements
- The student must maintain control of the interaction by validating the LLM's claims to ensure it has an accurate understanding of the hardware
- The student needs patience and endurance, and must commit to assertively correcting the LLM's misunderstandings
#### Constraints
- Prompting strategies will change as LLM models are regularly updated and improved

### Target Learners
- electrical and computer engineering students debugging circuits in labs and projects

### Learning Goals
- hardware debugging and troubleshooting skills
- debugging confidence

### Claims
- [Llm Provides Accurate Hardware Information](../claims/llm-provides-accurate-hardware-information.md) [+M]
- [Hardware Debugging Takes Multiple Prompts](../claims/hardware-debugging-takes-multiple-prompts.md) [+M]
- [Llm Debugging Requires Consistent Human Feedback](../claims/llm-debugging-requires-consistent-human-feedback.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Andrew Ash and John Hu. (2026). WIP: Chat-Debugging: Large Language Model as a Hardware Debugging Assistant. arXiv preprint. https://arxiv.org/abs/2608.02420
