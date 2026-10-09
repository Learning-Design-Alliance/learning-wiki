---
type: claim
title: The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders
description: The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders
id: bert-generalizes-external-self-affirmation-dataset
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: ye-2026
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`

## Subclaims
`q3 i?` On an external dataset of 7th-grade essays from another research team, the model achieved Cohen's Kappa of 0.86 with human coders (n = 150). [→ Ye 2026](#ye-2026)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Generalization test applying the fine-tuned model to an external dataset of 4,660 students in 25 schools collected by another organization in 2023-2024, with reliability coding on a stratified random subsample of 150 essays yielding "a Cohen’s Kappa of 0.86".

> "The model achieved a Cohen’s Kappa of 0.86 with human coders  (n = 150) , indicating almost perfect agreement (McHugh, 2012)."

## Discussion


## Related Claims
- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](bert-consistent-performance-across-student-subgroups.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) — related
