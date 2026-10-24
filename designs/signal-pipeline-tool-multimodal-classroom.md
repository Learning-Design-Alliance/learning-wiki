---
type: design
id: signal-pipeline-tool-multimodal-classroom
title: Automated Matlab signal pipeline synchronizing EDA, EEG, and survey data
description: The signal pipeline is an autonomous Matlab program into which raw signals from the Empatica E4, the CytonRK headsets, and Qualtrics survey data are fed, producing a synchronized and processed dataset without subjecti...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-23
sources:
  - id: kennett-2025
    resource: "https://doi.org/10.1037/edu0000964.supp"
    title: "Kennett, R., Martin, A. J., Pearson, J., Burns, E. C., & Collie, R. (2025). Challenge and Threat Appraisal of Tests in High School: Integrating Educational Psychology and Biopsychology Improves Understanding of How Students Take Tests. Journal of Educational Psychology. https://doi.org/10.1037/edu0000964.supp"
    author: "Kennett, R., Martin, A. J., Pearson, J., Burns, E. C., & Collie, R"
---

# Automated Matlab signal pipeline synchronizing EDA, EEG, and survey data

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The signal pipeline is an autonomous Matlab program into which raw signals from the Empatica E4, the CytonRK headsets, and Qualtrics survey data are fed, producing a synchronized and processed dataset without subjective human intervention. Each recording has an independent layered database so raw data or any processing step can be revisited, and a graphical interface allows visual inspection of each stage, including automated peak-alpha frequency identification.

## Design Implications

### Context
#### Requirements
- Individual per-participant data files were needed because some steps, such as Fourier transforms into time slices, took nearly 10 hours to process
#### Constraints
- Ledalab's conservative curve-matching approach may produce false negatives, so the research measured event amplitude rather than frequency

### Target Learners
- high school science students

### Learning Goals
- processing multimodal physiological and survey data for observational classroom research

### Claims
- 

## Related Designs

- [CytonRK: a custom head-mounted portable EEG recorder for classroom use](cytonrk-portable-eeg-headset.md)

## Examples
-

## Key Sources
- Kennett, R., Martin, A. J., Pearson, J., Burns, E. C., & Collie, R. (2025). Challenge and Threat Appraisal of Tests in High School: Integrating Educational Psychology and Biopsychology Improves Understanding of How Students Take Tests. Journal of Educational Psychology. https://doi.org/10.1037/edu0000964.supp
