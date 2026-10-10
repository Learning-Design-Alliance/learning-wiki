---
type: research-method
id: human-validated-llm-reconstruction-of-syllabus-assessment-weights
title: Human-validated LLM reconstruction of syllabus assessment weights
description: The pipeline converts syllabus PDFs to Markdown and uses an LLM through a university-managed API gateway to reconstruct final-grade weights for each assessment category, which feed the continuous GenAI-susceptibility treatment variable.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Human-validated LLM reconstruction of syllabus assessment weights

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The pipeline converts syllabus PDFs to Markdown and uses an LLM through a university-managed API gateway to reconstruct final-grade weights for each assessment category, which feed the continuous GenAI-susceptibility treatment variable. The authors use "reconstruction" rather than extraction because LLMs "generate labels that are likely to match the document". Validation against a stratified human-annotated sample found strong recovery, with susceptibility reconstructed at a mean absolute error of 0.063 on the 0–1 scale.

## Accounts
<!-- How each source describes or uses the method -->
- **Human-validated LLM annotation pipeline reconstructing assessment weights from syllabi to measure course GenAI susceptibility**: The pipeline converts syllabus PDFs to Markdown and uses an LLM through a university-managed API gateway to reconstruct final-grade weights for each assessment category, which feed the continuous GenAI-susceptibility treatment variable. The authors use "reconstruction" rather than extraction because LLMs "generate labels that are likely to match the document". Validation against a stratified human-annotated sample found strong recovery, with susceptibility reconstructed at a mean absolute error of 0.063 on the 0–1 scale. (Dumlao et al. (2026))

### Claims
- [GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones](../claims/genai-availability-no-significant-grade-effect-susceptible-courses.md) [+M]

## Related Research Methods
-

## Key Sources
- Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M. (2026). Generative AI Availability, Grades, and Student Satisfaction at a Large University. arXiv. https://arxiv.org/abs/2607.21534
