---
type: strategy
id: sealaas-service-oriented-architecture
title: Implement adaptive learning platforms as loosely coupled service-oriented architectures (X-as-a-service)
description: The article implements SEAL server-side as SEAL-as-a-service (SEALaaS), following MLaaS conventions, using a Service Oriented Architecture in which decoupled components communicate purely via APIs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: junhua-liu-2020
    resource: "https://doi.org/10.1145/3406865.3418326"
    title: "Junhua Liu, Lionell Loh, Ernest Ng, Yijia Chen, Kristin L. Wood, and Kwan Hui Lim. (2020). Self-Evolving Adaptive Learning for Personalized Education. CSCW '20 Companion. https://doi.org/10.1145/3406865.3418326"
    author: Junhua Liu, Lionell Loh, Ernest Ng, Yijia Chen, Kristin L. Wood, and Kwan Hui Lim
---

# Implement adaptive learning platforms as loosely coupled service-oriented architectures (X-as-a-service)

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article implements SEAL server-side as SEAL-as-a-service (SEALaaS), following MLaaS conventions, using a Service Oriented Architecture in which decoupled components communicate purely via APIs. The authors state such a loose coupling allows the system to be easily extensible to different use cases and enables scalability and robustness, prioritising scalability and usability of the solution.

## Design Implications

### Context
#### Requirements
- Components communicate purely via application programming interfaces (APIs)
- Services are stateless, with data queried from relevant databases per request
#### Constraints
- Scalability and robustness are design claims of the architecture, not empirically tested results in this paper

### Target Learners
- Primary and secondary school students
- Teachers

### Target Learning Goals
- Delivering personalized education at scale

## Claims

- [The authors claim no evaluation of SEAL yet: experiments to test effectiveness and experience are future work](../claims/seal-effectiveness-testing-future-work.md) [~W]
- [Mobile and web technology shifts forced re-conceptualization toward loose coupling of system components](../claims/platform-discontinuities-loose-coupling.md) [+W]

## Related Strategies
- Seal Self Evolving Adaptive Learning System

## Examples
-

## Key Sources
- Junhua Liu, Lionell Loh, Ernest Ng, Yijia Chen, Kristin L. Wood, and Kwan Hui Lim. (2020). Self-Evolving Adaptive Learning for Personalized Education. CSCW '20 Companion. https://doi.org/10.1145/3406865.3418326
