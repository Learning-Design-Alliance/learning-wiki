---
type: claim
title: Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone
description: Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone
id: model-family-beats-parameter-count-for-tutoring-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: h-chad-lane-2026
    resource: "https://github.com/InviteInstitute/CSTutorBench"
    title: "H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench"
    author: H. Chad Lane, Bryson Kageler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Within the 11-model sample, qwen3.5 at 9B parameters (79%) outperformed the 120B nemotron-3-super (73%), and deepseek-r1 at 8B (77%) scored well above the 30B qwen3-coder (52%), suggesting family-level differences influence tutoring quality better than size alone. [→ H. Chad Lane 2026](#h-chad-lane-2026)

## Evidence

### H. Chad Lane 2026

H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench

`q2 · i?` · `design · r2`

Comparison of overall Trial 2 scores across 11 models from six families (Table 2). The top three were gemma-4:31b (89%), qwen3.5:9b (79%), and qwen3.6 (78%); the weakest included olmo-3:7b (49%) and gemma3:4b (50%). The authors state they cannot cleanly disentangle family, instruction tuning, and parameter count with only 11 models.

> "Notably, qwen3.5 achieves this with only 9B parameters, outperforming the 120B nemotron-3-super (73%) by 6 percentage points."

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — a narrower finding that bears on this claim
- [A research-grounded prompt revision improved scores for 10 of 11 models, with gains of 6.6 to 16.2 percentage points](prompt-revision-improves-tutoring-scores-ten-of-eleven.md) — related
