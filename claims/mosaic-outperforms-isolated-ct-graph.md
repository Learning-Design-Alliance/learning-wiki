---
type: claim
title: "Communicating MOSAIC agents outperform isolated agents on the 28-task image sequence learning benchmark, with relative gains of 170.8%"
description: "Communicating MOSAIC agents outperform isolated agents on the 28-task image sequence learning benchmark, with relative gains of 170.8%"
id: mosaic-outperforms-isolated-ct-graph
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: saptarshi-nath-2026
    resource: "https://doi.org/10.1609/aaai.v40i29.39633"
    title: "Saptarshi Nath, Christos Peridis, Eseoghene Benjamin, Xinran Liu, Soheil Kolouri, Peter Kinnell, Zexin Li, Cong Liu, Shirin Dora, Andrea Soltoggio. (2026). Policy Search, Retrieval, and Composition via Task Similarity in Collaborative Agentic Systems. [doi:10.1609/aaai.v40i29.39633](https://doi.org/10.1609/aaai.v40i29.39633)"
    author: Saptarshi Nath, Christos Peridis, Eseoghene Benjamin, Xinran Liu, Soheil Kolouri, Peter Kinnell, Zexin Li, Cong Liu, Shirin Dora, Andrea Soltoggio
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Communicating MOSAIC agents outperform isolated agents on the 28-task image sequence learning benchmark, with relative gains of 170.8%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On the CT-graph image sequence learning benchmark, MOSAIC learns significantly faster and more broadly than MOSAIC-NoComm, outperforming it by 2.7x and failing on only 2 of 28 tasks versus 18 for isolated agents. [→ Saptarshi Nath 2026](#saptarshi-nath-2026)

## Evidence

### Saptarshi Nath 2026

Saptarshi Nath, Christos Peridis, Eseoghene Benjamin, Xinran Liu, Soheil Kolouri, Peter Kinnell, Zexin Li, Cong Liu, Shirin Dora, Andrea Soltoggio. (2026). Policy Search, Retrieval, and Composition via Task Similarity in Collaborative Agentic Systems. [doi:10.1609/aaai.v40i29.39633](https://doi.org/10.1609/aaai.v40i29.39633)

`q2 · i?` · `causal · r2`

Simulation study on the CT-graph image sequence learning benchmark: 28 tasks, five seeds per task, averaged over 140 runs with 95% confidence intervals. MOSAIC reaches 50% performance in 37 iterations (18,944 steps) while MOSAIC-NoComm plateaus at a maximum of 9.6; "On average, MOSAIC-NoComm fails on 18 tasks, whereas MOSAIC fails on only 2."

> "Results in Figure 2(A) show that MOSAIC achieves significantly faster learning and broader task coverage, outperforming MOSAIC-NoComm (no sharing among agents) by 2.7×, reaching a maximum total return of 26.0 across all 28 tasks."

## Discussion


## Related Claims
- Ablations show similarity-based selection, performance-based selection, and reward-guided initialization each contribute to MOSAIC's performance or stability — related
- Cosine similarity on Wasserstein task embeddings reconstructs task group structure, and policy reuse weights align with task similarity after fine-tuning — related
