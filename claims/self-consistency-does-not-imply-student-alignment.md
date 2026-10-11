---
type: claim
title: "High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior"
description: "High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior"
id: self-consistency-does-not-imply-student-alignment
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

# High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Prompting-based models achieve high self-consistency (86.9%-99.0%), with GPT-5 highest, yet GPT-5 performs among the worst at reproducing realistic student code trajectories. [→ Rose Niousha 2026](#rose-niousha-2026)

## Evidence

### Rose Niousha 2026

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492

`q2 · i?` · `design · r2`

Self-consistency evaluation (Table 4) measuring alignment between each model's generated internal dialogue and its own generated code diff, on test_OP and test_NP. The article concludes that "strong consistency between a model's reasoning and its own generated code does not necessarily imply alignment with real student reasoning or behavior," since GPT-5 is among the worst on action fidelity. INSIDE achieves 83.0%-87.3%.

> "Prompting-based models achieve high self-consistency scores (86.9%–99.0% across both test sets), with GPT-5 attaining the highest scores."

## Discussion


## Related Claims
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](inside-highest-reasoning-alignment-57-9.md) — related
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](inside-lowest-wasserstein-action-fidelity-test-op.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
