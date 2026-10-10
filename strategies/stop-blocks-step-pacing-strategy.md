---
type: strategy
id: stop-blocks-step-pacing-strategy
title: Use STOP blocks as explicit pacing primitives to manage information overload in AI-as-instructor instruction
description: STOP blocks are explicit pause directives embedded in module files that create hard boundaries in instruction delivery, addressing the risk that an AI agent instructed to teach a module generates thousands of words in...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: zain-naboulsi-2026
    resource: "https://arxiv.org/abs/2604.17460"
    title: "Zain Naboulsi. (2026). Agentic Education: Using Claude Code to Teach Claude Code. arXiv. https://arxiv.org/abs/2604.17460"
    author: Zain Naboulsi
---

# Use STOP blocks as explicit pacing primitives to manage information overload in AI-as-instructor instruction

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
STOP blocks are explicit pause directives embedded in module files that create hard boundaries in instruction delivery, addressing the risk that an AI agent instructed to teach a module generates thousands of words in a single response. The article states: "A STOP block serves three functions: (1) it forces the AI to pause and wait for the learner's response before continuing; (2) it provides a reflection prompt intended to consolidate learning from the preceding step; and (3) it creates a natural checkpoint where the learner can assess their understanding before moving forward." Pacing is enforced through a CLAUDE.md directive instructing the agent to halt after each STOP block, and step progress is tracked in a persistent state file that survives context compaction.

## Design Implications

### Context
#### Requirements
- A CLAUDE.md pacing directive and a per-session state file (CLAUDE.local.md) that is re-read at the start of each interaction
#### Constraints
- Enforcement relies on the LLM's adherence to prompt instructions rather than a hard system lock, so occasional violations are possible, though the authors report compliance to be reliable in practice

### Target Learners
- learners receiving instruction from an AI agent in a terminal-based environment

### Target Learning Goals
- managing extraneous cognitive load and information overload during step-by-step skill acquisition

## Related Strategies

- [Pacing](pacing.md)
- [Chunk Directions](chunk_directions.md)
- [Segmenting](segmenting.md)

## Examples
-

## Key Sources
- Zain Naboulsi. (2026). Agentic Education: Using Claude Code to Teach Claude Code. arXiv. https://arxiv.org/abs/2604.17460
