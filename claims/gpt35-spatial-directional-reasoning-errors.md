---
type: claim
title: GPT-3.5 struggled specifically with FCI problems requiring reasoning about directions and spatial relationships
description: GPT-3.5 struggled specifically with FCI problems requiring reasoning about directions and spatial relationships
id: gpt35-spatial-directional-reasoning-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: colin-g-west-2023
    resource: "https://doi.org/10.48550/arXiv.2303.17012"
    title: "Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# GPT-3.5 struggled specifically with FCI problems requiring reasoning about directions and spatial relationships

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-3.5's errors concentrated on problems depending on reasoning about directions and spatial relationships, such as the ball released from circular motion (item 7). [→ Colin G. West 2023](#colin-g-west-2023)

## Evidence

### Colin G. West 2023

Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)

`q2 · i?` · `qualitative · r2`

Qualitative error analysis of GPT-3.5's FCI responses. On item 7 it identified the correct principle (tangential motion) but could not situate it directionally, claiming a northward-moving ball's tangential velocity was directed east. The author hypothesizes corpus associations favor "tangential" but not specific directions like north.

> "GPT-3.5 struggled in particular with problems that depended on reasoning about directions and spatial relationships."

## Discussion


## Related Claims
- [Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally](mllm-flow-direction-interpretation-error-texture-based.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — a broader claim this one bears on
- [Per-student attempt data can localise specific directional difficulties, such as combining north-south with east-west coordinates](ejss-attempt-data-localise-direction-difficulties.md) — related
