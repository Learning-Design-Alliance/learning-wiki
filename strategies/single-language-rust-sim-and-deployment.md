---
type: strategy
id: single-language-rust-sim-and-deployment
title: Use Rust as a single programming language for both PC simulation and microcontroller deployment
description: The course uses Rust on the PC for simulation and on the STM32 microcontroller for robot deployment, exploiting compiled efficiency, compile-time safety guarantees from the borrow checker, and support for embedded tar...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: wolfgang-hönig-2026
    resource: "https://arxiv.org/abs/2604.00032"
    title: "Wolfgang Hönig, Christoph Scherer, and Khaled Wahba. (2026). Rusty Flying Robots: Learning a Full Robotics Stack with Real-Time Operation on an STM32 Microcontroller in a 9 ECTS MS Course. https://arxiv.org/abs/2604.00032"
    author: Wolfgang Hönig, Christoph Scherer, and Khaled Wahba
---

# Use Rust as a single programming language for both PC simulation and microcontroller deployment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The course uses Rust on the PC for simulation and on the STM32 microcontroller for robot deployment, exploiting compiled efficiency, compile-time safety guarantees from the borrow checker, and support for embedded target architectures. The authors state: "Our course combines simulation and real-robot deployment using a single programming language", avoiding rewriting or conversion to C for deployment.

## Design Implications

### Context
#### Requirements
- Students must learn Rust largely auto-didactically, as the lecture only includes a high-level overview and a few examples of the language.
#### Constraints
- Transfer from simulation to the robot is often quickly successful, but issues mostly arise from the language transition C/Rust and unit conversions; interoperability with the C flight firmware requires converting data types and tools such as bindgen.

### Target Learners
- masters students with prior experience in C and Python but not Rust

### Target Learning Goals
- deploying state-of-the-art algorithms in real time on highly constrained embedded hardware

## Claims

- [Students without prior Rust experience achieved implementation of state-of-the-art nonlinear robotics components within a 9 ECTS course without provided math libraries](../claims/no-prior-rust-students-complete-nonlinear-pipeline.md) [+W]
- [A masters-level Rust robotics projects course was rated very good (mean 1.1 on a 1–5 scale) across two offerings](../claims/rust-robotics-course-rated-1-1-two-offerings.md) [+W]
- [Self-reported weekly workload in the course stayed within the expected effort for a 9 ECTS class](../claims/rust-robotics-course-workload-within-9-ects.md) [+W]
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](../claims/llm-feedback-faster-time-to-solution.md) [+W]

## Related Strategies

- [Mitigate LLM feedback errors by supplying course materials and compiler errors in the prompt, fact-checking generated feedback, and adapting feedback structure to student behavior](mitigate-llm-feedback-errors-context-and-fact-checking.md)

## Examples
-

## Key Sources
- Wolfgang Hönig, Christoph Scherer, and Khaled Wahba. (2026). Rusty Flying Robots: Learning a Full Robotics Stack with Real-Time Operation on an STM32 Microcontroller in a 9 ECTS MS Course. https://arxiv.org/abs/2604.00032
