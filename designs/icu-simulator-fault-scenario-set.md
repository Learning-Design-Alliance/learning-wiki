---
type: design
id: icu-simulator-fault-scenario-set
title: Scenario-based fault analysis across four device modules with 18 fault patterns
description: "The simulator includes \"18 device-related fault patterns organized into scenario-based learning activities across four device modules\": ventilator (airway obstruction, low compliance, circuit leakage, auto-PEEP), moni..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: inan-onur-akyüz-ali-2026
    resource: "https://doi.org/10.1186/s12909-026-09952-8"
    title: "İnan Onur; Akyüz Ali. (2026). Simulation- and AI-supported technical troubleshooting training for biomedical device technology students in intensive care equipment education. BMC Medical Education. https://doi.org/10.1186/s12909-026-09952-8"
    author: İnan Onur; Akyüz Ali
---

# Scenario-based fault analysis across four device modules with 18 fault patterns

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The simulator includes "18 device-related fault patterns organized into scenario-based learning activities across four device modules": ventilator (airway obstruction, low compliance, circuit leakage, auto-PEEP), monitor (overdamping, underdamping, electrode disconnection, electromagnetic noise), infusion pump (line occlusion, free flow, air bubbles, low flow) and CRRT (filter clotting, blood line occlusion, effluent line problems, air detection, pump failure, sensor drift). Each scenario follows an observation–hypothesis–verification–interpretation pathway.

## Design Implications

### Context
#### Requirements
- Scenarios require instructor supervision and guiding questions rather than direct answers
#### Constraints
- Scopes are limited to selected mechanisms and parameter relationships; scenarios are model-based educational representations, not full clinical variability

### Target Learners
- biomedical device technology students

### Learning Goals
- distinguishing fault mechanisms
- localizing circuit faults
- interpreting signal-quality problems

### Claims
- 

## Related Designs

- [Hybrid rule-based plus LLM-supported AI interpretation module](hybrid-rule-based-llm-interpretation-module.md)
- [Mechanism-based technical troubleshooting as target competence](mechanism-based-technical-troubleshooting.md)

## Examples
-

## Key Sources
- İnan Onur; Akyüz Ali. (2026). Simulation- and AI-supported technical troubleshooting training for biomedical device technology students in intensive care equipment education. BMC Medical Education. https://doi.org/10.1186/s12909-026-09952-8
