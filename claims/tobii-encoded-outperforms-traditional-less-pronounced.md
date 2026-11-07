---
type: claim
title: In the larger Tobii experiment with 8 participants, encoded features generally outperformed traditional features, though the performance gap was less pronounced than in the EyeLink study
description: In the larger Tobii experiment with 8 participants, encoded features generally outperformed traditional features, though the performance gap was less pronounced than in the EyeLink study
id: tobii-encoded-outperforms-traditional-less-pronounced
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: stanford-martinez-2025
    resource: "https://doi.org/10.2196/53928"
    title: "Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob. (2025). Discrimination of Radiologists' Experience Level Using Eye-Tracking Technology and Machine Learning: Case Study. JMIR Formative Research. https://doi.org/10.2196/53928"
    author: Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# In the larger Tobii experiment with 8 participants, encoded features generally outperformed traditional features, though the performance gap was less pronounced than in the EyeLink study

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Within the Tobii dataset (8 participants, 27 images each), encoded-data AUC ranged from 0.55 to 0.82 versus 0.51 to 0.76 for traditional data, with a less pronounced gap than in the EyeLink dataset. [→ Stanford Martinez 2025](#stanford-martinez-2025)

## Evidence

### Stanford Martinez 2025

Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob. (2025). Discrimination of Radiologists' Experience Level Using Eye-Tracking Technology and Machine Learning: Case Study. JMIR Formative Research. https://doi.org/10.2196/53928

`q2 · i?` · `associational · r1`

Second experiment using a Tobii 5L eye tracker with 8 participants (4 faculty averaging 12.75 years of experience, 4 trainees averaging 2.25 years), each scanning 27 images, analyzed with the same cross-validated classifiers. Mean and variance AUC values are printed; no standardized effect size is reported.

> "For example, the Tobii average (and variance) AUC scores for the encoded data type ranged from 0.55 (0.05) to 0.82 (0.04), while the traditional data type ranged from 0.51 (0.07) to 0.76 (0.05), and the EyeLink average (variance) AUC scores for the same data types ranged from 0.63 (0.07) to 1.0 (0.0) and from 0.52 (0.08) to 0.96 (0.01), respectively."

## Discussion


## Related Claims
- [In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522](eyelink-encoded-auc-above-098.md) — related
- [Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, accuracy, F1-score, sensitivity, and specificity](spatiotemporal-encoding-outperforms-traditional-gaze-features.md) — a broader claim this one bears on
- [The more experienced radiologist showed a more uniformly distributed visual search pattern across the chest x-ray, while the less-experienced radiologist focused on regions suspected of abnormality](faculty-uniform-versus-trainee-focused-search-pattern.md) — related
