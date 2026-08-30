---
type: goal-map
title: "ESCO — HVAC Installation & Repair (Skill Subset)"
description: Flattened goal map of ESCO occupation/skill nodes for HVAC installation and repair.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-30
source:
  framework: ESCO
  kind: standard
  version: "1.1.1"
  source_url: https://esco.ec.europa.eu/en
  license: "CC BY 4.0 — verify against ESCO's current terms before real ingest"
nodes:
  - id: hvac-core-occupation
    display_id: "1"
    label: Install, maintain and repair HVAC systems
    student_facing_label: Work on heating and cooling systems
    description: Top-level occupational skill node from ESCO's HVAC technician occupation profile.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-hvac-core"
  - id: hvac-read-schematics
    display_id: "1.1"
    label: Read and interpret HVAC technical schematics and manufacturer specifications
    description: Interpret wiring diagrams, refrigerant flow schematics, and manufacturer install/service manuals.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-read-schematics"
  - id: hvac-diagnose-faults
    display_id: "1.2"
    label: Diagnose HVAC system faults using systematic troubleshooting
    description: Isolate the cause of a system fault by testing components against the schematic and manufacturer specs.
    competency_framework: ESCO
    assessment_suggestion: Present a simulated system fault and have the learner walk through a diagnostic sequence, citing the schematic at each step.
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-diagnose-faults"
  - id: hvac-install-systems
    display_id: "1.3"
    label: Install heating, ventilation and air conditioning units to code
    description: Mount, connect, and commission HVAC units in compliance with local building and safety codes.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-install-systems"
  - id: hvac-handle-refrigerants-safely
    display_id: "1.4"
    label: Handle and recover refrigerants in compliance with safety and environmental regulations
    description: Charge, recover, and dispose of refrigerants using certified procedures and equipment.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-handle-refrigerants"
  - id: hvac-repair-systems
    display_id: "1.5"
    label: Repair and replace faulty HVAC components
    description: Remove and replace failed parts identified during diagnosis, then verify system operation.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-repair-systems"
  - id: hvac-preventive-maintenance
    display_id: "1.6"
    label: Perform preventive maintenance on HVAC systems
    description: Execute scheduled inspection, cleaning, and part-replacement routines to prevent failures.
    competency_framework: ESCO
    external_id: "http://data.europa.eu/esco/skill/ILLUSTRATIVE-preventive-maintenance"
relationships:
  - source: hvac-core-occupation
    target: hvac-read-schematics
    type: default
  - source: hvac-core-occupation
    target: hvac-diagnose-faults
    type: default
  - source: hvac-core-occupation
    target: hvac-install-systems
    type: default
  - source: hvac-core-occupation
    target: hvac-handle-refrigerants-safely
    type: default
  - source: hvac-core-occupation
    target: hvac-repair-systems
    type: default
  - source: hvac-core-occupation
    target: hvac-preventive-maintenance
    type: default
  - source: hvac-read-schematics
    target: hvac-diagnose-faults
    type: prerequisite
  - source: hvac-diagnose-faults
    target: hvac-repair-systems
    type: prerequisite
  - source: hvac-handle-refrigerants-safely
    target: hvac-install-systems
    type: prerequisite
---

# ESCO — HVAC Installation & Repair (Skill Subset)

> **Illustrative placeholder.** Node labels, descriptions, and `external_id` values here are representative examples, not pulled from ESCO's live API/dataset. A real ingest would replace `external_id` with ESCO's actual skill URIs and copy `label`/`description` verbatim from the ESCO CSV or API export rather than paraphrasing them.

## Description
A subset of ESCO's occupation/skill taxonomy for the HVAC installation-and-repair trade, normalized into this wiki's flat goal-map schema: one hierarchical root skill, six child skills, and a few cross-cutting prerequisite edges (e.g. you must be able to read a schematic before you can diagnose a fault against it).

## Related Wiki Pages
- Diagnosing a fault by testing against a schematic is the same expert-modeling structure as [Cognitive Apprenticeship](../elements/cognitive-apprenticeship.md).
- Sequencing "read schematics" before "diagnose faults" reflects the same prerequisite-ordering logic used throughout [Scaffolding](../elements/scaffolding.md).

## Key Sources
- ESCO (European Commission). *Skills, Competences, Qualifications and Occupations* classification. https://esco.ec.europa.eu/en
