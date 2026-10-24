---
type: claim
title: The v2 synthetic generator was tuned for stricter trace-data realism with more incorrect code, retries, and longer dialogues
description: The v2 synthetic generator was tuned for stricter trace-data realism with more incorrect code, retries, and longer dialogues
id: astra-v2-generator-stricter-realism
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: solomon-sunday-oyelere-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100633"
    title: "Solomon Sunday Oyelere. (2026). ASTRA: A synthetic benchmark for trace-based evaluation of socially intelligent multi-agent tutoring and participation-balanced collaboration in introductory programming. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100633"
    author: Solomon Sunday Oyelere
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The v2 synthetic generator was tuned for stricter trace-data realism with more incorrect code, retries, and longer dialogues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The v2 generator encodes increased prevalence of incorrect final code, more iterative retries before success, and longer dialogues, especially in pair conditions, with added cross-session variance. [→ Solomon Sunday Oyelere 2026](#solomon-sunday-oyelere-2026)

## Evidence

### Solomon Sunday Oyelere 2026

Solomon Sunday Oyelere. (2026). ASTRA: A synthetic benchmark for trace-based evaluation of socially intelligent multi-agent tutoring and participation-balanced collaboration in introductory programming. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100633

`q1 · i?` · `design · r2`

Design description of the synthetic data generator (Section 4.3): it was tuned so traces include "increased prevalence of incorrect final code" and "more iterative retries prior to success", adding variance to challenge trace-based inference. No statistics are printed.

> "the v2 gen­ erator was tuned for stricter realism in the sense relevant to trace data: increased prevalence of incorrect final code, more iterative retries prior to success, and longer dialogues (especially in pair conditions), with additional variance across sessions to avoid unrealistically clean patterns."

## Discussion


## Related Claims
- [The ASTRA benchmark yields measurable condition-differentiated patterns consistent with its simulation assumptions](astra-benchmark-yields-condition-differentiated-patterns.md) — related
- [Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs](fine-tuning-limited-gains-hand-drawn-tasks.md) — related
