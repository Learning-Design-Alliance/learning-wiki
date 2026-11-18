---
type: design
id: imagej-fraclac-box-counting-procedure
title: ImageJ + FracLac computational box-counting procedure with student binarization
description: "A computational workflow in which students binarize an image in ImageJ (Process → Binary → Make Binary) and then run the free FracLac plugin (Plugins → Fractal Analysis: FracLac, BC, Scan) to obtain the box-counting f..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: pvs-souza-2018
    resource: "https://arxiv.org/abs/1804.01038"
    title: "P.V.S. Souza, R.L. Alves e W.F. Balthazar. (2018). A simple and didactic method to calculate the fractal dimension - an interdisciplinary tool. arXiv:1804.01038. https://arxiv.org/abs/1804.01038"
    author: P.V.S. Souza, R.L. Alves e W.F. Balthazar
---

# ImageJ + FracLac computational box-counting procedure with student binarization

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A computational workflow in which students binarize an image in ImageJ (Process → Binary → Make Binary) and then run the free FracLac plugin (Plugins → Fractal Analysis: FracLac, BC, Scan) to obtain the box-counting fractal dimension. The authors binarize images beforehand even though FracLac does this automatically, with the didactic objective "to allow students to understand the process of binarization that precedes the estimation of the fractal dimension". The software is free, runs on Windows, Mac OS X and Linux.

## Design Implications

### Context
#### Requirements
- A computer running a Java virtual machine 1.8 or higher with the free ImageJ software and the FracLac plugin installed.
#### Constraints
- The program is "not able to distinguish which part of the ﬁgure is the object and which part is the background", working only with black and white pixels and assuming the object is the least abundant pixel class.

### Target Learners
- high school students

### Learning Goals
- calculating the fractal dimension of two-dimensional figures
- understanding image binarization and the box-counting method

### Claims
- Imagej Dimension 1 68 Agrees With Manual 1 69 [+M]

## Related Designs

- [Manual grid-counting box-counting activity](manual-grid-counting-activity.md)

## Examples
-

## Key Sources
- P.V.S. Souza, R.L. Alves e W.F. Balthazar. (2018). A simple and didactic method to calculate the fractal dimension - an interdisciplinary tool. arXiv:1804.01038. https://arxiv.org/abs/1804.01038
