---
type: strategy
id: instructor-dashboard-topic-question-volume
title: Use a cohort-wide instructor dashboard of topic-level question volume, with assistant-surfaced prerequisite review suggestions as an extension
description: "The article's envisioned practical use of the pipeline: converting passively logged assistant interactions into topic-level difficulty signals without additional student burden."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: youssef-medhat-2026
    resource: "https://arxiv.org/abs/2606.10736"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
---

# Use a cohort-wide instructor dashboard of topic-level question volume, with assistant-surfaced prerequisite review suggestions as an extension

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's envisioned practical use of the pipeline: converting passively logged assistant interactions into topic-level difficulty signals without additional student burden. The authors state "The primary use we envision is a cohort-wide instructor dashboard", with the same signal passed to the conversational assistant as suggestions for prerequisite review when a student asks about a downstream topic, or surfaced through the LMS as student-specific recommendations. Instructors can verify the ranking against independent survey evidence.

## Design Implications

### Context
#### Requirements
- A deployed conversational AI teaching assistant producing logged question events, and a curriculum knowledge graph grounding the topic labels
#### Constraints
- The H2 result is aggregate at the topic level and does not by itself identify which individual students are struggling on which topic

### Target Learners
- students in large online courses using conversational AI teaching assistants

### Target Learning Goals
- identifying topics warranting instructional attention
- targeting prerequisite review

## Related Strategies

- [Use support-level filtering across cohorts to separate persistent from cohort-specific challenging topics](support-level-filtering-persistent-topics.md)

## Examples
-

## Key Sources
- Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736
