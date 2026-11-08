---
type: design
id: e-gal-reference-implementation
title: e-GAL reference implementation for German word learning (Unity WebGL player, XSENS gestures, webcam monitoring)
description: A working reference implementation of the e-GAL design built to learn German words.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: kremser-wolfgang-2021
    resource: "https://doi.org/10.3390/s21238042"
    title: "Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin. (2021). Design and Implementation of a Gesture-Aided E-Learning Platform. Sensors. https://doi.org/10.3390/s21238042"
    author: Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin
---

# e-GAL reference implementation for German word learning (Unity WebGL player, XSENS gestures, webcam monitoring)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A working reference implementation of the e-GAL design built to learn German words. The content catalog held 64 German words with text and WaveNet synthesized speech in PostgreSQL; gestures were recorded with the XSENS MTw Awinda full-body motion-capture system and exported as FBX files; the lesson player was a Unity 3D WebGL application featuring the robot-like avatar Y-Bot; and the webcam recorded learners during each GEC for upload to the monitoring log. The article reports: "The lesson player (Figure 5) of the reference implementation was a Unity 3D [32] application running in a WebGL environment."

## Design Implications

### Context
#### Requirements
- Learners assumed to sit behind a desk in front of a screen so the webcam captures at least the upper body
- Gestures chosen so they can be performed while sitting behind a desk
#### Constraints
- The avatar's extremities lacked collision boxes, so hands clipped into rather than touching each other
- The XSENS skeletal model has only a rough positioning of the hands

### Target Learners
- Adult remote learners (12 female, 7 male, mean age 36.6) with basic knowledge of using web applications

### Learning Goals
- German vocabulary learning with gesture enactment

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin. (2021). Design and Implementation of a Gesture-Aided E-Learning Platform. Sensors. https://doi.org/10.3390/s21238042
