---
type: strategy
id: session-level-measures-complement-surveys-strategy
title: Use naturally embedded session-level log measures as a survey-free complement for engagement monitoring and predictive modeling
description: The article recommends leveraging existing log data to mine session-level engagement measures rather than adding surveys or instrumentation.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: ashish-gurung-2025
    resource: "https://arxiv.org/abs/2505.13341"
    title: "Ashish Gurung, Jionghao Lin, Zhongtian Huang, Conrad Borchers, Ryan S. Baker, Vincent Aleven, Kenneth R. Koedinger. (2025). Starting Seatwork Earlier as a Valid Measure of Student Engagement. arXiv. https://arxiv.org/abs/2505.13341"
    author: Ashish Gurung, Jionghao Lin, Zhongtian Huang, Conrad Borchers, Ryan S. Baker, Vincent Aleven, Kenneth R. Koedinger
---

# Use naturally embedded session-level log measures as a survey-free complement for engagement monitoring and predictive modeling

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends leveraging existing log data to mine session-level engagement measures rather than adding surveys or instrumentation. It states these measures "complement motivational surveys without extra instrumentation or disruption of instruction time," capturing what students do rather than what they say. Suggested applications include predictive modeling of learning outcomes, teaching augmentation tools and dashboards, and contextualizing affect dynamics in classwork-based settings.

## Design Implications

### Context
#### Requirements
- A digital learning platform that logs timestamped student actions during structured classwork sessions
#### Constraints
- The article notes further validation of session boundary detection is needed; students who begin and end work on time may be incorrectly labeled as delayed starters or early stoppers when highly motivated peers skew boundaries

### Target Learners
- K-12 students using digital learning platforms in classwork settings

### Target Learning Goals
- Monitoring engagement, motivation, and self-regulation; predicting learning outcomes

## Claims

- [Early stop is markedly less reliable than other session-level measures, limiting its standalone utility](../claims/early-stop-low-reliability.md) [+W]
- [Relative delayed start generalizes across systems, predicting grade 7 state test scores in i-Ready data](../claims/relative-delayed-start-cross-system-generalizability.md) [+W]
- [Relative delayed start is the strongest individual session-level predictor of final math scores, outperforming time on task, attendance, and gaming tendency](../claims/relative-delayed-start-strongest-predictor.md) [+W]
- [Session-level time-based measures of classwork engagement show moderate-to-high month-to-month reliability, comparable to or exceeding gaming tendency](../claims/session-level-measures-moderate-high-reliability.md) [+W]
- [In stepwise combined models, relative delayed start, early stop, and idle time each negatively correlate with final math scores beyond prior performance](../claims/stepwise-combined-predictive-models.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ashish Gurung, Jionghao Lin, Zhongtian Huang, Conrad Borchers, Ryan S. Baker, Vincent Aleven, Kenneth R. Koedinger. (2025). Starting Seatwork Earlier as a Valid Measure of Student Engagement. arXiv. https://arxiv.org/abs/2505.13341
