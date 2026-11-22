---
type: strategy
id: spreadsheet-first-computational-assignments-strategy
title: Design all introductory computational assignments to be completable in spreadsheets so students without programming background can participate.
description: The author assigns computational projects, including the GW150914 analysis, that can all be completed with spreadsheets such as Excel or with laboratory software like PASCO Capstone, letting students choose any langua...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: lior-m-burko-2016
    resource: "https://losc.ligo.org/events/GW150914/"
    title: "Lior M. Burko. (2016). Gravitational Wave Detection in the Introductory Lab. https://losc.ligo.org/events/GW150914/"
    author: Lior M. Burko
---

# Design all introductory computational assignments to be completable in spreadsheets so students without programming background can participate.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 4 studies (4 design), `q1`–`q3` · 0 of 4 report an effect size · 3 claims rest on one study

## Description
The author assigns computational projects, including the GW150914 analysis, that can all be completed with spreadsheets such as Excel or with laboratory software like PASCO Capstone, letting students choose any language they know. Numerical derivatives are computed cell-by-cell, e.g. entering the formula (B3-B1)/(A3-A1) and filling the column. The author states the assignments "can all be done using spreadsheets, such that students without background in programming can still do all the assignments", while noting some instructors successfully require a specific language such as Python.

## Design Implications

### Context
#### Requirements
- Access to a spreadsheet program or widely available laboratory software such as PASCO Capstone
#### Constraints
- The author prefers not to devote class time to teaching programming, though he reports instructors requiring a language use the former approach with much success

### Target Learners
- introductory calculus-based physics students
- introductory astronomy students

### Target Learning Goals
- data analysis skills
- familiarity with computational tools used by working physicists

## Claims

- [Introductory students can extract a chirp mass of about 30 solar masses from the GW150914 waveform using simple data-analysis tools.](../claims/gw150914-chirp-mass-student-extraction.md) [+W]
- [Students can determine the final black hole mass of about 67 solar masses and spin parameter 0.67 from the ring-down using published quasi-normal-mode fit equations.](../claims/gw150914-final-black-hole-mass-spin-extraction.md) [+W]
- [Spreadsheets are harder to debug than comparable programs and lead less skilled users toward chartjunk](../claims/spreadsheet-drawbacks-debugging-chartjunk.md) [-W]
- [In a large introductory mechanics course, the majority of students (60.4%) successfully completed a proctored computational modeling evaluation on a novel central force problem after a semester of computational homework.](../claims/computational-evaluation-majority-success-intro-mechanics.md) [+M]

## Related Strategies

- [Spreadsheet homework sequence: reproduce small-system tables, then scale up and add entropy columns](spreadsheet-homework-sequence-einstein-solids.md)
- [Incorporate computation into an existing classical mechanics course through in-class demonstrations followed by student projects that progress from template modification to independent construction](demonstration-template-to-independent-projects.md)
- [Incorporate numerical calculation into introductory quantum courses to counteract abstraction-driven misconceptions](incorporate-numerical-calculation-in-quantum-courses.md)
- [Include a fully solved test case before the graded case in computational homework to support debugging and build confidence](test-case-before-grading-case-homework.md)
- [Embed computational skills into an existing lab course by replacing a preset analysis tool with Python while retaining original lab goals](embed-python-without-altering-course-structure.md)
- [Have introductory astronomy students measure waveform properties directly from plots with a straight edge and axis labels, then apply standard formulae to extract source parameters](straight-edge-waveform-measurement-extraction.md)

## Examples
-

## Key Sources
- Lior M. Burko. (2016). Gravitational Wave Detection in the Introductory Lab. https://losc.ligo.org/events/GW150914/
