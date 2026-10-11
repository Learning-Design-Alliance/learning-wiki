---
type: claim
title: LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback
description: LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback
id: llm-simulators-near-zero-sfs-indiscriminate-flipping
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://arxiv.org/abs/2605.12748"
    title: "Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748"
    author: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across seven LLMs (4B–120B), two datasets, and base/reflective prompting, SFS remains close to zero, with targeted feedback producing almost no additional behavioral change beyond contrastive controls. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748

`q2 · i?` · `causal · r2`

Simulation-based evaluation of seven instruction-tuned LLMs on Malrule and EEDI misconception-contrastive datasets under base and reflective prompts; Table 3 reports near-uniform flip rates (e.g., Qwen3-4B SFS +0.01) showing "Targeted feedback produces almost no additional behavioral change beyond the contrastive controls."

> "Across all models, datasets, and prompting strategies, SFS remains consistently close to zero (Tables 3). Targeted feedback produces almost no additional behavioral change beyond the contrastive controls."

## Discussion


## Related Claims
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)](model-capability-negatively-correlates-sfs.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — a narrower finding that bears on this claim
