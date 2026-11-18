---
type: strategy
id: engineering-like-approach-balance-functionality-effort
title: "Engineering-like approach: balance provided functionality against user effort"
description: "The authors' design strategy is to make the most important features of Arduino application as clear as possible while keeping the tools usable by non-engineers."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: gingl-z-2018
    resource: "https://github.com/miszak-mta-szte/Edaquino"
    title: "Gingl Z, Mellár J, Szépe T, Makan G, Mingesz R, Vadai G and Kopasz K. (2018). Universal Arduino-based experimenting system to support teaching of natural sciences. https://github.com/miszak-mta-szte/Edaquino"
    author: Gingl Z, Mellár J, Szépe T, Makan G, Mingesz R, Vadai G and Kopasz K
---

# Engineering-like approach: balance provided functionality against user effort

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors' design strategy is to make the most important features of Arduino application as clear as possible while keeping the tools usable by non-engineers. They write: "We try to balance an engineering-like and common approach in order to help students and teachers to freely but wisely use parts and tools previously employed only by engineers ." Concretely, they intentionally omit automatic sensor detection and other comfort functions, and state they "have tried to find the optimal balance between the provided functionality and user efforts required for a given measurement task."

## Design Implications

### Context
#### Requirements
- Software must support only the most general functions so that users configure ports and handle data themselves.
#### Constraints
- The strategy deliberately sacrifices convenience: automatic detection of sensors and other comfort functions were intentionally omitted.

### Target Learners
- high-school students
- teachers
- university students

### Target Learning Goals
- practical electronics and instrumentation skills
- coding and signal processing basics
- critical approach and carefulness

## Related Strategies
- 

## Examples
-

## Key Sources
- Gingl Z, Mellár J, Szépe T, Makan G, Mingesz R, Vadai G and Kopasz K. (2018). Universal Arduino-based experimenting system to support teaching of natural sciences. https://github.com/miszak-mta-szte/Edaquino
