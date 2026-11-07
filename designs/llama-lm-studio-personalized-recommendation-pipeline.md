---
type: design
id: llama-lm-studio-personalized-recommendation-pipeline
title: Proof-of-concept pipeline integrating Fitbit metrics, PSQI scores, and academic reports into a locally run LLaMA model for personalized recommendations
description: The pipeline combines weekly Fitbit averages (stress score, step counts, sleep minutes), PSQI sleep quality scores, and text from academic reports, then prompts a locally deployed LLaMA (Meta-Llama-3-Instruct) model i...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: ahmed-arfan-2025
    resource: "https://doi.org/10.1038/s41598-025-89386-2"
    title: "Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid (2025). Leveraging LLMs and wearables to provide personalized recommendations for enhancing student well-being and academic performance through a proof of concept. Scientific Reports 15, 4591. https://doi.org/10.1038/s41598-025-89386-2"
    author: Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid
---

# Proof-of-concept pipeline integrating Fitbit metrics, PSQI scores, and academic reports into a locally run LLaMA model for personalized recommendations

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The pipeline combines weekly Fitbit averages (stress score, step counts, sleep minutes), PSQI sleep quality scores, and text from academic reports, then prompts a locally deployed LLaMA (Meta-Llama-3-Instruct) model in LM Studio to generate personalized advice. The authors chose the model "due to its state-of-the-art performance in natural language understanding and generation tasks". Running the model offline kept sensitive student data on local storage and avoided API costs, which the authors present as secure and economically feasible for institutions with budget constraints.

## Design Implications

### Context
#### Requirements
- Participants must supply wearable data, PSQI survey responses, and school reports in PDF form; a smart mobile phone with internet access was an inclusion criterion.
#### Constraints
- The study was a proof of concept describing capability, not measuring intervention effects; data privacy concerns prevented use of more powerful cloud models like ChatGPT.

### Target Learners
- high school students aged 13 to 17

### Learning Goals
- improving sleep hygiene, physical activity, stress management, and academic performance

### Claims
- [Llm Recommendations Rated Clear Actionable](../claims/llm-recommendations-rated-clear-actionable.md) [+M]
- [Llm Recommendation Alignment Variable](../claims/llm-recommendation-alignment-variable.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid (2025). Leveraging LLMs and wearables to provide personalized recommendations for enhancing student well-being and academic performance through a proof of concept. Scientific Reports 15, 4591. https://doi.org/10.1038/s41598-025-89386-2
