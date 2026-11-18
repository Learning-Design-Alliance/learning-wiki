---
type: design
id: cms-wzh-measurement-ispy-webgl-cima
title: CMS WZH masterclass measurement with iSpy-WebGL event display and CIMA analysis tool
description: The CMS WZH measurement is a masterclass analysis similar to the ATLAS Z measurement but using entirely authentic data with a few Higgs candidates mixed in; students build a mass plot and find the W+ to W- ratio.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: k-cecire-2017
    resource: "http://www.physicsmasterclasses.org"
    title: "K. Cecire. (2017). Developments in International Masterclasses. Meeting of the Division of Particle and Fields (DPF), 31 July – 4 August, 2017 at Fermilab. http://www.physicsmasterclasses.org"
    author: K. Cecire
---

# CMS WZH masterclass measurement with iSpy-WebGL event display and CIMA analysis tool

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The CMS WZH measurement is a masterclass analysis similar to the ATLAS Z measurement but using entirely authentic data with a few Higgs candidates mixed in; students build a mass plot and find the W+ to W- ratio. It can be done entirely online: the event display, iSpy-WebGL, and the analysis tool, CMS Instrument for Masterclass Analysis (CIMA), are both browser-accessible. In CIMA, "students click the invariant masses into the appropriate 2 GeV bins to build the mass plot themselves; the mass plot is not built automatically." The measurement was upgraded in 2017 so students select leptons themselves and the event sample was increased.

## Design Implications

### Context
#### Requirements
- Internet browser access to iSpy-WebGL and CIMA
- Students must select leptons in the event display and enter invariant masses into CIMA bins
#### Constraints
- The 2017 upgrade retains automatic invariant masses only for Higgs candidates; for dileptons students must select the leptons themselves

### Target Learners
- high school students

### Learning Goals
- event classification
- invariant mass analysis
- building mass plots from authentic CMS data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- K. Cecire. (2017). Developments in International Masterclasses. Meeting of the Division of Particle and Fields (DPF), 31 July – 4 August, 2017 at Fermilab. http://www.physicsmasterclasses.org
