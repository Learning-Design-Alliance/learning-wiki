---
type: design
id: web-based-crowdsourced-finger-tapping-task
title: Web-based crowdsourced version of the sequential finger tapping task on Amazon Mechanical Turk
description: A web-based implementation of the well-characterized sequential finger tapping task (5-item keypress sequence, 4-1-3-2-4, with the nondominant left hand) programmed in Psytoolkit, administered on Amazon Mechanical Tur...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
sources:
  - id: marlene-bönstrup-2020
    resource: "https://doi.org/10.1038/s41539-020-0066-9"
    title: "Marlene Bönstrup, Iñaki Iturrate, Martin N. Hebart, Nitzan Censor and Leonardo G. Cohen. (2020). Mechanisms of offline motor learning at a microscale of seconds in large-scale crowdsourced data. npj Science of Learning. https://doi.org/10.1038/s41539-020-0066-9"
    author: Marlene Bönstrup, Iñaki Iturrate, Martin N. Hebart, Nitzan Censor and Leonardo G. Cohen
---

# Web-based crowdsourced version of the sequential finger tapping task on Amazon Mechanical Turk

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (2 causal), `q3` · 1 of 2 report an effect size

## Description
A web-based implementation of the well-characterized sequential finger tapping task (5-item keypress sequence, 4-1-3-2-4, with the nondominant left hand) programmed in Psytoolkit, administered on Amazon Mechanical Turk with participants using their own computers. It proved "useful to study human motor learning dynamics at a large scale", enabling samples of hundreds of participants (e.g., N = 389) with data collection averaging 16 h and 26 min per experiment, and replicated the in-lab learning-curve shape and microdynamics.

## Design Implications

### Context
#### Requirements
- Participants with >95% MTurk approval rate, US location, right-handedness; clear definitions of correct adherence to instructions for post-hoc data quality checks
#### Constraints
- A proportion of participants did not follow instructions and had to be excluded; variability is higher than in-lab at comparable sample sizes; designs requiring prolonged task durations or longitudinal measurements need extra care; groups must be properly randomized given rapid changes in worker pool composition

### Target Learners
- adult MTurk workers learning a motor sequence

### Learning Goals
- measurement of microscale motor skill learning dynamics in early acquisition

### Claims

- [Performance improvements during early motor skill learning occur predominantly during short rest periods (micro-offline gains), replicated in a large crowdsourced sample and in a laboratory study](../claims/micro-offline-gains-replicated-crowdsourced.md) [+S]

## Related Designs

- [Crowdsourcing as a knowledge base building model with three primary design issues](crowdsourcing-knowledge-base-building-model.md)

## Examples
-

## Key Sources
- Marlene Bönstrup, Iñaki Iturrate, Martin N. Hebart, Nitzan Censor and Leonardo G. Cohen. (2020). Mechanisms of offline motor learning at a microscale of seconds in large-scale crowdsourced data. npj Science of Learning. https://doi.org/10.1038/s41539-020-0066-9
