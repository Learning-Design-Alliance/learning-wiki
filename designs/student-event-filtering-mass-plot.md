---
type: design
id: student-event-filtering-mass-plot
title: Students filter real collider events by quality criteria to produce clean mass plots
description: Across the LHC exercises students act as analysts by filtering events rather than receiving pre-cleaned data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-16
sources:
  - id: k-cecire-2011
    resource: "https://quarknet.fnal.gov"
    title: "K. Cecire (2011). Particle Physics Masterclasses. Proceedings of the DPF-2011 Conference, Providence, RI. https://quarknet.fnal.gov"
    author: K. Cecire
---

# Students filter real collider events by quality criteria to produce clean mass plots

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Across the LHC exercises students act as analysts by filtering events rather than receiving pre-cleaned data. In the CMS exercise they "determine the quality of the events based on the muon tracks" and "filter the events in order to get the best possible mass plot"; in the ATLAS Z-path they filter out all but dilepton Z decays to create a mass plot. Filtering matters because unfiltered data shows a mass peak hard to distinguish from noise.

## Design Implications

### Context
#### Requirements
- Event displays with calculable invariant masses and quality criteria students can apply, such as muon tracks
#### Constraints
- Unfiltered data shows a J/ mass peak, which is hard to distinguish from noise

### Target Learners
- high school physics students

### Learning Goals
- data selection and quality judgment
- constructing a mass plot from filtered events

### Claims
- 

## Related Designs

- [LHC masterclass data exercises and analysis software for ATLAS, ALICE, and CMS](lhc-masterclass-data-exercises.md)
- [Searching for gravitational waves in noisy data activity](noisy-data-matched-filtering-activity.md)

## Examples
-

## Key Sources
- K. Cecire (2011). Particle Physics Masterclasses. Proceedings of the DPF-2011 Conference, Providence, RI. https://quarknet.fnal.gov
