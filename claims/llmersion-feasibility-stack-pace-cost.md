---
type: claim
title: A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour
description: A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour
id: llmersion-feasibility-stack-pace-cost
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: guo-2026
    resource: "https://arxiv.org/abs/2609.29672"
    title: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672"
    author: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X."
    q: 1
    i: "?"
    kind: design
    rigour: 1
  - id: guo-2026-2
    resource: "https://arxiv.org/abs/2609.29672"
    title: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672"
    author: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X."
    q: 1
    i: "?"
    kind: design
    rigour: 1
  - id: guo-2026-3
    resource: "https://arxiv.org/abs/2609.29672"
    title: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672"
    author: "Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X."
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r1` · `q1`

## Subclaims
`q1 i?` The complete four-skill stack totals under 4 GB, inside the 8-16 GB of the cheapest new laptops. [→ Guo 2026](#guo-2026)
`q1 i?` Community measurements report a 3B model at roughly 4-9 tokens per second on an $80 single-board computer and 5-15 tokens per second on the entry laptop CPU class, at or above the roughly four words per second of silent reading. [→ Guo 2026 (2)](#guo-2026-2)
`q1 i?` At the 2024 average US residential electricity price, a device drawing 15 W during study costs about a quarter of one US cent per study hour. [→ Guo 2026 (3)](#guo-2026-3)

## Evidence

### Guo 2026

Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672

`q1 · i?` · `design · r1`

This is the article's feasibility synthesis (Section 5.5, Table 3), a descriptive sizing argument from published file and model-card figures, not a measured experiment. It states "The complete four-skill stack totals under 4 GB, inside the 8–16 GB of the cheapest new laptops." No effect size applies.

> "The complete four-skill stack totals under 4 GB, inside the 8–16 GB of the cheapest new laptops."

### Guo 2026 (2)

Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672

`q1 · i?` · `design · r1`

The article reports attributed community throughput measurements, explicitly noting no peer-reviewed benchmark exists for LLM inference on the cheapest CPUs. It benchmarks against "silent reading averages 238 words per minute, about four words per second". Throughput figures are descriptive; impact is null.

> "reproducible community tables report a 3B model at roughly 4–9 tokens per second on an $80 single- board computer and 5–15 tokens per second on the entry laptop CPU class"

### Guo 2026 (3)

Guo, Q., Tang, J., Huang, X., Lin, H.-Y., Zhong, Y., & Zhuang, X. (2026). LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity. https://arxiv.org/abs/2609.29672

`q1 · i?` · `design · r1`

The article's cost derivation at the 2024 average US residential electricity price of 16.5 cents per kWh: "a device drawing 15 W during study ... costs about a quarter of one US cent per study hour". The arithmetic is the authors' own from cited inputs; no effect size applies.

> "a device drawing 15 W during study, the measured envelope of entry CPUs under inference (Shah, 2026), costs about a quarter of one US cent per study hour"

## Discussion


## Related Claims
- [Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05](clst-finetuning-compute-cost.md) — related
- [The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference](elevate-local-two-machine-low-latency-deployment.md) — related
- [The linearity bias heuristic enables robust alignment with low-dimensional embeddings on standard CPUs, lowering computational prerequisites](linearity-bias-lowers-computational-prerequisites.md) — related
