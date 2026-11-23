---
type: strategy
id: wearable-sensing-tailored-strategies-strategy
title: Use unobtrusive wearable sensing of physiological signals to tailor educational strategies and group students by synchronized responses
description: The article proposes using unobtrusive physiological sensing (EDA and HR via wrist-worn wearables) to understand engagement dynamics and adapt teaching.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: soundariya-ananthan-2024
    resource: "https://doi.org/10.1145/3675095.3676620"
    title: "Soundariya Ananthan, Nan Gao, and Flora D. Salim. 2024. Understanding Physiological Responses of Students Over Different Courses. In Proceedings of the 2024 ACM International Symposium on Wearable Computers (ISWC '24). https://doi.org/10.1145/3675095.3676620"
    author: Soundariya Ananthan, Nan Gao, and Flora D. Salim
---

# Use unobtrusive wearable sensing of physiological signals to tailor educational strategies and group students by synchronized responses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 10 claims (10 for) · 4 studies (2 associational, 1 review, 1 design), `q2` · 0 of 4 report an effect size · 9 claims rest on one study

## Description
The article proposes using unobtrusive physiological sensing (EDA and HR via wrist-worn wearables) to understand engagement dynamics and adapt teaching. It states this "opens up possibilities for tailoring educational strategies based on unobtrusive sensing data to optimize learning outcomes", and suggests that "collaborative learning environment can be created for students with synchronized physiological responses thereby enhancing their engagement". The strategy rests on the observed course- and student-level differences in physiological patterns.

## Design Implications

### Context
#### Requirements
- Students wear physiological sensing devices (e.g., Empatica E4) during classes so EDA and IBI/HR signals can be collected and analyzed per course and per student.
#### Constraints
- The article notes its analysis considers only a limited number of signals for some courses and does not completely consider the unique characteristics of each course.

### Target Learners
- K-12 classroom students

### Target Learning Goals
- Understanding and supporting student engagement across different courses

## Claims

- [Mean heart rate is higher in Assembly (109.4 bpm) than in PE (101.3 bpm), with both courses showing shorter NNI intervals than other courses](../claims/assembly-heart-rate-exceeds-pe.md) [+W]
- [EDA changepoint and autocorrelation values are high for PE and low for Assembly, with Assembly showing fewer SCR peaks](../claims/eda-changepoint-autocorrelation-course-differences.md) [+W]
- [Frequency-domain HRV features differ by course: Assembly shows high VLF and HF activation while PE has the lowest HF value](../claims/frequency-domain-hrv-course-differences.md) [+W]
- [PE shows the highest physiological synchrony score (195.3) and Assembly the lowest (3.3), with other courses scoring similarly](../claims/pe-highest-assembly-lowest-synchrony.md) [+W]
- [Students' physiological synchrony differs statistically significantly across academic courses, with all significant pairwise differences involving PE](../claims/physiological-synchrony-varies-across-courses.md) [+M]
- [Individual students exhibit unique physiological synchrony patterns across courses](../claims/unique-per-student-synchrony-patterns.md) [+W]
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](../claims/chest-ecg-strongest-cardiac-engagement-signal.md) [+W]
- [Static HRV devices were associated with high-correlation studies, while wristband and chest belt wearables showed no significant difference in correlation levels](../claims/hrv-device-accuracy-static-vs-wearable.md) [+W]
- [Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost](../claims/sensor-stream-performance-non-monotonic.md) [+W]
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](../claims/edugage-modality-aware-model-outperforms-baselines.md) [+W]

## Related Strategies

- [Choose sensing configurations by target metric and deployment burden, favoring compact five-stream or chest-ECG setups for lightweight deployments](engagement-sensing-configuration-tradeoff-strategy.md)
- [Design multimodal biometric sensing deployments to be minimally intrusive and validated against educational outcomes](minimally-intrusive-biometric-sensing-validation.md)
- [Use biometric mood sensing with machine learning to adaptively personalize the learning experience](biometric-mood-adaptive-personalization.md)

## Examples
-

## Key Sources
- Soundariya Ananthan, Nan Gao, and Flora D. Salim. 2024. Understanding Physiological Responses of Students Over Different Courses. In Proceedings of the 2024 ACM International Symposium on Wearable Computers (ISWC '24). https://doi.org/10.1145/3675095.3676620
