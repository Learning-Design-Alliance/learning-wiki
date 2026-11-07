---
type: design
id: two-scenario-cervix-simulator-design
title: Two-scenario cervix design pairing a closed cervix with an open cervix with bulging membranes
description: "The simulator's design pattern is to represent two distinct clinical scenarios with separate physical cervix models: a closed cervix of 5 cm length for prophylactic cerclage, and a cervix \"already opened to 1.5 cm wit..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: buechel-j-2024
    resource: "https://doi.org/10.1007/s00404-024-07812-8"
    title: "Buechel J, Kalisz A, Herbert S-L, Scherer-Quenzer A, Blau-Schneider B, Starrach T, Kraft K, Wöckel A, Pecks U, Kiesel M. (2024). Development and validation of a cost-effective DIY simulation model for McDonald cerclage training. Archives of Gynecology and Obstetrics. https://doi.org/10.1007/s00404-024-07812-8"
    author: Buechel J, Kalisz A, Herbert S-L, Scherer-Quenzer A, Blau-Schneider B, Starrach T, Kraft K, Wöckel A, Pecks U, Kiesel M
---

# Two-scenario cervix design pairing a closed cervix with an open cervix with bulging membranes

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The simulator's design pattern is to represent two distinct clinical scenarios with separate physical cervix models: a closed cervix of 5 cm length for prophylactic cerclage, and a cervix "already opened to 1.5 cm with bulging membranes" in which the membranes are simulated with a water-filled balloon. Different silicone shore hardnesses (00 for the closed cervix, 10 for the open cervix) were chosen to balance tactile feel with suture interaction.

## Design Implications

### Context
#### Requirements
- Silicone shore hardness must be matched to the scenario: shore 00 for the closed cervix and shore 10 for the open cervix, since smoother shore-00 material for the open cervix led to common suture tearing.
- A water-filled balloon is required to reassemble the bulging membranes (0.02 EUR per use).
#### Constraints
- The shore-hardness choice trades off tactile realism against suture interaction, so the material does not meet all criteria of real tissue.

### Target Learners
- obstetricians and gynecologists in perinatal units

### Learning Goals
- prophylactic cerclage placement
- emergency or rescue cerclage with bulging membranes

### Claims
- [Wccs Realism Ratings Scenarios](../claims/wccs-realism-ratings-scenarios.md) [+M]

## Related Designs
- Wuerzburg Cervical Cerclage Simulator

## Examples
-

## Key Sources
- Buechel J, Kalisz A, Herbert S-L, Scherer-Quenzer A, Blau-Schneider B, Starrach T, Kraft K, Wöckel A, Pecks U, Kiesel M. (2024). Development and validation of a cost-effective DIY simulation model for McDonald cerclage training. Archives of Gynecology and Obstetrics. https://doi.org/10.1007/s00404-024-07812-8
