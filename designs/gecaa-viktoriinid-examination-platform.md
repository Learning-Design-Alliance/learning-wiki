---
type: design
id: gecaa-viktoriinid-examination-platform
title: Custom online examination platform adapted from the viktoriinid.ee environment for GeCAA
description: A tailor-made web examination package adapted from the Estonian national quiz environment viktoriinid.ee, written mostly in Javascript on an AWS server-less solution with active session tracking and results stored as...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: ioana-a-zelko-2023
    resource: "https://arxiv.org/abs/2111.12095"
    title: "Ioana A. Zelko, Charles Barclay, T˜onis Eenm¨ae, Taavet Kalda, Hara Papathanassiou, Nikita Poljakov, Gustavo A. Rojas, Tiit Sepp, Greg Stachowski, and Aniket Sule. (2023). The first Global e-Competition on Astronomy and Astrophysics. https://arxiv.org/abs/2111.12095"
    author: Ioana A. Zelko, Charles Barclay, T˜onis Eenm¨ae, Taavet Kalda, Hara Papathanassiou, Nikita Poljakov, Gustavo A. Rojas, Tiit Sepp, Greg Stachowski, and Aniket Sule
---

# Custom online examination platform adapted from the viktoriinid.ee environment for GeCAA

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A tailor-made web examination package adapted from the Estonian national quiz environment viktoriinid.ee, written mostly in Javascript on an AWS server-less solution with active session tracking and results stored as JSON entities in a NoSQL database. "The system is able to automatically grade numeric, lingua franca" textual answers "including spelling mistakes, and different checkbox-type questions."

## Design Implications

### Context
#### Requirements
- Questions must be designed so final answers take forms the system can check, since "Any diagrams or plots included in scanned worksheets could not be graded electronically."
- The upload system "should be tested rigorously by the participating teams during the trial phase."
#### Constraints
- Although adapted from existing software, the load was higher than anything previously tested, so "even an online competition based on existing software needs to budget for an expert IT support team."
- pCloud-based image uploads were difficult to match to students and "created confusion for the graders."

### Target Learners
- international senior secondary-school competition participants

### Learning Goals
- automated marking of astronomy theory, data analysis, and sky-map tasks
- multilingual delivery of examination tasks

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Ioana A. Zelko, Charles Barclay, T˜onis Eenm¨ae, Taavet Kalda, Hara Papathanassiou, Nikita Poljakov, Gustavo A. Rojas, Tiit Sepp, Greg Stachowski, and Aniket Sule. (2023). The first Global e-Competition on Astronomy and Astrophysics. https://arxiv.org/abs/2111.12095
