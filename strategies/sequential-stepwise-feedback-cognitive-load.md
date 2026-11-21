---
type: strategy
id: sequential-stepwise-feedback-cognitive-load
title: Deliver sequential, step-by-step feedback addressing one error at a time to support cognitive load management
description: The article proposes studying iterative error resolution in which the system surfaces instructor-identified issues one at a time.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: muntasir-hoq-2026
    resource: "https://arxiv.org/abs/2606.12425"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
---

# Deliver sequential, step-by-step feedback addressing one error at a time to support cognitive load management

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes studying iterative error resolution in which the system surfaces instructor-identified issues one at a time. The authors note that "sequential, step-by-step, and immediate feedback could support cognitive load management" and state that future work will examine whether iteratively addressing errors one at a time improves learning outcomes compared to addressing all issues simultaneously. A preliminary analysis suggested that once identified issues are addressed, the system can successfully recall remaining issues.

## Design Implications

### Context
#### Requirements
- the system must be able to retrieve remaining instructor-identified errors sequentially after earlier identified issues are addressed
#### Constraints
- the current framework sometimes struggles to identify all issues present in a submission (completeness)

### Target Learners
- novice students in introductory programming courses

### Target Learning Goals
- managing cognitive load while correcting multiple logical errors in a single submission

## Claims

- [Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness](../claims/insight-feedback-beats-gpt4o-selectivity-suitability.md) [+W]

## Related Strategies

- [Chunk Directions](chunk_directions.md)
- [Revision Cycles](revision-cycles.md)

## Examples
-

## Key Sources
- Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425
