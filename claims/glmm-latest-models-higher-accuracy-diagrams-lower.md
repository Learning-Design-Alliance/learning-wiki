---
type: claim
title: GLMM shows latest 2024 flagship models had significantly higher accuracy than early 2024 models, with diagram-based questions significantly less accurate than text-only questions and no significant flagship-by-question-type interaction
description: GLMM shows latest 2024 flagship models had significantly higher accuracy than early 2024 models, with diagram-based questions significantly less accurate than text-only questions and no significant flagship-by-questio...
id: glmm-latest-models-higher-accuracy-diagrams-lower
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: sato-hiroyasu-2025
    resource: "https://doi.org/10.2196/76925"
    title: "Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko. (2025). Performance Evaluation of 18 Generative AI Models (ChatGPT, Gemini, Claude, and Perplexity) in 2024 Japanese Pharmacist Licensing Examination: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/76925"
    author: Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: sato-hiroyasu-2025-2
    resource: "https://doi.org/10.2196/76925"
    title: "Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko. (2025). Performance Evaluation of 18 Generative AI Models (ChatGPT, Gemini, Claude, and Perplexity) in 2024 Japanese Pharmacist Licensing Examination: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/76925"
    author: Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# GLMM shows latest 2024 flagship models had significantly higher accuracy than early 2024 models, with diagram-based questions significantly less accurate than text-only questions and no significant flagship-by-question-type interaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A generalized linear mixed model found latest flagship models significantly more accurate than earlier models (P<.001) and diagram-based questions significantly less accurate than text-only questions (P<.001), with a non-significant interaction (P=.53). [→ Sato Hiroyasu 2025](#sato-hiroyasu-2025)

## Evidence

### Sato Hiroyasu 2025

Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko. (2025). Performance Evaluation of 18 Generative AI Models (ChatGPT, Gemini, Claude, and Perplexity) in 2024 Japanese Pharmacist Licensing Examination: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/76925

`q2 · i?` · `associational · r2`

GLMM with correctness per question as dependent variable, model era and question type as fixed effects, and models and questions as random effects. The analysis found flagship status "significantly higher than that of earlier models (P<.001)" and lower diagram accuracy.

> "The GLMM analysis demonstrated that the accuracy of the latest flagship models was significantly higher than that of earlier models (P<.001). In addition, questions containing diagrams had significantly lower accuracy than that of text-only questions (P<.001)."

### Sato Hiroyasu 2025 (2)

Sato Hiroyasu, Ogasawara Katsuhiko, Sakurai Hidehiko. (2025). Performance Evaluation of 18 Generative AI Models (ChatGPT, Gemini, Claude, and Perplexity) in 2024 Japanese Pharmacist Licensing Examination: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/76925

`q2 · i?` · `associational · r2`

The same GLMM's interaction test: the flagship-by-question-type interaction was not significant (P=.53), so the early-versus-latest improvement held for both text-only and diagram-based questions.

> "The interaction term between the flagship status and question type was not significant (P=.53). Therefore, the difference in accuracy between the early and most recent models was consistently observed, regardless of whether the questions included diagrams or were text-based."

## Discussion


## Related Claims
- [The top-performing OC-LLM differed by question type: Perplexity Pro overall, ChatGPT o1 preview on text-only, and Claude 3.5 Sonnet (new) on diagram-based questions](top-oc-llm-varies-by-question-type.md) — related
- [GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats](text-only-beats-image-based-kmle-accuracy.md) — related
- [Four 2024 flagship OC-LLMs exceeded 80% accuracy on the 107th Japanese pharmacist licensing examination, surpassing the passing threshold and the average examinee score](flagship-oc-llms-exceed-80-percent-jnlep-107.md) — related
- [Answer consistency among the four flagship OC-LLMs was only moderate (Fleiss' κ = 0.334), indicating differing strengths and weaknesses across models](flagship-models-moderate-answer-consistency-kappa-0334.md) — related
- [Chemistry and chemical-structure questions remain the weakest areas for 2024 flagship OC-LLMs on the Japanese pharmacist examination](oc-llm-chemistry-chemical-structure-low-accuracy.md) — related
- [Across models, higher problem-solving accuracy is associated with lower grading error on imperfect handwritten scripts, more strongly for text-based than diagram-based accuracy](reasoning-accuracy-predicts-grading-reliability.md) — related
