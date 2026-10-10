---
type: design
id: skin-lesion-group-annotation-activity
title: Two-part skin lesion annotation activity (individual dataset exploration plus group annotation on a 3-point scale) implemented at Fontys and ITU Copenhagen
description: "An educational activity integrated into two existing courses: Data Mining (5 ECTS, Fontys) and Projects in Data Science (7.5 ECTS, ITU)."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: ralf-raumanns-2026
    resource: "https://arxiv.org/abs/2607.20149v2"
    title: "Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149v2"
    author: Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina
---

# Two-part skin lesion annotation activity (individual dataset exploration plus group annotation on a 3-point scale) implemented at Fontys and ITU Copenhagen

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An educational activity integrated into two existing courses: Data Mining (5 ECTS, Fontys) and Projects in Data Science (7.5 ECTS, ITU). The first part is an individual Jupyter-notebook assignment exploring ISIC (or PAD-UFES-20) images including agreement analysis; the second is a group task annotating 100–200 skin lesion images for visible hair on a 3-point ordinal scale (0 = none, 1 = some, 2 = a lot), using Label Studio or a CSV template. Group members annotate the same subset to enable comparison of inter-annotator agreement. Surveys from 43 students measured its pedagogical effectiveness.

## Design Implications

### Context
#### Requirements
- Each group annotates at least 100 images with all members labelling the same subset to enable inter-annotator agreement analysis
#### Constraints
- The annotation task was a mandatory course component at both institutions, while the survey was voluntary
- At ITU the task later used the PAD-UFES-20 smartphone image dataset instead of ISIC

### Target Learners
- Fourth-semester bachelor students at Fontys University of Applied Sciences
- Second-semester bachelor students at IT University of Copenhagen

### Learning Goals
- Critical thinking about data quality and label subjectivity
- Understanding bias and fairness in AI models
- Data literacy and ethical awareness in machine learning

### Claims
- Annotation Task Familiarity Gains Subjectivity Bias [+M]
- [Moderate Kappa Versus Perceived Consensus Gap](../claims/moderate-kappa-versus-perceived-consensus-gap.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149v2
