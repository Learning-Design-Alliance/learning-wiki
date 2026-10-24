---
type: claim
title: The three system architectures differ sharply in computational cost, with MAS-CMD trading the highest rubric scores for the greatest latency and token usage
description: The three system architectures differ sharply in computational cost, with MAS-CMD trading the highest rubric scores for the greatest latency and token usage
id: quality-efficiency-tradeoff-mas-architectures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: jiayi-wang-2025
    resource: "https://doi.org/10.48550/arxiv.2508.16659"
    title: "Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper. (2025). Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design. https://arxiv.org/abs/2508.16659 [doi:10.48550/arxiv.2508.16659](https://doi.org/10.48550/arxiv.2508.16659)"
    author: Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The three system architectures differ sharply in computational cost, with MAS-CMD trading the highest rubric scores for the greatest latency and token usage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SAS was fastest and lightest (25±16 s; ~3.4k tokens; one request), MAS-Roles required roughly 3× the time and ~7× the tokens, and MAS-CMD used 272±168 s, ~71.6k tokens, and 13 requests. [→ Jiayi Wang 2025](#jiayi-wang-2025)

## Evidence

### Jiayi Wang 2025

Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper. (2025). Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design. https://arxiv.org/abs/2508.16659 [doi:10.48550/arxiv.2508.16659](https://doi.org/10.48550/arxiv.2508.16659)

`q2 · i?` · `causal · r1`

Descriptive operational-efficiency analysis of generation statistics by system (Table 3). The article reports SAS at 25±16 s with ~3.4k tokens and one request, MAS-Roles at roughly 3× time and ~7× tokens, and "substantially greater latency and usage" for MAS-CMD.

> "MAS-CMD traded the highest rubric scores for substantially greater latency and usage (272±168 s;∼71.6k tokens; 13 requests)."

## Discussion


## Related Claims
- [Teachers qualitatively preferred MAS-CMD activities for creativity, real-world context, and classroom-ready completeness](teachers-prefer-mas-cmd-creativity-context-completeness.md) — related
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](llm-judge-small-incremental-differences-ceiling.md) — related
