---
type: claim
title: Similarity-based retrieval degrades as the Knowledge Base grows, consistent with the fan effect, stalling the agent
description: Similarity-based retrieval degrades as the Knowledge Base grows, consistent with the fan effect, stalling the agent
id: fan-effect-kb-growth-retrieval-degradation
status: review
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

# Similarity-based retrieval degrades as the Knowledge Base grows, consistent with the fan effect, stalling the agent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` As the Knowledge Base grew, similarity-based retrieval increasingly failed to surface newly added Declarative Memories, consistent with the fan effect, causing the agent to stall even after 150 iterations; in several cases the agent retrieved entirely irrelevant knowledge, consistent with deceptive overgeneralization. [→ Hyeongdon Moon 2026](#hyeongdon-moon-2026)

## Evidence

### Hyeongdon Moon 2026

Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)

`q1 · i?` · `design · r2`

Observation from the proof-of-concept run (Section 6.2); this issue was the primary reason the experiment was terminated at the 28th problem. The authors report retrieval failures "consistent with the fan effect" and note a more selective retrieval mechanism is needed. No effect sizes are printed.

> "As the KB grew, similarity-based retrieval increasingly failed to surface newly added DMs, consistent with the fan effect [4] in which retrieval accuracy degrades as more items share overlapping cues. This caused the agent to stall even after 150 iterations."

## Discussion


## Related Claims
- [The CAC proof of concept compiled 27 biology problems successfully, accumulating 188 Declarative Memory entries, but failed on the 28th problem](cac-proof-of-concept-27-problems-188-dms.md) — related
