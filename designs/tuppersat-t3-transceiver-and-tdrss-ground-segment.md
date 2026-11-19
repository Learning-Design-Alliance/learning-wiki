---
type: design
id: tuppersat-t3-transceiver-and-tdrss-ground-segment
title: T³ LoRa transceiver and TDRSS ground segment
description: The TupperSat Telemetry Thingamabob (T³) is a small self-contained radio unit featuring an RFM95 LoRa radio and an ATMega328 processor that manages the radio interface and communicates with a TupperSat over TTL serial...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: david-murphy-2020
    resource: "https://arxiv.org/abs/2010.03332"
    title: "David Murphy, Robert Jeffrey, Deirdre Coffey, Morgan Fraser, Sheila McBreen, Lorraine Hanlon. (2020). TupperSats: Thinking Inside the Box for Space Systems Engineering. https://arxiv.org/abs/2010.03332"
    author: David Murphy, Robert Jeffrey, Deirdre Coffey, Morgan Fraser, Sheila McBreen, Lorraine Hanlon
---

# T³ LoRa transceiver and TDRSS ground segment

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The TupperSat Telemetry Thingamabob (T³) is a small self-contained radio unit featuring an RFM95 LoRa radio and an ATMega328 processor that manages the radio interface and communicates with a TupperSat over TTL serial; it evolved through CanSat and XBee radios after earlier reliability problems. The instructor-operated ground segment, the TupperSat Data Relay Satellite System (TDRSS), deploys several ground stations on pursuit vehicles, each running a Tornado web server that logs telemetry and re-transmits packets over HTTP to a central UCD server with an online tracking interface. The authors report that "The T³ has proved to be reliable and versatile" and expect it to form the basis of the communications system for years to come.

## Design Implications

### Context
#### Requirements
- Line-of-sight communication is needed for reliable reception; low transmission cadence (about one packet every 30 seconds) conserves battery and reduces collisions
- The central server stores every packet, which may be the only data available for post-flight analysis if a payload is not recovered
#### Constraints
- The low-power radio signal becomes too weak to receive once line-of-sight is lost at low altitude, so pursuit vehicles must be within a few hundred metres of the landing site

### Target Learners
- postgraduate MSc students building the onboard flight software and payloads

### Learning Goals
- communications systems engineering
- embedded serial interfacing
- telemetry and ground segment operations

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- David Murphy, Robert Jeffrey, Deirdre Coffey, Morgan Fraser, Sheila McBreen, Lorraine Hanlon. (2020). TupperSats: Thinking Inside the Box for Space Systems Engineering. https://arxiv.org/abs/2010.03332
