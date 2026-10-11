---
type: design
id: gpt4-curriculum-prerequisite-knowledge-graph
title: GPT-4-extracted curriculum prerequisite knowledge graph (54 topic nodes, 47 directed prerequisite edges)
description: A prerequisite knowledge graph extracted by GPT-4 from 26 lesson PDFs of a graduate-level AI course, following a three-stage protocol of topic extraction, boundary consolidation, and edge extraction.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: youssef-medhat-2026
    resource: "https://dilab.gatech.edu"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://dilab.gatech.edu"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
---

# GPT-4-extracted curriculum prerequisite knowledge graph (54 topic nodes, 47 directed prerequisite edges)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A prerequisite knowledge graph extracted by GPT-4 from 26 lesson PDFs of a graduate-level AI course, following a three-stage protocol of topic extraction, boundary consolidation, and edge extraction. The graph contains "54 topic nodes and 47 directed prerequisite edges" and serves two roles: its topic nodes provide the closed label space for classification and survey alignment, and its directed prerequisite edges encode curriculum structure for future per-student gap propagation. The authors describe it as "a low-cost, instructor-auditable way to obtain a topic–edge artifact".

## Design Implications

### Context
#### Requirements
- A course instructor with domain expertise to run and audit the GPT-4 extraction protocol over lesson PDFs
#### Constraints
- The authors do not claim the graph is the unique correct structure; only unambiguous, non-bidirectional GPT-4 prerequisite judgments are retained

### Target Learners
- graduate-level AI course students

### Learning Goals
- mapping student questions to curriculum topics
- identifying topic-level knowledge gaps

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://dilab.gatech.edu
