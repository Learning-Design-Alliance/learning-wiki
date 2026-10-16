---
type: claim
title: "TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model"
description: "TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model"
id: tei4-selects-deliberation-rich-candidates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: schoenfeld-tei-1
    resource: "https://doi.org/10.48550/arxiv.2605.30666"
    title: schoenfeld-tei-1
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Starting from the Base R1 candidate pool, TEI@4 raises Explore from 20.3% to 31.1% (+10.8pp) and lowers General by −11.7pp, while Verify is roughly preserved (16.0→16.9%). [→ schoenfeld-tei-1](#schoenfeld-tei-1)

## Evidence

### schoenfeld-tei-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666 [doi:10.48550/arxiv.2605.30666](https://doi.org/10.48550/arxiv.2605.30666)

`q2 · i?` · `causal · r2`

Schoenfeld phase analysis of thinking-trace paragraphs (Table 9, GPT-4o-mini paragraph classifier at temperature 0): "TEI@4raises Explore by +10.8pp (20.3%→ 31.1%)". Aligned GRPO instead drops Verify to 5.6% and raises General to 73.2%. No effect size printed.

> "Starting from the Base R1 candidate pool,TEI@4raises Explore by +10.8pp (20.3%→ 31.1%) and lowers General by−11.7pp, reaching a deeper deliberation density without changing the model."

## Discussion


## Related Claims
- [TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base](tei-selection-raises-improvement-rate-pre-incorrect.md) — related
- [On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost](tei4-beats-dtr4-and-greedy-same-base.md) — related
