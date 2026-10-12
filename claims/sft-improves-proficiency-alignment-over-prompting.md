---
type: claim
title: Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation
description: Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation
id: sft-improves-proficiency-alignment-over-prompting
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://arxiv.org/abs/2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On the same backbone and fold, SFT achieves average trait-level QWK of 0.501 versus 0.036 for CTP+FS and 0.153 for SRLP+FS prompting. [→ Heejin Do 2026](#heejin-do-2026)
`q2 i?` The SFT advantage persists across five-fold evaluation (Qwen2.5-7B-Instruct 0.474±0.023; Qwen3-4B 0.428±0.062), though alignment remains uneven, with Language, Sentence Fluency, and Conventions more challenging than Content and Prompt Adherence. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215

`q2 · i?` · `causal · r2`

Comparison of SFT against prompting on the same Qwen2.5-7B-Instruct backbone and fold, plus five-fold cross-validation on ASAP/ASAP++ with a frozen AES verifier. The paper reports SFT "substantially outperforming both CTP+FS (0.036) and SRLP+FS (0.153)".

> "SFT achieves an average trait-level QWK of0.501, substantially outperforming both CTP+FS (0.036) and SRLP+FS (0.153). This advantage persists across the full five-fold evaluation: Qwen2.5-7B-Instruct reaches an average QWK of 0.474±0.023 , while Qwen3-4B achieves 0.428±0.062 ."

## Discussion


## Related Claims
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — reports the opposite
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method](low-proficiency-linguistic-form-bottleneck.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
- [PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts](psyscore-aes-sota-qwk-0-747-asap.md) — related
- [GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization](par-gains-transfer-to-independent-evaluators.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LearnLens's modular pipeline outperforms direct-prompt baselines on scoring quality while matching latency and cost on 100 authentic student answers](learnlens-modular-pipeline-beats-baselines-scoring.md) — related
- [Supervised fine-tuning was less effective than direct prompting of SOTA LLMs for generating deep-level feedback, a task with non-deterministic output](sft-less-effective-than-prompting-for-feedback-generation.md) — reports the opposite
