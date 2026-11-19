---
type: design
id: teach-quantum-computing-through-software-engineering
title: Teach quantum computing through software engineering rather than physics
description: "The course's guiding principle was to \"Teach quantum computing through software engineering instead of physics\", approaching the material as computer scientists and deliberately avoiding physics in lectures."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: mariia-mykhailova-and-krysta-m-svore-2020
    resource: "https://doi.org/10.1145/3328778.3366952"
    title: "Mariia Mykhailova and Krysta M. Svore. 2020. Teaching Quantum Computing through a Practical Software-driven Approach: Experience Report. In The 51st ACM Technical Symposium on Computer Science Education (SIGCSE '20). https://doi.org/10.1145/3328778.3366952"
    author: Mariia Mykhailova and Krysta M. Svore
---

# Teach quantum computing through software engineering rather than physics

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The course's guiding principle was to "Teach quantum computing through software engineering instead of physics", approaching the material as computer scientists and deliberately avoiding physics in lectures. Qubits were presented as abstract objects described by vectors and operations as matrix transformations, with a single end-of-term lecture on physical implementations. This made the course accessible to undergraduates without physics prerequisites.

## Design Implications

### Context
#### Requirements
- A high-level domain-specific quantum programming language and a simulator running on classical computers so assignments can be implemented and executed without quantum hardware
#### Constraints
- Quantum computing is not yet at the stage where algorithms of practical interest can run on real quantum hardware, so assignments execute on a simulator

### Target Learners
- 3rd and 4th year undergraduate computer science students

### Learning Goals
- implementing and debugging quantum algorithms
- foundations of quantum computing

### Claims
- Programming Sections Helped Internalize Theory Quantum Course [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Mariia Mykhailova and Krysta M. Svore. 2020. Teaching Quantum Computing through a Practical Software-driven Approach: Experience Report. In The 51st ACM Technical Symposium on Computer Science Education (SIGCSE '20). https://doi.org/10.1145/3328778.3366952
