---
type: research-method
id: quantitative-motion-capture-and-eye-tracking-analysis-of-medical-skill-proficiency
title: Quantitative motion-capture and eye-tracking analysis of medical skill proficiency
description: "The article frames an explanatory approach in which \"motion measurement using motion capture and gaze measurement using an eye-tracking device were combined\" to quantify differences in body movement and gaze by skill level."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
---

# Quantitative motion-capture and eye-tracking analysis of medical skill proficiency

> **Research Method** · [All research methods](index.md)
> **Evidence** · 8 claims (8 for) · 3 studies (3 associational), `q2`–`q3` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
The article frames an explanatory approach in which "motion measurement using motion capture and gaze measurement using an eye-tracking device were combined" to quantify differences in body movement and gaze by skill level. This engineering perspective visualizes physical movements objectively, addressing the limitation that biosignal analysis captures only physiological responses after the action, and supports efficient skill acquisition based on objective data.

## Accounts
<!-- How each source describes or uses the method -->
- **Quantitative motion-capture and eye-tracking analysis as an engineering approach to medical skill proficiency**: The article frames an explanatory approach in which "motion measurement using motion capture and gaze measurement using an eye-tracking device were combined" to quantify differences in body movement and gaze by skill level. This engineering perspective visualizes physical movements objectively, addressing the limitation that biosignal analysis captures only physiological responses after the action, and supports efficient skill acquisition based on objective data. (Yasuda Yukinori et al. (2026))
- **CV-DL (Mask R-CNN) pipeline for automatic AOI detection and eye-tracking metric extraction in laparoscopic box training**: A computer vision-deep learning pipeline built on Mask R-CNN automatically detects areas of interest (objects and graspers) in eye-tracking recordings of the peg transfer task, then matches fixation points to AOI masks to compute fixation rates and tool speed. The model achieved "98.5% precision in classifying AOIs" and "74.8% precision in generating masks around the predicted object," with Cohen's kappa exceeding 0.8 against manual frame-by-frame annotation across both trainer types. It enables AOI-dependent metrics (feedback and feedforward fixation rates) in dynamic training environments where AOI positions continuously shift. (Khanfar Aseel F. et al. (2025))
- **Spatiotemporal discretized vector encoding of fixation data for radiologist classification**: A feature-encoding method that maps eye fixations on a chest x-ray onto a Cartesian grid and into temporal bins: "Fixations are split into temporal bins, preserving the sequence of visual inspection." Fixations are counted within square grid subdivisions for each temporal segment, and the grids are flattened into a single vector of size 1-by-(x×x×t) that captures both where and when fixations occurred. The encoded vectors serve as feature input for machine-learning classifiers and were the basis for the study's improved experience-level discrimination. (Stanford Martinez et al. (2025))

### Claims
- [Gaze-distance differences during tube insertion are not significant with either laryngoscope type](../claims/tube-insertion-phase-no-gaze-difference-either-device.md) [+W]
- [With a direct laryngoscope, experts direct their gaze farther than novices during the laryngoscope insertion phase](../claims/direct-laryngoscope-experts-gaze-farther-laryngoscope-insertion.md) [+W]
- [With a direct laryngoscope, experts maintain greater head-to-mouth distance than novices](../claims/direct-laryngoscope-experts-greater-head-distance.md) [+W]
- [No significant gaze-distance difference between experts and novices when using a video laryngoscope](../claims/video-laryngoscope-no-gaze-distance-difference.md) [+W]
- [AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training](../claims/aoi-metrics-classify-novice-skill-levels-early-training.md) [+M]
- [Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors](../claims/random-forest-predicts-visual-behavior-levels.md) [+M]
- [Machine-learning classifiers using spatiotemporal encoded eye-fixation features outperform those using traditional gaze features in discriminating radiologists' experience levels, with aggregated gains across AUC, accuracy, F1-score, sensitivity, and specificity](../claims/spatiotemporal-encoding-outperforms-traditional-gaze-features.md) [+M]
- [In the EyeLink experiment, classifiers consuming the original encoded fixation data achieved AUC scores consistently above 0.98 across all classifiers, while traditional features performed as low as roughly 0.522](../claims/eyelink-encoded-auc-above-098.md) [+M]

## Related Research Methods

- [Time-course and mixed-effects analysis of educational eye-tracking data](time-course-and-mixed-effects-analysis-of-educational-eye-tracking-data.md)
- [Multiagent first-person perspective analysis (FPA)](multiagent-first-person-perspective-analysis-fpa.md)
- [Multimodal analysis](multimodal-analysis.md)
- [Body-to-Body Coupling (BtBC) via Motion Energy Analysis](body-to-body-coupling-btbc-via-motion-energy-analysis.md)
- [Eye-tracking research paradigm for studying professional vision and teacher expertise](eye-tracking-research-paradigm-for-studying-professional-vision-and-teacher-expertise.md)
- [Mobile eye-tracking methodology for capturing joint visual attention in co-located groups](mobile-eye-tracking-methodology-for-capturing-joint-visual-attention-in-co-located-groups.md)

## Key Sources
- Yasuda Yukinori, Takehara Shoichiro, Inoue Soichiro. (2026). Quantitative analysis of gaze and body movement differences by proficiency in direct and video laryngoscope intubation. Scientific Reports. https://doi.org/10.1038/s41598-026-44432-5
- Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x
- Stanford Martinez, Carolina Ramirez-Tamayo, Syed Hasib Akhter Faruqui, Kal Clark, Adel Alaeddini, Nicholas Czarnek, Aarushi Aggarwal, Sahra Emamzadeh, Jeffrey R Mock, Edward J Golob. (2025). Discrimination of Radiologists' Experience Level Using Eye-Tracking Technology and Machine Learning: Case Study. JMIR Formative Research. https://doi.org/10.2196/53928
