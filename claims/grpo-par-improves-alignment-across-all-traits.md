---
type: claim
title: GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt
description: GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt
id: grpo-par-improves-alignment-across-all-traits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Beyond SFT, GRPO with PAR improves average trait-wise QWK by +0.144 for Qwen2.5-7B-Instruct and +0.246 for Qwen3-4B, and prompt-wise by +0.131 and +0.243. [→ Heejin Do 2026](#heejin-do-2026)
`q2 i?` The SFT-weaker Qwen3-4B benefits most from RL and achieves the strongest overall alignment, and improvements are uniform across traits rather than concentrated in a few dimensions. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `causal · r2`

RL refinement of SFT-initialized policies with GRPO and the AES-derived PAR reward, evaluated on ASAP/ASAP++ with the frozen ArTS verifier across five folds. The paper reports trait-wise gains of "+0.144 for Qwen2.5-7B-Instruct and +0.246 for Qwen3-4B".

> "Beyond SFT, average trait-wise QWK improves by +0.144 for Qwen2.5-7B-Instruct and +0.246 for Qwen3-4B, while prompt-wise improves by +0.131 and +0.243, respectively. Notably, the SFT-weaker Qwen3-4B benefits most from RL and achieves the strongest overall alignment"

## Discussion


## Related Claims
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — reports the opposite
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization](par-gains-transfer-to-independent-evaluators.md) — related
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](no-memorization-or-generation-collapse-in-trained-simulators.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
- [PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts](psyscore-aes-sota-qwk-0-747-asap.md) — related
