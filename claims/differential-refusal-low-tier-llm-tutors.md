---
type: claim
title: "Safety-aligned LLM tutors refuse educational requests asymmetrically, with low-resource students facing the highest refusal rates (76.7% vs 62.2%)"
description: "Safety-aligned LLM tutors refuse educational requests asymmetrically, with low-resource students facing the highest refusal rates (76.7% vs 62.2%)"
id: differential-refusal-low-tier-llm-tutors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexis-popovici-2026
    resource: "https://doi.org/10.48550/arxiv.2607.11292"
    title: "Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran. (2026). The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students. arXiv preprint. https://arxiv.org/abs/2607.11292 [doi:10.48550/arxiv.2607.11292](https://doi.org/10.48550/arxiv.2607.11292)"
    author: Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Safety-aligned LLM tutors refuse educational requests asymmetrically, with low-resource students facing the highest refusal rates (76.7% vs 62.2%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Kimi K2 refuses or errors on 76.7% of requests from Low Tier students versus 62.2% for Roma Minority and Romanian baseline profiles, a 14.5 percentage-point gap. [→ Alexis Popovici 2026](#alexis-popovici-2026)

## Evidence

### Alexis Popovici 2026

Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran. (2026). The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students. arXiv preprint. https://arxiv.org/abs/2607.11292 [doi:10.48550/arxiv.2607.11292](https://doi.org/10.48550/arxiv.2607.11292)

`q2 · i?` · `causal · r2`

Controlled T=0 API audit with n=30 iterations per condition across four LLMs and five personas. The audit found refusal is asymmetric and socio-economic: "resource-poor contexts trigger the highest access barriers" in the heavily safety-aligned Kimi K2 model.

> "Low Tier students face a 76.7% refusal rate, compared to 62.2% for both the Roma Minority and the Romanian baseline. This represents a 14.5 percentage-point gap between the most and least affected profiles."

## Discussion


## Related Claims
- [Deepseek's justification scores vary by student socio-economic profile, with Top Tier students averaging 9.60 versus 6.90 for Low Tier students](elite-hermeneutics-justification-gap.md) — related
- [LLM history tutors reduce marginalized students' access to contested geopolitical framing, with the coup theory appearing in 2.6% of Low Tier responses versus 7.9% for the baseline](epistemic-gatekeeping-coup-gap.md) — related
- [Chinese-developed models lead the safety module, with the refusal gap concentrated on region-specific normative content (difference-in-differences of 28.9 points)](chinese-models-safety-refusal-gap.md) — related
- [LLaMA produces a fivefold higher victimization-to-politics vocabulary ratio for the Roma persona (≈0.15) than for elite peers (≈0.03)](agency-theft-victimization-framing.md) — related
