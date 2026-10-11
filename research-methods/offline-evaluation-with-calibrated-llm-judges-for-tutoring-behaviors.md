---
type: research-method
id: offline-evaluation-with-calibrated-llm-judges-for-tutoring-behaviors
title: Offline evaluation with calibrated LLM judges for tutoring behaviors
description: "The team maintains targeted offline datasets sampled from production completions, including an answer-giveaway dataset where \"The final dataset consists of 63 data points\" and a Tutor Me input-classification dataset where \"the dataset consisted of 794 data points.\" LLM judges calibrated against huma"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Offline evaluation with calibrated LLM judges for tutoring behaviors

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The team maintains targeted offline datasets sampled from production completions, including an answer-giveaway dataset where "The final dataset consists of 63 data points" and a Tutor Me input-classification dataset where "the dataset consisted of 794 data points." LLM judges calibrated against human experts measure cognitive engagement, math errors, and answer giveaway; the engagement judge shows "an F1 score of 0.83, Matthews Correlation Coefficient of 0.75, false positive rate of 0.08, and false negative rate of 0.17."

## Accounts
<!-- How each source describes or uses the method -->
- **Offline evaluation datasets and calibrated LLM judges for tutoring behaviors**: The team maintains targeted offline datasets sampled from production completions, including an answer-giveaway dataset where "The final dataset consists of 63 data points" and a Tutor Me input-classification dataset where "the dataset consisted of 794 data points." LLM judges calibrated against human experts measure cognitive engagement, math errors, and answer giveaway; the engagement judge shows "an F1 score of 0.83, Matthews Correlation Coefficient of 0.75, false positive rate of 0.08, and false negative rate of 0.17." (Udeshi et al. (2026))
- **FATE: a lightweight 8B-parameter LLM evaluator of AI tutors across four pedagogical dimensions**: FATE (FLC AI Tutor Evaluator) is a specialized evaluator built on Llama 3.1 8B that assesses AI tutor responses across the four BEA 2025 dimensions: Mistake Identification, Mistake Location, Providing Guidance, and Actionability. The authors describe it as "a lightweight evaluator based on Llama 3.1 8B" trained on 1,450 student-tutor conversations using knowledge distillation from Claude Opus 4.7. Four task-specific models were fine-tuned, one per dimension, each using prompts describing the dialogue history and evaluation rubric. (Tahmid Al Hannan et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home
- Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647
