---
type: claim
title: "LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades"
description: "LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades"
id: llm-high-consensus-agreement-circularity-risk
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: marcin-jukiewicz-2025
    resource: "https://doi.org/10.48550/arxiv.2509.26483"
    title: "Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)"
    author: Marcin Jukiewicz
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the majority-vote grade across the 18 models was the reference, most models reached ICC values above 0.8 (highest gpt-4.1-mini at 0.892), while gpt-4.1-nano (0.599) and claude-haiku-3.5 (0.664) diverged most. [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)

`q2 · i?` · `associational · r2`

Analysis using the most frequent grade across the 18 models as the reference (Table 6). The study reports "Most models reached ICC values above 0.8, indicating good agreement with the consensus", with the lowest values for gpt-4.1-nano (0.599) and claude-haiku-3.5 (0.664).

> "The highest agreement with this consensus grade was obtained
by gpt-4.1-mini (ICC = 0.892), followed closely by claude-opus-4.1 (0.888)
and gpt-5-mini (0.877). Most models reached ICC values above 0.8, indicat-
ing good agreement with the consensus."

## Discussion


## Related Claims

- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — related
- [Teachers systematically assign higher grades than all evaluated LLM grading models](teachers-grade-higher-than-all-llm-models.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md)
