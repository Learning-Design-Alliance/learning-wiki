---
type: claim
title: SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse
description: SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse
id: no-memorization-or-generation-collapse-in-trained-simulators
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
    kind: design
    rigour: 2
---

# SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` For non-source-based prompts, neither SFT nor GRPO produces any near-duplicate of a training essay (0.00% with ROUGE-L>0.7), and 8-gram overlap is negligible and comparable to held-out real essays. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215

`q2 · i?` · `design · r2`

Memorization and diversity analysis of SFT and GRPO generations, checking ROUGE-L near-duplicates, 8-gram overlap, and within-profile repetition across 132 groups. The paper reports "neither method produces any near-duplicate of a training essay (0.00% with ROUGE-L>0.7 )".

> "For non-source-based prompts, neither method produces any near-duplicate of a training essay (0.00% with ROUGE-L>0.7 ), and their 8-gram overlap is negligible"

## Discussion


## Related Claims
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
