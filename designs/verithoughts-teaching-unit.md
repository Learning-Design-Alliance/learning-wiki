---
type: design
id: verithoughts-teaching-unit
title: "VeriThoughts unit: reasoning and formal-verification-backed RTL generation"
description: The VeriThoughts unit teaches students how verification-backed reasoning datasets are constructed and how to analyze RTL generation quality through formal equivalence checking.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: weihua-xiao-2026
    resource: "https://arxiv.org/abs/2603.17296"
    title: "Weihua Xiao, Jason Blocklove, Matthew DeLorenzo, Johann Knechtel, Ozgur Sinanoglu, Kanad Basu, Jeyavijayan Rajendran, Siddharth Garg, Ramesh Karri. (2026). GUIDE: GenAI Units In Digital Design Education. https://arxiv.org/abs/2603.17296"
    author: Weihua Xiao, Jason Blocklove, Matthew DeLorenzo, Johann Knechtel, Ozgur Sinanoglu, Kanad Basu, Jeyavijayan Rajendran, Siddharth Garg, Ramesh Karri
---

# VeriThoughts unit: reasoning and formal-verification-backed RTL generation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The VeriThoughts unit teaches students how verification-backed reasoning datasets are constructed and how to analyze RTL generation quality through formal equivalence checking. "Students first select a subset of ground-truth Verilog modules from the VeriThoughts dataset", then run a synthesis pipeline where an LLM generates NL questions, a reasoning-capable LLM produces reasoning traces and candidate Verilog, and a formal equivalence checker labels each candidate as match or mismatch. Students submit the subset configuration, synthesized dataset, checker logs, and an analysis report.

## Design Implications

### Context
#### Requirements
- Submission of a formal equivalence checker log for at least one match and one mismatch example
#### Constraints
- 

### Target Learners
- students learning prompting, RTL generation, and formal verification

### Learning Goals
- understanding how formal-equivalence-checked pipelines produce reliable training data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Weihua Xiao, Jason Blocklove, Matthew DeLorenzo, Johann Knechtel, Ozgur Sinanoglu, Kanad Basu, Jeyavijayan Rajendran, Siddharth Garg, Ramesh Karri. (2026). GUIDE: GenAI Units In Digital Design Education. https://arxiv.org/abs/2603.17296
