---
type: design
id: unreal-engine-4-vr-desktop-assembly-training-systems
title: Paired VR and desktop structural cognition training systems built in Unreal Engine 4 with model, UV, and rendering optimization
description: "The study developed \"two structural cognition training systems using Unreal Engine 4 for VR and desktop platforms\" around assembling a machine vise, deployed on Oculus Quest 2 headsets and Windows 10 PCs."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: weichao-lin-2023
    resource: "https://arxiv.org/abs/2312.10387"
    title: "Weichao Lin, Liang Chen, Wei Xiong, Kang Ran, Anlan Fan. (2023). Measuring the Sense of Presence and Learning Efficacy in Immersive Virtual Assembly Training. https://arxiv.org/abs/2312.10387"
    author: Weichao Lin, Liang Chen, Wei Xiong, Kang Ran, Anlan Fan
---

# Paired VR and desktop structural cognition training systems built in Unreal Engine 4 with model, UV, and rendering optimization

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The study developed "two structural cognition training systems using Unreal Engine 4 for VR and desktop platforms" around assembling a machine vise, deployed on Oculus Quest 2 headsets and Windows 10 PCs. Because Quest 2 has "limited computational power similar to smartphones", the pipeline includes model topology reduction (Maya Quadrangulate/QuadRemesher), UDIM UV tiling, and Forward Rendering with MSAA for VR. Both configurations share most software modules and handle task visuals and audio identically.

## Design Implications

### Context
#### Requirements
- Optimization measures are crucial to achieve real-time rendering of high-quality visuals and smooth performance on headset hardware
- Unreal Engine 4 was chosen over Unity 3D for demanding artistic expression and high realism
#### Constraints
- VR device computational power is limited, similar to smartphones
- Prolonged headset wear may cause neck fatigue and motion sickness

### Target Learners
- undergraduate engineering students
- manufacturing industry employees in training initiatives

### Learning Goals
- bench vise assembly structure comprehension
- component name familiarity
- assembly-disassembly skill

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Weichao Lin, Liang Chen, Wei Xiong, Kang Ran, Anlan Fan. (2023). Measuring the Sense of Presence and Learning Efficacy in Immersive Virtual Assembly Training. https://arxiv.org/abs/2312.10387
