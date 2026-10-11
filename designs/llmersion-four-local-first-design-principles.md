---
type: design
id: llmersion-four-local-first-design-principles
title: Four design principles for a local-first AI language-tutor scheme (P1-P4)
description: "The article's scheme is organized as four design principles, each answering one identified constraint: \"(P1) a web interface backed entirely by local, free, lowest-hardware-cost models\"; (P2) the complete listening-re..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: guo-2026
    resource: "https://arxiv.org/abs/2609.29672"
    title: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672"
    author: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X"
---

# Four design principles for a local-first AI language-tutor scheme (P1-P4)

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's scheme is organized as four design principles, each answering one identified constraint: "(P1) a web interface backed entirely by local, free, lowest-hardware-cost models"; (P2) the complete listening-reading-speaking-writing loop "played in the teacher's order"; (P3) the learner's own documents and self-built vocabulary as first-class input rather than a fixed curriculum; and (P4) a codebase that is AI-written, AI-understood, and AI-updated so customization does not require professional engineering. The pattern operates at whole-program grain: the four principles together define how a home language-learning agent is composed and maintained.

## Design Implications

### Context
#### Requirements
- Small open-weight models that fit commodity household hardware, since the scheme stands or falls on whether machines low-cost households own can run the stack.
#### Constraints
- The article states the scheme establishes feasibility, not efficacy: whether the software teaches is a separate, measurable question.

### Target Learners
- home learners of English lacking access to oral tutoring, including offline households

### Learning Goals
- integrated listening-reading-speaking-writing practice over the learner's own materials

### Claims
- Four Binding Constraints Equitable Language Education [+M]
- [Llmersion Feasibility Stack Pace Cost](../claims/llmersion-feasibility-stack-pace-cost.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672
