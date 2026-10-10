---
type: strategy
id: human-review-of-llm-ttx-assessment
title: Be cautious with LLM-based TTX assessment and have a human instructor review automated outputs
description: Based on their findings that general-purpose LLMs sometimes failed to recognize nuances in the domain-specific TTX context even when guided by a standardized rubric, the authors recommend caution about LLM-based asses...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: v-švábenský-2026
    resource: "https://arxiv.org/abs/2607.19209"
    title: "V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209"
    author: V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada
---

# Be cautious with LLM-based TTX assessment and have a human instructor review automated outputs

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Based on their findings that general-purpose LLMs sometimes failed to recognize nuances in the domain-specific TTX context even when guided by a standardized rubric, the authors recommend caution about LLM-based assessment and state that, as with all automated decisions, the output must be reviewed by a human instructor to ensure accountability and fairness. They further note clustering's advantage: it considers only teams' activity logs, runs locally, and does not share learners' data with an external service, preserving privacy.

## Design Implications

### Context
#### Requirements
- A human instructor must review automated assessment outputs before they affect learners
#### Constraints
- Public (non-local) LLM assessment depends on an external service; if the LLM becomes unavailable or its version changes, the assessment's validity and reliability would change as well

### Target Learners
- student teams in cybersecurity TTXs

### Target Learning Goals
- fair and accountable automated assessment of team communication

## Related Strategies

- [Design TTXs with assessment in mind so that log data capture the learning process](design-ttx-with-assessment-in-mind.md)

## Examples
-

## Key Sources
- V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209
