---
type: strategy
id: chatgpt-counterfactual-feedback-conversion
title: Use ChatGPT via API to convert counterfactual analytics outputs into human-readable prescriptive feedback for learners
description: The strategy converts numeric counterfactual outputs into natural-language prescriptive feedback using ChatGPT and available APIs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: teo-susnjak-2024
    resource: "https://doi.org/10.1007/s40593-023-00336-3"
    title: "Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3"
    author: Teo Susnjak
---

# Use ChatGPT via API to convert counterfactual analytics outputs into human-readable prescriptive feedback for learners

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The strategy converts numeric counterfactual outputs into natural-language prescriptive feedback using ChatGPT and available APIs. The article proposes that "the conversion is performed using ChatGPT and automated using available APIs," with the LLM primed by devising "an ideal template response" and extracting feature names and values into a structured JSON format from which feedback text is constructed. Feedback can be dispensed directly via LA dashboards and emails or through conversations with academic advisors, and human-readable format also helps advisors filter and select the most suitable candidate feedback.

## Design Implications

### Context
#### Requirements
- An ideal template response must be devised and feature names/values extracted into a structured format such as JSON to prime the LLM
- Engineered feature values must first be converted back into raw values so they become interpretable and actionable
#### Constraints
- Demonstrated only on two hypothetical-student case studies; feasibility of the generated text was assessed qualitatively

### Target Learners
- at-risk learners receiving intervention support, and the academic advisors managing interventions

### Target Learning Goals
- actionable, evidence-based behavioural adjustments likely to improve completion outcomes

## Claims

- [Predictive LA research neglects interpretability, explainability, and prescriptive analytics, with course-level prediction dominating over programme-level](../claims/la-interpretability-prescriptive-gap.md) [+W]

## Related Strategies

- [Generate prescriptive feedback via counterfactual modelling constrained to actionable features](counterfactual-prescriptive-feedback.md)

## Examples
-

## Key Sources
- Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3
