---
type: claim
title: A persistent agentic research environment sustained near-daily use over 115 days, with 75,671 de-duplicated telemetry records across 96 active days (active-day fraction 0.835)
description: A persistent agentic research environment sustained near-daily use over 115 days, with 75,671 de-duplicated telemetry records across 96 active days (active-day fraction 0.835)
id: persistent-agent-96-active-days-75671-records
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: anas-h-alzahrani-2026
    resource: "https://doi.org/10.48550/arxiv.2605.26870"
    title: "Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870 [doi:10.48550/arxiv.2605.26870](https://doi.org/10.48550/arxiv.2605.26870)"
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

# A persistent agentic research environment sustained near-daily use over 115 days, with 75,671 de-duplicated telemetry records across 96 active days (active-day fraction 0.835)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` Over a 115-day observation window, recoverable main-agent telemetry contained 75,671 de-duplicated records across 96 active days, an active-day fraction of 0.835. [→ Anas H. Alzahrani 2026](#anas-h-alzahrani-2026)
`q1 i?` Active system time was estimated at 579.7 hours with a 30-minute capped-gap rule and 674.1 hours with a 60-minute sensitivity rule; these are system-activity estimates, not human labor hours. [→ Anas H. Alzahrani 2026 (2)](#anas-h-alzahrani-2026-2)

## Evidence

### Anas H. Alzahrani 2026

Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870 [doi:10.48550/arxiv.2605.26870](https://doi.org/10.48550/arxiv.2605.26870)

`q1 · i?` · `design · r2`

Descriptive telemetry analysis of recoverable main-agent session records in a single-investigator self-observed case study (Jan 31–May 25, 2026). The article reports "75,671 de-duplicated records" across 96 active days, ADF = 0.835; counts are lower-bound estimates because recoverable telemetry starts February 2.

> "Recoverable main-agent telemetry contained 75,671 de-duplicated records (DRC = 75,671) across 96 active days, corresponding to an active-day fraction of 0.835 (ADF = 96/115; Table 2)."

### Anas H. Alzahrani 2026 (2)

Anas H. Alzahrani, MD, PhD, MPH. (2026). Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study. arXiv preprint. https://arxiv.org/abs/2605.26870

`q1 · i?` · `design · r2`

Capped-gap active-time algorithm applied to sorted unique event timestamps from the same recoverable main-agent telemetry, with a 60-minute cap as sensitivity analysis. The article states these are "system-activity estimates, not direct human labor hours." No effect size is printed.

> "Active system time was 579.7 hours using the primary 30-minute capped-gap estimate (ATE = 579.7 hours) and 674.1 hours using the 60-minute sensitivity estimate."

## Discussion


## Related Claims

- [The memory layer recorded 889 failure, verification, correction, or protocol-proxy events (9.26 per active day), making governance part of the operating environment](governance-889-events-ger-9-26.md) — related
- [The environment produced 482 memory-recorded output-proxy events (5.02 per active day) across 10 artifact-surface categories spanning research, teaching, software, content, and operations](output-proxy-482-events-breadth-10-surfaces.md) — related
- [May 2026 token telemetry was cache-dominant: 82.9% of 73,950,305 recorded tokens were cache reads, suggesting persistent workflows shift the economic unit from cost per token to cost per completed artifact](cache-dominant-82-9-percent-tokens.md) — related
- [Empirical ILE papers show a strong increase in breadth of content and time of use](aied-breadth-increase-topics-time.md) — related
