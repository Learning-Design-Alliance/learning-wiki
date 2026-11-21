---
type: claim
title: "GPT-4o and GPT-4-turbo assessed tutors' open-ended equity responses proficiently, with few-shot prompting outperforming zero-shot"
description: "GPT-4o and GPT-4-turbo assessed tutors' open-ended equity responses proficiently, with few-shot prompting outperforming zero-shot"
id: llm-few-shot-outperforms-zero-shot-equity-assessment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
sources:
  - id: danielle-r-thomas-2025
    title: Danielle R. Thomas 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o and GPT-4-turbo assessed tutors' open-ended equity responses proficiently, with few-shot prompting outperforming zero-shot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For the same LLM, few-shot prompting outperformed zero-shot prompting, with F1 scores for all models ranging from 0.79 to 0.92, and better performance on predict than explain responses. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger. 2025. Do Tutors Learn from Equity Training and Can Generative AI Assess It?. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA. https://doi.org/10.1145/3706468.3706531

`q2 · i?` · `design · r2`

Evaluation of GPT-4o and GPT-4-turbo under zero-shot and few-shot prompting against human-coded binary scores of 81 tutors' predict and explain responses (Table 5). For example, GPT-4o few-shot achieved accuracy 0.89, AUC 0.88, F1 0.92 on predict responses; accuracy and AUC are not effect sizes.

> "Given the same LLM, few-shot prompting outperformed zero-shot prompting. However, F1 scores for all models performed well ranging from 0.79 to 0.92."

## Discussion


## Related Claims
- [GPT-4o and GPT-4-turbo demonstrate proficiency autograding open responses for low-stakes assessment, with poor GPT-4-turbo performance on some lessons](gpt-llm-autograding-proficiency-low-stakes.md) — possibly the same claim (merge candidate)
- [GPT-4o with few-shot learning offers the best balance of performance, cost, and speed for large-scale assessment, far cheaper than human grading](gpt4o-fewshot-preferred-cost-speed.md) — related
- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](gpt4-few-shot-classifies-trainee-responses.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
