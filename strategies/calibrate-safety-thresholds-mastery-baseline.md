---
type: strategy
id: calibrate-safety-thresholds-mastery-baseline
title: "Calibrate formal safety constraint thresholds against a mastery-only baseline agent's logged behavior"
description: The article proposes a practitioner procedure for setting constraint thresholds in the four-layer framework.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: oluseyi-olukolaa-2026
    resource: "https://arxiv.org/abs/2604.04237"
    title: "Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237"
    author: Oluseyi Olukolaa, Nick Rahimia
---

# Calibrate formal safety constraint thresholds against a mastery-only baseline agent's logged behavior

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes a practitioner procedure for setting constraint thresholds in the four-layer framework. For the progress constraint, the authors "setεprog to the 25th percentile of MAS's per-window progress distribution", chosen because it is "conservative enough that a well-behaved mastery-focused agent passes C2 approximately 75% of the time, yet strict enough to flag sustained stagnation". The demand floor δmin=0.4 is set at the ICAP passive/active boundary, and the coupling bound ρmax=1.2 permits modest engagement surplus. The authors argue the formal framework surfaces calibration requirements that informal approaches would obscure during evaluation rather than after student outcomes deteriorate.

## Design Implications

### Context
#### Requirements
- Session logs from a well-behaved mastery-focused baseline agent in the target domain, from which the progress-threshold percentile is computed
#### Constraints
- Threshold calibration "remains domain-specific and requires validation in each new educational setting"

### Target Learners
- Learners in intelligent tutoring systems across domains

### Target Learning Goals
- Detecting sustained mastery stagnation and uncoupled engagement without flagging well-behaved policies

## Related Strategies

- [Differentiated enrollment thresholds for school autonomy based on territorial fragility](fragility-differentiated-enrollment-thresholds.md)

## Examples
-

## Key Sources
- Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237
