---
type: design
id: cytonrk-portable-eeg-headset
title: "CytonRK: a custom head-mounted portable EEG recorder for classroom use"
description: The CytonRK is a bespoke head-mounted EEG device built by the lead author because no commercial device met classroom requirements.
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

# CytonRK: a custom head-mounted portable EEG recorder for classroom use

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The CytonRK is a bespoke head-mounted EEG device built by the lead author because no commercial device met classroom requirements. It uses an OPENBCI Cyton board with an ADS1299 8-channel converter, records at 250Hz to local micro-SD memory with a battery-backed real-time clock, and uses dry Silver Chloride comb electrodes on a 25mm elasticized harness designed for minimal invasiveness in hair.

## Design Implications

### Context
#### Requirements
- Local memory recording was chosen because Bluetooth pairing of up to 26 devices in one classroom was impractical and school WiFi networks were infeasible
#### Constraints
- The article notes temporal electrode placement was moved from just in front to just behind the ears after participant feedback about pressure irritation

### Target Learners
- high school students in naturalistic classroom settings

### Learning Goals
- recording EEG-based indicators of attention and working memory during real classroom assessments

### Claims
- 

## Related Designs

- [Simulated classroom assessment with educational films, quizzes, and video/EEG monitoring](simulated-classroom-film-quiz-assessment.md)
- [Automated Matlab signal pipeline synchronizing EDA, EEG, and survey data](signal-pipeline-tool-multimodal-classroom.md)

## Examples
-

## Key Sources
- Kennett, R., Martin, A. J., Pearson, J., Burns, E. C., & Collie, R. (2025). Challenge and Threat Appraisal of Tests in High School: Integrating Educational Psychology and Biopsychology Improves Understanding of How Students Take Tests. Journal of Educational Psychology. https://doi.org/10.1037/edu0000964.supp
