---
type: claim
title: In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522
description: In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522
id: eyelink-encoded-auc-above-098
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
    kind: design
    rigour: 2
---

# In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the EyeLink dataset, the original encoded data type yielded the highest performance with AUC above 0.98 across all five classifiers, whereas the traditional data type yielded roughly 0.522 at worst (AlexNet). [→ Stanford Martinez 2025](#stanford-martinez-2025)

## Evidence

### Stanford Martinez 2025

Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob. (2025). Discrimination of Radiologists' Experience Level Using Eye-Tracking Technology and Machine Learning: Case Study. JMIR Formative Research. https://doi.org/10.2196/53928

`q2 · i?` · `design · r2`

Numerical classification study on the EyeLink dataset (2 participants, 110 trials) using stratified 10-fold cross-validation over Gaussian process, logistic regression, KNN, XGBoost, and an AlexNet-like classifier, with AUC tabulated in Table 2. Only AUC scores are printed; no standardized effect size is reported.

> "This table illustrates the original encoded data to possess the highest performance, with AUC scores consistently above 0.98 across all classifiers. However, usage of the traditional data yields roughly 0.522 at worst, as seen in the reported results for the AlexNet classifier."

## Discussion


## Related Claims
- [Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, accuracy, F1-score, sensitivity, and specificity](spatiotemporal-encoding-outperforms-traditional-gaze-features.md) — a broader claim this one bears on
- [In the larger Tobii experiment with 8 participants, encoded features generally outperformed traditional features, though the performance gap was less pronounced than in the EyeLink study](tobii-encoded-outperforms-traditional-less-pronounced.md) — related
- [The more experienced radiologist showed a more uniformly distributed visual search pattern across the chest x-ray, while the less-experienced radiologist focused on regions suspected of abnormality](faculty-uniform-versus-trainee-focused-search-pattern.md) — related
