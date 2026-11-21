---
type: claim
title: "SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution"
description: "SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution"
id: slm-failure-stage-shifts-with-capability
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

# SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The dominant reasoning bottleneck differs by model strength: early formulation for weaker models, procedural execution for stronger models. [→ Nicy Scaria 2025](#nicy-scaria-2025)

## Evidence

### Nicy Scaria 2025

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Progressive degradation analysis across P-REFS error categories (Figure 6) for problem-solving questions, tracking the percentage of questions remaining error-free at each stage. After interpretation, weaker models retained fewer than 10% error-free solutions.

> "This pattern suggests that the dominant bottleneck shifts with model strength: weaker models fail primarily at early formulation, whereas stronger models are limited by procedural reliability in multi-step execution."

## Discussion


## Related Claims
- [Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions](cultural-context-rewrites-degrade-mid-tier-slms.md) — related
- [SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap](slm-conceptual-problem-solving-performance-gap.md) — related
- [Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution](slm-physics-answer-reasoning-gap.md) — related
- [Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations](executable-reasoning-failure-redistribution-layers.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge](slm-performance-declines-with-cognitive-complexity.md) — related
