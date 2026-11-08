---
type: product
id: classroom-interaction-detection-and-recognition-cidr-system
title: Classroom Interaction Detection and Recognition (CIDR) system
description: An open-source audiovisual processing pipeline developed by Gonzalez Villasanti et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
---

# Classroom Interaction Detection and Recognition (CIDR) system

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An open-source audiovisual processing pipeline developed by Gonzalez Villasanti et al. for automatically transcribing and classifying preschool children's exposure to adult-directed, peer-directed, and non-child-directed speech.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CIDR system for automatic detection and recognition of interactions and child-directed speech in preschool classrooms**: The Classroom Interaction Detection and Recognition (CIDR) system is an open-source pipeline that automatically transcribes and codes child-directed speech experienced by individual preschool children. It comprises four components: "scene parsing and featurization module, feature extraction module, interaction detector, and mappings to interaction and CDS measures". Cloud services (Amazon Rekognition and Transcribe) supply audiovisual features, which feed bi-directional LSTM detectors whose predicted interaction trajectories are used to label utterances as adult-CDS, peer-CDS, or non-CDS. Matlab and Python code is released at a public repository and validation and test data at OSF. (Gonzalez Villasanti et al. (2020))

### Claims
- [A BILSTM classifier using facial features and speech activity detects preschool children's interactions with adults with 81.1% accuracy under leave-one-subject-out validation](../claims/bilstm-facial-features-detect-adult-interactions.md) [+M]
- [Ordinary least products calibration of ASR output lowers error in CDS measures, with adult word counts comparable to LENA-level performance](../claims/olp-calibration-cds-measures.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511
