---
type: claim
title: "May 2026 token telemetry was cache-dominant: 82.9% of 73,950,305 recorded tokens were cache reads, suggesting persistent workflows shift the economic unit from cost per token to cost per completed artifact"
description: "May 2026 token telemetry was cache-dominant: 82.9% of 73,950,305 recorded tokens were cache reads, suggesting persistent workflows shift the economic unit from cost per token to cost per completed artifact"
id: cache-dominant-82-9-percent-tokens
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: anas-h-alzahrani-2026
    resource: "https://arxiv.org/abs/2605.26870"
    title: "Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870"
    author: Anas H. Alzahrani, MD, PhD, MPH
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: anas-h-alzahrani-2026-2
    resource: "https://arxiv.org/abs/2605.26870"
    title: "Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870"
    author: Anas H. Alzahrani, MD, PhD, MPH
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# May 2026 token telemetry was cache-dominant: 82.9% of 73,950,305 recorded tokens were cache reads, suggesting persistent workflows shift the economic unit from cost per token to cost per completed artifact

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` In the strict May 1–May 25 trajectory subset (627 model-completed events), cache-read tokens represented 61,278,669 of 73,950,305 recorded tokens, a cache-dominance ratio of 0.829. [→ Anas H. Alzahrani 2026](#anas-h-alzahrani-2026)
`q1 i?` The author interprets the cache-heavy profile as evidence that persisted context was central to the workflow and that per-token accounting alone is a poor proxy for value. [→ Anas H. Alzahrani 2026 (2)](#anas-h-alzahrani-2026-2)

## Evidence

### Anas H. Alzahrani 2026

Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870

`q1 · i?` · `design · r2`

Token-telemetry analysis of the strict May 1–May 25 model-completed trajectory subset (627 events) in the single-investigator case study. The article states token telemetry is usage telemetry, not invoice cost, and covers only a partial month.

> "Cache-read tokens represented 61,278,669 of the total, yielding a cache-dominance ratio of 0.829 (CDR = 82.9%), compared with 10,697,394 input tokens, 754,633 output tokens, and 1,219,609 cache-write tokens."

### Anas H. Alzahrani 2026 (2)

Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870

`q1 · i?` · `design · r2`

Authors' interpretation (type e) of the cache-dominance finding in the Resource Profile section, attributed to reused context rather than isolated fresh inference. Provider routes included OpenAI Codex-route, OpenAI-route, and Anthropic-route usage.

> "The cache-heavy profile is an empirical signal that persisted context was central to the workflow. It also shows why per-token accounting alone is a poor proxy for value."

## Discussion


## Related Claims
- [Within May completions, cache-read tokens per completion were positively associated with output tokens per completion (Pearson r = 0.47 on log-transformed counts; Spearman rho = 0.70)](cache-read-output-positive-association.md) — related
- [Human-written AGENTS.md context files improve agent performance by approximately 4 per cent, while LLM-generated context files decrease performance by 3 per cent and increase token cost by over 20 per cent, as the article reports citing recent research](agents-md-human-written-context-files-improve-agent-performance.md) — related
- [The memory layer recorded 889 failure, verification, correction, or protocol-proxy events (9.26 per active day), making governance part of the operating environment](governance-889-events-ger-9-26.md) — related
- [A persistent agentic research environment sustained near-daily use over 115 days, with 75,671 de-duplicated telemetry records across 96 active days (active-day fraction 0.835)](persistent-agent-96-active-days-75671-records.md) — related
