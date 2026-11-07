---
type: design
id: multimodal-sensing-laryngoscope-biometrics
title: Multi-modal sensing framework with pressure-instrumented laryngoscope and biometric vest
description: "The system's data-acquisition layer streams real-time performance and physiological data during simulation."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: jain-saurabh-2025
    resource: "https://doi.org/10.1109/JTEHM.2025.3529748"
    title: "Jain Saurabh, Dripta Barua Chowdhury Bijoy, Mosier Jarrod M., Subbian Vignesh, Hughes Kate, Son Young-Jun. (2025). Design and Development of an Integrated Virtual Reality (VR)-Based Training System for Difficult Airway Management. IEEE Journal of Translational Engineering in Health and Medicine. https://doi.org/10.1109/JTEHM.2025.3529748"
    author: Jain Saurabh, Dripta Barua Chowdhury Bijoy, Mosier Jarrod M., Subbian Vignesh, Hughes Kate, Son Young-Jun
---

# Multi-modal sensing framework with pressure-instrumented laryngoscope and biometric vest

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system's data-acquisition layer streams real-time performance and physiological data during simulation. The article states that "The backend data collection module captures and utilizes real-time sensory data from: (a) HTC Vive VR headset, (b) pressure sensing module, and (c) Hexoskin biometric vest", with five pressure sensors, an Arduino nano BLE, and battery embedded in the laryngoscope. Data stream at 10 Hz, capturing pressure profiles, tool position, heart rate variability and respiratory rate for offline analysis of technical and cognitive performance.

## Design Implications

### Context
#### Requirements
- A data streaming frequency of 10 Hz to ensure smooth data collection and real-time analysis without lag
- Pressure values streamed only when the laryngoscope tip approaches the collider near goal anatomical structures to reduce computational lag
#### Constraints
- 

### Target Learners
- medical trainees
- simulation researchers

### Learning Goals
- objective measurement of procedural performance
- study of decision-making and stress responses during airway management

### Claims
- 

## Related Designs
- Hybrid Vr Airway Management Training System

## Examples
-

## Key Sources
- Jain Saurabh, Dripta Barua Chowdhury Bijoy, Mosier Jarrod M., Subbian Vignesh, Hughes Kate, Son Young-Jun. (2025). Design and Development of an Integrated Virtual Reality (VR)-Based Training System for Difficult Airway Management. IEEE Journal of Translational Engineering in Health and Medicine. https://doi.org/10.1109/JTEHM.2025.3529748
