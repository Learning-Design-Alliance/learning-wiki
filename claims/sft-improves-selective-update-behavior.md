---
type: claim
title: Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)
description: Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)
id: sft-improves-selective-update-behavior
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2605.12748"
    title: "Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)"
    author: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` SFT on synthetic demonstrations mapping each feedback condition to its ideal response suppresses flips under misaligned and generic feedback while largely preserving flips under targeted feedback, yielding large SFS gains across both models and datasets. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)

`q2 · i?` · `causal · r1`

Post-training experiment on Qwen3-4B and Llama3.1-8B-Instruct across Malrule and EEDI test sets, comparing baseline, SFT, DPO, and GRPO (Figure 5); the printed SFS gains are +0.555, +0.250, +0.447, and +0.090.

> "SFT sharply suppresses flips under misaligned and generic feedback while largely preserving flips under targeted feedback, yielding large SFS gains (Qwen3-4B: +0.555 on Malrule and +0.250 on EEDI; Llama3-8B: +0.447 on Malrule and +0.090 on EEDI)."

## Discussion


## Related Claims
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other](sfs-post-training-cross-domain-generalization.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — a narrower finding that bears on this claim
- [Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back](sycophancy-limits-genai-pushback.md) — related
