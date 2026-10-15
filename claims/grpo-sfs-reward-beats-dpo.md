---
type: claim
title: GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall
description: GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall
id: grpo-sfs-reward-beats-dpo
status: draft
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
    rigour: 2
---

# GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across three of four settings, GRPO increases targeted-feedback flip rate while maintaining or reducing misaligned flip rate relative to SFT, achieving the highest SFS overall; DPO produces only modest changes over SFT. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)

`q2 · i?` · `causal · r2`

Post-training comparison of DPO and GRPO on Qwen3-4B and Llama3.1-8B-Instruct across Malrule and EEDI (Figure 5); the text states GRPO "achieving the highest SFS overall" in three of four settings.

> "GRPO, by contrast, yields more consistent improvements: across three of four settings, GRPO increasesFT while maintaining or reducingFM relative to SFT, achieving the highest SFS overall."

## Discussion


## Related Claims
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other](sfs-post-training-cross-domain-generalization.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — a narrower finding that bears on this claim
- [Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back](sycophancy-limits-genai-pushback.md) — related
