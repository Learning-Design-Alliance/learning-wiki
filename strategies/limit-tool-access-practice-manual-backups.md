---
type: strategy
id: limit-tool-access-practice-manual-backups
title: Replicate tool latency and outages in training by limiting or removing tool access so learners practice manual backups
description: "To prepare operators for software latency or outages during time-critical operations, the authors recommend that training deliberately constrain tool availability: \"This issue can be replicated in training by limiting..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: kent-2022
    resource: "https://arxiv.org/abs/2211.09976"
    title: "Kent, Evelyn; Gabriel, Jason; Gunn-Golkin, Anna; Langdon, Charles; Nayak, Michael; Remeta, Emily; Willett, Michelle. (2022). How to Train Your Space Tester, Part 2: Enabling Capabilities. https://arxiv.org/abs/2211.09976"
    author: Kent, Evelyn; Gabriel, Jason; Gunn-Golkin, Anna; Langdon, Charles; Nayak, Michael; Remeta, Emily; Willett, Michelle
---

# Replicate tool latency and outages in training by limiting or removing tool access so learners practice manual backups

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
To prepare operators for software latency or outages during time-critical operations, the authors recommend that training deliberately constrain tool availability: "This issue can be replicated in training by limiting tool usage, or removing access, so that Guardians receive practice in moving to manual backup capabilities." The strategy treats degraded tool availability as a trainable scenario rather than an exception, building operator readiness for the anecdotal lag or failure of data manipulation tools during critical operations.

## Design Implications

### Context
#### Requirements
- Manual backup capabilities that operators can transition to when tools are unavailable
#### Constraints
- The article notes this addresses latency or outages anecdotally observed, not a measured failure rate

### Target Learners
- space operators
- space test professionals

### Target Learning Goals
- operating under degraded tool availability
- mission planning around latency
- manual backup procedures

## Claims

- [Representative simulators are the safest way to gain repetitions in dynamic decision-making and fault response](../claims/simulators-safest-repetitions-dynamic-decisions.md) [+W]

## Related Strategies

- [Prepare backup head-mounted displays and on-site technical knowledge for VR simulation sessions, and develop scenarios through co-creative processes with end-users](vr-simi-backup-hmd-cocreative-scenario-development-strategy.md)

## Examples
-

## Key Sources
- Kent, Evelyn; Gabriel, Jason; Gunn-Golkin, Anna; Langdon, Charles; Nayak, Michael; Remeta, Emily; Willett, Michelle. (2022). How to Train Your Space Tester, Part 2: Enabling Capabilities. https://arxiv.org/abs/2211.09976. [doi:10.48550/arxiv.2211.09976](https://doi.org/10.48550/arxiv.2211.09976)
