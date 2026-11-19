---
type: strategy
id: define-operating-conditions-before-classroom-ar-deployment
title: Before deploying location-based AR with pupils, run a comparative usability test to define optimal operating conditions and prefer filtered embedded GNSS data over raw RTK
description: The authors recommend ensuring usability and defining suitable conditions of use before offering the system to a young audience.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: j-mercier-2023
    resource: "https://arxiv.org/abs/2308.13544"
    title: "J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo. (2023). Impact of Geolocation Data on Augmented Reality Usability: A Comparative User Test. https://arxiv.org/abs/2308.13544"
    author: J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo
---

# Before deploying location-based AR with pupils, run a comparative usability test to define optimal operating conditions and prefer filtered embedded GNSS data over raw RTK

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors recommend ensuring usability and defining suitable conditions of use before offering the system to a young audience. Their test showed raw RTK data, valuable for advanced users at a 2D map scale, is "not particularly suitable for a real-time continuous usage" on a 1:1 tridimensional scale without filters, so embedded GNSS data served learners better in this system.

## Design Implications

### Context
#### Requirements
- A usability assessment (SUS, UEQ, HARUS) and in-test logging of accuracy, exploration, and focus before classroom introduction
#### Constraints
- RTK data without outlier filters degraded rather than improved usability in this test; future studies should test RTK with proper outlier processing

### Target Learners
- pupils in outdoor biodiversity education

### Target Learning Goals
- usable location-based AR-supported field exploration of biodiversity

## Claims

- [Participants using an external RTK module were exposed to less accurate and less continuous geolocation data than participants using the device's embedded GNSS sensor](../claims/rtk-less-accurate-than-embedded-gnss-location-ar.md) [+W]
- [The group exposed to less accurate geolocation data reported lower usability on all nine scales, of which five were statistically significant](../claims/geolocation-accuracy-predicts-ar-usability.md) [+W]
- [No significant group differences in exploration diversity or ease: POIs visited and 2D map openings did not differ between GNSS and RTK groups](../claims/no-group-difference-pois-visited-map-openings.md) [~W]
- [Geolocation data accuracy showed no significant relation to focus: screen-gaze time ratios did not differ between groups](../claims/no-relation-geolocation-accuracy-focus-screen-gaze.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo. (2023). Impact of Geolocation Data on Augmented Reality Usability: A Comparative User Test. https://arxiv.org/abs/2308.13544
