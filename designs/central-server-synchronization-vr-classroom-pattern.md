---
type: design
id: central-server-synchronization-vr-classroom-pattern
title: Central-server synchronization pattern replacing peer-to-peer HMD relaying for multi-user VR classrooms
description: The design pattern routes all client communication through Photon Cloud as a central server that synchronizes object states and audio among all clients in real time, instead of the prior peer-to-peer arrangement whose...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: iwai-wataru-2026
    resource: "https://arxiv.org/abs/2606.10325"
    title: "Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325"
    author: Iwai Wataru, Duc V . Nguyen
---

# Central-server synchronization pattern replacing peer-to-peer HMD relaying for multi-user VR classrooms

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The design pattern routes all client communication through Photon Cloud as a central server that synchronizes object states and audio among all clients in real time, instead of the prior peer-to-peer arrangement whose performance "depended on the processing power of the Head-Mounted Display (HMD)". This decouples stability from individual headset processing load and supports simultaneous multi-user participation.

## Design Implications

### Context
#### Requirements
- A central synchronization server (Photon Cloud) reachable by all clients over Wi-Fi
#### Constraints
- The prior peer-to-peer approach became unstable with multiple users, with FPS unstable and only up to five participants possible

### Target Learners
- undergraduate and graduate students in VR-supported lessons

### Learning Goals
- real-time shared manipulation of 3D learning materials with voice communication

### Claims
- [Photon Fusion Stable Realtime Communication](../claims/photon-fusion-stable-realtime-communication.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325
