---
type: claim
title: "Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage"
description: "Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage"
id: scale-alone-does-not-induce-socratic-behavior
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: xiaokun-wang-2026
    resource: "https://arxiv.org/abs/2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Qwen-72B-Direct without task-specific alignment reaches SE=0.000 and leakage of 96.7% on the 30-question test set. [→ Xiaokun Wang 2026](#xiaokun-wang-2026)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996

`q2 · i?` · `causal · r1`

Scale-baseline condition in the same 30-question simulated evaluation (Table 3). The article reports "Qwen-72B without task-specific alignment achieves 0%SE and 96.7% leakage", matching the direct-answerer failure mode.

> "Qwen-72B without task-specific alignment achieves 0%SE and 96.7% leakage, matching the direct-answering failure observed in the unaligned API baseline rather than the prompted PT-Base system."

## Discussion


## Related Claims
- [Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs](llm-scale-does-not-predict-tutor-safety.md) — a broader claim this one bears on
- [Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject](single-turn-answer-disclosure-challenge-near-zero.md) — related
