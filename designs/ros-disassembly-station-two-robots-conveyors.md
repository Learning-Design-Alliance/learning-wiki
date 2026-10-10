---
type: design
id: ros-disassembly-station-two-robots-conveyors
title: ROS-based disassembly station with two robots and conveyor belts as the project hardware platform
description: The student project used a hardware disassembly station consisting of two robots and two conveyor belts, with a ROS backbone controlling the robots and adjunct installations.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: tobias-geger-2026
    resource: "https://arxiv.org/abs/2603.14529"
    title: "Tobias Geger, Dominique Briechle and Andreas Rausch. (2026). Bots and Blocks: Presenting a project-based approach for robotics education. https://arxiv.org/abs/2603.14529"
    author: Tobias Geger, Dominique Briechle and Andreas Rausch
---

# ROS-based disassembly station with two robots and conveyor belts as the project hardware platform

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The student project used a hardware disassembly station consisting of two robots and two conveyor belts, with a ROS backbone controlling the robots and adjunct installations. The system exposes topics for moving, rotating, grasping, digital outputs and inputs, joint states, conveyor and clamp control. Because some components were implemented in ROS 1, "a ROS bridge is required in order to integrate all functionalities into the new ROS2 system that the students are implementing." Students aligned the AI camera frame with the world frame via the /tf2 node for precise grasping.

## Design Implications

### Context
#### Requirements
- ROS drivers for both robots and a ROS bridge integrating legacy ROS components into the students' ROS2 system
#### Constraints
- Project goal is transferred from complex real products to plastic building bricks (4x2, 2x2 and 2x2 round blocks) configured under rules that keep bricks graspable by the hardware effectors

### Target Learners
- undergraduate student teams working on cyber-physical systems projects

### Learning Goals
- robot programming with ROS/ROS2, system integration, and AI-based object detection and localization

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Tobias Geger, Dominique Briechle and Andreas Rausch. (2026). Bots and Blocks: Presenting a project-based approach for robotics education. https://arxiv.org/abs/2603.14529
