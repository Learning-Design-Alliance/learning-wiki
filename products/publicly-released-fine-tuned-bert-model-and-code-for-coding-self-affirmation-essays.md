---
type: product
id: publicly-released-fine-tuned-bert-model-and-code-for-coding-self-affirmation-essays
title: Publicly released fine-tuned BERT model and code for coding self-affirmation essays
description: "Ye et al.'s publicly released Keras implementation and fine-tuned BERT classifier automate coding student essays as self-affirming or general for research use."
product_kind: software
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: ye-2026
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D"
---

# Publicly released fine-tuned BERT model and code for coding self-affirmation essays

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
Ye et al.'s publicly released Keras implementation and fine-tuned BERT classifier automate coding student essays as self-affirming or general for research use.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims
- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](../claims/bert-consistent-performance-across-student-subgroups.md) [+W]
- [The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding](../claims/bert-error-pattern-false-positives-align-double-coding.md) [+W]
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](../claims/bert-generalizes-external-self-affirmation-dataset.md) [+W]
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](../claims/bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) [+W]
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](../claims/fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) [+W]
- [GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it](../claims/gpt4-zero-shot-below-finetuned-bert-fewshot-plateau.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

<!-- merged 2026-10-10 from elements/bert-self-affirmation-essay-classifier-released-model ("Publicly released fine-tuned BERT model and code for coding self-affirmation essays"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Publicly released fine-tuned BERT model and code for coding self-affirmation essays

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A fine-tuned BERT-base (uncased) binary classifier, built in Keras with a frozen pre-trained BERT layer, a sigmoid output layer, class weighting, and early stopping, that labels student writing exercises as self-affirming or general. The article states: "We make the fine -tuned model publicly available to help the research community automate the burdensome task of coding". It was trained on labeled essays from a large-scale randomized trial and validated against human coders and on an external dataset.

## Design Implications

### Context
#### Requirements
- Labeled student essays for fine-tuning or reuse of the released model
- Validation by double-coding a random sample when deployed in new work
#### Constraints
- Trained on 7th-grade self-affirmation writing exercises; the article recommends retraining with new coded samples if the context shifts

### Target Learners
- 7th-grade students in self-affirmation intervention studies

### Target Learning Goals
- Automated classification of self-affirming content in student writing to support value-affirmation intervention research and implementation

## Claims

- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](../claims/bert-consistent-performance-across-student-subgroups.md) [+W]
- [The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding](../claims/bert-error-pattern-false-positives-align-double-coding.md) [+W]
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](../claims/bert-generalizes-external-self-affirmation-dataset.md) [+W]
- [Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays](../claims/bert-outperforms-naive-bayes-and-gpt4-essay-coding.md) [+W]
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](../claims/fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) [+W]
- [GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it](../claims/gpt4-zero-shot-below-finetuned-bert-fewshot-plateau.md) [+W]

## Related Elements
- 

## Examples

- [Automate self-affirmation essay coding with a fine-tuned model while double-coding a random sample for reliability](../strategies/automated-coding-with-random-sample-double-coding.md)

## Key Sources
- Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm
-->
