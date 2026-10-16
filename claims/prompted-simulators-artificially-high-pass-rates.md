---
type: claim
title: "Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories"
description: "Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories"
id: prompted-simulators-artificially-high-pass-rates
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

# Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Real students start with low pass rates and improve sharply near final steps; prompting-based models maintain high pass rates from the beginning, whereas fine-tuned models closely track this trajectory. [→ Rose Niousha 2026](#rose-niousha-2026)
`q2 i?` On test_OP_1, the three lowest-MAE models against student pass-rate trajectories are all INSIDE models (0.094, 0.098, 0.113). [→ Rose Niousha 2026 (2)](#rose-niousha-2026-2)

## Evidence

### Rose Niousha 2026

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492 [doi:10.48550/arxiv.2608.10492](https://doi.org/10.48550/arxiv.2608.10492)

`q2 · i?` · `design · r2`

Pass-rate trajectory analysis over submission steps (Figure 2) on representative problems test_OP_1 and test_NP_1, comparing fine-tuned and prompted models to real students. The article reports real students "start with low pass rates and exhibit a sharp increase near the final steps" while prompted models stay near 80% throughout.

> "In contrast, prompting-based models maintain relatively high pass rates ( ≈ 80%) from the beginning, with little variation across steps."

### Rose Niousha 2026 (2)

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492

`q2 · i?` · `design · r2`

Mean Absolute Error between model and student pass rates averaged over steps on test_OP_1 (n=968 submissions). The article reports the top three models are all INSIDE variants; on test_NP_1 the closest models are Qwen2.5-Coder-7B-INSIDE (0.162), Qwen2.5-7B-SFT (0.181), and Qwen2.5-7B-INSIDE (0.182).

> "Ontest_OP_1, the top three models are Qwen3-8B-INSIDE (0.094), Qwen2.5-Coder-7B-INSIDE (0.098), and Qwen2.5-7B-INSIDE (0.113)."

## Discussion


## Related Claims
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](inside-highest-reasoning-alignment-57-9.md) — related
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](inside-lowest-wasserstein-action-fidelity-test-op.md) — related
- [Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP](pass-rate-distribution-explains-split-gap.md) — related
- [ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors](profilerl-outperforms-student-simulation-baselines.md) — related
- [Immediate post-feedback improvement is near zero on average and does not differ significantly across feedback conditions](baseline-post-feedback-gains-near-zero-no-condition-differences.md) — related
- [GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data](gpt-feedback-passes-automated-helpfulness-35-percent.md) — related
