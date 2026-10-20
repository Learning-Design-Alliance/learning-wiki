---
type: claim
title: Behavior-prediction accuracy rises with more past learning records, reaching 0.94 at 40 records
description: Behavior-prediction accuracy rises with more past learning records, reaching 0.94 at 40 records
id: more-past-records-improve-simulation-accuracy
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
---

# Behavior-prediction accuracy rises with more past learning records, reaching 0.94 at 40 records

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Increasing past learning records from 10 to 40 consistently improves behavior prediction and solution simulation, with accuracy reaching 0.94 at 40 records. [→ Tao Wu 2025](#tao-wu-2025)

## Evidence

### Tao Wu 2025

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)

`q2 · i?` · `design · r2`

Analysis of past learning record volumes shown in Figure 4(a), a plotted numerical pattern rather than an analytic derivation. The article attributes the trend to a more comprehensive cognitive prototype; 0.94 is an accuracy, not an effect size.

> "As shown in Figure 4 (a), increasing the number of past learning records from 10 to 40 leads to con- sistent improvements in both behavior prediction and solution simulation. Specifically, the behav- ior prediction accuracy reaches 0.94 at 40 records, marking a substantial improvement."

## Discussion


## Related Claims
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
- [Knowledge-graph prototype mapping outperforms existing behavior-prediction baselines for student simulation](prototype-mapping-outperforms-behavior-prediction-baselines.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior](self-consistency-does-not-imply-student-alignment.md) — related
