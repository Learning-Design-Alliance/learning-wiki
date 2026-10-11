---
type: strategy
id: line-level-kc-rationales-for-recommendations
title: Provide line-level KC-based rationales to make recommendations auditable and pattern-focused
description: Because similarity is computed over pattern-based KCs, the system decomposes the cosine score into per-KC contributions and traces high-contributing KCs back through the pipeline to high-attention subtree instances an...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: muntasir-hoq-2026
    resource: "https://arxiv.org/abs/2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
---

# Provide line-level KC-based rationales to make recommendations auditable and pattern-focused

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because similarity is computed over pattern-based KCs, the system decomposes the cosine score into per-KC contributions and traces high-contributing KCs back through the pipeline to high-attention subtree instances and their code spans, highlighting them "with color intensity proportional to the underlying attention weight". For students, highlighted regions direct attention to abstract decision-making schemas to support transfer; for instructors, contribution breakdowns provide an auditable account of matches, help diagnose failure modes, and support maintenance of the KC inventory.

## Design Implications

### Context
#### Requirements
- Explanation quality depends on the attention weights assigned by the framework and the KC clustering resolution
#### Constraints
- Highly overlapping KCs can produce adjacent or redundant highlights, as the authors state; the pipeline's topic-label training step limits direct application to unlabeled corpora

### Target Learners
- introductory programming students
- instructors curating programming content

### Target Learning Goals
- internalizing general structures of conditional reasoning and other programming patterns
- auditing and refining content repositories

### Affordances
- [Pattern Based Kc Representation Framework](../research-methods/pattern-based-knowledge-component-extraction-from-program-asts.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409
