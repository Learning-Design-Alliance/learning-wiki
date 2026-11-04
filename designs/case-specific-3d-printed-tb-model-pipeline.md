---
type: design
id: case-specific-3d-printed-tb-model-pipeline
title: Case-specific 3D-printed temporal bone model pipeline (CBCT imaging, VESTool segmentation, STL printing)
description: "The article describes a manufacturing pipeline for case-specific 3D-printed temporal bone models: cadaveric temporal bones were scanned on a cone-beam CT scanner, DICOM data were imported into \"VESTool (in-house softw..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: omari-adam-2026
    resource: "https://doi.org/10.1007/s00405-026-10099-x"
    title: "Omari Adam, Nøhr Anders, Suleiman Elissa, Cayé‑Thomasen Per, Sørensen Mads Sølvsten, Frithioff Andreas, Andersen Steven Arild Wuyts. (2026). Effect of case-specific 3D-printed models on surgical performance in cadaveric dissection—a randomized controlled trial. European Archives of Oto-Rhino-Laryngology. https://doi.org/10.1007/s00405-026-10099-x"
    author: Omari Adam, Nøhr Anders, Suleiman Elissa, Cayé‑Thomasen Per, Sørensen Mads Sølvsten, Frithioff Andreas, Andersen Steven Arild Wuyts
---

# Case-specific 3D-printed temporal bone model pipeline (CBCT imaging, VESTool segmentation, STL printing)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a manufacturing pipeline for case-specific 3D-printed temporal bone models: cadaveric temporal bones were scanned on a cone-beam CT scanner, DICOM data were imported into "VESTool (in-house software for 3D segmentation)", which resampled the virtual models to 0.2 mm voxel size and segmented the bony volume using "interactive and localized thresholding features with minimal manual effort required"; models were exported as STL files and 3D-printed with identical specifications, then individually drilled to validate accuracy against CT imaging data.

## Design Implications

### Context
#### Requirements
- Requires CBCT imaging of the target bone, segmentation software, 3D printing, and quality control by test drilling to validate accuracy against imaging data
#### Constraints
- The authors state manufacturing case-specific models requires considerably more resources and effort than standard models, with 1–4 h spent per model, making routine use unlikely to be cost-effective for initial training until automation reduces manual steps

### Target Learners
- ORL residents in simulation-based temporal bone training

### Learning Goals
- rehearsal and planning of mastoidectomy on patient-specific anatomy

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Omari Adam, Nøhr Anders, Suleiman Elissa, Cayé‑Thomasen Per, Sørensen Mads Sølvsten, Frithioff Andreas, Andersen Steven Arild Wuyts. (2026). Effect of case-specific 3D-printed models on surgical performance in cadaveric dissection—a randomized controlled trial. European Archives of Oto-Rhino-Laryngology. https://doi.org/10.1007/s00405-026-10099-x
