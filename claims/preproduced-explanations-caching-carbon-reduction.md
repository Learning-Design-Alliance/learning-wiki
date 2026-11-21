---
type: claim
title: Pre-producing LLM explanations enables significant caching and a negligible operational carbon footprint
description: Pre-producing LLM explanations enables significant caching and a negligible operational carbon footprint
id: preproduced-explanations-caching-carbon-reduction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: boris-ruf-2024
    resource: "https://doi.org/10.1109/ism63611.2024.00064"
    title: "Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. [doi:10.1109/ism63611.2024.00064](https://doi.org/10.1109/ism63611.2024.00064)"
    author: Boris Ruf, Marcin Detyniecki
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: boris-ruf-2024-2
    resource: "https://doi.org/10.1109/ism63611.2024.00064"
    title: "Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. [doi:10.1109/ism63611.2024.00064](https://doi.org/10.1109/ism63611.2024.00064)"
    author: Boris Ruf, Marcin Detyniecki
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pre-producing LLM explanations enables significant caching and a negligible operational carbon footprint

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Because explanations depend only on the timestamp and are the same for all users, LLM-powered applications like this one are subject to significant caching. [→ Boris Ruf 2024](#boris-ruf-2024)
`q2 i?` During operation the application loads text via lightweight HTTP requests with a negligible carbon footprint compared to running LLM inference. [→ Boris Ruf 2024 (2)](#boris-ruf-2024-2)

## Evidence

### Boris Ruf 2024

Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. [doi:10.1109/ism63611.2024.00064](https://doi.org/10.1109/ism63611.2024.00064)

`q2 · i?` · `design · r2`

Authors' environmental analysis of their prototype's architecture: the linear dependence of explanations on the timestamp, shared by all users, makes significant caching possible; queries can be scheduled in regions with low carbon factors at off-peak times.

> "the presented application shows a rare use case where the utilization of LLMs can be subject to significant caching. This is due to the linear nature of the approach, where the explanation depends only on the timestamp, but is the same for all users."

### Boris Ruf 2024 (2)

Boris Ruf, Marcin Detyniecki. (2024). The «Huh?» Button: Improving Understanding in Educational Videos with Large Language Models. [doi:10.1109/ism63611.2024.00064](https://doi.org/10.1109/ism63611.2024.00064)

`q2 · i?` · `design · r2`

The authors report that during operation the prototype only serves pre-produced text over HTTP, which they state has a negligible carbon footprint compared to using LLM models; no measured operational emissions figure is printed.

> "During operation, interaction is only based on lightweight HTTP requests loading text, which has a negligible carbon footprint compared to using LLM models."

## Discussion


## Related Claims
- [Measured inference-phase carbon emissions of 150.7 kg CO2e for one lecture and 209.4 kg CO2e for another](llm-inference-emissions-huh-button-development.md) — related
- [Interacting with an eco-feedback LLM interface surfaces gaps in students' understanding of digital sustainability and supports learning about the environmental impact of everyday LLM use](eco-feedback-interface-supports-sustainability-learning.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
