---
type: strategy
id: knowledge-ablation-and-downstream-kt-validation
title: Test whether success depends on compiled knowledge via knowledge ablation and downstream Knowledge Tracing validation
description: The article proposes two conceptual tests for judging whether the remaining black-box component is small enough for educational use.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: hyeongdon-moon-2026
    resource: "https://arxiv.org/abs/2605.07040"
    title: "Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040"
    author: Hyeongdon Moon, Carolyn Rosé, and John Stamper
---

# Test whether success depends on compiled knowledge via knowledge ablation and downstream Knowledge Tracing validation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes two conceptual tests for judging whether the remaining black-box component is small enough for educational use. First, knowledge ablation: remove candidate core knowledge from the Knowledge Base and verify whether the agent can still answer correctly, suspecting prior-knowledge reliance if it does. Second, implement a Knowledge Tracing model using the generated Knowledge Components and evaluate how well it predicts student errors, enforcing knowledge-performance monotonicity.

## Design Implications

### Context
#### Requirements
- Requires a compiled Knowledge Base with candidate core knowledge identifiable for removal, and student interaction data for downstream Knowledge Tracing evaluation
#### Constraints
- The authors frame these as needed tests because the study does not yet establish CAC as a validated learner model

### Target Learners
- students in intelligent tutoring system settings

### Target Learning Goals
- predicting problem resolvability and student errors from explicit knowledge states

## Related Strategies
- 

## Examples
-

## Key Sources
- Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040
