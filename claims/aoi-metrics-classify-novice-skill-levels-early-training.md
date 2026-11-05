---
type: claim
title: AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training
description: AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training
id: aoi-metrics-classify-novice-skill-levels-early-training
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: khanfar-aseel-f-2025
    resource: "https://doi.org/10.1007/s00464-025-12369-x"
    title: "Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x"
    author: Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: khanfar-aseel-f-2025-2
    resource: "https://doi.org/10.1007/s00464-025-12369-x"
    title: "Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x"
    author: Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` K-means++ clustering of AOI-dependent and motion metrics grouped 18 novices into three clusters that mapped to two skill levels (High, Mid-Low) based on completion-time differences. [→ Khanfar Aseel F. 2025](#khanfar-aseel-f-2025)
`q2 i?` All extracted metrics differed significantly across visual behavior levels (p < 0.05). [→ Khanfar Aseel F. 2025 (2)](#khanfar-aseel-f-2025-2)

## Evidence

### Khanfar Aseel F. 2025

Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x

`q2 · i?` · `associational · r1`

Clustering analysis of 18 novices (medical students and residents) performing the FLS peg transfer task using k-means++ on CV-DL-extracted metrics. The elbow method identified three clusters (N = 5, 14, 5), later mapped to "two skill levels" via completion-time differences.

> "Based on the elbow method [72] three clusters were determined by plotting the within-cluster sum of squares (WCSS) against the number of clusters, see Fig. 7. Participants were classified as follows: Cluster 1 (N = 5), Cluster 2 (N = 14), and Cluster 3 (N = 5)."

### Khanfar Aseel F. 2025 (2)

Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x

`q2 · i?` · `associational · r1`

Six one-way ANOVAs with Tukey post-hoc comparisons tested the three clusters across all AOI-dependent and motion metrics extracted by the Mask R-CNN model; all showed statistically significant differences between visual behavior levels (p < 0.05), shown in box plots in Fig. 10.

> "There was a statistically significant difference between different visual behavior levels across all extracted metrics (p < 0.05), see Fig. 10."

## Discussion


## Related Claims
- [More-skilled novices fixate more on objects and less on tools, with slower tool speed, than less-skilled novices](skilled-novices-object-fixation-pattern.md) — a narrower finding that bears on this claim
- [Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors](random-forest-predicts-visual-behavior-levels.md) — related
- [Cognitive and behavioral metrics via EEG and eye-tracking with machine learning predicted surgical training outcomes with 72.5% accuracy](eeg-eye-metrics-ml-predict-training-outcomes.md) — a broader claim this one bears on
- [Novices' visual attention did not differ between pediatric and adult box trainers](no-visual-attention-difference-pediatric-adult-trainers.md) — related
- [Fixation on not-moving objects was lower for more-skilled novices, contradicting the expected looking-ahead pattern](not-moving-object-fixation-contradicts-hypothesis.md) — related
