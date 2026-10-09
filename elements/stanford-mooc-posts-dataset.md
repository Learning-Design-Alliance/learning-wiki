---
type: element
id: stanford-mooc-posts-dataset
title: Stanford MOOC Posts dataset of annotated learner forum posts
description: The Stanford MOOC Posts dataset is the corpus used to fine-tune the LLMs and train the sentiment classifier.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: liu-2025
    resource: "https://doi.org/10.18608/jla.2025.8885"
    title: "Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885"
    author: "Liu, Z., Xing, W., Jiao, X., & Li, C"
---

# Stanford MOOC Posts dataset of annotated learner forum posts

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The Stanford MOOC Posts dataset is the corpus used to fine-tune the LLMs and train the sentiment classifier. It "comprises 29,604 anonymized learner forum posts from 11 public online courses offered by Stanford University, spanning three subjects: humanities, medicine, and education." Posts carry sentiment, confusion, and urgency ratings on a 1–7 scale from three human raters, post-type flags, and course-type metadata; preprocessing yielded 8,322 matched post-reply pairs used for fine-tuning and evaluation.

## Design Implications

### Context
#### Requirements
- Preprocessing to pair parent and reply posts via forum post id, post type, and comment thread id
#### Constraints
- Gender is treated as a binary attribute in the counterfactual analysis

### Target Learners
- MOOC learners in humanities, medicine, and education courses

### Target Learning Goals
- automated reply generation and sentiment analysis for online discussion support

## Related Elements
- 

## Examples
-

## Key Sources
- Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885
