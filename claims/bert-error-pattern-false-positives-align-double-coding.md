---
type: claim
title: "The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding"
description: "The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding"
id: bert-error-pattern-false-positives-align-double-coding
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: ye-2026
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D."
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: ye-2026-2
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` The model showed more false positives (0.05) than false negatives (0.01) for the self-affirming attribute. [→ Ye 2026](#ye-2026)
`q3 i?` In 6 of 9 disagreement cases the model's prediction matched the double human coder's revised coding rather than the original coder's. [→ Ye 2026 (2)](#ye-2026-2)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Confusion matrix analysis (Figure 1) of BERT predictions on the comparison dataset, showing the model is marginally more likely to classify essays as self-affirming when they are not, which the authors say warrants careful interpretation.

> "The model exhibited a higher number of false positives (0.0 5) compared to false negatives (0.01) for the self-affirming attribute."

### Ye 2026 (2)

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Qualitative review of the 9 disagreement cases (Table 4): in 6 the model and double coder agreed against the original coder; in the remaining 3 the model diverged from both coders, misclassifying two, leading the authors to call performance mixed in edge cases.

> "a closer analysis reveals that in the majority of disagreement cases (6 out of 9), the model’s predictions aligned with those from a second round of human coding"

## Discussion


## Related Claims
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it](gpt4-zero-shot-below-finetuned-bert-fewshot-plateau.md) — related
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) — related
