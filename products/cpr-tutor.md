---
type: product
id: cpr-tutor
title: CPR Tutor
description: "CPR Tutor is a C# multimodal CPR-training application developed by Di Mitri et al."
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# CPR Tutor

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 quant-synthesis), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
CPR Tutor is a C# multimodal CPR-training application developed by Di Mitri et al. that uses Kinect depth-camera and Myo EMG data to classify chest-compression technique and provide real-time audio feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CPR Tutor system architecture implementing the five-step Multimodal Pipeline with three layers**: The CPR Tutor is a C# application collecting Kinect v2 depth-camera and Myo EMG armband data for CPR training. Its architecture "implements the five-step approach introduced by the Multimodal Pipeline" for collection, storing, annotation, processing and exploitation of multimodal data, and features Presentation, Application and Data layers. It supports offline model training and real-time exploitation with audio feedback. (Di Mitri et al. (2022))
- **Voice advisory mannequin (VAM) with feedback and voice prompts for self-directed CPR training**: A training mannequin equipped with a feedback system and voice prompts that correct errors during CPR practice, enabling self-directed learning without a continuous instructor presence. The review identifies it as the most effective resource analysed for CPR skill learning among health science students, noting it "allows them to correct their mistakes or undertake knowledge refreshers independently". It appeared in four of the eleven reviewed trials as the intervention device. (García-Suárez et al. (2019))

### Claims
- [The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision](../claims/cpr-tutor-real-time-classification-speed.md) [+M]
- [Real-time audio feedback from the CPR Tutor is followed by a short-term decrease in Error Rates across all five target CPR classes within 10 seconds](../claims/cpr-tutor-short-term-error-rate-decrease.md) [+M]
- [Voice advisory mannequin training produces better CPR skill acquisition than other training resources among health science students, though not in every comparison](../claims/vam-training-better-cpr-skills-health-students.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Di Mitri, D., Schneider, J., & Drachsler, H. (2022). KeepMeInTheLoop: Real-Time Feedback with Multimodal Data. International Journal of Artificial Intelligence in Education (2022) 32:1093–1118. https://doi.org/10.1007/s40593-021-00281-z
- García-Suárez, M., Méndez-Martínez, C., Martínez-Isasi, S., Gómez-Salgado, J., & Fernández-García, D. (2019). Basic Life Support Training Methods for Health Science Students: A Systematic Review. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph16050768
