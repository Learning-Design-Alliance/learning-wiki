---
type: design
id: ai-teaching-tech-stack-dash-pytorch-qwen
title: "AI teaching technology stack: dashboard, reinforcement-learning feedback, and LLM-based semantic assessment"
description: The article specifies the implemented technologies behind the smart teaching ecosystem.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: wang-j-and-li-p-2026
    resource: "https://doi.org/10.3389/fpsyg.2026.1790916"
    title: "Wang J and Li P (2026). AI-driven educational reform: enhancing talent cultivation in computer-related majors for the digital era. Front. Psychol. 17:1790916. https://doi.org/10.3389/fpsyg.2026.1790916"
    author: Wang J and Li P
---

# AI teaching technology stack: dashboard, reinforcement-learning feedback, and LLM-based semantic assessment

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article specifies the implemented technologies behind the smart teaching ecosystem. As printed, "The intelligent dashboard was implemented in a Python 3.10 environment using Dash and Plotly for visualization, and integrated with a PostgreSQL database to store students' activity logs and analysis results." Adaptive feedback loops use a reinforcement learning model in PyTorch to adjust learning tasks and personalized exercises; open-ended assignments are evaluated by converting text to vectors with the Qwen-7B pre-trained large language model and computing cosine similarity against reference documents.

## Design Implications

### Context
#### Requirements
- Storage of student activity logs and analysis results in a database; vector representation of submissions for semantic similarity analysis
#### Constraints
- Described as employed within this study's computing-related majors

### Target Learners
- undergraduate computer-related majors

### Learning Goals
- formative feedback
- data-driven instructional intervention
- academic integrity checking

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Wang J and Li P (2026). AI-driven educational reform: enhancing talent cultivation in computer-related majors for the digital era. Front. Psychol. 17:1790916. https://doi.org/10.3389/fpsyg.2026.1790916
