---
type: design
id: crazyflie-loco-positioning-drone-mechanics-testbed
title: Crazyflie 2.1 and Loco Positioning System hardware configuration for drone-based mechanics demonstrations
description: "The experimental testbed comprises Bitcraze's open-source Crazyflie 2.1 nano quadcopters (92 mm rotor-to-rotor, about 27 g with battery), each carrying a Loco Positioning Deck tag in an Ultra Wide Band indoor position..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: harshvardhan-uppaluru-and-hossein-rastgoftar-2022
    resource: "https://arxiv.org/abs/2201.08004"
    title: "Harshvardhan Uppaluru and Hossein Rastgoftar. (2022). Drones Practicing Mechanics. https://arxiv.org/abs/2201.08004"
    author: Harshvardhan Uppaluru and Hossein Rastgoftar
---

# Crazyflie 2.1 and Loco Positioning System hardware configuration for drone-based mechanics demonstrations

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The experimental testbed comprises Bitcraze's open-source Crazyflie 2.1 nano quadcopters (92 mm rotor-to-rotor, about 27 g with battery), each carrying a Loco Positioning Deck tag in an Ultra Wide Band indoor positioning system with Loco Positioning Nodes as anchors, communicating with a PC via Crazyradio PA. The authors "choose the Time Di erence of Arrival 3 (TDoA3) positioning mode since it can accommodate an unlimited number of Crazy ies and Anchors." Flight experiments used ROS Noetic with the Crazyswarm ROS stack in an indoor flying area with eight positioning nodes.

## Design Implications

### Context
#### Requirements
- Loco Positioning Nodes positioned at the corners of the flying volume as reference points
- Crazyradio PA link and the Crazyswarm ROS stack for flight control
#### Constraints
- LPS tracking of quadcopters is accurate up to 0.1 m, which motivated choosing a more conservative tracking error δ = 0.125 m

### Target Learners
- junior undergraduate engineering students

### Learning Goals
- strain and deformation analysis
- multi-agent coordination

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Harshvardhan Uppaluru and Hossein Rastgoftar. (2022). Drones Practicing Mechanics. https://arxiv.org/abs/2201.08004
