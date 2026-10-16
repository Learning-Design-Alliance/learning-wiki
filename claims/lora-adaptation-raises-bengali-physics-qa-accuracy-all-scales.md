---
type: claim
title: LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales
description: LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales
id: lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rashid-azraf-jahin-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00664"
    title: "Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)"
    author: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Fine-tuning with a unified LoRA recipe improves every metric at every scale, with accuracy gains of +5.5, +15.0 and +23.3 percentage points at 0.6B, 1.7B and 4B. [→ Rashid Azraf Jahin 2026](#rashid-azraf-jahin-2026)

## Evidence

### Rashid Azraf Jahin 2026

Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)

`q2 · i?` · `causal · r1`

Evaluation on the 275 held-out test questions with greedy decoding, LLM-judge accuracy (Gemini-2.5-Flash-Lite). The 1.7B model's accuracy "is doubled, from 10.5% to 25.5%", and the 4B model reaches 50.9% fine-tuned versus 27.6% raw. No effect sizes are printed.

> "Fine-tuning improves every metric at every scale. The base model, Qwen3-0.6B, is not able to get the correct answer rate on the test set, but following adaptation, the rate becomes 5.5%"

## Discussion


## Related Claims
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](adaptation-gains-grow-with-model-capacity.md) — a broader claim this one bears on
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](model-size-and-lora-rank-joint-effects.md) — related
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](omniedu-general-capability-retained-after-specialization.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — related
