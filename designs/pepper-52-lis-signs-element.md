---
type: design
id: pepper-52-lis-signs-element
title: Pepper robot with 52 co-designed LIS signs and four SOV-order signed sentences
description: "The element is the Pepper social robot configured as a LIS signing agent: the authors co-designed and implemented \"a total of 52 LIS signs\" spanning school-related terms, common actions and nouns, and work-related voc..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: giulia-boaa-2025
    resource: "https://github.com/CodeCruncher63/ISCR2025"
    title: "Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025"
    author: Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo
---

# Pepper robot with 52 co-designed LIS signs and four SOV-order signed sentences

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The element is the Pepper social robot configured as a LIS signing agent: the authors co-designed and implemented "a total of 52 LIS signs" spanning school-related terms, common actions and nouns, and work-related vocabulary, plus four short sentences following LIS Subject–Object–Verb word order. Signs were built with the Pepper SDK Animation Editor and a MATLAB inverse-kinematics toolchain, with videos released on GitHub. It was evaluated for intelligibility with 12 LIS-proficient participants.

## Design Implications

### Context
#### Requirements
- Signs must be performable with hand configurations in which all fingers are either open or closed, since Pepper's fingers cannot move independently
#### Constraints
- The chest-mounted tablet interferes with arm movements, making signs near the torso difficult or impossible
- Constrained wrist and elbow mobility limits faithful reproduction of LIS handshapes

### Target Learners
- Deaf LIS users
- LIS interpreters

### Learning Goals
- Accessible signed communication from a social robot in public and assistive settings

### Claims
- [Pepper Lis Sign Recognition Binomial Tests](../claims/pepper-lis-sign-recognition-binomial-tests.md) [+M]
- [Pepper Isolated Signs Recognized Better Than Sentences](../claims/pepper-isolated-signs-recognized-better-than-sentences.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025
