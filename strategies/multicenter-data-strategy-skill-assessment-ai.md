---
type: strategy
id: multicenter-data-strategy-skill-assessment-ai
title: Gather multicenter expert datasets and strengthen annotation criteria to enable AI-based skill assessment in robotic cardiac surgery
description: The authors recommend that future research adopt a multicenter approach to data collection and improve annotation practices.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: atroshchenko-gennady-v-2025
    resource: "https://doi.org/10.1007/s11701-025-02563-3"
    title: "Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3"
    author: Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten
---

# Gather multicenter expert datasets and strengthen annotation criteria to enable AI-based skill assessment in robotic cardiac surgery

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The authors recommend that future research adopt a multicenter approach to data collection and improve annotation practices. They argue that "Developing robust, scalable models will require large datasets, ideally drawn from multiple institutions, and procedure types", with key considerations including "ensuring annotation consistency, addressing patient privacy, and developing shared platforms to enable widespread data sharing and model training". A more comprehensive effort including "stronger annotation criteria, richer task diversity, and more rigorous evaluation" is described as necessary to enhance model performance.

## Design Implications

### Context
#### Requirements
- Standardized criteria for what constitutes an expert robotic cardiac surgeon whose performance is acceptable for training AI models
#### Constraints
- Limited number of expert robotic cardiac surgeons globally, high costs, restricted access to animal models, and availability of robotic platforms complicate gathering additional expert data at a single center

### Target Learners
- novice surgeons in robotic cardiac surgery training programs

### Target Learning Goals
- reliable automated skill assessment and post-procedure feedback without reliance on expert raters

## Claims

- [Current data indicate AI-based automated assessment tools in robotic surgery are not well validated and remain at a conceptual stage](../claims/ai-robotic-surgery-assessment-not-well-validated.md) [+W]
- [Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)](../claims/cross-validation-ar-98-sa-79-mean-accuracy.md) [+W]
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](../claims/dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) [+W]
- [The predictive certainty of the trained networks was high (99% for action recognition, 95% for skill assessment) despite differing accuracies](../claims/predictive-certainty-ar-99-sa-95.md) [+W]
- [The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance](../claims/skill-assessment-network-56-percent-accuracy-failed.md) [+W]

## Related Strategies

- [Prioritize predictive-validity research, benchmarking of existing tools, and integration of kinematic data and AI in surgical skill assessment](future-migs-assessment-kinematic-ai-benchmarking.md)
- [Pursue AI-based and console-data evaluation platforms for assessing novice robotic surgical skill](ai-based-robotic-skill-evaluation-strategy.md)
- [Future validation studies should build on existing assessment tools rather than develop new ones](validate-existing-tools-strategy.md)
- [Develop AI algorithms to automatically annotate surgical gestures and provide targeted feedback, with substantial testing before clinical implementation](ai-automatic-gesture-annotation-targeted-feedback-strategy.md)

## Examples
-

## Key Sources
- Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3
