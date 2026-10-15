---
type: claim
title: Self-refinement gains depend on model strength and on behavior-prediction quality
description: Self-refinement gains depend on model strength and on behavior-prediction quality
id: self-refinement-gains-depend-on-model-and-prediction-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: tao-wu-2025
    resource: "https://doi.org/10.48550/arxiv.2505.19997"
    title: "Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)"
    author: Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: tao-wu-2025-2
    resource: "https://arxiv.org/abs/2505.19997"
    title: "Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997"
    author: Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Self-refinement gains depend on model strength and on behavior-prediction quality

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` More powerful LLMs such as GPT-4o exhibit greater performance gains from self-refinement. [→ Tao Wu 2025](#tao-wu-2025)
`q2 i?` When behavior prediction quality is low, self-refinement can underperform IO or CoT prompting. [→ Tao Wu 2025 (2)](#tao-wu-2025-2)

## Evidence

### Tao Wu 2025

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)

`q2 · i?` · `design · r2`

Observation from the end-to-end comparison in Section 5.2, where the authors note that "more powerful mod- els ( e.g., GPT-4o) exhibit greater performance gains"; they hypothesize this is due to stronger models' superior self-evaluation capabilities during refinement. No effect size is printed.

> "We observe that more powerful mod- els ( e.g., GPT-4o) exhibit greater performance gains with our method."

### Tao Wu 2025 (2)

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997

`q2 · i?` · `design · r2`

Boundary condition reported in Section 5.2: low-quality behavior descriptions can mislead the refinement process, causing the model to iteratively adjust solutions in the wrong direction and degrade simulation quality.

> "we find that in some cases—particularly when behavior prediction quality is low—it underperforms compared to IO or CoT prompting."

## Discussion


## Related Claims
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — a narrower finding that bears on this claim
