---
type: claim
title: "Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, accuracy, F1-score, sensitivity, and specificity"
description: "Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, acc..."
id: spatiotemporal-encoding-outperforms-traditional-gaze-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-11-07
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

# Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, accuracy, F1-score, sensitivity, and specificity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-11-07 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across both EyeLink and Tobii datasets, classifiers using the proposed encoded features showed performance gains over traditional features of 6.9% (AUC), 7.11% (accuracy), 9.14% (F1-score), 9.59% (sensitivity), and 5.61% (specificity). [→ Stanford Martinez 2025](#stanford-martinez-2025)

## Evidence

### Stanford Martinez 2025

Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob. (2025). Discrimination of Radiologists' Experience Level Using Eye-Tracking Technology and Machine Learning: Case Study. JMIR Formative Research. https://doi.org/10.2196/53928

`q2 · i?` · `associational · r1`

The authors' principal-findings analysis aggregates classification results from the EyeLink (2 participants, 110 trials) and Tobii (8 participants, 216 trials) experiments, reporting "performance gains" of 6.9% (AUC) through 5.61% (specificity) for encoded versus traditional features. Gains are reported as percentages, with no standardized effect size.

> "Using the encoding approach allows classifiers to better distinguish between participants in terms of experience level, which highlights performance gains (when compared with using traditional features for discrimination) of 6.9%, 7.11%, 9.14%, 9.59%, and 5.61% for AUC, accuracy, F1-score, sensitivity, and specificity, respectively, aggregated across both EyeLink and Tobii datasets in Table 3."

## Discussion


## Related Claims
- [In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522](eyelink-encoded-auc-above-098.md) — a narrower finding that bears on this claim
- [In the larger Tobii experiment with 8 participants, encoded features generally outperformed traditional features, though the performance gap was less pronounced than in the EyeLink study](tobii-encoded-outperforms-traditional-less-pronounced.md) — a narrower finding that bears on this claim
- [The more experienced radiologist showed a more uniformly distributed visual search pattern across the chest x-ray, while the less-experienced radiologist focused on regions suspected of abnormality](faculty-uniform-versus-trainee-focused-search-pattern.md) — related
