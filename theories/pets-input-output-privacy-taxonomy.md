---
type: theory
title: Taxonomy of PETs by input privacy versus output privacy
description: "The article organizes PETs into two categories: input privacy methods, which largely relate to limiting access and use of data under active management, and output privacy, which minimizes the risk of reidentification..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: dorie-vincent-2025-december-privacy
    resource: "https://doi.org/10.51388/20.500.12265/278"
    title: "Dorie, Vincent. (2025, December). Privacy enhancing technologies in digital learning platforms. Digital Promise. https://doi.org/10.51388/20.500.12265/278"
---

# Taxonomy of PETs by input privacy versus output privacy

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 theoretical), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article organizes PETs into two categories: input privacy methods, which largely relate to limiting access and use of data under active management, and output privacy, which minimizes the risk of reidentification in uncontrolled settings such as public datasets or published figures. Input techniques include cryptographic protocols, secure multiparty computation, federated learning, secure enclaves, and zero-knowledge proofs; output techniques include differential privacy and synthetic data. Each technique is described with its mechanism, limitations, and example uses.

## Design Implications

### Context
#### Requirements
- Specific applications or services that employ PETs may use more than one of the above tools
#### Constraints
- Many PETs are immature, costly, or lack standards

### Target Learners
- educational researchers and platform developers handling learner data

### Target Learning Objectives
- selecting appropriate privacy techniques across the data lifecycle

### Claims

- [PETs expand the value of data by enabling sharing where in-the-clear approaches are infeasible](../claims/pets-expand-data-value-through-sharing.md) [+W]
- [PETs trade utility for privacy, limiting use where accuracy is mandated](../claims/pets-utility-privacy-tradeoff.md) [+W]

## Related Theories

- [PETs as dual technical and social technologies for protecting data while preserving utility](pets-dual-technical-social-technologies.md)

## Examples

- [Integrate PETs at every stage of the research lifecycle](../strategies/integrate-pets-across-research-lifecycle.md)
- [End-to-end PET workflow: SMPC linkage of DLP engagement data with state college outcomes](../elements/end-to-end-pet-workflow-dlp-example.md)

## Key Sources
- Dorie, Vincent. (2025, December). Privacy enhancing technologies in digital learning platforms. Digital Promise. https://doi.org/10.51388/20.500.12265/278
