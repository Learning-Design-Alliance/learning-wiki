---
type: design
id: train-technologists-as-weak-label-annotators
title: Train technologists (rather than crowdsourcing untrained workers) to generate labeled body-imaging datasets for AI, positioning their output as weak labels for radiologist refinement or weakly supervised learning
description: The article argues that expert labeling is ideal but costly and not scalable, while crowdsourcing suits only tasks with well-defined geometry.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: suman-garima-2020
    resource: "https://doi.org/10.1007/s00261-020-02741-x"
    title: "Suman Garima, Panda Ananya, Korfiatis Panagiotis, Edwards Marie E., Garg Sushil, Blezek Daniel J., Chari Suresh T., Goenka Ajit H. (2020). Development of a volumetric pancreas segmentation CT dataset for AI applications through trained technologists: a study during the COVID 19 containment phase. Abdominal Radiology. https://doi.org/10.1007/s00261-020-02741-x"
    author: Suman Garima, Panda Ananya, Korfiatis Panagiotis, Edwards Marie E., Garg Sushil, Blezek Daniel J., Chari Suresh T., Goenka Ajit H
---

# Train technologists (rather than crowdsourcing untrained workers) to generate labeled body-imaging datasets for AI, positioning their output as weak labels for radiologist refinement or weakly supervised learning

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article argues that expert labeling is ideal but costly and not scalable, while crowdsourcing suits only tasks with well-defined geometry. It recommends instead that trained technologists "could increase the efficiency of image annotation projects by creating weak labels, which could be used for weakly supervised learning or could subsequently be improvised upon by radiologists", keeping data within institutional security firewalls and yielding a redeployable trained workforce.

## Design Implications

### Context
#### Requirements
- Investment in upfront training of technologists (curriculum, sessions, software workflow instructions)
- Cloud-based image annotation platforms with an intuitive interface, validated curriculums, and structured training modules, per the authors' closing recommendation
#### Constraints
- Technologists' labels may not be reasonable surrogates for radiologist segmentations; the article positions them as weak labels
- A manual approach to pancreas segmentation is cumbersome, inaccurate, and not scalable

### Target Learners
- Radiology technologists being upskilled for data-annotation roles

### Learning Goals
- Acquisition of fine organ-segmentation skill on cross-sectional imaging
- Sustained accurate performance on annotation tasks during clinical downtime

### Claims
- [Technologist Initial Training 62 Percent Accurate Segmentation](../claims/technologist-initial-training-62-percent-accurate-segmentation.md) [+M]
- [Supplementary Training No Significant Metric Change](../claims/supplementary-training-no-significant-metric-change.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Suman Garima, Panda Ananya, Korfiatis Panagiotis, Edwards Marie E., Garg Sushil, Blezek Daniel J., Chari Suresh T., Goenka Ajit H. (2020). Development of a volumetric pancreas segmentation CT dataset for AI applications through trained technologists: a study during the COVID 19 containment phase. Abdominal Radiology. https://doi.org/10.1007/s00261-020-02741-x
