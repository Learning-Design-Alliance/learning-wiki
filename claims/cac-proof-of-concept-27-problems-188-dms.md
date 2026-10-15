---
type: claim
title: The CAC proof of concept compiled 27 biology problems successfully, accumulating 188 Declarative Memory entries, but failed on the 28th problem
description: The CAC proof of concept compiled 27 biology problems successfully, accumulating 188 Declarative Memory entries, but failed on the 28th problem
id: cac-proof-of-concept-27-problems-188-dms
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hyeongdon-moon-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07040"
    title: "Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)"
    author: Hyeongdon Moon, Carolyn Rosé, and John Stamper
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The CAC proof of concept compiled 27 biology problems successfully, accumulating 188 Declarative Memory entries, but failed on the 28th problem

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In a proof-of-concept run, the agent was iteratively compiled to correct answers on 27 biology problems, accumulating 188 Declarative Memory entries with a mean of 3.1 compilation iterations per problem (SD = 2.5), and failed on the 28th problem after 150 iterations. [→ Hyeongdon Moon 2026](#hyeongdon-moon-2026)

## Evidence

### Hyeongdon Moon 2026

Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)

`q2 · i?` · `design · r2`

Proof-of-concept implementation with Small Language Models on the OLI_Biology dataset from CMU DataShop. The run compiled 27 problems successfully, accumulating "188 Declarative Memory entries with a mean of 3.1 compilation iterations per problem (SD = 2.5)"; the 28th problem failed after 150 iterations and the experiment was terminated. No effect sizes are reported.

> "We executed problem-solving attempts for a total of 27 biology problems. During training, the agent was iteratively compiled until it produced the correct answer for each problem, accumulating 188 Declarative Memory entries with a mean of 3.1 compilation iterations per problem (SD = 2.5). On the 28th problem, the agent failed to produce the correct answer after 150 iterations, and the experiment was terminated."

## Discussion


## Related Claims
- [Similarity-based retrieval degrades as the Knowledge Base grows, consistent with the fan effect, stalling the agent](fan-effect-kb-growth-retrieval-degradation.md) — related
- [The hybrid qualitative-COM solver solves arbitrary Camelot Jr. configuration challenges within the game's problem space](camelot-jr-solver-solves-arbitrary-configurations.md) — related
