---
type: claim
title: Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method
description: Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method
id: low-proficiency-linguistic-form-bottleneck
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: heejin-do-2026-2
    resource: "https://arxiv.org/abs/2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Models reproduce high-proficiency writing more faithfully than authentic low-proficiency linguistic form, with distinct failure modes by method

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At low proficiency targets, prompting (Claude CTP) simulates low proficiency mainly through excessive casing and spelling errors with overly simple syntax, while SFT and GRPO recover lexical and structural properties but generate unrealistically few grammatical and spelling errors. [→ Heejin Do 2026](#heejin-do-2026)
`q2 i?` The discrepancy shrinks at high proficiency: SFT's grammatical-error gap decreases from 84% below the real rate at low targets to 5% below it at high targets. [→ Heejin Do 2026 (2)](#heejin-do-2026-2)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `design · r2`

Linguistic cohort analysis comparing 247 low-target essays per source against a prompt-matched high-target cohort of 245 essays, measuring grammatical, spelling, and casing errors, lexical diversity, and syntactic complexity. At low targets Claude CTP simulates low proficiency "through excessive casing and spelling errors" with simpler syntax, while SFT and GRPO "generate unrealistically few grammatical and spelling errors".

> "we compare 247 low-target essays per source (Overall ≤0.33 of the prompt-normalized range) with a prompt-matched high-target cohort of 245 essays per source (Overall≥0.67 )"

### Heejin Do 2026 (2)

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215

`q2 · i?` · `design · r2`

Same linguistic cohort analysis, contrasting error-rate gaps at low versus high proficiency targets. The paper reports that "SFT’s grammatical-error gap decreases from 84% below the real rate at low targets to 5% below it at high targets."

> "for example, SFT’s grammatical-error gap decreases from 84% below the real rate at low targets to 5% below it at high targets."

## Discussion


## Related Claims
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](no-memorization-or-generation-collapse-in-trained-simulators.md) — related
