---
type: claim
title: Glove-derived force features could not distinguish clinicians by seniority but showed modest ability to classify perceived task difficulty
description: Glove-derived force features could not distinguish clinicians by seniority but showed modest ability to classify perceived task difficulty
id: glove-features-seniority-null-difficulty-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: parris-dawn-2025
    resource: "https://doi.org/10.1111/1471-0528.70107"
    title: "Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios. (2025). Characterising Forces Applied During the Simulated Management of Impacted Fetal Head: Pre‐Clinical Methods Study. BJOG: An International Journal of Obstetrics and Gynaecology. https://doi.org/10.1111/1471-0528.70107"
    author: Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: parris-dawn-2025-2
    resource: "https://doi.org/10.1111/1471-0528.70107"
    title: "Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios. (2025). Characterising Forces Applied During the Simulated Management of Impacted Fetal Head: Pre‐Clinical Methods Study. BJOG: An International Journal of Obstetrics and Gynaecology. https://doi.org/10.1111/1471-0528.70107"
    author: Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Glove-derived force features could not distinguish clinicians by seniority but showed modest ability to classify perceived task difficulty

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Quantitative features and basic machine learning models were unable to distinguish clinicians based on seniority. [→ Parris Dawn 2025](#parris-dawn-2025)
`q2 i?` The same features showed modest predictive ability for classifying subjective task difficulty, with ROC AUCs of 0.82 (logistic regression) and 0.91 (random forest). [→ Parris Dawn 2025 (2)](#parris-dawn-2025-2)

## Evidence

### Parris Dawn 2025

Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios. (2025). Characterising Forces Applied During the Simulated Management of Impacted Fetal Head: Pre‐Clinical Methods Study. BJOG: An International Journal of Obstetrics and Gynaecology. https://doi.org/10.1111/1471-0528.70107

`q2 · i?` · `design · r2`

Secondary machine-learning analysis (Appendix S5, Figure S28) of the 13-participant sensor data: PCA stratified by seniority and perceived difficulty; the models were "unable to distinguish clinicians based on seniority". The authors call perceived task difficulty a key confounder for future motor-skill studies.

> "Furthermore, using quantitative features extracted from the calibrated sensor output time series and basic machine learning models, we were unable to distinguish clinicians based on seniority, and demonstrated a modest predictive ability for classifying the subjective experience of task difficulty."

### Parris Dawn 2025 (2)

Parris Dawn, Xue Yang, Navaseelan Thurga, Salvadores Fernandez Carmen, Javidan Maryam, Gupta Rohit, Salaris Nikolaos, Chen Jeremy, Tiwari Manish K., Siassakos Dimitrios. (2025). Characterising Forces Applied During the Simulated Management of Impacted Fetal Head: Pre‐Clinical Methods Study. BJOG: An International Journal of Obstetrics and Gynaecology. https://doi.org/10.1111/1471-0528.70107

`q2 · i?` · `design · r2`

Figure S29 caption reports ROC curves for logistic regression and random forest models evaluated with leave-one-out cross-validation and bootstrapping, distinguishing Hard versus Easy perceived-difficulty classes; the random forest AUC of 0.91 exceeded the logistic regression AUC of 0.82.

> "The classifiers yielded an AUC ROC of 0.82 and 0.91 for the Logistic Regression and Random Forest models, respectively."

## Discussion


## Related Claims
- [During simulated fetal head disimpaction, fingertip sensors record the highest maximum forces with low variability, indicating consistent use of fingertips across obstetricians](fingertips-deliver-highest-consistent-disimpaction-force.md) — related
- [3D-printed pediatric chest model with embedded force sensors distinguished skill levels where a conventional box trainer did not](takazawa-chest-model-skill-differentiation.md) — reports the opposite
- [Sensor-based force measurement discriminates skill levels, with experts suturing faster and with lower applied force than novices](force-sensing-discriminates-surgical-skill.md) — reports the opposite
- [In neonatal minimally invasive surgery, operative performance is shaped more by recency and depth of MIS-focused training than by surgeon seniority](mis-performance-shaped-by-training-recency-not-seniority.md) — related
