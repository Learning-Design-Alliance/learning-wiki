---
type: design
id: chatgpt-two-mode-lab-report-evaluation-protocol
title: AI-assisted laboratory report evaluation protocol with two ChatGPT interaction modalities
description: "A structured evaluation protocol in which a comprehensive prompt assigned \"a teaching role to the model\", a checklist of tasks, the instructor evaluation guide, and a required output format."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: abreu-m-2025
    resource: "https://arxiv.org/abs/2510.16137"
    title: "Abreu M, Suárez A, Stari C and Martí A C. (2025). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2510.16137"
    author: Abreu M, Suárez A, Stari C and Martí A C
---

# AI-assisted laboratory report evaluation protocol with two ChatGPT interaction modalities

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A structured evaluation protocol in which a comprehensive prompt assigned "a teaching role to the model", a checklist of tasks, the instructor evaluation guide, and a required output format. Reports were evaluated via an automated API-based mode for batch processing under controlled and reproducible conditions, and via a customized GPT profile ("Physics Instructor GPT") accessed through the native interface to emulate a physics instructor. AI evaluations were compared with teachers' assessments of the same reports.

## Design Implications

### Context
#### Requirements
- The evaluation guide developed in 2024 by course instructors for the Simple Pendulum and Error and uncertainties experiments
- Reports with data, graphs and equations embedded as machine-readable text rather than images or screenshots for the API mode
#### Constraints
- The API mode could not correctly render images, tables, graphs or embedded equations; the customized mode had lower reproducibility

### Target Learners
- undergraduate physics students

### Learning Goals
- assessment of laboratory report quality
- formal and structural integrity
- technical accuracy and conceptual depth

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Abreu M, Suárez A, Stari C and Martí A C. (2025). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2510.16137
