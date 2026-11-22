---
type: design
id: dual-manual-automated-kit-progression
title: Dual manual-then-automated progression for hands-on quantum kits
description: A lesson-level design pattern in which learners first operate a physical apparatus manually to build familiarity with components and underlying optics principles, then transition to an automated mode that removes oper...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: john-m-donohue-2026
    resource: "https://arxiv.org/abs/2607.20738v1"
    title: "John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738v1"
    author: John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini
---

# Dual manual-then-automated progression for hands-on quantum kits

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A lesson-level design pattern in which learners first operate a physical apparatus manually to build familiarity with components and underlying optics principles, then transition to an automated mode that removes operational slowness and enables exploration of higher-level protocol and data-manipulation concepts. The authors report that "The dual manual/automated modes of the kit allowed for students to first gain familiarity with the components and the basic optics principles such as polarization states and quantum randomness in the manual mode before transitioning to the automated mode to explore the cryptography concepts and implementations."

## Design Implications

### Context
#### Requirements
- Both a manual operating mode and an automated mode built on the same physical components
- An automated mode fast enough to generate keys long enough for realistic cryptographic activities
#### Constraints
- The manual mode is slow to operate, making it difficult to generate long keys in a reasonable time frame, which limits the types of activities that can be done

### Target Learners
- undergraduate students
- high-school students

### Learning Goals
- polarization states
- quantum randomness
- QKD protocol implementation
- cryptographic key manipulation

### Claims
- 

## Related Designs

- [Manual QKD analogy kit with 3D-printed components and classical-light polarization analogy](manual-qkd-analogy-kit-3d-printed.md)
- [Two-hour pre-aligned laboratory shifts with at-home data processing for quantum optics tomography](pre-aligned-two-hour-shifts-at-home-data-processing.md)

## Examples
-

## Key Sources
- John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738v1
