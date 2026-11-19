---
type: design
id: dicam-blended-lecture-hardware-setup
title: Low-cost hardware setup for high-quality low-bandwidth streaming of blackboard lectures
description: "The article specifies a per-lecture-hall equipment set: the professor's own laptop as control hub, a full HD camcorder with directional microphone (wide-angle PTZ camera for large blackboards), a Camlink 4K HDMI-to-US..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: saray-busto-2021
    resource: "https://arxiv.org/abs/2010.14247"
    title: "Saray Busto, Michael Dumbser, and Elena Gaburro. (2021). A Simple but Efficient Concept of Blended Teaching of Mathematics for Engineering Students during the COVID-19 Pandemic. https://arxiv.org/abs/2010.14247"
    author: Saray Busto, Michael Dumbser, and Elena Gaburro
---

# Low-cost hardware setup for high-quality low-bandwidth streaming of blackboard lectures

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article specifies a per-lecture-hall equipment set: the professor's own laptop as control hub, a full HD camcorder with directional microphone (wide-angle PTZ camera for large blackboards), a Camlink 4K HDMI-to-USB converter, active USB 3.0 extension cable, USB hub, Wacom Cintiq 22 graphics tablet with OpenBoard software, 4K HDMI splitter, bluetooth airlink or Jabra Speak 810 speakerphone for bidirectional communication, and a personal bluetooth ear microphone. Table 5 prints a total cost estimate of 1700 EUR including 22% VAT. Two completely redundant systems (videocamera and graphics tablet) were installed in each hall so professors could freely choose their teaching means.

## Design Implications

### Context
#### Requirements
- the professor's laptop must be connected with a single USB/A cable and one HDMI cable, with sound system and ear speaker paired via bluetooth
- a large set of adapters was made available due to heterogeneous professor laptops (VGA, DisplayPort, mini HDMI, micro HDMI, USB-C)
#### Constraints
- ZOOM's automatic 360 p limit for meetings with three or more participants required the screen-sharing workaround
- the reduced framerate of the video capturing setup is the stated compromise

### Target Learners
- undergraduate engineering students at the University of Trento

### Learning Goals
- transmission of complex mathematical blackboard content with readable small indices and superscripts
- high-quality audio and bidirectional communication for online students

### Claims
- [Zoom 360P Insufficient For Math Blackboard](../claims/zoom-360p-insufficient-for-math-blackboard.md) [+M]
- [Screen Sharing Full Hd Improves Blackboard Video Quality](../claims/screen-sharing-full-hd-improves-blackboard-video-quality.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Saray Busto, Michael Dumbser, and Elena Gaburro. (2021). A Simple but Efficient Concept of Blended Teaching of Mathematics for Engineering Students during the COVID-19 Pandemic. https://arxiv.org/abs/2010.14247
