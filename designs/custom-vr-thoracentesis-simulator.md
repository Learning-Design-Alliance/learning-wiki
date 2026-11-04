---
type: design
id: custom-vr-thoracentesis-simulator
title: Custom VR thoracentesis simulator with real-time feedback but no haptic feedback
description: A custom-built VR thoracentesis simulator reconstructed a three-dimensional chest model from anonymized patient CT and ultrasound images in Yingtong 3D software, then imported it into Unity for rendering and interacti...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: han-shaoyu-2026
    resource: "https://doi.org/10.1186/s12909-026-09801-8"
    title: "Han Shaoyu, Tian Zhen, Cui Bingjun, Wu Lang, Chen Zhixiang. (2026). Virtual reality-based training improves thoracentesis skills in medical interns: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-026-09801-8"
    author: Han Shaoyu, Tian Zhen, Cui Bingjun, Wu Lang, Chen Zhixiang
---

# Custom VR thoracentesis simulator with real-time feedback but no haptic feedback

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A custom-built VR thoracentesis simulator reconstructed a three-dimensional chest model from anonymized patient CT and ultrasound images in Yingtong 3D software, then imported it into Unity for rendering and interactive function development. Deployed on the Yingtong VR platform with an HTC Vive headset and hand controllers, it provided "visual guidance, anatomical labeling, and performance feedback" on needle insertion angle, depth, and aspiration success. The system did not provide haptic (force) feedback, which 20% of participants identified as a limitation.

## Design Implications

### Context
#### Requirements
- Requires the Yingtong VR platform with HTC Vive headset and hand controllers, and real-time performance feedback functionality built in Unity
#### Constraints
- The system did not provide haptic (force) feedback, which 20% of participants later identified as a limitation

### Target Learners
- Final-year medical interns rotating through respiratory medicine

### Learning Goals
- Thoracentesis procedural skill: needle insertion site selection, angle, depth control, and aspiration technique

### Claims

- [Students trained via VR report significantly greater satisfaction than students trained on real patients or a mannequin](../claims/vr-training-greater-satisfaction-ecg-training.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Han Shaoyu, Tian Zhen, Cui Bingjun, Wu Lang, Chen Zhixiang. (2026). Virtual reality-based training improves thoracentesis skills in medical interns: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-026-09801-8
