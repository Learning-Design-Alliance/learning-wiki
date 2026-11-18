---
type: design
id: marker-based-ar-object-development
title: "Marker-based AR object development pattern: a 3D model, a quickly recognizable 2D marker, and a marker-to-model association in the AR software"
description: "The article describes, following Caudell and Mizell, the workflow for building an AR object: \"1) у 3D-середовищі створюється візуальна модель компоненту доповненої реальності;\" a simple 2D marker that the AR system ca..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: modlo-e-o-2016
    resource: "https://scholar.google.com/scholar?q=Using+Technology+of+Augmented+Reality+in+a+Mobile-Based+Learning+Environment+of+the+Higher+Educational+Institution"
    title: "Modlo E. O., Echkalo Y. V., Semerikov S. O., Tkachuk V. V. (2016). USING TECHNOLOGY OF AUGMENTED REALITY IN A MOBILE-BASED LEARNING ENVIRONMENT OF THE HIGHER EDUCATIONAL INSTITUTION. НАУКОВI ЗАПИСКИ Серія: Проблеми методики фізико-математичної і технологічної освіти, Випуск 11(І). https://scholar.google.com/scholar?q=Using+Technology+of+Augmented+Reality+in+a+Mobile-Based+Learning+Environment+of+the+Higher+Educational+Institution"
    author: Modlo E. O., Echkalo Y. V., Semerikov S. O., Tkachuk V. V
---

# Marker-based AR object development pattern: a 3D model, a quickly recognizable 2D marker, and a marker-to-model association in the AR software

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article describes, following Caudell and Mizell, the workflow for building an AR object: "1) у 3D-середовищі створюється візуальна модель компоненту доповненої реальності;" a simple 2D marker that the AR system can quickly recognize is created in a 2D environment, and in the AR-support software the marker is associated with the 3D model. On recognition, the corresponding 3D model is overlaid on the recognized marker image on the device screen. Laboratory stands and measuring instruments serve as markers, e.g. supplemented with usage instructions.

## Design Implications

### Context
#### Requirements
- A 3D visual model of the AR component, a simple 2D marker quickly recognizable by the AR system, and marker–model linkage in the AR software
#### Constraints
- Marker tracking is specific to the software architecture used for marker detection and tracking, as the article notes for prepared scenes

### Target Learners
- higher education students in physics laboratory courses

### Learning Goals
- visualizing instructions and learning materials during laboratory work

### Claims
- [Ar Mobile Lab Environment Benefits](../claims/ar-mobile-lab-environment-benefits.md) [+W]

## Related Designs

- [Structured workflow integrating donor-specific pathologies and XR technologies into a case-based learning framework for gross anatomy](donor-derived-xr-cbl-workflow-pattern.md)

## Examples
-

## Key Sources
- Modlo E. O., Echkalo Y. V., Semerikov S. O., Tkachuk V. V. (2016). USING TECHNOLOGY OF AUGMENTED REALITY IN A MOBILE-BASED LEARNING ENVIRONMENT OF THE HIGHER EDUCATIONAL INSTITUTION. НАУКОВI ЗАПИСКИ Серія: Проблеми методики фізико-математичної і технологічної освіти, Випуск 11(І). https://scholar.google.com/scholar?q=Using+Technology+of+Augmented+Reality+in+a+Mobile-Based+Learning+Environment+of+the+Higher+Educational+Institution
