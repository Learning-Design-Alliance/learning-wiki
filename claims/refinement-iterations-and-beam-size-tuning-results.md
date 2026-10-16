---
type: claim
title: Refinement gains stabilize or decline beyond three iterations, and beam-size gains become negligible beyond two samples
description: Refinement gains stabilize or decline beyond three iterations, and beam-size gains become negligible beyond two samples
id: refinement-iterations-and-beam-size-tuning-results
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Refinement gains stabilize or decline beyond three iterations, and beam-size gains become negligible beyond two samples

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Solution simulation improves with more refinement iterations up to L = 3, then stabilizes or slightly declines. [→ Tao Wu 2025](#tao-wu-2025)
`q2 i?` Performance improves as beam size B increases, but gains become negligible beyond B = 2. [→ Tao Wu 2025 (2)](#tao-wu-2025-2)

## Evidence

### Tao Wu 2025

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)

`q2 · i?` · `design · r2`

Grid search over refinement iterations L from 1 to 5 and beam size B from 1 to 3, shown in Figure 4(b). The article reports that when L exceeds 3, performance stabilizes or slightly declines, which it speculates is over-correction.

> "the performance of solution simulation improves with an increasing iteration of refinements, highlighting the limitations of current LLMs in generating accurate student answers in a single pass."

### Tao Wu 2025 (2)

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997

`q2 · i?` · `design · r2`

Same grid search in Section 5.3. The authors set B = 2 to balance performance and simulation cost.

> "A similar trend is observed for the beam sizeB: performance improves asB increases, but the gains become negligible beyond B = 2."

## Discussion


## Related Claims
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
- [Review-revise iterations improve synthesized problem quality, with gains largely stabilizing by the third iteration](review-revise-iterations-quality-stabilizes.md) — related
- [Iterative generate-then-refine with multi-axis critiques raises the share of usable generated simulations from 3.5% after first generation to 69.3% after 10 improvement rounds](generate-then-refine-raises-usable-simulations-3-5-to-69-3.md) — related
