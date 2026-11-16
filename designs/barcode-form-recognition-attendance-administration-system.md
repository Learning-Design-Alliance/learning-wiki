---
type: design
id: barcode-form-recognition-attendance-administration-system
title: Barcode-scanner and form-recognition attendance and assessment administration system with MySQL database
description: "An administrative toolkit for large classes: portable hand-held barcode scanners record lecture attendance from matriculation-card barcodes; paper enrolment forms and laboratory registers and MCQ answer sheets are bat..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-16
sources:
  - id: mm-casey-and-mw-kille-2011
    resource: "https://arxiv.org/abs/1102.2581"
    title: "MM Casey and MW Kille. (2011). Effective Administration of a Large Undergraduate Physics Class: From Enrolment to Assessment Feedback. Journal of Science Education / Revista de Educación en Ciencias 12 (2). https://arxiv.org/abs/1102.2581"
    author: MM Casey and MW Kille
---

# Barcode-scanner and form-recognition attendance and assessment administration system with MySQL database

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
An administrative toolkit for large classes: portable hand-held barcode scanners record lecture attendance from matriculation-card barcodes; paper enrolment forms and laboratory registers and MCQ answer sheets are batch-scanned and read by optical form recognition; all data feeds a bespoke MySQL database from which post-processing originates. The authors state form recognition "is particularly useful for collating the answers from multiple choice question (MCQ) papers" and that scanner data "is downloaded into a MySQL database on a daily basis". Requirements: a requirements

## Design Implications

### Context
#### Requirements
- Students must possess registration cards with a scannable barcode; adequate staffing to check signatures against barcodes and perform manual headcounts
#### Constraints
- Fixed scanners at room entrances caused severe bottle-necking, motivating portable handsets; class-register finalization still requires significant human effort because of early-semester student flux

### Target Learners
- first-year undergraduate physics students in large classes

### Learning Goals
- institutional retention and progression support; timely assessment feedback on continuous assessment

### Claims

- [Computer Based Administration Reduced Turnaround Times First Year Physics](../claims/computer-based-administration-reduced-turnaround-times-first-year-physics.md) [+M]
- [Rapid Marking Feedback Within 30 Minutes Class Of 240](../claims/rapid-marking-feedback-within-30-minutes-class-of-240.md) [+M]
- [The streamlined administration system coped with an unexpected 50% increase in class size by 2009-10](../claims/administration-system-coped-with-50-percent-class-size-increase.md) [+W]

## Related Designs

- [Self-developed learning platform with barcode-based assignment tracking in a personalized learning school](barcode-learning-platform-assignment-tracking.md)

## Examples
-

## Key Sources
- MM Casey and MW Kille. (2011). Effective Administration of a Large Undergraduate Physics Class: From Enrolment to Assessment Feedback. Journal of Science Education / Revista de Educación en Ciencias 12 (2). https://arxiv.org/abs/1102.2581
