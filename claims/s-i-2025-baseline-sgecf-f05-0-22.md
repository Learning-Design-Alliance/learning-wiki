---
type: claim
title: The baseline SGECF system detects and labels learner error types at an overall ERRANT F0.5 of 0.22, with preposition replacement errors best detected
description: The baseline SGECF system detects and labels learner error types at an overall ERRANT F0.5 of 0.22, with preposition replacement errors best detected
id: s-i-2025-baseline-sgecf-f05-0-22
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mengjie-qian-2025
    resource: "https://doi.org/10.21437/slate.2025-9"
    title: "Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls. (2025). Speak & Improve Challenge 2025: Tasks and Baseline Systems. [doi:10.21437/slate.2025-9](https://doi.org/10.21437/slate.2025-9)"
    author: Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The baseline SGECF system detects and labels learner error types at an overall ERRANT F0.5 of 0.22, with preposition replacement errors best detected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the SGECF feedback task, the baseline achieves overall ERRANT F0.5 of 0.22 (P 0.37, R 0.08), with R:PREP highest (F0.5 0.416) and R:VERB lowest among listed types (F0.5 0.087). [→ Mengjie Qian 2025](#mengjie-qian-2025)

## Evidence

### Mengjie Qian 2025

Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls. (2025). Speak & Improve Challenge 2025: Tasks and Baseline Systems. [doi:10.21437/slate.2025-9](https://doi.org/10.21437/slate.2025-9)

`q2 · i?` · `design · r2`

Baseline system evaluation: the SGECF baseline is the same cascade as SGEC, but evaluated against MaxMatch (M2) references using ERRANT F0.5. Overall F0.5 is 0.22; per-type F0.5 ranges from 0.416 (R:PREP) down to 0.087 (R:VERB, R:NOUN), with recall of 0.08 overall.

> "Table 6: Baseline SGECF results on Dev set."

## Discussion


## Related Claims
- [Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality](reference-alignment-boosts-sgec-feedback-f05.md) — related
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
- [Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline](edit-confidence-filtering-improves-feedback-f05.md) — related
