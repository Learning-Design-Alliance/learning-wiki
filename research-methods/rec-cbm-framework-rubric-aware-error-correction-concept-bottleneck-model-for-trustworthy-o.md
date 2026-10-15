---
type: research-method
id: rec-cbm-framework-rubric-aware-error-correction-concept-bottleneck-model-for-trustworthy-o
title: "REC-CBM framework: rubric-aware error-correction concept bottleneck model for trustworthy open-ended grading"
description: "REC-CBM is a concept bottleneck model for open-ended grading that integrates three components: a rubric-aware concept encoder that learns concept-specific representations over responses using a concept query bank, an ordinal pairwise calibration objective that preserves ranking structure among rubri"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# REC-CBM framework: rubric-aware error-correction concept bottleneck model for trustworthy open-ended grading

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
REC-CBM is a concept bottleneck model for open-ended grading that integrates three components: a rubric-aware concept encoder that learns concept-specific representations over responses using a concept query bank, an ordinal pairwise calibration objective that preserves ranking structure among rubric dimensions, and a latent concept error-correction module that denoises concept predictions before final grade prediction while preserving interpretability. The framework uses two-stage training: Stage I learns rubric-aligned concept predictors, and Stage II fits latent-correction parameters on frozen concept outputs. The article states this design "preserves the interpretable bottleneck while cor-recting concept-level noise before grade prediction."

## Accounts
<!-- How each source describes or uses the method -->
- **REC-CBM framework: rubric-aware error-correction concept bottleneck model for trustworthy open-ended grading**: REC-CBM is a concept bottleneck model for open-ended grading that integrates three components: a rubric-aware concept encoder that learns concept-specific representations over responses using a concept query bank, an ordinal pairwise calibration objective that preserves ranking structure among rubric dimensions, and a latent concept error-correction module that denoises concept predictions before final grade prediction while preserving interpretability. The framework uses two-stage training: Stage I learns rubric-aligned concept predictors, and Stage II fits latent-correction parameters on frozen concept outputs. The article states this design "preserves the interpretable bottleneck while cor-recting concept-level noise before grade prediction." (Chengshuai Zhao et al. (2025))
- **Route automated grading predictions through human-interpretable rubric-level concepts so educators can inspect, verify, and intervene**: In high-stakes educational assessment, raw accuracy alone is insufficient; instructors need to understand why a score was produced and how to intervene on questionable judgments. Routing grading predictions through human-interpretable rubric-level concepts provides a mechanistic guarantee of transparency, decomposing the final grade into rubric-level concept predictions that educators can examine or modify. The article states this enables educators to "inspect, verify, and intervene on reasoning," supporting intervention and auditing and promoting pedagogical usefulness through concept-level outputs aligned with feedback categories. (Chengshuai Zhao et al. (2025))

### Claims

- [The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy](../claims/causal-assessment-framework-validation-limitations.md) [-W]

## Related Research Methods
-

## Key Sources
- Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM
