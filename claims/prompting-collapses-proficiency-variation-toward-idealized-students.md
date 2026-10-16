---
type: claim
title: Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions
description: Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions
id: prompting-collapses-proficiency-variation-toward-idealized-students
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
  - id: heejin-do-2026-2
    resource: "https://arxiv.org/abs/2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` Zero-shot prompting shows a strong bias toward high-scoring essays (mean normalized score 0.74, 25% at the cap) versus a human mean of 0.58; SFT (0.57) and GRPO (0.53) closely match the human distribution. [→ Heejin Do 2026](#heejin-do-2026)
`q2 i?` Zero-shot prompting produces substantially longer essays than real students (median 304 vs. 167 words), while SFT (158) and GRPO (141) closely recover the human length distribution without explicit length supervision. [→ Heejin Do 2026 (2)](#heejin-do-2026-2)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `causal · r2`

Distributional analysis of AES-predicted Overall scores on the test set (Qwen2.5-7B-Instruct, fold 1), normalized per prompt, comparing real, zero-shot, SFT, and GRPO essays (Figure 3). The paper reports zero-shot's "mean normalized score of 0.74 and 25% of generations receiving the maximum score".

> "Zero-shot prompting exhibits a strong bias toward high-scoring essays, with a mean normalized score of 0.74 and 25% of generations receiving the maximum score. In contrast, SFT (0.57) and GRPO (0.53) closely match the human distribution (0.58)."

### Heejin Do 2026 (2)

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215

`q2 · i?` · `causal · r2`

Essay-length distribution analysis on the test set (Qwen2.5-7B-Instruct, fold 1; Figure 4) comparing real, zero-shot, SFT, and GRPO essays. The paper reports zero-shot medians of "304 vs. 167 words" and that "SFT (158) and GRPO (141) closely recover the human distribution".

> "Zero-shot prompting produces substantially longer essays than real students (median 304 vs. 167 words), reflecting the well-known tendency of instruction-tuned LLMs toward verbose and polished responses (Singhal et al., 2023; Saito et al., 2023). In contrast, SFT (158) and GRPO (141) closely recover the human distribution despite receiving no explicit length supervision."

## Discussion


## Related Claims
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — related
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](no-memorization-or-generation-collapse-in-trained-simulators.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method](low-proficiency-linguistic-form-bottleneck.md) — related
- [GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization](par-gains-transfer-to-independent-evaluators.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
