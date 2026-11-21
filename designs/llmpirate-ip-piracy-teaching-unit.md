---
type: design
id: llmpirate-ip-piracy-teaching-unit
title: "LLMPirate unit: LLM-driven IP piracy and obfuscation from an attacker's perspective"
description: LLMPirate teaches students how LLMs can be maliciously leveraged to obfuscate circuit designs to evade piracy-detection tools while maintaining functionality.
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

# LLMPirate unit: LLM-driven IP piracy and obfuscation from an attacker's perspective

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
LLMPirate teaches students how LLMs can be maliciously leveraged to obfuscate circuit designs to evade piracy-detection tools while maintaining functionality. "The lab consists of developing an iterative prompting framework for hardware IP piracy": students prompt an LLM to rewrite Verilog circuits so the gate-level structure differs, use Boolean netlist representations in prompts, and add iterative feedback prompts using formal-equivalence and piracy-detection tool outputs. Students submit their prompting framework, equivalence and structural similarity scores, and an evaluation of which configuration best facilitated IP piracy.

## Design Implications

### Context
#### Requirements
- Evaluation of generated circuits for functional equivalence and structural similarity through formal-equivalence and piracy-detection tools
#### Constraints
- Students learn the initial limitations of LLMs in rewriting large-scale Verilog code, including context-window and training challenges

### Target Learners
- students in hardware security courses

### Learning Goals
- understanding LLM-aided hardware attacks and evasion of piracy detection

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Weihua Xiao, Jason Blocklove, Matthew DeLorenzo, Johann Knechtel, Ozgur Sinanoglu, Kanad Basu, Jeyavijayan Rajendran, Siddharth Garg, Ramesh Karri. (2026). GUIDE: GenAI Units In Digital Design Education. https://arxiv.org/abs/2603.17296
