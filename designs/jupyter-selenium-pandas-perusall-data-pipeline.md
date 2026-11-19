---
type: design
id: jupyter-selenium-pandas-perusall-data-pipeline
title: Jupyter-based open data science pipeline (Python Selenium and Pandas) for automating Perusall assessment data processing
description: "To overcome manual report handling that is \"not easily reproducible, is still very tedious and painful, and there is a significant risk of errors,\" the authors built a pipeline using open data science tools led by Jup..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: jozef-hanč-2023
    resource: "https://arxiv.org/abs/2308.07188"
    title: "Jozef Hanč, Martina Hančová, and Dominik Borovský. (2023). Social Reader Perusall – a Highly Effective Tool and Source of Formative Assessment Data. https://arxiv.org/abs/2308.07188"
    author: Jozef Hanč, Martina Hančová, and Dominik Borovský
---

# Jupyter-based open data science pipeline (Python Selenium and Pandas) for automating Perusall assessment data processing

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
To overcome manual report handling that is "not easily reproducible, is still very tedious and painful, and there is a significant risk of errors," the authors built a pipeline using open data science tools led by Jupyter. "Python Selenium can be thought of as a virtual robotic arm that understands Python commands. It can autonomously open Perusall and download the data we need in the xlsx format," after which the Python Pandas library processes the data, yielding results "within milliseconds." Visualizations combine boxplots and swarmplots in blue and orange for comments and questions.

## Design Implications

### Context
#### Requirements
- Python with the Selenium and Pandas libraries and Jupyter notebooks; a Perusall account with access to course data reports
#### Constraints
- The article notes manual downloading and Excel processing of Perusall data is not easily reproducible and error-prone, motivating the automation; the pipeline is illustrated on one course's data (N = 4)

### Target Learners
- instructors and educational researchers processing Perusall course data

### Learning Goals
- formative assessment data analysis
- efficient preparation of face-to-face sessions
- reproducible educational data processing

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Jozef Hanč, Martina Hančová, and Dominik Borovský. (2023). Social Reader Perusall – a Highly Effective Tool and Source of Formative Assessment Data. https://arxiv.org/abs/2308.07188
