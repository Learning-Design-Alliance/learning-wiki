---
type: claim
title: Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation
description: Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation
id: reasoning-variants-no-alignment-improvement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.00883"
    title: "Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883"
    author: Michael Hardy, Yunsung Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Comparing paired models sharing the same base, additional test-time reasoning produced no measurable improvement on expert-rating or learning-gain alignment, and chain-of-thought prompting findings were similar. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883

`q2 · i?` · `causal · r1`

Paired comparisons in Sec. 5.2 of reasoning variants against their base models (e.g., DeepSeek-R1 vs DeepSeek-V3.1) on both Kendall's tau alignment axes. The article concludes additional reasoning context alone does not repair the core mismatch.

> "we findno measurable improvementon either axis of alignment in Figure 4. Findings comparing the chain-of-thought prompt were similar"

## Discussion


## Related Claims
- [Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers](educlaw-bench-model-harness-interaction.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — reports the opposite
- [Chain-of-thought prompting improved LLM multistep reasoning, operationalized via decomposition and interleaved planning approaches](cot-planning-decomposition-interleaved.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
