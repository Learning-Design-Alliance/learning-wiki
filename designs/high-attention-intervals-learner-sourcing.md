---
type: design
id: high-attention-intervals-learner-sourcing
title: "High attention intervals derived from past learners' comments"
description: High attention intervals are a learner-sourcing mechanism that aggregates comments made by past learners into continuous stretches of video, using a time-gap parameter θ (set to 4 seconds for tutorials and 6 seconds f...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: vania-dimitrova-antonija-mitrovic-2021
    resource: "https://doi.org/10.1007/s40593-021-00263-1"
    title: "Vania Dimitrova & Antonija Mitrovic. (2021). Choice Architecture for Nudges to Support Constructive Learning in Active Video Watching. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00263-1"
    author: "Vania Dimitrova & Antonija Mitrovic"
---

# High attention intervals derived from past learners' comments

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
High attention intervals are a learner-sourcing mechanism that aggregates comments made by past learners into continuous stretches of video, using a time-gap parameter θ (set to 4 seconds for tutorials and 6 seconds for examples) and an aggregation predicate. The intervals indicate areas in a video where users have noted something and are used to trigger interactive prompts and visualisations such as heat maps. The article states: "The high attention intervals are used for identifying situations that could trigger interactive prompts", implementing nudging as signposting through interactive visualisations and personalised prompts in AVW-Space.

## Design Implications

### Context
#### Requirements
- A corpus of timestamped comments from past learners, and a chosen time-gap parameter θ that gives a reasonable interval partitioning
#### Constraints
- Larger values of θ will aggregate almost all comments into one interval, limiting the granularity of the partitioning

### Target Learners
- future learners watching videos in AVW-Space

### Learning Goals
- noticing important segments in videos and making comments at high-attention points

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Vania Dimitrova & Antonija Mitrovic. (2021). Choice Architecture for Nudges to Support Constructive Learning in Active Video Watching. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00263-1
