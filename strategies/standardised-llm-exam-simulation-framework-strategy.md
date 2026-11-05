---
type: strategy
id: standardised-llm-exam-simulation-framework-strategy
title: Evaluate LLM examination performance with a standardised simulation framework using repeated independent runs and Monte Carlo confidence intervals
description: "The article's method is a reusable recipe for benchmarking LLMs on professional examinations: identical prompt delivery, disabled conversational memory, deactivated internet access, five independent runs per model, an..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: kafagi-abdul-rhaman-atassi-nazih-kafagi-abdul-hadi-2026
    resource: "https://doi.org/10.1136/bmjopen-2025-108775"
    title: "Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi. (2026). Performance of large language models (GPT-5.2, Gemini 3 Pro, Claude Sonnet 4.6 and Grok 4.1) on the Fellowship of The Royal College of Surgeons Urology Part A examination. BMJ Open. https://doi.org/10.1136/bmjopen-2025-108775"
    author: Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi
---

# Evaluate LLM examination performance with a standardised simulation framework using repeated independent runs and Monte Carlo confidence intervals

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (6 for, 2 mixed) · 3 studies (3 design), `q2` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
The article's method is a reusable recipe for benchmarking LLMs on professional examinations: identical prompt delivery, disabled conversational memory, deactivated internet access, five independent runs per model, and 95% CIs built by a "sequential Monte Carlo sampling procedure" with sampling continued until the CI half-width was less than 2.5% of the point estimate. Questions were mapped to the official syllabus blueprint and marked against an official answer key.

## Design Implications

### Context
#### Requirements
- Access to a static proprietary question bank mapped to the official syllabus blueprint and an official answer key
#### Constraints
- Consumer-facing interfaces rather than controlled API access introduce potential variability from server load and interface-level processing that cannot be fully accounted for; sampling parameters such as temperature cannot be adjusted by the user

### Target Learners
- researchers and educators benchmarking LLMs in medical education

### Target Learning Goals
- reliable comparative evaluation of AI model performance on professional assessments

## Claims

- [Frontier LLM scores on the FRCS Urology examination represent a substantial improvement over ChatGPT-3.5's reported 35% failure](../claims/frontier-llms-improve-over-chatgpt-3-5-frcs-urol.md) [+W]
- [GPT-5.2's 95% CI straddled the 74% pass mark, making its pass status dependent on sitting-specific calibration](../claims/gpt-5-2-ci-straddles-pass-mark.md) [~W]
- [Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)](../claims/llm-output-instability-female-urology-anatomy.md) [~W]
- [LLM performance was weakest in paediatric urology and testicular cancer and strongest in research methodology and andrology](../claims/llm-subspecialty-weaknesses-paediatric-urology-testicular-cancer.md) [+W]
- [All four LLMs completed the 240-question assessment in under 3 minutes, far faster than the human time allocation](../claims/llms-complete-frcs-urol-under-three-minutes.md) [+W]
- [Three of four frontier LLMs exceeded the indicative 74% pass threshold on a simulated FRCS (Urol) Part A examination, while Grok 4.1 failed](../claims/three-of-four-llms-pass-simulated-frcs-urol-part-a.md) [+W]
- [Monte Carlo simulation confirms weight and score stability of the expert-derived priorities under judgment perturbation](../claims/mc-simulation-robustness-ahp-fahp-weights.md) [+W]
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](../claims/llm-ebhs-inter-run-reliability-high-kappa-0821.md) [+W]

## Related Strategies

- [Evaluate LLMs for educational use with repeated-attempt consistency testing rather than single-attempt performance only](repeated-attempt-llm-evaluation-strategy.md)

## Examples
-

## Key Sources
- Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi. (2026). Performance of large language models (GPT-5.2, Gemini 3 Pro, Claude Sonnet 4.6 and Grok 4.1) on the Fellowship of The Royal College of Surgeons Urology Part A examination. BMJ Open. https://doi.org/10.1136/bmjopen-2025-108775
