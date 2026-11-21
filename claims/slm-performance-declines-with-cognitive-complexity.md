---
type: claim
title: "SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge"
description: "SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge"
id: slm-performance-declines-with-cognitive-complexity
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

# SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Performance follows a knowledge-type hierarchy from Factual to Conceptual to Procedural, with degradation most pronounced in execution. [→ Nicy Scaria 2025](#nicy-scaria-2025)

## Evidence

### Nicy Scaria 2025

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Knowledge-dimension breakdown of PhysBench performance (Appendix Figure 18). The article reports degradation is particularly pronounced in execution, calling procedural execution a core limiter for SLM physics competence.

> "Performance shows a clear hierarchy across knowledge types: models perform strongest on Factual knowledge, followed by Conceptual knowledge, and weakest on Procedural knowledge."

## Discussion


## Related Claims
- [Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions](cultural-context-rewrites-degrade-mid-tier-slms.md) — related
- [SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap](slm-conceptual-problem-solving-performance-gap.md) — a narrower finding that bears on this claim
- [GPT-4 performance degrades on harder and cognitively more complex questions](gpt4-performance-degrades-on-harder-questions.md) — a broader claim this one bears on
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — a broader claim this one bears on
- [Proportions of variance explained follow a curvilinear pattern across the six taxonomy levels](curvilinear-variance-pattern-across-taxonomy-levels.md) — related
- [SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution](slm-failure-stage-shifts-with-capability.md) — related
