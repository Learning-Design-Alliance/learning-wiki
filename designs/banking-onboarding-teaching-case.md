---
type: design
id: banking-onboarding-teaching-case
title: Banking customer-onboarding teaching case with AI-constrained fraud-screening agent
description: A fictitious retail-bank customer onboarding process (registration, fraud assessment, approval) facing a scalability crisis, deliberately rich in regulatory constraints, knowledge-intensive work, and heterogeneous dat...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: amin-jalali-2026
    resource: "https://arxiv.org/abs/2610.06207"
    title: "Amin Jalali. (2026). AI-Decision Checkpoints for AI-Augmented Business Process Management: Framework and Educational Instantiation. https://arxiv.org/abs/2610.06207"
    author: Amin Jalali
---

# Banking customer-onboarding teaching case with AI-constrained fraud-screening agent

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A fictitious retail-bank customer onboarding process (registration, fraud assessment, approval) facing a scalability crisis, deliberately rich in regulatory constraints, knowledge-intensive work, and heterogeneous data sources. Document B proposes AI agents, prioritizing email-based registration extraction and RAG-based fraud screening; the fraud-screening agent is "deliberately constrained by a known class-imbalance problem (the data science team reports high recall but imperfect precision)". Case materials, module instructions, and datasets are openly available in a GitHub repository.

## Design Implications

### Context
#### Requirements
- Two main documents (Document A as-is process with seven roles; Document B redesign brief) distributed at different course points
#### Constraints
- The fraud agent's class-imbalance problem forces students to reason about when output can be trusted autonomously and when a human must remain in the loop

### Target Learners
- Master-level students with no prior BPM or AI knowledge assumed

### Learning Goals
- designing, implementing, and evaluating AI-augmented process variants across the full lifecycle
- governance concerns such as human-in-the-loop routing and fallback handling

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Amin Jalali. (2026). AI-Decision Checkpoints for AI-Augmented Business Process Management: Framework and Educational Instantiation. https://arxiv.org/abs/2610.06207
