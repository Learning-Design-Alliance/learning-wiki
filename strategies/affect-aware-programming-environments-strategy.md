---
type: strategy
id: affect-aware-programming-environments-strategy
title: Design affect-aware programming learning environments to track the five frequent affective states and use interaction-event log-based affect detection with hint recommendations
description: The article derives design guidance for intelligent learning environments for programming from its affect findings.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: bosch-2017
    resource: "https://doi.org/10.1007/s40593-015-0069-5"
    title: "Bosch, N., & D'Mello, S. (2017). The Affective Experience of Novice Computer Programmers. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0069-5"
    author: "Bosch, N., & D'Mello, S"
---

# Design affect-aware programming learning environments to track the five frequent affective states and use interaction-event log-based affect detection with hint recommendations

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article derives design guidance for intelligent learning environments for programming from its affect findings. Affect-aware technologies "should focus on engagement, confusion, frustration, boredom, and curiosity," with particular attention to the negatively valenced confusion, frustration, and boredom. Interaction events "can be used to develop log-file based affect detectors that can complement face-based affect detection," and can drive "affect-aware interventions, such as recommending a hint when excessive frustration is detected." Co-occurrence findings inform detectors about which states are likely confused together.

## Design Implications

### Context
#### Requirements
- Requires affect detection to determine which states to track and when to intervene; log-based detection requires interaction events logged with enough context to disambiguate activities
#### Constraints
- The article notes state-of-the-art affect detection accuracies are somewhat low and asks whether co-occurring affect contributes to this; it poses open questions about whether detectors should detect blends and how to respond when confusion and frustration co-occur

### Target Learners
- novice computer programming students

### Target Learning Goals
- learning to program; sustaining engagement and managing negative affect during learning

### Affordances
- Updated Affect Dynamics Model Revised

## Claims

- [Confusion and frustration followed incorrect solution submissions and preceded hint requests, while coding was the central activity surrounding all affective states](../claims/affect-interaction-event-transitions-programming.md) [+M]
- [During novices' first programming lesson, engagement, confusion, frustration, boredom, and curiosity are the dominant affective states, collectively accounting for approximately 73% of affect judgments](../claims/novice-programming-affect-incidence-five-dominant-states.md) [+W]
- [After partialling out control variables, boredom and frustration during scaffolded learning negatively correlated with fadeout performance, while confusion↔frustration transitions and boredom→engagement transition positively correlated with it](../claims/affect-learning-partial-correlations-programming.md) [+W]

## Related Strategies

- [Affect-aware CPS systems should monitor local trajectories of confusion and disengagement over time rather than responding to isolated affective signals](monitor-local-affect-trajectories-in-cps-systems.md)

## Examples
-

## Key Sources
- Bosch, N., & D'Mello, S. (2017). The Affective Experience of Novice Computer Programmers. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0069-5
