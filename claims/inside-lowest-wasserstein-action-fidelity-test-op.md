---
type: claim
title: Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics
description: Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics
id: inside-lowest-wasserstein-action-fidelity-test-op
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rose-niousha-2026
    resource: "https://arxiv.org/abs/2608.10492"
    title: "Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492"
    author: Rose Niousha, Minwoo Kang, Narges Norouzi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On test_OP, models fine-tuned with INSIDE produce code distributions closest to real student submissions across pass rate, LOC, AST depth/width, and PEP 8 metrics, outperforming both SFT and prompting baselines. [→ Rose Niousha 2026](#rose-niousha-2026)

## Evidence

### Rose Niousha 2026

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492

`q2 · i?` · `design · r2`

Distributional evaluation comparing fine-tuned and prompted LLMs against real student submissions on test_OP (5,262 submissions from Spring 2024 students), reporting Wasserstein distance over pass rate, LOC, AST, and PEP 8 metrics. The article reports INSIDE "consistently achieves the lowest Wasserstein distances across all metrics"; e.g., pass-rate distance 0.05 for INSIDE models vs 0.14-0.15 for SFT.

> "Ontest_OP (Table 1a), INSIDE consistently achieves the lowest Wasserstein distances across all metrics, indicating the closest match to real student code distributions."

## Discussion


## Related Claims
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](inside-highest-reasoning-alignment-57-9.md) — related
- [Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories](prompted-simulators-artificially-high-pass-rates.md) — related
- [High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior](self-consistency-does-not-imply-student-alignment.md) — related
- [Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP](pass-rate-distribution-explains-split-gap.md) — related
- [GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data](gpt-feedback-passes-automated-helpfulness-35-percent.md) — related
