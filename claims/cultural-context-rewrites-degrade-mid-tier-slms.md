---
type: claim
title: Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions
description: Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions
id: cultural-context-rewrites-degrade-mid-tier-slms
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
  - id: nicy-scaria-2025-2
    resource: "https://doi.org/10.48550/arXiv.2505.20707"
    title: "Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)"
    author: Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Culturally contextualized rewrites of identical physics problems minimally affect top SLMs but degrade mid-tier models, with no differential effect across regions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Top models maintain near-invariant scores across cultural variants, while mid-tier models drop from baseline to any cultural variant but perform nearly identically across Asia, Africa, and OcSA versions. [→ Nicy Scaria 2025](#nicy-scaria-2025)
`q2 i?` Mid-tier models such as Phi4 Mini and Qwen3 0.6B show a performance drop when moving from the baseline subset to cultural variants. [→ Nicy Scaria 2025 (2)](#nicy-scaria-2025-2)

## Evidence

### Nicy Scaria 2025

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Comparison of overall performance on a 900-question baseline subset and its region-specific contextualized variants (Figure 5). The article reports Phi4 Reason's 0.5% variation and Qwen3 1.7B's 62.1-62.5% range across regions.

> "Phi4 Reason maintains scores between 66.0% and 66.5% across all regions (a variation of just 0.5%), and Qwen3 1.7B remains within the 62.1-62.5% range."

### Nicy Scaria 2025 (2)

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Same contextual-variation comparison (Figure 5), reporting baseline-to-variant drops for mid-tier models. The article notes Phi4 Mini's variant scores cluster at 23.6%, 22.6%, and 23.1%, showing no regional differential effect.

> "Phi4 Mini drops from 30.4% (baseline) to approximately 23% across contextual variants, and Qwen3 0.6B drops from 38.6% to approximately 30-31%."

## Discussion


## Related Claims
- [SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap](slm-conceptual-problem-solving-performance-gap.md) — related
- [SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution](slm-failure-stage-shifts-with-capability.md) — related
- [SLM physics performance declines monotonically with Bloom's cognitive complexity and is weakest on procedural knowledge](slm-performance-declines-with-cognitive-complexity.md) — related
