---
type: claim
title: GPT-4o and GPT-4-turbo demonstrate proficiency autograding open responses for low-stakes assessment, with poor GPT-4-turbo performance on some lessons
description: GPT-4o and GPT-4-turbo demonstrate proficiency autograding open responses for low-stakes assessment, with poor GPT-4-turbo performance on some lessons
id: gpt-llm-autograding-proficiency-low-stakes
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
    kind: causal
    rigour: 2
  - id: danielle-r-thomas-2025-2
    title: Danielle R. Thomas 2025 (2)
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o and GPT-4-turbo demonstrate proficiency autograding open responses for low-stakes assessment, with poor GPT-4-turbo performance on some lessons

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Both models' accuracy ranged from 71% to 91% for predict responses and 71% to 87% for explain responses, with some exceptions in GPT-4-turbo. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)
`q2 i?` GPT-4-turbo performed poorly distinguishing correct from incorrect predict responses in Helping Students Manage Inequity (AUC = 0.17, F1 = 0.45). [→ Danielle R. Thomas 2025 (2)](#danielle-r-thomas-2025-2)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger. 2025. Does Multiple Choice Have a Future in the Age of Generative AI? A Posttest-only RCT. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA. https://doi.org/10.1145/3706468.3706530

`q2 · i?` · `causal · r2`

Evaluation of GPT-4o and GPT-4-turbo few-shot prompted scoring of tutors' posttest open responses against human binary codes; accuracy, precision, recall, AUC and F1 are reported per lesson in Tables 6 and 7.

> "In general, both models demonstrated proficiency in performance, with accuracy ranging from 71% to 91% for predict responses and 71% to 87% for explain responses—with some exceptions in GPT-4-turbo."

### Danielle R. Thomas 2025 (2)

Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger. 2025. Does Multiple Choice Have a Future in the Age of Generative AI? A Posttest-only RCT. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA. https://doi.org/10.1145/3706468.3706530

`q2 · i?` · `causal · r2`

GPT-4-turbo's weakest results were Helping Students Manage Inequity predict responses (AUC = 0.17, F1 = 0.45), Exploring Implicit Bias predict (AUC = 0.43), and Building Cultural Competence explain (AUC = 0.45), suggesting poor class discrimination on nuanced topics.

> "GPT-4-turbo demonstrated proficiency across all lessons with poorer performance relative to the other lessons for assessing predict responses in Helping Students Manage Inequity (𝐴𝑈𝐶 = 0.17,𝐹1 = 0.45)."

## Discussion


## Related Claims
- [GPT-4o and GPT-4-turbo assessed tutors' open-ended equity responses proficiently, with few-shot prompting outperforming zero-shot](llm-few-shot-outperforms-zero-shot-equity-assessment.md) — possibly the same claim (merge candidate)
- [GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)](gpt4v-subdomain-performance-inconsistent.md) — related
- [GPT-4 answers 65.8% of university assessment questions correctly by majority vote and can produce correct answers for 85.1% of questions with at least one prompting strategy](gpt4-answers-65-8-percent-majority-vote.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [GPT-4.0-Turbo outperformed GPT-3.5-Turbo in dialogue authenticity, user experience, and feedback quality](gpt4-outperforms-gpt35-vp-quality.md) — related
- [On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation](phinetuned-benchmark-comparison-gpt.md) — related
- [GPT-4o with few-shot learning offers the best balance of performance, cost, and speed for large-scale assessment, far cheaper than human grading](gpt4o-fewshot-preferred-cost-speed.md) — related
