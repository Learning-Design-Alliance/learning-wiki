---
type: claim
title: Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays
description: Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays
id: bert-outperforms-naive-bayes-and-gpt4-essay-coding
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: mixed
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

# Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` BERT achieved accuracy of 0.93 and F1 of 0.95, above Naive Bayes (0.86/0.88) and GPT-4 with instructions only (0.90/0.93). [→ Ye 2026](#ye-2026)
`q3 i?` Against double human coders as ground truth, BERT significantly outperformed Naive Bayes (McNemar p = 0.004), but the difference was not statistically significant against original coders (p = 0.167). [→ Ye 2026 (2)](#ye-2026-2)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Model performance comparison (Table 2) on the out-of-sample double-coded dataset. The article prints Naive Bayes at accuracy 0.86/F1 0.88, GPT-4 instructions-only at 0.90/0.93, and BERT at "accuracy of 0.93 and an F1 score of 0.95".

> "In contrast, the BERT model achieved an accuracy of 0.93 and an F1 score of 0.95, re flecting its advanced capability to capture nuanced patterns in the text data."

### Ye 2026 (2)

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

McNemar's tests on paired predictions over the 134 double-coded cases: BERT correctly classified 127 cases versus 115 for Naive Bayes using double coders (p = 0.004), but with original coders as ground truth the difference was not significant (p = 0.167).

> "McNemar’s test produced a test statistic of 6.72 and a p-value of 0.004, suggesting that BERT performed significantly better than the Naive Bayes model at the 0.01 level."

## Discussion


## Related Claims
- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](bert-consistent-performance-across-student-subgroups.md) — related
- [GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it](gpt4-zero-shot-below-finetuned-bert-fewshot-plateau.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](bert-generalizes-external-self-affirmation-dataset.md) — related
- [The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding](bert-error-pattern-false-positives-align-double-coding.md) — related
