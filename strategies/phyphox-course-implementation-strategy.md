---
type: strategy
id: phyphox-course-implementation-strategy
title: Implement collaborative network experiments in other courses using phyphox XML configurations plus a simple PHP server
description: "The article outlines how educators can adopt collaborative smartphone experiments: all examples can be realized within the documented XML format defining which sensors are read, which mathematical operations to apply,..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: s-staacks-2022
    resource: "https://doi.org/10.1088/1361-6404/ac7830"
    title: "S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830"
    author: S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer
---

# Implement collaborative network experiments in other courses using phyphox XML configurations plus a simple PHP server

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article outlines how educators can adopt collaborative smartphone experiments: all examples can be realized within the documented XML format defining which sensors are read, which mathematical operations to apply, and how to transmit data, without modifying the open-source app. The authors assess that such an experiment "can be set up in a trusted network environment by anyone with basic web hosting knowledge using PHP", with an example provided in the documentation and supplementary material.

## Design Implications

### Context
#### Requirements
- A server to receive and store incoming data; basic knowledge of HTTP or MQTT; sufficient IT security understanding appropriate to the audience, scale and duration of the experiment
#### Constraints
- The phyphox project cannot offer hosting services; the technical hurdle for educators is described as the biggest problem, and a ready-to-use service would require funding for staff and hardware

### Target Learners
- higher-education students
- learners in other science courses

### Target Learning Goals
- collaborative experimentation across course contexts

## Claims

- [Filtering incoming data is essential for large-audience network experiments, and autocorrelation-quality thresholds plus mid-series mass selection remove most erroneous points](../claims/filtering-large-audience-experiment-data.md) [+W]
- [The phyphox network interface enables real-time collaborative lecture-hall experiments in which students jointly determine a spring constant from a live frequency-over-mass plot](../claims/real-time-lecture-hall-network-experiment.md) [+W]
- [Collaborative smartphone pendulum data collected via a web form let students conduct an experiment before the lecture explains the theory, reproducing the expected pendulum behavior](../claims/web-form-flipped-lecture-experiment.md) [+W]

## Related Strategies

- Phyphox Network Interface
- [Use the phyphox Arduino/MicroPython libraries so educators and learners with rudimentary programming knowledge can build app-connected experiments](phyphox-libraries-teaching-strategy.md)

## Examples
-

## Key Sources
- S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830
