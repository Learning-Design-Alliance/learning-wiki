---
type: strategy
id: cas-client-server-interface-strategy
title: Professor-created CAS interfaces in a client/server arrangement, with calculations processed locally or on a remote server that manages the queue
description: "An implementable arrangement for classroom use of CAS-based interfaces: n students each use a client computer with an interactive interface created by the professor."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-16
sources:
  - id: danilo-t-alves-2011
    resource: "https://arxiv.org/abs/1104.4461"
    title: "Danilo T. Alves, Silvio C. F. Pereira Filho. (2011). Computer algebra systems as tools for learning Physics and Mathematics. https://arxiv.org/abs/1104.4461"
    author: Danilo T. Alves, Silvio C. F. Pereira Filho
---

# Professor-created CAS interfaces in a client/server arrangement, with calculations processed locally or on a remote server that manages the queue

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An implementable arrangement for classroom use of CAS-based interfaces: n students each use a client computer with an interactive interface created by the professor. When a student requires a calculation, the interface sends an input which can be processed by a CAS installed on the client computer or by a CAS on a server machine remotely accessed via intranet or internet; the output is returned to the client interface. In the remote case, the server machine manages the queue of requested processes.

## Design Implications

### Context
#### Requirements
- One client computer per student running the interactive interface
- A CAS such as Maxima installed on the client or on a server machine
- The professor creates the interactive interface for the issue at hand
#### Constraints
- Remote access requires a server machine to manage the queue of requested processes

### Target Learners
- students in a computer-equipped class using interfaces built by their professor

### Target Learning Goals
- solving analytical problems step-by-step with feedback about errors and interactive graphs

## Claims

- [Public high-school students used the free CAS Maxima to build small routines, such as a unit-conversion routine, and created, answered and tested questions; the authors again report a successful experience](../claims/high-school-maxima-routines-introductory-physics.md) [+W]
- [Undergraduate students learning electromagnetism created their own Maple routines for vector-calculus operators and explored the meaning of the operators by applying them to fields](../claims/undergraduates-create-maple-routines-vector-operators.md) [+W]

## Related Strategies

- [Embed a CAS in an e-book file to give e-books interactive step-by-step problem solving, error feedback and interactive graphs](cas-attached-ebook-interactivity-strategy.md)

## Examples
-

## Key Sources
- Danilo T. Alves, Silvio C. F. Pereira Filho. (2011). Computer algebra systems as tools for learning Physics and Mathematics. https://arxiv.org/abs/1104.4461
