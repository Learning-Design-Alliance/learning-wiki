---
type: research-method
id: privacy-preserving-linkage-and-analysis-of-educational-data-using-privacy-enhancing-techno
title: Privacy-preserving linkage and analysis of educational data using privacy-enhancing technologies
description: The article presents a worked scenario in which a DLP used across several school districts for high school math instruction is linked with state college enrollment and persistence records using secure multiparty computation, producing aggregate correlations between engagement patterns and college ou
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: dorie-vincent-2025-december-privacy
    resource: "https://doi.org/10.51388/20.500.12265/278"
    title: "Dorie, Vincent. (2025, December). Privacy enhancing technologies in digital learning platforms. Digital Promise. https://doi.org/10.51388/20.500.12265/278"
---

# Privacy-preserving linkage and analysis of educational data using privacy-enhancing technologies

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 5 studies (3 theoretical, 1 review, 1 design), `q1` · 0 of 5 report an effect size · 5 claims rest on one study

## Description
The article presents a worked scenario in which a DLP used across several school districts for high school math instruction is linked with state college enrollment and persistence records using secure multiparty computation, producing aggregate correlations between engagement patterns and college outcomes with no raw data ever moving between the parties. The researcher tests analysis code on synthetic student data and applies differential privacy to summary tables before publication. The article describes this as turning a previously impossible study into a feasible one.

## Accounts
<!-- How each source describes or uses the method -->
- **End-to-end PET workflow: SMPC linkage of DLP engagement data with state college outcomes**: The article presents a worked scenario in which a DLP used across several school districts for high school math instruction is linked with state college enrollment and persistence records using secure multiparty computation, producing aggregate correlations between engagement patterns and college outcomes with no raw data ever moving between the parties. The researcher tests analysis code on synthetic student data and applies differential privacy to summary tables before publication. The article describes this as turning a previously impossible study into a feasible one. (Privacy Enhancing Technologies in Digital Learning Platforms)
- **Design the de-identified data architecture before data collection begins**: Because external evidence goals often emerge after a product ships, the guide urges teams to decide up front whether researchers will ever touch identifiable data. It states that "If there is a realistic possibility that the project will become research, design the data architecture before data collection begins," since de-identifying after analysis is fundamentally different from never granting access. Early architecture decisions preserve the option of an NHSR pathway and avoid costly retrofits. (Navigating Research Approvals for EdTech Research and Evaluation: A Practical Guide)

### Claims
- [PETs expand the value of data by enabling sharing where in-the-clear approaches are infeasible](../claims/pets-expand-data-value-through-sharing.md) [+W]
- [PETs trade utility for privacy, limiting use where accuracy is mandated](../claims/pets-utility-privacy-tradeoff.md) [-W]
- [Working a research scenario against a DLP surfaced concrete platform needs: adding measures, linking observational data, and enabling districtwide studies](../claims/scenario-terracotta-platform-capability-lessons.md) [+W]
- [Researcher access to identifiable student information, not research intent alone, determines NHSR status](../claims/access-not-intent-determines-nhsr.md) [+W]
- [Maintaining NHSR status requires no researcher access to identifiable records, no added procedures, and no non-standard prompts](../claims/nhsr-maintenance-three-conditions.md) [+W]

## Related Research Methods
-

## Key Sources
- Dorie, Vincent. (2025, December). Privacy enhancing technologies in digital learning platforms. Digital Promise. https://doi.org/10.51388/20.500.12265/278
<!-- merged 2026-10-10 from elements/end-to-end-pet-workflow-dlp-example ("End-to-end PET workflow: SMPC linkage of DLP engagement data with state college outcomes"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Younger, J. (2026, September). Navigating research approvals for edtech research and evaluation: A practical guide. Digital Promise. https://doi.org/10.51388/20.500.12265/318

# End-to-end PET workflow: SMPC linkage of DLP engagement data with state college outcomes

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 3 studies (2 theoretical, 1 design), `q1` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The article presents a worked scenario in which a DLP used across several school districts for high school math instruction is linked with state college enrollment and persistence records using secure multiparty computation, producing aggregate correlations between engagement patterns and college outcomes with no raw data ever moving between the parties. The researcher tests analysis code on synthetic student data and applies differential privacy to summary tables before publication. The article describes this as turning a previously impossible study into a feasible one.

## Design Implications

### Context
#### Requirements
- Willingness of school districts and the state education agency to compute outcome statistics jointly
#### Constraints
- Ordinarily, linking these datasets would mean transferring identifiable student information

### Target Learners
- high school math students whose engagement data is analyzed

### Target Learning Goals
- understanding which learning behaviors predict later college math success

### Affordances
- [Pets Dual Technical Social Technologies](../theories/pets-dual-technical-social-technologies.md)

## Claims

- [PETs expand the value of data by enabling sharing where in-the-clear approaches are infeasible](../claims/pets-expand-data-value-through-sharing.md) [+W]
- [PETs trade utility for privacy, limiting use where accuracy is mandated](../claims/pets-utility-privacy-tradeoff.md) [-W]
- [Working a research scenario against a DLP surfaced concrete platform needs: adding measures, linking observational data, and enabling districtwide studies](../claims/scenario-terracotta-platform-capability-lessons.md) [+W]

## Related Elements

- [Districtwide data system for secure, reliable data management](../elements/districtwide-data-system-element.md)

## Examples

- [Integrate PETs at every stage of the research lifecycle](../strategies/integrate-pets-across-research-lifecycle.md)

## Key Sources
- Dorie, Vincent. (2025, December). Privacy enhancing technologies in digital learning platforms. Digital Promise. https://doi.org/10.51388/20.500.12265/278
-->
