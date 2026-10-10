---
type: design
id: clover-instrumented-code-completion-tool
title: "Clover: an instrumented AI code completion tool with attention checks"
description: Clover is a Visual Studio Code extension that uses the Gemini 3 Large Language Model to provide real-time, single-line code suggestions at the cursor position.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: jessica-hutchison-2026
    resource: "https://doi.org/10.1145/3803400.3809394"
    title: "Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394"
    author: Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil
---

# Clover: an instrumented AI code completion tool with attention checks

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
Clover is a Visual Studio Code extension that uses the Gemini 3 Large Language Model to provide real-time, single-line code suggestions at the cursor position. It logs fine-grained interaction events (generation, acceptance, rejection, revision, execution) with timestamps, and deliberately injects attention checks: suggestions "semantically inconsistent with the student's immediate coding goal" whose acceptance or rejection probes critical engagement. It was designed to mirror GitHub Copilot's interface for ecological validity.

## Design Implications

### Context
#### Requirements
- Implemented as a Visual Studio Code extension mirroring widely-adopted tools like GitHub Copilot to collect authentic behavioral data
#### Constraints
- Attention checks are deliberate deterministic incorrect suggestions and do not fully replicate spontaneous AI hallucinations in real-world coding
- Relies on a single AI model, with significant differences in performance and latency based on model selection

### Target Learners
- CS1 / introductory programming students

### Learning Goals
- Critical evaluation of AI-generated code suggestions during programming tasks

### Claims
- [Tab Accept Rate Strongly Associated Failed Attention Checks](../claims/tab-accept-rate-strongly-associated-failed-attention-checks.md) [+M]
- [Dwell Time Attention Checks Versus Task Performance](../claims/dwell-time-attention-checks-versus-task-performance.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394
