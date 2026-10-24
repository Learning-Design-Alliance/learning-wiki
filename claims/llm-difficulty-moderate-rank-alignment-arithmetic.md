---
type: claim
title: LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items
description: LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items
id: llm-difficulty-moderate-rank-alignment-arithmetic
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: la-hadi-2025
    resource: "https://doi.org/10.48550/arxiv.2607.26067"
    title: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)"
    author: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across four LLM systems, Spearman rank correlations with empirical difficulty ranged from 0.52 to 0.77, indicating models capture only the coarse ordering of item difficulty. [→ La Hadi 2025](#la-hadi-2025)

## Evidence

### La Hadi 2025

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)

`q2 · i?` · `associational · r2`

Comparison of difficulty ratings from four LLM systems (four repetitions per item) against CTT and 2PL IRT difficulty from 770 Indonesian undergraduates on 32 arithmetic items. The study reports "moderate rank alignment" with Spearman's ρ = 0.52 – 0.77; similar patterns held for IRT and CTT measures.

> "Across models (32 arithmetic items), LLM predictions show moderate rank alignment with empirical difficulty (Spearman’s ρ = 0.52 – 0.77; Table 1), indicating that models capture coarse ordering of item difficulty."

## Discussion


## Related Claims
- CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations — related
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — a narrower finding that bears on this claim
- [The negative AI-difficulty–performance correlation is stable across exposure-discount values 0 to 0.40, and is strongest with no adjustment](exposure-discount-sensitivity-stable-correlation.md) — related
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — reports the opposite
- [LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families](llm-grading-vendor-specific-six-clusters.md) — related
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](proxy-alignment-not-impact-alignment-llm-classroom.md) — related
- [LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set](llm-fraction-predictions-run-to-run-instability.md) — related
- [Item-difficulty orderings diverge across cohorts, with the weakest correlation between academics and students (r = 0.188) and no stable shared developmental hierarchy](cohort-difficulty-ordering-correlations-diverge.md) — related
