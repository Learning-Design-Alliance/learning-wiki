---
type: strategy
id: engagement-sensing-configuration-tradeoff-strategy
title: Choose sensing configurations by target metric and deployment burden, favoring compact five-stream or chest-ECG setups for lightweight deployments
description: The article recommends treating sensing configuration as a design decision balancing predictive value against practical burden.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: zikang-leng-2026
    resource: "https://arxiv.org/abs/2605.01238"
    title: "Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238"
    author: Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz
---

# Choose sensing configurations by target metric and deployment burden, favoring compact five-stream or chest-ECG setups for lightweight deployments

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends treating sensing configuration as a design decision balancing predictive value against practical burden. It reports that "the preferred configuration depends on the performance metric and the practical cost of its sensors", with a five-stream setup (EEG, EDA, eSense IMU, HR, Ring Temperature) achieving the highest Within-1 and binary accuracy and chest ECG alone achieving the highest binary Macro-F1, so lighter deployments can drop streams without uniform loss.

## Design Implications

### Context
#### Requirements
- Screen candidate sensor combinations under the same participant-grouped evaluation protocol so performance changes reflect the simplified sensing setup
#### Constraints
- Differences between independently selected configurations at adjacent subset sizes should not be interpreted as the effect of adding or removing a single stream; performance is not monotonic in stream count

### Target Learners
- college students in self-guided computer-based video learning

### Target Learning Goals
- fine-grained estimation of attention difficulty under practical wearable deployment constraints

## Related Strategies
- 

## Examples
-

## Key Sources
- Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238
