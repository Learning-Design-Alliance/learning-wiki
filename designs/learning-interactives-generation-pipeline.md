---
type: design
id: learning-interactives-generation-pipeline
title: "Learning interactives generation pipeline: four stages from teacher request to guidance components"
description: "Learning interactives are generated in four stages (Figure 2): Planning (from a teacher request to learning objectives and a simulation idea), Scaffolding (from objectives to K=5 levelled goals), Gen-UI (from idea and..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: alisa-kovshov-2026
    resource: "https://arxiv.org/abs/2609.20738"
    title: "Alisa Kovshov, Anisha Choudhury, Anna Iurchenko, Amy Keeling, Avinatan Hassidim, Ayelet Shasha Evron, Ayça Çakmakli, Diana Akrong, Femi Olanubi, Gal Elidan, Ian Li, Ido Lerer, Katherine Chou, Lidan Hackmon, Michal Gordon, Nir Kerem, Niv Efron, Preeti Singh, Rena Levitt, Rotem Yulzary, Shlomi Ben Shimon, Sophie Allweis, Tracey Lee-Joe, Tzvika Stein, Yaniv Carmel, Yael Haramaty, Yishay Mor, Yossi Matias and Yuri Lev. (2026). Harnessing Generative UI for Education: Tailored Learning Interactives. Google Research. https://arxiv.org/abs/2609.20738"
    author: Alisa Kovshov, Anisha Choudhury, Anna Iurchenko, Amy Keeling, Avinatan Hassidim, Ayelet Shasha Evron, Ayça Çakmakli, Diana Akrong, Femi Olanubi, Gal Elidan, Ian Li, Ido Lerer, Katherine Chou, Lidan Hackmon, Michal Gordon, Nir Kerem, Niv Efron, Preeti Singh, Rena Levitt, Rotem Yulzary, Shlomi Ben Shimon, Sophie Allweis, Tracey Lee-Joe, Tzvika Stein, Yaniv Carmel, Yael Haramaty, Yishay Mor, Yossi Matias and Yuri Lev
---

# Learning interactives generation pipeline: four stages from teacher request to guidance components

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Learning interactives are generated in four stages (Figure 2): Planning (from a teacher request to learning objectives and a simulation idea), Scaffolding (from objectives to K=5 levelled goals), Gen-UI (from idea and goals to a generated simulation UI), and Guidance (tour, hints, solutions, feedback). The textual planning stage produces entities, relations, telemetry, visual features, knobs and actions; the scaffolding stage iteratively generates and critiques each level's goal; the Gen-UI stage applies generate-then-refine with visual, solution, telemetry and mechanical critiques. A collection of teacher-approved interactives is available at research.google.com/p/learning-interactives.

## Design Implications

### Context
#### Requirements
- An educator-initiated request specifying subject, grade level and query, with teacher review/approval of generated learning objectives
#### Constraints
- Single-prompt UI generation satisfying pedagogical requirements succeeds only 3.5% of the time, so iterative critique loops are required

### Target Learners
- Students of teacher-creators across STEM subjects and grade levels

### Learning Goals
- Topic-specific STEM learning objectives defined or approved by the teacher

### Claims
- [Generate Then Refine Raises Usable Simulations 3 5 To 69 3](../claims/generate-then-refine-raises-usable-simulations-3-5-to-69-3.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Alisa Kovshov, Anisha Choudhury, Anna Iurchenko, Amy Keeling, Avinatan Hassidim, Ayelet Shasha Evron, Ayça Çakmakli, Diana Akrong, Femi Olanubi, Gal Elidan, Ian Li, Ido Lerer, Katherine Chou, Lidan Hackmon, Michal Gordon, Nir Kerem, Niv Efron, Preeti Singh, Rena Levitt, Rotem Yulzary, Shlomi Ben Shimon, Sophie Allweis, Tracey Lee-Joe, Tzvika Stein, Yaniv Carmel, Yael Haramaty, Yishay Mor, Yossi Matias and Yuri Lev. (2026). Harnessing Generative UI for Education: Tailored Learning Interactives. Google Research. https://arxiv.org/abs/2609.20738
