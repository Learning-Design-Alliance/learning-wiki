---
type: claim
title: A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking
description: A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking
id: llm-human-agreement-ct-practices
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sean-savage-2026
    resource: "https://doi.org/10.48550/arxiv.2608.06200"
    title: "Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello. (2026). Using LLMs to Detect Growth in Computational Thinking in Introductory Physics. arXiv preprint. https://arxiv.org/abs/2608.06200 [doi:10.48550/arxiv.2608.06200](https://doi.org/10.48550/arxiv.2608.06200)"
    author: Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Against a 50-student human baseline, the LLM achieved DP κ = 0.90 (93% agreement), MSP κ = 0.78 (85%), and CPP κ = 0.69 (74%), with lower agreement on Physics Correctness (κ = 0.53) and STP (κ = 0.48). [→ Sean Savage 2026](#sean-savage-2026)

## Evidence

### Sean Savage 2026

Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello. (2026). Using LLMs to Detect Growth in Computational Thinking in Introductory Physics. arXiv preprint. https://arxiv.org/abs/2608.06200 [doi:10.48550/arxiv.2608.06200](https://doi.org/10.48550/arxiv.2608.06200)

`q2 · i?` · `design · r2`

Validation of GPT-5.4-mini scoring against the 50-student human consensus baseline, using the same rubric and majority vote over three independent runs. The article reports kappa values it characterizes as moderate to substantial, with lower agreement for multi-component constructs.

> "The model achieved substantial agreement and high raw accuracy on explicitly defined practices, including DP (κ= 0.90, with93%agreement), MSP (κ= 0.78, with 85%agreement), and CPP (κ= 0.69, with74%agreement)."

## Discussion


## Related Claims
- [Students in a computationally intensive introductory physics course show large-magnitude growth in Data Practices and moderate growth in Computational Problem-Solving and Systems Thinking on written CT assessments](ct-growth-data-practices-intro-physics.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
