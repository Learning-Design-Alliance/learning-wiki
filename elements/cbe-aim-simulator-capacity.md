---
type: element
id: cbe-aim-simulator-capacity
title: Enhanced CBE simulator in Assessment Integration Management (AIM)
description: The simulator used for the comparability study was enhanced in 2018–2019 within AIM, the web interface for creating tests and uploading test models, item pools, and student samples to run simulations.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: hu-2021
    resource: "https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/"
    title: "Hu, A., Chien, M., & Meyer, P. (2021). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: A simulation study. NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/"
    author: "Hu, A., Chien, M., & Meyer, P"
---

# Enhanced CBE simulator in Assessment Integration Management (AIM)

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The simulator used for the comparability study was enhanced in 2018–2019 within AIM, the web interface for creating tests and uploading test models, item pools, and student samples to run simulations. Users can now specify longitudinal exposure control, content balancing, termination and invalidation rules, and provide testing dates, true thetas, and student attributes for multiple administrations. "The simulator capacity was scaled up to administer items to up to 8,000 simulees concurrently, with a maximum of 2,000 simulees allowed in each simulation," compared with 1,000 previously on the CBE and 400 on COLO.

## Design Implications

### Context
#### Requirements
- A test key, list of true thetas, and output delivery configuration are needed to run the COLO Jenkins-Validator-Runner simulator
#### Constraints
- Maximum of 2,000 simulees allowed in each CBE simulation; COLO allows only 400 simulees

### Target Learners
- K-12 students represented by simulated examinees

### Target Learning Goals
- Evaluating adaptive test engine comparability on validity, reliability, adaptivity, and item exposure

## Related Elements

- [CBE enhancements for MAP Growth delivery (Project Altair)](cbe-project-altair-enhancements.md)
- [Enhanced constraint-based engine (CBE) test models with guidelines and constraints for MAP Growth delivery](cbe-test-models-guidelines-constraints.md)
- [MAP Growth grade-level item pool simulation design (on-grade, ±1-grade, and all-grade pools with on- and off-grade simulees)](map-growth-pool-simulation-design.md)

## Examples
-

## Key Sources
- Hu, A., Chien, M., & Meyer, P. (2021). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: A simulation study. NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/
