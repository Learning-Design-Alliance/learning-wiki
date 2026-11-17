---
type: design
id: inverting-cascade-amplifier-troubleshooting-task
title: Faulty inverting cascade amplifier troubleshooting task with two planted faults
description: A two-stage op-amp circuit designed to study both the iterative and strategic aspects of troubleshooting.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: dimitri-r-dounas-frazer-2015
    resource: "https://arxiv.org/abs/1507.03939"
    title: "Dimitri R. Dounas-Frazer, Kevin L. Van De Bogart, MacKenzie R. Stetzer, and H. J. Lewandowski. (2015). The role of modeling in troubleshooting: an example from electronics. https://arxiv.org/abs/1507.03939"
    author: Dimitri R. Dounas-Frazer, Kevin L. Van De Bogart, MacKenzie R. Stetzer, and H. J. Lewandowski
---

# Faulty inverting cascade amplifier troubleshooting task with two planted faults

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A two-stage op-amp circuit designed to study both the iterative and strategic aspects of troubleshooting. Stage 1 is a noninverting amplifier (G1 = 2) and Stage 2 an inverting amplifier (G2 = −10), giving overall gain Gtot = −20. Two faults were planted in Stage 2: "the resistor R3 had a value of 100 Ω rather than the nominal value of 1 kΩ" and a broken op-amp producing a dc output of −15 V regardless of input. Both faults were localized in Stage 2 so students could use the Split-Half strategy early on.

## Design Implications

### Context
#### Requirements
- Students received a schematic including an algebraic expression for the gain of the entire circuit, but not for either stage
#### Constraints
- Both faults were localized in Stage 2, leaving Stage 1 functional

### Target Learners
- junior-level undergraduate physics majors in electronics courses

### Learning Goals
- diagnosing and repairing a malfunctioning electronic circuit

### Claims
- [Comparison Good Enough Agreement Localizes Faults](../claims/comparison-good-enough-agreement-localizes-faults.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Dimitri R. Dounas-Frazer, Kevin L. Van De Bogart, MacKenzie R. Stetzer, and H. J. Lewandowski. (2015). The role of modeling in troubleshooting: an example from electronics. https://arxiv.org/abs/1507.03939
