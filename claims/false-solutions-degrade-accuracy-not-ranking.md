---
type: claim
title: False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact
description: False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact
id: false-solutions-degrade-accuracy-not-ranking
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: will-yeadon-2026
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: will-yeadon-2026-2
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Exposing models to a deliberately corrupted solution raises fractional MAE to approximately 0.22–0.38, exceeding blind MAE for every model, showing deference to the provided reference. [→ Will Yeadon 2026](#will-yeadon-2026)
`q2 i?` Under false solutions, rank correlations dip but remain robust (e.g., Gemini false rho = 0.744; Claude false rho = 0.719). [→ Will Yeadon 2026 (2)](#will-yeadon-2026-2)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

False-solution condition on curriculum questions (n=1151), where corrupted references were generated via five mechanical perturbations. The article reports fractional MAE "rising to approximately 0.22–0.38", confirming models defer to provided references.

> "Providing a false solution dramatically degrades absolute performance for all models, with fractional MAE rising to approximately 0.22–0.38 (GPT-5.2: 0.381; Claude: 0.249; Gemini: 0.216; DeepSeek: 0.369; Grok: 0.384; committee: 0.316)."

### Will Yeadon 2026 (2)

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Rank-order analysis of the same false-solution condition. The article reports correlations "dip but remain robust", indicating models retain the ability to rank good answers above bad while shifting absolute scores toward the incorrect reference.

> "When exposed to the false solu- tion, these correlations dip but remain robust (e.g., Gem- ini falseρ= 0.744; Claude falseρ= 0.719; Table II)."

## Discussion


## Related Claims
- [Providing official reference solutions consistently reduces LLM marking error on structured physics questions](official-solutions-reduce-llm-marking-error.md) — related
- [LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions](llm-rank-order-agreement-structured-physics-questions.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — related
