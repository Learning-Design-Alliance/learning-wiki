---
type: design
id: event-driven-directed-graph-vle-framework
title: Event-driven, directed-graph VLE framework using the Observer Pattern for modular, interchangeable VR interactions
description: "The framework organizes a virtual laboratory environment as an event-driven, directed-graph architecture in which \"specific components within the virtual reality space trigger different visual and haptic events upon i..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: rafael-padilla-perez-2024
    resource: "https://youtu.be/NBAVW_nH-1w"
    title: "Rafael Padilla Perez, Özgür Keleş. (2024). Immersive Virtual Reality Environments for Embodied Learning of Engineering Students. San Jose State University. https://youtu.be/NBAVW_nH-1w"
    author: Rafael Padilla Perez, Özgür Keleş
---

# Event-driven, directed-graph VLE framework using the Observer Pattern for modular, interchangeable VR interactions

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The framework organizes a virtual laboratory environment as an event-driven, directed-graph architecture in which "specific components within the virtual reality space trigger different visual and haptic events upon interaction." It is built with C# and Unity 3D using the XR Interaction Toolkit and OpenXR for the Meta Quest 2. Its core is the Observer Pattern, categorizing behaviors into "events," triggers from world state changes, and "observers," which execute as a result of events, so that any VR interaction (button press, lever pull, hand gesture) can trigger an event of any kind, making features replaceable and the same laboratory usable with interchangeable interaction types.

## Design Implications

### Context
#### Requirements
- Developed with C# and Unity 3D leveraging the XR interaction toolkit and the OpenXR framework for the Meta Quest 2
#### Constraints
- Version B of the architecture was not tested in this study

### Target Learners
- university engineering students

### Learning Goals
- tensile testing practices
- physical behavior of Poisson's ratio coefficients in different materials

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Rafael Padilla Perez, Özgür Keleş. (2024). Immersive Virtual Reality Environments for Embodied Learning of Engineering Students. San Jose State University. https://youtu.be/NBAVW_nH-1w
