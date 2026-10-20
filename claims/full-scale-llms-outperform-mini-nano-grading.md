---
type: claim
title: Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts
description: Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts
id: full-scale-llms-outperform-mini-nano-grading
status: review
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

# Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Full-scale models outperform their simplified counterparts on human-agreement ICC: gpt-4.1 (0.421) vs gpt-4.1-nano (0.204), gpt-5 (0.378) vs gpt-5-nano (0.314), gpt-4o (0.438) vs gpt-4o-mini (0.365). [→ Marcin Jukiewicz 2025](#marcin-jukiewicz-2025)

## Evidence

### Marcin Jukiewicz 2025

Marcin Jukiewicz. (2025). A systematic comparison of Large Language Models for automated assignment assessment in programming education: Exploring the importance of architecture and vendor. arXiv preprint. https://arxiv.org/abs/2509.26483 [doi:10.48550/arxiv.2509.26483](https://doi.org/10.48550/arxiv.2509.26483)

`q2 · i?` · `associational · r2`

ICC(2,1) comparison with human grades across model size variants (Table 5). The study reports "the full gpt-4.1 (0.421) significantly outperforms gpt-4.1-nano (0.204)" and similar patterns for gpt-5 and gpt-4o families, suggesting reduced model complexity diminishes consistency.

> "For instance, the full gpt-4.1 (0.421) significantly outperforms gpt-4.1-nano (0.204).
Similarly, gpt-5 (0.378) performs better than gpt-5-nano (0.314), and gpt-4o
(0.438) outperforms gpt-4o-mini (0.365)."

## Discussion


## Related Claims
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — related
- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](gpt-4o-mini-lowest-act-balance-mae.md) — related
