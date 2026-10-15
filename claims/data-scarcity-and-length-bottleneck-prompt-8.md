---
type: claim
title: "Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO"
description: "Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO"
id: data-scarcity-and-length-bottleneck-prompt-8
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On Prompt 8, which has only 723 training essays and requires substantially longer responses (average length ≈650), prompting-based methods outperform both SFT and GRPO. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `causal · r2`

Discussion-section analysis of the clearest failure case, Prompt 8 in Table 5, where prompting-based methods outperform both SFT and GRPO. The paper reports Prompt 8 "contains only 723 training essays (less than half the size of most other prompts)" with average length ≈650.

> "Prompt 8 contains only 723 training essays (less than half the size of most other prompts) while requiring substantially longer responses (average length ≈650 )."

## Discussion


## Related Claims
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — reports the opposite
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — reports the opposite
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](no-memorization-or-generation-collapse-in-trained-simulators.md) — related
- [GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization](par-gains-transfer-to-independent-evaluators.md) — reports the opposite
- [Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method](low-proficiency-linguistic-form-bottleneck.md) — related
