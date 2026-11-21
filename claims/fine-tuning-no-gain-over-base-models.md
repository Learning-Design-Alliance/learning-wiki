---
type: claim
title: Domain fine-tuning did not outperform strong base LLMs for feedback generation and mostly slightly reduced performance
description: Domain fine-tuning did not outperform strong base LLMs for feedback generation and mostly slightly reduced performance
id: fine-tuning-no-gain-over-base-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: vikrant-sahu-2025
    resource: "https://doi.org/10.1145/3799830.3799878"
    title: Vikrant Sahu 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Domain fine-tuning did not outperform strong base LLMs for feedback generation and mostly slightly reduced performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the Autograder+ evaluation, fine-tuned model variants did not outperform the strong base models and in most cases showed slightly reduced BERTScore and SBERT performance. [→ Vikrant Sahu 2025](#vikrant-sahu-2025)

## Evidence

### Vikrant Sahu 2025

Vikrant Sahu, Dr. Gagan Raj Gupta, Raghav Borikar, and Nitin Mane. 2025. Autograder+: A Multi-Faceted AI Framework for Rich Pedagogical Feedback in Programming Education. CODS '25. [doi:10.1145/3799830.3799878](https://doi.org/10.1145/3799830.3799878)

`q2 · i?` · `design · r2`

Configuration comparison on the 600-submission IITBh PC25 evaluation corpus (Table 5), contrasting fine-tuned (FT) and Base variants of falcon3:10b and llama3.2:3b. The article reports "fine-tuning did not outperform the strong base models"; no effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "Interestingly, fine-tuning did not outperform the strong base models, and in most cases resulted in a slightly reduced performance."

## Discussion


## Related Claims
- [Among baseline LLMs integrated without fine-tuning or prompt pooling, falcon3:10b and llama3.2:3b achieved the highest BERTScore F1](baseline-llm-feedback-comparison.md) — related
- [Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.](sft-ineffective-reference-metrics-unreliable.md) — related
- [Generated feedback across models shows a considerable gap from teacher-written feedback: fine-tuned models score near zero on LLM rating, and human experts rate all model feedback below the ideal score of 3](mathedu-feedback-generation-gap-from-teachers.md) — related
- [On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation](phinetuned-benchmark-comparison-gpt.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
