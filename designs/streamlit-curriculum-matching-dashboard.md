---
type: design
id: streamlit-curriculum-matching-dashboard
title: Interactive Streamlit dashboard for exploring matched learning outcomes
description: An interactive dashboard was built for the curriculum department using the open-source Streamlit package to let specialists search, navigate, and explore learning outcomes and check similar ones.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: tamador-alkhidir-2024
    resource: "https://arxiv.org/abs/2403.05553"
    title: "Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi. (2024). Understanding the Progression of Educational Topics via Semantic Matching. arXiv preprint. https://arxiv.org/abs/2403.05553"
    author: Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi
---

# Interactive Streamlit dashboard for exploring matched learning outcomes

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An interactive dashboard was built for the curriculum department using the open-source Streamlit package to let specialists search, navigate, and explore learning outcomes and check similar ones. It includes a filter section (cycle, stream, program), a program heat map of matching percentages between subjects, a subject heat map across grades, a topic-distribution bar chart, and a table of learning-outcome pairs under the same topic. Specialists can filter matched outcomes by courses, grade levels, streams, and percentage of matching.

## Design Implications

### Context
#### Requirements
- Requires the semantic matching pipeline's topic assignments and matching percentages as its data source
#### Constraints
- 

### Target Learners
- curriculum specialists at the UAE Ministry of Education

### Learning Goals
- curriculum planning and alignment of learning outcomes

### Claims
- [Bert Matching 95 Percent Standard Agreement](../claims/bert-matching-95-percent-standard-agreement.md) [+M]
- [Cross Subject Overlap Percentages](../claims/cross-subject-overlap-percentages.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Tamador Alkhidir, Edmond Awad, and Aamena Alshamsi. (2024). Understanding the Progression of Educational Topics via Semantic Matching. arXiv preprint. https://arxiv.org/abs/2403.05553
