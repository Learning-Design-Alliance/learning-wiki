---
type: design
id: kpu-mk-ii-webcam-ccd-camera
title: "KPU Mk II: a telescope camera built from a retail webcam's CCD"
description: "A low-cost imaging camera made by removing 'the lens and much of the factory casing from a webcam' and retaining the electronics as-is, with 'a tube matching the diameter of an eyepiece' placed over the imaging chip s..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: takashi-sato-2013
    resource: "https://arxiv.org/abs/1312.1788"
    title: "Takashi Sato. (2013). Imaging the Moon II: Webcam CCD Observations & Analysis (a two week lab for non-majors). ASP Conference Series. https://arxiv.org/abs/1312.1788"
    author: Takashi Sato
---

# KPU Mk II: a telescope camera built from a retail webcam's CCD

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A low-cost imaging camera made by removing 'the lens and much of the factory casing from a webcam' and retaining the electronics as-is, with 'a tube matching the diameter of an eyepiece' placed over the imaging chip so the CCD sits at the telescope's focal plane. Removing the lens sets an image scale that places each frame across a small lunar region, forcing students to plan and combine frames into a mosaic.

## Design Implications

### Context
#### Requirements
- A retail webcam, an eyepiece-diameter tube, and a telescope with an eyepiece holder; stock webcam software controls capture.
#### Constraints
- Default auto-exposure software sets exposure by average pixel value across the frame, producing an overexposed lunar surface when blank sky dominates a frame; manual overrides are considered beyond the non-majors course scope. Nominally identical cameras can have CCD chips of varying size, resulting in varying sky coverage.

### Target Learners
- non-major undergraduate astronomy students

### Learning Goals
- capturing telescope images for quantitative analysis

### Claims
- Two Week Webcam Lunar Imaging Lab [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Takashi Sato. (2013). Imaging the Moon II: Webcam CCD Observations & Analysis (a two week lab for non-majors). ASP Conference Series. https://arxiv.org/abs/1312.1788
