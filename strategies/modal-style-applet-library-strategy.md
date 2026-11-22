---
type: strategy
id: modal-style-applet-library-strategy
title: Use a completely modal programming style in applet class libraries to minimize instructor programming effort
description: "Whereas interface design guides recommend modeless interfaces that keep many user options available at once, this strategy deliberately makes the applet's operation modal, with an integer mouseMode variable controllin..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: michael-e-peskin-2003
    resource: "https://arxiv.org/abs/physics/0302044"
    title: "Michael E. Peskin. (2003). Abstract Applets: a Method for Integrating Numerical Problem-Solving into the Undergraduate Physics Curriculum. https://arxiv.org/abs/physics/0302044"
    author: Michael E. Peskin
---

# Use a completely modal programming style in applet class libraries to minimize instructor programming effort

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Whereas interface design guides recommend modeless interfaces that keep many user options available at once, this strategy deliberately makes the applet's operation modal, with an integer mouseMode variable controlling mouse actions and ModeButton objects switching modes. The author states: "I would like to make the programming task as easy as possible for the instructor, even if this co sts the user some ﬂexibility. Thus, the programming style is completely modal." This trades end-user flexibility for simpler instructor code.

## Design Implications

### Context
#### Requirements
- A mouseMode variable in the parent class, changed by ModeButton objects, with mouse-action functions testing the mode value before acting
#### Constraints
- The article acknowledges this costs the user some flexibility relative to a modeless interface

### Target Learners
- instructors writing problem-set applets for undergraduate physics courses

### Target Learning Goals
- simplifying construction of numerical exercises so they can be integrated into weekly problem sets

## Related Strategies

- Physicsapplet Java Class Library
- [Keep the video player user interface consistent when pausing for self-explanation prompts to avoid extraneous reorientation](consistent-ui-when-video-prompts-pause.md)

## Examples
-

## Key Sources
- Michael E. Peskin. (2003). Abstract Applets: a Method for Integrating Numerical Problem-Solving into the Undergraduate Physics Curriculum. https://arxiv.org/abs/physics/0302044
