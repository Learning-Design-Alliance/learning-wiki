---
type: claim
title: SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap
description: SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap
id: slm-conceptual-problem-solving-performance-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: nicy-scaria-2025
    resource: "https://doi.org/10.48550/arXiv.2505.20707"
    title: "Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)"
    author: Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All model families show sharply lower rubric scores on multi-step problem-solving questions than on conceptual questions. [→ Nicy Scaria 2025](#nicy-scaria-2025)

## Evidence

### Nicy Scaria 2025

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Part-wise performance breakdown for PhysBench conceptual versus problem-solving questions (Figure 3) across ten SLMs. The article reports Phi4 Mini's drop from 80.6% to 33.1% and Phi4 Reason's from 82.4% to 69.1%.

> "For example, Phi4 Mini drops from 80.6% (conceptual) to 33.1% (problem-solving), while Phi4 Reason drops from 82.4% to 69.1%, indicating that reasoning-optimized training improves robustness but does not eliminate the procedural bottleneck in multi-step quantitative physics."

## Discussion


## Related Claims
- [Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions](cultural-context-rewrites-degrade-mid-tier-slms.md) — related
- [Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution](slm-physics-answer-reasoning-gap.md) — related
- [SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution](slm-failure-stage-shifts-with-capability.md) — related
- [SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge](slm-performance-declines-with-cognitive-complexity.md) — a broader claim this one bears on
- [Students in college physics courses perform poorly on conceptual questions while sometimes solving difficult multiple-step quantitative problems better](conceptual-questions-poor-quantitative-better.md) — related
