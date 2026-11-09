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
> **Evidence** · 5 claims (5 for) · 3 studies (1 causal, 1 quant-synthesis, 1 design), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
CPR Tutor is a C# multimodal CPR-training application developed by Di Mitri et al. that uses Kinect depth-camera and Myo EMG data to classify chest-compression technique and provide real-time audio feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CPR Tutor system architecture implementing the five-step Multimodal Pipeline with three layers**: The CPR Tutor is a C# application collecting Kinect v2 depth-camera and Myo EMG armband data for CPR training. Its architecture "implements the five-step approach introduced by the Multimodal Pipeline" for collection, storing, annotation, processing and exploitation of multimodal data, and features Presentation, Application and Data layers. It supports offline model training and real-time exploitation with audio feedback. (Di Mitri et al. (2022))
- **Voice advisory mannequin (VAM) with feedback and voice prompts for self-directed CPR training**: A training mannequin equipped with a feedback system and voice prompts that correct errors during CPR practice, enabling self-directed learning without a continuous instructor presence. The review identifies it as the most effective resource analysed for CPR skill learning among health science students, noting it "allows them to correct their mistakes or undertake knowledge refreshers independently". It appeared in four of the eleven reviewed trials as the intervention device. (García-Suárez et al. (2019))
- **Multimodal Tutor for CPR — a multi-sensor intelligent tutoring system combining Kinect, Myo armband and ResusciAnne manikin data**: The Multimodal Tutor for CPR is "a multi-sensor, intelligent tutoring system to train CPR using the ResusciAnne manikins", built as "a specific implementation of the Multimodal Tutoring System, consisting of a Kinect camera and a Myo armband". It gathers 60 Kinect attributes from 15 body joints, 18 Myo attributes, and SimPad baseline indicators, and its mistake-detection system was validated with LSTM classifiers on data from 11 experts. The authors demonstrate that "multimodal data can be used as the base to drive machine reasoning and adaptation during learning" for automatic and retrospective feedback. (Di Mitri Daniele et al. (2019))

### Claims
- [The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision](../claims/cpr-tutor-real-time-classification-speed.md) [+M]
- [Real-time audio feedback from the CPR Tutor is followed by a short-term decrease in Error Rates across all five target CPR classes within 10 seconds](../claims/cpr-tutor-short-term-error-rate-decrease.md) [+M]
- [Voice advisory mannequin training produces better CPR skill acquisition than other training resources among health science students, though not in every comparison](../claims/vam-training-better-cpr-skills-health-students.md) [+M]
- [Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline](../claims/multimodal-data-detect-standard-cpr-mistakes.md) [+M]
- [Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy](../claims/multimodal-detect-additional-cpr-mistakes.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Di Mitri, D., Schneider, J., & Drachsler, H. (2022). KeepMeInTheLoop: Real-Time Feedback with Multimodal Data. International Journal of Artificial Intelligence in Education (2022) 32:1093–1118. https://doi.org/10.1007/s40593-021-00281-z
- García-Suárez, M., Méndez-Martínez, C., Martínez-Isasi, S., Gómez-Salgado, J., & Fernández-García, D. (2019). Basic Life Support Training Methods for Health Science Students: A Systematic Review. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph16050768
- Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099
