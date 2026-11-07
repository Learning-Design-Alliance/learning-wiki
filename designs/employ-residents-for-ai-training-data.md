---
type: design
id: employ-residents-for-ai-training-data
title: Employ radiology residents, with an initial introduction and continuous feedback, to prepare segmentation training data for AI development
description: The article recommends that for preparing datasets for artificial intelligence development, employing radiology residents seems safe and provides a good balance between cost-effectiveness and segmentation accuracy.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: langkilde-fredrik-2024
    resource: "https://doi.org/10.1007/s00330-023-10515-4"
    title: "Langkilde Fredrik, Masaba Patrick, Edenbrandt Lars, Gren Magnus, Halil Airin, Hellström Mikael, Larsson Måns, Naeem Ameer Ali, Wallström Jonas, Maier Stephan E., Jäderling Fredrik. (2024). Manual prostate MRI segmentation by readers with different experience: a study of the learning progress. European Radiology. https://doi.org/10.1007/s00330-023-10515-4"
    author: Langkilde Fredrik, Masaba Patrick, Edenbrandt Lars, Gren Magnus, Halil Airin, Hellström Mikael, Larsson Måns, Naeem Ameer Ali, Wallström Jonas, Maier Stephan E., Jäderling Fredrik
---

# Employ radiology residents, with an initial introduction and continuous feedback, to prepare segmentation training data for AI development

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that for preparing datasets for artificial intelligence development, employing radiology residents seems safe and provides a good balance between cost-effectiveness and segmentation accuracy. In the authors' words, "To prepare datasets for AI development, employing radiology residents seems safe and provides a good balance between cost-effectiveness and segmentation accuracy." The conclusion adds this should follow an initial introduction and evaluation, with continuous feedback, while employing novices should only be considered on an individual basis.

## Design Implications

### Context
#### Requirements
- An initial introduction and evaluation of readers before data collection
- Continuous feedback from an expert during segmentation
#### Constraints
- The article states employing novices should only be considered on an individual basis due to higher inter-reader variability
- Findings come from a single center and one scanner and protocol, which the authors note might limit generalization

### Target Learners
- radiology residents

### Learning Goals
- producing accurate whole-gland prostate segmentation labels for AI training data

### Claims
- [Residents High Prostate Segmentation Accuracy](../claims/residents-high-prostate-segmentation-accuracy.md) [+M]
- [Novice Inter Reader Variability Higher](../claims/novice-inter-reader-variability-higher.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Langkilde Fredrik, Masaba Patrick, Edenbrandt Lars, Gren Magnus, Halil Airin, Hellström Mikael, Larsson Måns, Naeem Ameer Ali, Wallström Jonas, Maier Stephan E., Jäderling Fredrik. (2024). Manual prostate MRI segmentation by readers with different experience: a study of the learning progress. European Radiology. https://doi.org/10.1007/s00330-023-10515-4
