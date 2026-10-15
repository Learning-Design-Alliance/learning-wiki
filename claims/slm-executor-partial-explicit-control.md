---
type: claim
title: An SLM executor under tight constraints can drive a Cognitive Agent through formatted outputs and logit-based action selection, yielding partial rather than full explainability
description: An SLM executor under tight constraints can drive a Cognitive Agent through formatted outputs and logit-based action selection, yielding partial rather than full explainability
id: slm-executor-partial-explicit-control
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: hyeongdon-moon-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07040"
    title: "Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)"
    author: Hyeongdon Moon, Carolyn Rosé, and John Stamper
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# An SLM executor under tight constraints can drive a Cognitive Agent through formatted outputs and logit-based action selection, yielding partial rather than full explainability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The authors report that an SLM with sufficient performance capacity can execute the minimal, formatted outputs required to drive the Cognitive Agent within tightly constrained action spaces, making certain state transitions more inspectable, though this should not be interpreted as full explainability. [→ Hyeongdon Moon 2026](#hyeongdon-moon-2026)

## Evidence

### Hyeongdon Moon 2026

Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)

`q1 · i?` · `design · r2`

Authors' preliminary observation from the SLM proof-of-concept run (Section 5.2), not a validated empirical comparison. They report that enforcing "predefined output formats and leveraging logit-based signals" makes certain state transitions more inspectable, while cautioning this is not full explainability. No effect sizes are printed.

> "The results suggest that an SLM with sufficient performance capacity can execute the minimal, formatted outputs required to drive the Cognitive Agent within tightly constrained action spaces. By enforcing the generation of predefined output formats and leveraging logit-based signals, the system allows certain state transitions to become more inspectable."

## Discussion


## Related Claims

- [Model size defines a core trade-off: too-large SLMs answer without the cognitive structure while too-small SLMs break instruction-following coherence](curse-of-prior-knowledge-size-tradeoff.md) — related
- [A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible](quantized-local-teacher-llm-feasible.md)
