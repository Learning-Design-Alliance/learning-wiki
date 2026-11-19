---
type: claim
title: Image generation frequently failed to represent all components of multi-component STEM analogies
description: Image generation frequently failed to represent all components of multi-component STEM analogies
id: image-generation-misses-analogy-components
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: cao-2023
    resource: "https://doi.org/10.48550/arXiv.2308.10454"
    title: "Cao, C., Ding, Z., Lee, G.-G., Jiao, J., Lin, J., & Zhai, X. (2023). Elucidating STEM Concepts through Generative AI: A Multi-modal Exploration of Analogical Reasoning. arXiv preprint. [doi:10.48550/arXiv.2308.10454](https://doi.org/10.48550/arXiv.2308.10454)"
    author: "Cao, C., Ding, Z., Lee, G.-G., Jiao, J., Lin, J., & Zhai, X."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Image generation frequently failed to represent all components of multi-component STEM analogies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Despite prompt emphasis on differentiating components, the generative model frequently fell short in representing each part of multi-component analogies comprehensively. [→ Cao 2023](#cao-2023)

## Evidence

### Cao 2023

Cao, C., Ding, Z., Lee, G.-G., Jiao, J., Lin, J., & Zhai, X. (2023). Elucidating STEM Concepts through Generative AI: A Multi-modal Exploration of Analogical Reasoning. arXiv preprint. [doi:10.48550/arXiv.2308.10454](https://doi.org/10.48550/arXiv.2308.10454)

`q1 · i?` · `design · r2`

Case evaluation of the second phase, converting text analogies to static images. In the water pressure/current and electric voltage/current example, only one of the generated images showed two tanks, and it "lacked a connecting tube, a critical element" for the mapping.

> "Despite our emphasis on differentiating these components in the image generation prompts, the generative model frequently fell short in representing each part comprehensively."

## Discussion


## Related Claims
- [Creating dynamic visual analogies posed challenges in devising suitable transitions or motions](dynamic-analogy-motion-challenges.md) — related
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — a broader claim this one bears on
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [The tool generates informative text-based analogies from STEM concepts in preliminary trials](tool-generates-informative-text-analogies.md) — related
