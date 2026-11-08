---
type: design
id: distance-force-visualisation-concept-set
title: "Distance and force visualisation concept set: colour maps, cylinders, rays and glyphs"
description: The article integrates three distance visualisation concepts (a colour map on the vessel surface, a cylinder highlighting the smallest distance, and semi-transparent rays showing all distances below a threshold) and f...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: allgaier-m-2021
    resource: "https://doi.org/10.1007/s11548-021-02413-1"
    title: "Allgaier M, Neyazi B, Preim B, Saalfeld S. (2021). Distance and force visualisations for improved simulation of intracranial aneurysm clipping. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-021-02413-1"
    author: Allgaier M, Neyazi B, Preim B, Saalfeld S
---

# Distance and force visualisation concept set: colour maps, cylinders, rays and glyphs

> **Design** · [All designs](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article integrates three distance visualisation concepts (a colour map on the vessel surface, a cylinder highlighting the smallest distance, and semi-transparent rays showing all distances below a threshold) and four force visualisation concepts (colour map, semi-transparent displacement rays, arrow glyphs and drop glyphs scaled and faded by strength). All concepts employ an underlying colour scale classifying values into low, mid-range and high regions, with green for non-critical and red for critical values.

## Design Implications

### Context
#### Requirements
- An underlying colour scale; the drop glyph scales only within a certain range and is drawn semi-transparently so strong displacements do not occlude smaller ones
#### Constraints
- The green-to-red map is not usable for people with dyschromatopsia, for whom a red-to-blue scale is provided

### Target Learners
- neurosurgeons
- neurosurgery trainees

### Learning Goals
- perceiving clip-to-vessel distances
- assessing force on vessel surface

### Claims

- [Colour Map Best Force Visualisation Clipping Survey](../claims/colour-map-best-force-visualisation-clipping-survey.md) [+M]
- [Semi-transparent distance rays were the only distance visualisation concept that supported clip navigation appropriately](../claims/distance-rays-only-concept-supporting-navigation.md) [+W]
- [A neurosurgeon expert rated the simulation workflow as clear and intuitive and the vessel deformation as plausible](../claims/expert-rates-workflow-clear-deformation-plausible.md) [+W]
- [On a monoscopic desktop display, distance visualisations are required for proper clip navigation, as the expert could not estimate depth without them](../claims/distance-visualisations-required-monoscopic-navigation.md) [+W]
- [The mixed-reality aneurysm clipping simulator achieved robust face and content validity, with mean questionnaire scores between 3.13 and 4.25 among 40 neurosurgeons](../claims/medusa-simulator-face-content-validity.md) [+W]
- [Blood flow simulation was the highest-rated simulator component (mean 4.25), and preoperative planning potential was rated 4.20](../claims/medusa-blood-flow-simulation-highest-rated.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Allgaier M, Neyazi B, Preim B, Saalfeld S. (2021). Distance and force visualisations for improved simulation of intracranial aneurysm clipping. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-021-02413-1
