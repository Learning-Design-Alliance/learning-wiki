---
type: design
id: photon-fusion-vr-immersive-learning-system
title: Photon Fusion-based multi-site VR immersive learning system with real-time voice and shared 3D materials
description: A VR learning environment in which teachers and students connect via Wi-Fi using VR headsets and communicate through Photon Cloud, which acts as a central server to synchronize object states and audio among all client...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: iwai-wataru-2026
    resource: "https://arxiv.org/abs/2606.10325"
    title: "Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325"
    author: Iwai Wataru, Duc V . Nguyen
---

# Photon Fusion-based multi-site VR immersive learning system with real-time voice and shared 3D materials

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A VR learning environment in which teachers and students connect via Wi-Fi using VR headsets and communicate through Photon Cloud, which acts as a central server to synchronize object states and audio among all clients in real time. Voice communication integrates Photon Fusion with Photon Voice 2, initiated when a client enters the VR classroom. Learning materials include 3D chemistry apparatus, e.g. a flask containing Calcium hypochlorite and a pipette containing hydrochloric acid, with chlorine gas rendered as yellow-green smoke that bleaches blue litmus paper.

## Design Implications

### Context
#### Requirements
- Participants connect to the Internet via Wi-Fi using a VR headset (Meta Quest 3 in the reported use)
#### Constraints
- The prior peer-to-peer system it replaces supported only up to five people; the new system is designed for twenty participants

### Target Learners
- undergraduate and graduate students

### Learning Goals
- science experiment learning, e.g. three-dimensional understanding of chemistry phenomena

### Claims

- [VR sickness in the system is minimal overall (SSQ total 12.88), with nausea lowest and oculomotor symptoms most significant](../claims/photon-fusion-minimal-vr-sickness-ssq.md) [+W]
- [The system receives a good average usability rating (SUS 69.7, grade B) but with wide individual variation, which the authors take to suggest UI consistency issues](../claims/photon-fusion-sus-good-but-variable-usability.md) [+W]

## Related Designs

- [Central-server synchronization pattern replacing peer-to-peer HMD relaying for multi-user VR classrooms](central-server-synchronization-vr-classroom-pattern.md)

## Examples
-

## Key Sources
- Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325
