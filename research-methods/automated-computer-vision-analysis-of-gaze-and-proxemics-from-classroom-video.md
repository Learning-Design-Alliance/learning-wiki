---
type: research-method
id: automated-computer-vision-analysis-of-gaze-and-proxemics-from-classroom-video
title: Automated computer-vision analysis of gaze and proxemics from classroom video
description: The study adapted the Sharingan gaze-estimation framework (Tafasca et al., 2024), a pretrained transformer-based model reported with AUC 0.944, to derive joint attention and mutual gaze frame by frame from standard 2D video.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-18
---

# Automated computer-vision analysis of gaze and proxemics from classroom video

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 associational, 1 design), `q2`–`q3` · 1 of 2 report an effect size · 2 claims rest on one study

## Description
The study adapted the Sharingan gaze-estimation framework (Tafasca et al., 2024), a pretrained transformer-based model reported with AUC 0.944, to derive joint attention and mutual gaze frame by frame from standard 2D video. A separate pipeline combining YOLOv11 pose estimation, DeepOCSort tracking, and depth-based distance computation computed pairwise interpersonal distances, categorized via 33rd/66th percentile thresholds into close, neutral, and far levels. The authors present this as a nonintrusive, scalable methodological alternative to intrusive sensors, lab-only setups, and manual coding in authentic classrooms.

## Accounts
<!-- How each source describes or uses the method -->
- **Automated computer-vision pipeline for extracting gaze and proxemics from ordinary 2D classroom video**: The study adapted the Sharingan gaze-estimation framework (Tafasca et al., 2024), a pretrained transformer-based model reported with AUC 0.944, to derive joint attention and mutual gaze frame by frame from standard 2D video. A separate pipeline combining YOLOv11 pose estimation, DeepOCSort tracking, and depth-based distance computation computed pairwise interpersonal distances, categorized via 33rd/66th percentile thresholds into close, neutral, and far levels. The authors present this as a nonintrusive, scalable methodological alternative to intrusive sensors, lab-only setups, and manual coding in authentic classrooms. (Ridwan Whitehead · Andy Nguyen · Sanna Järvelä (2026))
- **Three-layer architecture for intelligent classroom engagement analysis**: The article proposes an organizing architecture for engagement analysis in authentic classrooms with three layers: "a data layer, a technology layer, and an application layer". The data layer collects video via front and rear wall cameras sampled at 3-second intervals; the technology layer runs multi-person body orientation estimation in real time; the application layer displays bounding boxes and orientation arrows for students and teachers. The framework was applied across regular, small-group discussion, and circular seminar configurations. (Chen Yuqing et al. (2025))

### Claims
- [Proxemic configuration significantly shifts the relational organization of regulation, from a visually anchored system when far to a strategy-oriented system when close](../claims/proxemic-configuration-rr1-relational-shift.md) [+W]
- [In authentic classroom videos, students' attention directions are almost consistent with their body orientations, allowing engagement to be inferred non-intrusively](../claims/body-orientation-indicates-classroom-attention.md) [+M]

## Related Research Methods

- [Multimodal analysis](multimodal-analysis.md)

## Key Sources
- Ridwan Whitehead · Andy Nguyen · Sanna Järvelä. (2026). How gaze and proxemics shape and signal shared regulatory processes during AI-supported collaborative learning. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-026-09478-7
- Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421
