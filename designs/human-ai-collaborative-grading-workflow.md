---
type: design
id: human-ai-collaborative-grading-workflow
title: "Human-AI collaborative grading workflow: metric co-design, benchmark-driven regrading, and instructor-centered feedback"
description: A lesson/workflow-level design pattern for AI-assisted assessment in which the LLM provides preliminary scores, comments, and benchmark comparisons while instructors control metric selection, benchmark designation, an...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: zixin-chen-2025
    resource: "https://doi.org/10.1145/3746059.3747670"
    title: "Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu. (2025). CoGrader: Transforming Instructors' Assessment of Project Reports through Collaborative LLM Integration. UIST '25. https://doi.org/10.1145/3746059.3747670"
    author: Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu
---

# Human-AI collaborative grading workflow: metric co-design, benchmark-driven regrading, and instructor-centered feedback

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A lesson/workflow-level design pattern for AI-assisted assessment in which the LLM provides preliminary scores, comments, and benchmark comparisons while instructors control metric selection, benchmark designation, and final grades. The workflow moves from requirement analysis and collaborative metric design, through AI grading and benchmark-driven regrading, to feedback generation. The system "must maintain instructors' full authority over the grading process by clearly positioning AI outputs as supportive references rather than final decisions".

## Design Implications

### Context
#### Requirements
- AI-generated comments must include direct excerpts from student reports as evidence to encourage instructor review
- Critical actions such as selecting criteria, identifying benchmarks, and assigning final grades remain under instructor control
#### Constraints
- The pattern targets open-ended project report grading in project-based learning, where metrics are multifaceted and subjective

### Target Learners
- university instructors and teaching assistants grading project reports

### Learning Goals
- fair, consistent, and efficient assessment of open-ended project reports

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu. (2025). CoGrader: Transforming Instructors' Assessment of Project Reports through Collaborative LLM Integration. UIST '25. https://doi.org/10.1145/3746059.3747670
