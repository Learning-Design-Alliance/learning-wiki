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
> **Evidence** · 8 claims (3 for, 4 mixed, 1 against) · 7 studies (4 design, 2 causal, 1 associational), `q2`–`q3` · 0 of 7 report an effect size · 8 claims rest on one study

## Description
The team maintains targeted offline datasets sampled from production completions, including an answer-giveaway dataset where "The final dataset consists of 63 data points" and a Tutor Me input-classification dataset where "the dataset consisted of 794 data points." LLM judges calibrated against human experts measure cognitive engagement, math errors, and answer giveaway; the engagement judge shows "an F1 score of 0.83, Matthews Correlation Coefficient of 0.75, false positive rate of 0.08, and false negative rate of 0.17."

## Accounts
<!-- How each source describes or uses the method -->
- **Offline evaluation datasets and calibrated LLM judges for tutoring behaviors**: The team maintains targeted offline datasets sampled from production completions, including an answer-giveaway dataset where "The final dataset consists of 63 data points" and a Tutor Me input-classification dataset where "the dataset consisted of 794 data points." LLM judges calibrated against human experts measure cognitive engagement, math errors, and answer giveaway; the engagement judge shows "an F1 score of 0.83, Matthews Correlation Coefficient of 0.75, false positive rate of 0.08, and false negative rate of 0.17." (Udeshi et al. (2026))
- **FATE: a lightweight 8B-parameter LLM evaluator of AI tutors across four pedagogical dimensions**: FATE (FLC AI Tutor Evaluator) is a specialized evaluator built on Llama 3.1 8B that assesses AI tutor responses across the four BEA 2025 dimensions: Mistake Identification, Mistake Location, Providing Guidance, and Actionability. The authors describe it as "a lightweight evaluator based on Llama 3.1 8B" trained on 1,450 student-tutor conversations using knowledge distillation from Claude Opus 4.7. Four task-specific models were fine-tuned, one per dimension, each using prompts describing the dialogue history and evaluation rubric. (Tahmid Al Hannan et al. (2026))
- **14-criteria LLM evaluator as a proxy for learner success**: A lightweight LLM-based evaluator (GPT-5-mini) that decomposes each tutoring transcript into 14 binary pedagogical criteria (e.g., tutor scaffolding, student understanding, curiosity) and computes a weighted score. Weights derive from Pearson correlations with expert-labeled sessions (N=138), and three evaluation runs are aggregated by majority voting, improving self-consistency to 94.31%. The article introduces it as "an immediate proxy for learners' success, even in the absence of downstream exercise scores." (Po-Chin Chang et al. (2026))

### Claims

- [The LLM evaluator score discriminates between simulated-student motivation profiles](../claims/llm-evaluator-discriminates-student-profiles.md) [+M]
- [Higher AI pedagogical scores are associated with exercise conversion in real student sessions](../claims/pedagogical-score-predicts-exercise-conversion.md) [+M]
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](../claims/educlaw-bench-judge-panel-human-validation.md) [+W]
- [The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases](../claims/helpfulness-ordering-judge-contingent.md) [~W]
- [Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges](../claims/har-outperforms-llm-judge-acceptance-alignment.md) [~W]
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](../claims/llm-judge-small-incremental-differences-ceiling.md) [~W]
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](../claims/slm-judges-show-severe-leniency-bias.md) [-W]
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](../claims/llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) [~W]

## Related Research Methods

- [Multi-turn synthetic-dialogue evaluation protocol for AI tutors](multi-turn-synthetic-dialogue-evaluation-protocol-for-ai-tutors.md)

## Key Sources
- Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home
- Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647
- Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138
