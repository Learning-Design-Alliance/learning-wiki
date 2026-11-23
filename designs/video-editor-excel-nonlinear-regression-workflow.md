---
type: design
id: video-editor-excel-nonlinear-regression-workflow
title: "Frame-by-frame video analysis workflow: Windows 10 Video Editor frame stepping plus Excel nonlinear regression with Solver for laboratory data"
description: "The article describes a data-capture and processing workflow in which the built-in \"Windows 10's built-in ”Video Editor”\" is used to \"view the video frame by frame\", with a time step of 0.033 s, capturing about 130 fr..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: ivan-z-stefanov-2023
    resource: "https://arxiv.org/abs/2304.11390"
    title: "Ivan Z. Stefanov, Nikolay Denev, Sava Donkov. (2023). VIDEO ANALYSIS OF THE DAMPED OSCILLATIONS OF POHL'S PENDULUM. Rom. Rep. Phys. (preprint). https://arxiv.org/abs/2304.11390"
    author: Ivan Z. Stefanov, Nikolay Denev, Sava Donkov
---

# Frame-by-frame video analysis workflow: Windows 10 Video Editor frame stepping plus Excel nonlinear regression with Solver for laboratory data

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a data-capture and processing workflow in which the built-in "Windows 10's built-in ”Video Editor”" is used to "view the video frame by frame", with a time step of 0.033 s, capturing about 130 frames over 4.5 s (2.5 periods). Deviations are entered into Excel, where the model function's four free parameters are optimised by minimising the SSD merit function with the Solver add-in, and fit quality is checked with a weighted chi-square. This replaces the standard once-per-period amplitude reading with a dense time series.

## Design Implications

### Context
#### Requirements
- A video recording of the laboratory exercise with a known frame rate and readable scale divisions
- Microsoft Excel with the Solver function enabled
#### Constraints
- Frames are step-processed at 0.033 s, so processes faster than the frame interval are undersampled; duplicate adjacent frames were discarded

### Target Learners
- undergraduate physics laboratory students

### Learning Goals
- data analysis and nonlinear regression skills
- understanding damped mechanical oscillations

### Claims
- Video Data Nonlinear Regression Fitted Parameters [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ivan Z. Stefanov, Nikolay Denev, Sava Donkov. (2023). VIDEO ANALYSIS OF THE DAMPED OSCILLATIONS OF POHL'S PENDULUM. Rom. Rep. Phys. (preprint). https://arxiv.org/abs/2304.11390
