---
type: claim
title: GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it
description: GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it
id: gpt4-zero-shot-below-finetuned-bert-fewshot-plateau
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

# GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` Zero-shot GPT-4 achieved accuracy 0.90, precision 0.89, recall 0.97, F1 0.93, and Cohen's Kappa of approximately 0.78 with human coders. [→ Ye 2026](#ye-2026)
`q3 i?` Adding up to 6 example essays left GPT-4's accuracy in the 0.89–0.91 range, with no significant improvement. [→ Ye 2026 (2)](#ye-2026-2)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

GPT-4 prompting experiment (Section 3.3) on the same test set, run via API with temperature=0. The article reports "an accuracy of 0.90" and a Cohen's Kappa of approximately 0.78 with human coders, categorized as substantial agreement, below human-human agreement.

> "On the same test set of essays, GPT -4 achieved an accuracy of 0.90, with a precision of 0.89, recall of 0.97, and F1 of 0.93."

### Ye 2026 (2)

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Few-shot variants appended 2, 4, or 6 example essays of mixed length to the prompt; accuracy plateaued in the "0.89–0.91 range" across alternative example sets, which the authors attribute to diminishing returns from few-shot examples.

> "We tried up to 6 examples with representative texts, but GPT -4’s accuracy remained in the 0.89–0.91 range."

## Discussion


## Related Claims
- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](bert-consistent-performance-across-student-subgroups.md) — related
- [The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding](bert-error-pattern-false-positives-align-double-coding.md) — related
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
