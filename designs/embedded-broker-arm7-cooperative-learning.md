---
type: design
id: embedded-broker-arm7-cooperative-learning
title: Embedded broker on an ARM7 board replacing an expensive server
description: The embedded broker is the backend of the whole system, built on an ARM7 development board to replace an expensive high-end server.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-16
sources:
  - id: kao-2010
    resource: "https://www.ijcsi.org"
    title: "Kao, F.-C., Wang, S.-R. & Huang, T.-H. (2010). The Design of Circuit-Measuring Collaborative Learning System with Embedded Broker. IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 1, No. 3. https://www.ijcsi.org"
    author: "Kao, F.-C., Wang, S.-R. & Huang, T.-H"
---

# Embedded broker on an ARM7 board replacing an expensive server

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The embedded broker is the backend of the whole system, built on an ARM7 development board to replace an expensive high-end server. When started, its main duty is "to listen to the status of each user constantly", determine each learner's group immediately, and copy status-change information to members of the same group so that instrument operation and measured circuit data display identically for all group members. Control parameters flow through TCP/IP control functions between users' 3D virtual instruments via the broker.

## Design Implications

### Context
#### Requirements
- users input the IP of the embedded broker and an assigned port to connect
#### Constraints
- high-end general-purpose servers are described as complicated, expensive and a direct increase to system building cost, which the broker addresses

### Target Learners
- networked cooperative learning groups of electronics learners

### Learning Goals
- synchronized real-time shared operation of 3D virtual instruments

### Claims
- 

## Related Designs

- [Circuit-measuring cooperative learning system with 3D virtual instruments](circuit-measuring-3d-virtual-instrument-cooperative-learning-system.md)
- [Embedded RS-232 module capturing multimeter panel data with an 89C51 chip](embedded-rs232-module-89c51-multimeter.md)

## Examples
-

## Key Sources
- Kao, F.-C., Wang, S.-R. & Huang, T.-H. (2010). The Design of Circuit-Measuring Collaborative Learning System with Embedded Broker. IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 1, No. 3. https://www.ijcsi.org. [doi:10.48550/arxiv.1002.1181](https://doi.org/10.48550/arxiv.1002.1181)
