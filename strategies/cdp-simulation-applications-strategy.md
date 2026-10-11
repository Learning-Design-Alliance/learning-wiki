---
type: strategy
id: cdp-simulation-applications-strategy
title: Use CDP-simulated examinees for early item calibration, data augmentation, diagnostic item design, and fairness review before human field testing
description: The article recommends several operational uses of profile-conditioned simulation.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: wenjie-zhou-2026
    resource: "https://osf.io/p6fam/"
    title: "Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/"
    author: "Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson"
---

# Use CDP-simulated examinees for early item calibration, data augmentation, diagnostic item design, and fairness review before human field testing

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends several operational uses of profile-conditioned simulation. It states that "CDP can serve as a data-augmentation tool when human examinees are scarce or cluster in a narrow range of cognitive profiles", at a cost the authors report as less than 0.03 USD to about 14 USD per 100 simulated examinees. For platforms with continually refreshed item pools, CDP offers a scalable way to produce difficulty estimates for new items before human data exist, narrowing a large pool to a smaller set worth field testing. It also supports diagnostic design by showing how simulated examinees with different mastery patterns respond, and fairness review by generating responses across the full range of profiles to flag potentially differential item behavior.

## Design Implications

### Context
#### Requirements
- Attribute descriptions and Q-matrices that assessment design already produces, such as student models, construct maps, and diagnostic attribute specifications
#### Constraints
- CDP complements rather than replaces human calibration; the informative condition's gain depends on profile-level alignment and prior quality

### Target Learners
- Test developers and assessment platforms serving school-age and online learners

### Target Learning Goals
- Efficient item calibration, diagnostic item discrimination checks, and fairness review of new assessment items

### Affordances
- [Cognitive Diagnostic Profiling Framework](../research-methods/cognitive-diagnostic-profiling-cdp.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Wenjie Zhou, Yunting Liu, Renjiao Tang, & Mark Wilson. (2026). Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach. https://osf.io/p6fam/
