---
type: claim
title: Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores
description: Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores
id: deep-learning-high-accuracy-skill-prediction-jigsaws
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-11-06
recheck_by: 2028
sources:
  - id: laughlin-jacob-l-bs-2025
    resource: "https://doi.org/10.14797/mdcvj.1667"
    title: "Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD. (2025). Technical Skills Assessment in Robotic Surgery: A Review of Recent Methods. Methodist DeBakey Cardiovascular Journal. https://doi.org/10.14797/mdcvj.1667"
    author: "Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD"
    q: 2
    i: "?"
    kind: review
    rigour: 2
  - id: laughlin-jacob-l-bs-2025-2
    resource: "https://doi.org/10.14797/mdcvj.1667"
    title: "Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD. (2025). Technical Skills Assessment in Robotic Surgery: A Review of Recent Methods. Methodist DeBakey Cardiovascular Journal. https://doi.org/10.14797/mdcvj.1667"
    author: "Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-11-06 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` CNN-based models achieved 100% accuracy on suturing and needle passing tasks in JIGSAWS, and video-based 3D CNN approaches achieved at least 95% accuracy in all three tasks. [→ Laughlin Jacob L. BS 2025](#laughlin-jacob-l-bs-2025)
`q2 i?` Video-only assessment using computer vision enables skill level prediction, with tool tracking from robotic thoracic surgery videos achieving 83% accuracy against OSATS and GEARS thresholds. [→ Laughlin Jacob L. BS 2025 (2)](#laughlin-jacob-l-bs-2025-2)

## Evidence

### Laughlin Jacob L. BS 2025

Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD. (2025). Technical Skills Assessment in Robotic Surgery: A Review of Recent Methods. Methodist DeBakey Cardiovascular Journal. https://doi.org/10.14797/mdcvj.1667

`q2 · i?` · `review · r2`

The review reports deep learning results on JIGSAWS: Fawaz et al. achieved "100% accuracy on suturing and needle passing tasks", and Benmansour et al. showed Spearman correlations of ρ ≥ 0.6 between predicted and OSATS scores; Funke et al. achieved ≥ 95% accuracy in all three tasks.

> "Fawaz et al. achieved 100% accuracy on suturing and needle passing tasks in the JIGSAWS dataset, while Benmansour et al. also showed Spearman correlation values with moderate-to-high correlation (ρ ≥ 0.6) when comparing predicted scores to OSATS scores."

### Laughlin Jacob L. BS 2025 (2)

Laughlin Jacob L. BS, Johnson Lianne R. MS, Ghanekar Bhargav MS, O'Malley Marcia K. PhD. (2025). Technical Skills Assessment in Robotic Surgery: A Review of Recent Methods. Methodist DeBakey Cardiovascular Journal. https://doi.org/10.14797/mdcvj.1667

`q2 · i?` · `design · r2`

The review reports a video-only assessment study: "surgical tool tracking from robotic thoracic surgery videos enabled skill level prediction using OSATS and GEARS thresholds with 83% accuracy", avoiding proprietary kinematic data restrictions.

> "Lee et al. demonstrated that surgical tool tracking from robotic thoracic surgery videos enabled skill level prediction using OSATS and GEARS thresholds with 83% accuracy."

## Discussion


## Related Claims
- [In the narrative synthesis, deep learning models classify surgeon skill levels from kinematic data with accuracy up to 95.4%](deep-learning-skill-classification-up-to-95-percent.md) — related
- [A Leap Motion Controller-based system discriminated expert from novice surgical knot-tying performance with 100% accuracy, supporting construct validity for objective dexterity assessment](lmc-construct-validity-dexterity-assessment.md) — related
- [Structured grading rubrics such as OSATS and GEARS are validated to reliably distinguish levels of surgical expertise and remain the standard approach to surgical skill assessment](structured-rubrics-standard-surgical-skill-assessment.md) — related
