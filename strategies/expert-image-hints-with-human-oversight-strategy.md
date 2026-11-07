---
type: strategy
id: expert-image-hints-with-human-oversight-strategy
title: Provide expert-written image hints and human oversight when using multimodal LLMs for image-based medical learning or decision support
description: "The article shows that supplying a short expert-written hint describing the image substantially improves a multimodal LLM's accuracy, and that expert oversight is needed because incorrect answers carry flawed explanat..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: yang-z-2025
    resource: "https://doi.org/10.2196/65146"
    title: "Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146"
    author: Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H
---

# Provide expert-written image hints and human oversight when using multimodal LLMs for image-based medical learning or decision support

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article shows that supplying a short expert-written hint describing the image substantially improves a multimodal LLM's accuracy, and that expert oversight is needed because incorrect answers carry flawed explanations. It reports that "40% (22/55) of responses switched to the correct answer" when an image-describing hint was added, and that with hints performance plateaued across difficulty levels. The strategy is to pair the model with expert hints and physician review rather than rely on it autonomously.

## Design Implications

### Context
#### Requirements
- Requires clinical expertise to create image-related hints, which the article states limits use as a CDSS
#### Constraints
- In realistic curbside consult settings, continuous and highly specialized prompting was still required
- Incorrect AI-generated explanations risk disseminating misinformation, particularly for less experienced students and residents

### Target Learners
- medical students preparing for licensing exams
- residents and physicians using image-based question practice

### Target Learning Goals
- interpreting clinical images
- answering image-based medical licensing exam questions

## Claims

- [Expert hints raised GPT-4V's accuracy and flattened its performance across question difficulty levels, while medical students' performance declined with difficulty](../claims/expert-hints-raise-gpt4v-accuracy-plateau-difficulty.md) [+M]
- [Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect](../claims/explanation-preference-correct-versus-incorrect.md) [+M]
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](../claims/gpt4v-poor-explanations-incorrect-answers.md) [+M]
- [With expert hints describing the image, 40% (22/55) of GPT-4V's incorrect responses switched to the correct answer](../claims/image-hints-corrected-40-percent-errors.md) [+M]
- [In a simulated curbside consultation, GPT-4V required multiple specific physician-guided prompts to interpret complex case data accurately](../claims/curbside-consultation-required-multiple-prompts.md) [+M]
- [GPT-4V outperformed medical students on the most difficult AMBOSS questions, by 60% with hints and 26.7% without hints](../claims/gpt4v-outperforms-medical-students-difficult-questions.md) [+M]

## Related Strategies

- [Automated assessment outputs must retain human monitoring and never serve as official grades or sole decision bases](human-monitoring-automated-assessment.md)
- [Implement targeted error-mitigation strategies—expert-reviewed benchmark validation, clinician oversight, and continuous updating—when using LLMs in neurosurgical education](llm-error-mitigation-strategies-neurosurgical-education.md)
- [Deploy healthcare LLMs as augmentative tools under human oversight rather than autonomous decision-makers](llm-augmentative-tools-human-oversight.md)
- [Design human-LLM collaborative systems in which LLMs assist diagnostic reasoning while human experts oversee complex decisions](human-llm-collaborative-diagnostic-reasoning-strategy.md)
- [Use LLMs in medical education as support tools requiring human review, not as independent decision-makers or authoritative instructors](llms-as-support-tools-medical-education.md)

## Examples
-

## Key Sources
- Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146
