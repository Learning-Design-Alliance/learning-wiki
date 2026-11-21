---
type: claim
title: Adding a prompt to fine-tuned LLaMA yields performance similar to unprompted fine-tuned LLaMA
description: Adding a prompt to fine-tuned LLaMA yields performance similar to unprompted fine-tuned LLaMA
id: prompted-llama-similar-to-unprompted
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: rebeckah-k-fussell-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010128"
    title: "Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)"
    author: Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding a prompt to fine-tuned LLaMA yields performance similar to unprompted fine-tuned LLaMA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The prompted LLaMA model performed similarly to the unprompted LLaMA model across all performance metrics for both codes, suggesting the unprompted model was near the human inter-rater ceiling. [→ Rebeckah K. Fussell 2025](#rebeckah-k-fussell-2025)

## Evidence

### Rebeckah K. Fussell 2025

Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)

`q2 · i?` · `design · r2`

Results section, QC code performance comparison. The article reports that in preliminary tests with a less-optimized LLaMA, the prompted model outperformed the unprompted one, indicating prompts can add value.

> "Surprisingly, the prompted LLaMA model performed similarly to the unprompted LLaMA model across all these metrics. This result suggests that the unprompted LLaMA model is near the ceiling of possible performance as it approaches the human inter-rater ceiling"

## Discussion


## Related Claims
- [Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code](llama-outperforms-bow-bert-qc-code.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification](few-shot-llama-underperforms-trained-models.md) — related
