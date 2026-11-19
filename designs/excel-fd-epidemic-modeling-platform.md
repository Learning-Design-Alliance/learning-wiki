---
type: design
id: excel-fd-epidemic-modeling-platform
title: Excel-based finite difference modeling platform with preformatted spreadsheets and Solver fitting
description: The modeling platform is Microsoft Excel (or compatible spreadsheet programs), chosen because it is non-threatening to students and widely available.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: nelson-2021
    resource: "https://scholar.google.com/scholar?q=Introductory+models+of+COVID-19+in+the+United+States"
    title: "Nelson, P. H. (2021). Introductory models of COVID-19 in the United States. Department of Physics, Fisk University. https://scholar.google.com/scholar?q=Introductory+models+of+COVID-19+in+the+United+States"
    author: Nelson, P. H
---

# Excel-based finite difference modeling platform with preformatted spreadsheets and Solver fitting

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The modeling platform is Microsoft Excel (or compatible spreadsheet programs), chosen because it is non-threatening to students and widely available. Students implement finite difference algorithms row by row in preformatted spreadsheets, plot semi-log charts, use NORM.DIST for Gaussian transition functions, and fit models to data with Solver's least-squares engine. The article argues these methods are ideal for introducing undergraduates because "the computational steps of the FD model are represented by successive rows of the spreadsheet".

## Design Implications

### Context
#### Requirements
- A spreadsheet providing Solver for least-squares fitting and the NORM.DIST function for Gaussian cumulative probabilities, with students following condensed FD instructions implemented one row per computational step.
#### Constraints
- Keeping track of each individual and how long they have been infected "would be difficult to do in Excel", so the models track aggregate box counts rather than individuals.

### Target Learners
- undergraduate students new to scientific modeling

### Learning Goals
- implementing finite difference models
- least-squares fitting of models to data

### Claims
- 

## Related Designs
- Scaffolded Spreadsheet Epidemic Modeling Sequence

## Examples
-

## Key Sources
- Nelson, P. H. (2021). Introductory models of COVID-19 in the United States. Department of Physics, Fisk University. https://scholar.google.com/scholar?q=Introductory+models+of+COVID-19+in+the+United+States
