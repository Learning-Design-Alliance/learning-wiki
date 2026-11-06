---
type: claim
title: Reasoning models performed best for case generation but were unsuitable for real-time patient simulation due to long response latency
description: Reasoning models performed best for case generation but were unsuitable for real-time patient simulation due to long response latency
id: reasoning-models-latency-unsuitable-simulator
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: maimaris-s-2026
    resource: "https://doi.org/10.1186/s12909-026-09709-3"
    title: "Maimaris S, Tedino G, Memoli GA, Crisciotti C, Albrizio A, Sammartino C, Bartolotta E, Massetti G, Mantica G, Minerba P, Biagi F, Schiepatti A. (2026). Development and pilot evaluation of a large language model-based clinical simulation system for medical education in gastroenterology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09709-3"
    author: Maimaris S, Tedino G, Memoli GA, Crisciotti C, Albrizio A, Sammartino C, Bartolotta E, Massetti G, Mantica G, Minerba P, Biagi F, Schiepatti A.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Reasoning models performed best for case generation but were unsuitable for real-time patient simulation due to long response latency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Reasoning models (e.g. Gemini-2.5-pro, o4-mini) gave the highest-quality case generation but response latency over 30 seconds made them unsuitable for the interactive simulator role. [→ Maimaris S 2026](#maimaris-s-2026)

## Evidence

### Maimaris S 2026

Maimaris S, Tedino G, Memoli GA, Crisciotti C, Albrizio A, Sammartino C, Bartolotta E, Massetti G, Mantica G, Minerba P, Biagi F, Schiepatti A. (2026). Development and pilot evaluation of a large language model-based clinical simulation system for medical education in gastroenterology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09709-3

`q1 · i?` · `design · r2`

Development-phase preliminary testing observation (April 2025) comparing several open-weights and proprietary LLMs for the two system roles; reported as the authors' testing observation, not a controlled experiment.

> "However, they were not suitable for use for the clinical simulator part of the system mainly due to long response latency (> 30s) due to the 'thinking time' that these models require before responding."

## Discussion


## Related Claims
- [Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier](code-augmented-latency-cost-increases.md) — related
- [Gemini Flash 2.0 was selected for production over GPT-4o-mini and Llama 3.1 for its superior faithfulness and speed-to-cost ratio](gemini-flash-2-selected-for-faithfulness-and-cost.md) — related
- [Asynchronous concurrent execution bounds overall latency to approximately the slowest individual model's inference time](async-concurrency-latency-bounded-by-slowest-model.md) — related
- [In the developers' comparison tests, GPT-4 outperformed GPT-3.5 and Gemini in response generation time, role-playing ability, and validity of generated feedback](gpt4-outperformed-gpt35-gemini-vsp-testing.md) — related
