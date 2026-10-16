---
type: claim
title: "On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost"
description: "On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost"
id: tei4-beats-dtr4-and-greedy-same-base
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tei4-vs-dtr4-1
    resource: "https://doi.org/10.48550/arxiv.2605.30666"
    title: tei4-vs-dtr4-1
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` TEI@4 raises ΔSol from .180 to .184, lowers Leak from .583 to .572, and improves R_total from .272 to .280, while DTR@4 moves these only marginally (+.000/−.002/+.002). [→ tei4-vs-dtr4-1](#tei4-vs-dtr4-1)

## Evidence

### tei4-vs-dtr4-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666 [doi:10.48550/arxiv.2605.30666](https://doi.org/10.48550/arxiv.2605.30666)

`q2 · i?` · `causal · r2`

Main results comparison (Table 2, Section 4.2) among training-free rows on the DeepSeek-R1-8B base across 1,000 in-domain BigMath scenarios. Differences are small in absolute terms; no effect size printed.

> "On DS-R1 base, TEI@4raises ΔSol from.180to .184, lowers Leak from.583to .572, and improves𝑅tot from.272to .280at no training cost; DTR@4 moves these only marginally (+.000/−.002/+.002)."

## Discussion


## Related Claims
- [DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy](dtr-does-not-predict-tutoring-quality.md) — related
- [TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base](tei-selection-raises-improvement-rate-pre-incorrect.md) — related
- [TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model](tei4-selects-deliberation-rich-candidates.md) — related
