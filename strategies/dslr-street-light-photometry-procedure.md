---
type: strategy
id: dslr-street-light-photometry-procedure
title: "Photometry procedure: raw-format capture, aperture photometry with background subtraction, and spreadsheet analysis"
description: "An implementable measurement recipe for the activity: save DSLR images in raw format so pixel values remain proportional to received light, convert to a measurable format, and perform aperture-style photometry that su..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: markus-pössel-2017
    resource: "https://arxiv.org/abs/1702.02391"
    title: "Markus Pössel. (2017). Street lights as standard candles: A student activity for understanding astronomical distance measurements. astroEDU 1535. https://arxiv.org/abs/1702.02391"
    author: Markus Pössel
---

# Photometry procedure: raw-format capture, aperture photometry with background subtraction, and spreadsheet analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
An implementable measurement recipe for the activity: save DSLR images in raw format so pixel values remain proportional to received light, convert to a measurable format, and perform aperture-style photometry that sums pixel brightness over a region containing the lamp while subtracting background estimated from a shielded area above each lamp. The article instructs that "the first step is to make the camera save the image in a raw format, which does not throw any of the brightness information away". Calculations are simple enough for a spreadsheet.

## Design Implications

### Context
#### Requirements
- Raw-format image capture to preserve linear pixel values
- Background estimate from a region shielded from the lamp's own light
- Exposure chosen so no pixel is saturated
#### Constraints
- JPG images are processed non-linearly and are not intended for quantitative measurements

### Target Learners
- high school physics students
- astronomy club members

### Target Learning Goals
- learning astronomical photometry techniques
- performing quantitative image analysis

## Related Strategies

- [Three-hour exoplanet transit analysis activity using differential photometry of public telescope images](wasp2b-differential-photometry-classroom-activity.md)
- [Delay the automated photometry pipeline so students analyse raw data first, then compare with the reference pipeline](delayed-pipeline-student-analysis-first.md)

## Examples
-

## Key Sources
- Markus Pössel. (2017). Street lights as standard candles: A student activity for understanding astronomical distance measurements. astroEDU 1535. https://arxiv.org/abs/1702.02391
