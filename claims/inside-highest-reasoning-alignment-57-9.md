---
type: claim
title: "INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%"
description: "INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%"
id: inside-highest-reasoning-alignment-57-9
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rose-niousha-2026
    resource: "https://doi.org/10.48550/arxiv.2608.10492"
    title: "Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492 [doi:10.48550/arxiv.2608.10492](https://doi.org/10.48550/arxiv.2608.10492)"
    author: Rose Niousha, Minwoo Kang, Narges Norouzi
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: rose-niousha-2026-2
    resource: "https://arxiv.org/abs/2608.10492"
    title: "Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492"
    author: Rose Niousha, Minwoo Kang, Narges Norouzi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` On test_NP, Qwen3-8B-INSIDE reaches 57.9% alignment versus 56.0% for the strongest BloomCoT prompting model; on test_OP, Qwen2.5-7B-INSIDE reaches 51.8% versus 49.6% for the best prompting baseline. [→ Rose Niousha 2026](#rose-niousha-2026)
`q2 i?` The LLM-judge alignment metric was validated against human annotations, achieving 88.0% agreement (kappa = 0.754). [→ Rose Niousha 2026 (2)](#rose-niousha-2026-2)

## Evidence

### Rose Niousha 2026

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492 [doi:10.48550/arxiv.2608.10492](https://doi.org/10.48550/arxiv.2608.10492)

`q2 · i?` · `design · r2`

Evaluation of Experiment 2 models on test_NP (1,054 submissions) using an LLM judge that decomposes generated internal dialogue into atomic claims checked against ground-truth code diffs. The article reports Qwen3-8B-INSIDE "achieves 57.9% compared to 56.0% for the strongest BloomCoT model"; test_NP has larger standard errors (~2.0-2.3).

> "Ontest_NP, Qwen3-8B-INSIDE achieves 57.9% compared to 56.0% for the strongest BloomCoT model."

### Rose Niousha 2026 (2)

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492

`q2 · i?` · `design · r2`

Validation study of the alignment metric: 25 generated internal dialogues were manually annotated for whether each extracted claim was reflected in the corresponding code edit. The article reports "88.0% agreement with the LLM judge labels ( κ= 0.754)"; a separate teacher-trace check (n=209) yielded 95.2% average alignment.

> "The manual annotations achieved 88.0% agreement with the LLM judge labels ( κ= 0.754), indicating substantial agreement between the LLM judge and human annotations."

## Discussion


## Related Claims
- [Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories](prompted-simulators-artificially-high-pass-rates.md) — related
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](inside-lowest-wasserstein-action-fidelity-test-op.md) — related
- [High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior](self-consistency-does-not-imply-student-alignment.md) — related
- [Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP](pass-rate-distribution-explains-split-gap.md) — related
