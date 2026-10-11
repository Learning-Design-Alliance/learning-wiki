---
type: claim
title: Instances occurred where the Teacher LLM directly provided the final answer, bypassing the intended cognitive process, and can be programmatically filtered
description: Instances occurred where the Teacher LLM directly provided the final answer, bypassing the intended cognitive process, and can be programmatically filtered
id: collaborative-cheating-teacher-provides-answer
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: hyeongdon-moon-2026
    resource: "https://arxiv.org/abs/2605.07040"
    title: "Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040"
    author: Hyeongdon Moon, Carolyn Rosé, and John Stamper
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Instances occurred where the Teacher LLM directly provided the final answer, bypassing the intended cognitive process, and can be programmatically filtered

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Instances were identified where the Teacher LLM directly provided the final answer to the student agent, bypassing the intended cognitive process; because such answer-dictating knowledge lacks generalizability, the authors state these instances can be programmatically identified and filtered out during compilation. [→ Hyeongdon Moon 2026](#hyeongdon-moon-2026)

## Evidence

### Hyeongdon Moon 2026

Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040

`q1 · i?` · `design · r2`

Authors' observation from the proof of concept (Section 6.5), termed collaborative cheating. They state that knowledge explicitly dictating a specific answer "lacks generalizability to other similar problems" and can be programmatically identified and filtered during compilation. No effect sizes are printed.

> "Instances were identified where the Teacher LLM directly provided the final answer to the student agent, bypassing the intended cognitive process. This issue can be mitigated using the methodology discussed in Section 4.2."

## Discussion


## Related Claims
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related
- [Higher seed-problem filtering thresholds yield better downstream reasoning performance, indicating problem quality directly impacts results](higher-seed-filtering-thresholds-improve-reasoning.md) — related
