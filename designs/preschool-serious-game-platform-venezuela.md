---
type: design
id: preschool-serious-game-platform-venezuela
title: Multiuser offline Android serious-game platform for preschool math reinforcement
description: A tablet-based serious-game solution built in Unity3d and packaged as an APK, with a games module, a reports module, and a users module, storing all data in a local SQLite database so it runs without Internet connecti...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: luis-ortegano-2018
    title: Luis Ortegano, Esmitt Ramírez. (2018). Serious Educational Reinforcement Game in Preschool.
    author: Luis Ortegano, Esmitt Ramírez
---

# Multiuser offline Android serious-game platform for preschool math reinforcement

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A tablet-based serious-game solution built in Unity3d and packaged as an APK, with a games module, a reports module, and a users module, storing all data in a local SQLite database so it runs without Internet connectivity. It uses child photo-based profiles, progressively unlocked games and levels configured in JSON, and D3.js-based graphical reports for teachers. The authors state the software "solo se enfoca en utilizar los recursos locales del dispositivo para hacerlo independiente de la estructura de los planteles educativos".

## Design Implications

### Context
#### Requirements
- Games and their levels must be registered in the local database with JSON level configurations before they appear to children
#### Constraints
- Runs only on Android devices as an APK and relies solely on local device resources, with no Internet connectivity

### Target Learners
- Preschool children (ages 4-7) in Venezuelan initial education

### Learning Goals
- Reinforcement of mathematical skills such as geometric shape recognition and number ordering

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Luis Ortegano, Esmitt Ramírez. (2018). Serious Educational Reinforcement Game in Preschool.
