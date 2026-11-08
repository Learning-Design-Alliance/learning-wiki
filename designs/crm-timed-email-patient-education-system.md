---
type: design
id: crm-timed-email-patient-education-system
title: Automated CRM-based timed email delivery system for pre-appointment patient education material
description: "An automated system built on the institution's customer relationship management software (Salesforce) that monitors a patient's treatment schedule, adapts dynamically to schedule changes, and delivers precisely timed..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: schuller-bw-2022
    resource: "https://doi.org/10.1002/acm2.13601"
    title: "Schuller BW, Burch C, Casterton T, Crowther C, Fowler J, Stenmark MH. (2022). Precision patient education using a “flipped classroom” approach. J Appl Clin Med Phys. https://doi.org/10.1002/acm2.13601"
    author: Schuller BW, Burch C, Casterton T, Crowther C, Fowler J, Stenmark MH
---

# Automated CRM-based timed email delivery system for pre-appointment patient education material

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
An automated system built on the institution's customer relationship management software (Salesforce) that monitors a patient's treatment schedule, adapts dynamically to schedule changes, and delivers precisely timed emails at three time points ahead of appointments. It also tracks engagement metrics including email open rates, education material open rates, average read times, and number of times material was accessed, which served as the study's primary endpoint.

## Design Implications

### Context
#### Requirements
- CRM software integrated with the patient treatment schedule
- Three written education pieces timed to the care path between consult, planning scan, and first treatment
#### Constraints
- Technical errors meant two patients never received emails and four patients never received email no. 3

### Target Learners
- radiation oncology patients

### Learning Goals
- pre-appointment preparation and understanding of treatment procedures

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Schuller BW, Burch C, Casterton T, Crowther C, Fowler J, Stenmark MH. (2022). Precision patient education using a “flipped classroom” approach. J Appl Clin Med Phys. https://doi.org/10.1002/acm2.13601
