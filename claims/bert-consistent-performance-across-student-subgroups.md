---
type: claim
title: "The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups"
description: "The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups"
id: bert-consistent-performance-across-student-subgroups
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
  - id: ye-2026-2
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` BERT maintained consistent performance across threatened (Black and Hispanic) and non-threatened students, unlike Naive Bayes which showed discrepancies. [→ Ye 2026](#ye-2026)
`q3 i?` BERT showed no notable performance gaps by gender or FRPL eligibility, with accuracy clustering around 93–95%. [→ Ye 2026 (2)](#ye-2026-2)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Subgroup analysis (Table 3) of classification performance by stereotype-threatened status. BERT scored F1 0.95 for threatened and 0.95 for non-threatened students, while Naive Bayes showed discrepancies between groups; the article calls BERT's classification more equitable.

> "the BERT model maintained consistent performance across both groups."

### Ye 2026 (2)

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Fairness analysis across gender and free or reduced-price lunch status found "no notable performance gaps"; the article states this analysis was not carried out for English learners and students with Individualized Educational Plans due to limited sample sizes.

> "the BERT model maintained consistently high accuracy, clustering around 93–95% for essays written by both male and female students"

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](bert-generalizes-external-self-affirmation-dataset.md) — related
- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) — related
- [GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it](gpt4-zero-shot-below-finetuned-bert-fewshot-plateau.md) — related
