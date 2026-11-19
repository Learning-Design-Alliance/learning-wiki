---
type: strategy
id: self-contained-interactive-code-blocks
title: Present interactive code in self-contained logical blocks with stable function definitions to shorten the hypothesis–experiment–result feedback loop
description: The textbook runs Qiskit code directly on its website via Thebe, letting readers test their own hypotheses about quantum computer behaviour and shorten the feedback loop between hypothesis, experiment and result.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: wootton-2020
    resource: "https://arxiv.org/abs/2012.09629"
    title: "Wootton, J. R., Harkins, F., Bronn, N. T., Carrera Vazquez, A., Phan, A., & Asfaw, A. T. (2020). Teaching quantum computing with an interactive textbook. https://arxiv.org/abs/2012.09629"
    author: "Wootton, J. R., Harkins, F., Bronn, N. T., Carrera Vazquez, A., Phan, A., & Asfaw, A. T"
---

# Present interactive code in self-contained logical blocks with stable function definitions to shorten the hypothesis–experiment–result feedback loop

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The textbook runs Qiskit code directly on its website via Thebe, letting readers test their own hypotheses about quantum computer behaviour and shorten the feedback loop between hypothesis, experiment and result. To make this workable, the authors made specific presentation choices: "we avoided splitting logical blocks of code into separate cells, as changing and running multiple cells can lead to confusion and errors", and they avoided overwriting function definitions so behaviour does not change depending on the order cells are run.

## Design Implications

### Context
#### Requirements
- Code must be runnable in-browser without installing Python, Qiskit, or other packages, with relevant code already run.
- Logical blocks of code must not be split across separate cells.
- Function definitions must not be overwritten at different points on the page.
#### Constraints
- These presentation choices were made specifically in response to problems observed in a reading group, where readers wanted to change variables or print values mid-code.

### Target Learners
- self-studying readers of interactive online textbooks
- reading-group participants

### Target Learning Goals
- experimenting with quantum computing code
- testing hypotheses about quantum computer behaviour

## Related Strategies

- [Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning](python-quantum-libraries-simulation-exercises.md)

## Examples
-

## Key Sources
- Wootton, J. R., Harkins, F., Bronn, N. T., Carrera Vazquez, A., Phan, A., & Asfaw, A. T. (2020). Teaching quantum computing with an interactive textbook. https://arxiv.org/abs/2012.09629
