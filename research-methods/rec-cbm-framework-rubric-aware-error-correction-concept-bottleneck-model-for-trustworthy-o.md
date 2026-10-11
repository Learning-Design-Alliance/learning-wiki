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
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
REC-CBM is a concept bottleneck model for open-ended grading that integrates three components: a rubric-aware concept encoder that learns concept-specific representations over responses using a concept query bank, an ordinal pairwise calibration objective that preserves ranking structure among rubric dimensions, and a latent concept error-correction module that denoises concept predictions before final grade prediction while preserving interpretability. The framework uses two-stage training: Stage I learns rubric-aligned concept predictors, and Stage II fits latent-correction parameters on frozen concept outputs. The article states this design "preserves the interpretable bottleneck while cor-recting concept-level noise before grade prediction."

## Accounts
<!-- How each source describes or uses the method -->
- **REC-CBM framework: rubric-aware error-correction concept bottleneck model for trustworthy open-ended grading**: REC-CBM is a concept bottleneck model for open-ended grading that integrates three components: a rubric-aware concept encoder that learns concept-specific representations over responses using a concept query bank, an ordinal pairwise calibration objective that preserves ranking structure among rubric dimensions, and a latent concept error-correction module that denoises concept predictions before final grade prediction while preserving interpretability. The framework uses two-stage training: Stage I learns rubric-aligned concept predictors, and Stage II fits latent-correction parameters on frozen concept outputs. The article states this design "preserves the interpretable bottleneck while cor-recting concept-level noise before grade prediction." (Chengshuai Zhao et al. (2025))

### Claims
- [REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines](../claims/rec-cbm-best-task-accuracy-f1-every-backbone.md) [+M]
- [Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging](../claims/rec-cbm-ablation-components-complementary.md) [+M]
- [Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable](../claims/rec-cbm-intervention-faithfulness-asymmetry.md) [+M]

## Related Research Methods
-

## Key Sources
- Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM
