---
type: design
id: addie-orchestration-framework-llm-lesson-generation
title: ADDIE-based orchestration framework for curriculum-aligned LLM lesson generation with teacher validation gates
description: "ConnectED uses the ADDIE instructional design model as a unifying orchestration layer, using \"ADDIE to structure instructional reasoning, decompose pedagogical goals, and control generation flow\" rather than treating..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: thang-doan-viet-2026
    resource: "https://arxiv.org/abs/2607.28647"
    title: "Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647"
    author: Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy
---

# ADDIE-based orchestration framework for curriculum-aligned LLM lesson generation with teacher validation gates

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
ConnectED uses the ADDIE instructional design model as a unifying orchestration layer, using "ADDIE to structure instructional reasoning, decompose pedagogical goals, and control generation flow" rather than treating the LLM as a black-box generator. Each of the five phases produces concrete, evaluable artifacts and serves as a prompt boundary where curriculum compliance can be verified and teacher approval solicited before the next phase begins. The Evaluation phase feeds student learning signals back into Design and Develop, closing the instructional loop.

## Design Implications

### Context
#### Requirements
- Teacher validation checkpoints at each ADDIE phase boundary, with teachers retaining authority to review, revise, or regenerate AI outputs
- Structured prompt templates encoding Official Dispatch 5512 requirements, including three-dimensional learning objectives and the mandated four-step activity structure
#### Constraints
- The paper acknowledges ADDIE-based orchestration may introduce a degree of rigidity in lesson generation, and experienced teachers may prefer more flexible workflows beyond predefined instructional phases

### Target Learners
- Vietnamese secondary school teachers (grades 6-12)

### Learning Goals
- Curriculum-aligned lesson planning compliant with Official Dispatch 5512

### Claims
- [System Ablation Teacher Oversight And Addie Orchestration Value](../claims/system-ablation-teacher-oversight-and-addie-orchestration-value.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647
