---
type: claim
title: LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments
description: LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments
id: llms-differ-liberal-restrictive-balanced-grading-styles
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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

# LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Models such as gpt-4o and claude-haiku-3.5 assign high proportions of maximum grades, deepseek-reasoner and gpt-4.1-nano are dominated by failing grades, and models such as claude-sonnet-4 and gemini-2.0-flash-lite extensively use the intermediate 0.5 grade. [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)

`q2 · i?` · `associational · r2`

Descriptive analysis of grade distributions (0, 0.5, 1) across 18 LLMs grading 6,081 programming submissions, shown in Figure 1 and Table 3. The study reports that "Models such as gpt-4o, its mini variant, and claude-haiku-3.5 exhibited a relatively high proportion of maximum scores (1.0)" while deepseek-reasoner and gpt-4.1-nano were dominated by failing grades.

> "Models such as gpt-4o, its mini variant, and claude-haiku-3.5 exhibited a relatively high proportion of maximum scores (1.0), suggesting a more liberal grading approach and a tendency to recognize solutions as correct more frequently."

## Discussion


## Related Claims
- [LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families](llm-grading-vendor-specific-six-clusters.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
