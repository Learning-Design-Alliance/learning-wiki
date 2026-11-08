---
type: strategy
id: trained-rater-consensus-sessions-ai-ground-truth
title: Use validated global rating scales with trained, expert raters and consensus sessions when generating ground truth for surgical AI skill assessment
description: "The article recommends that, given the need for valid skill ratings in AI development and evaluation, surgical groups should use OSATS and M-GEARS — the most prevalent and most robotically evaluated tools — with \"trai..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: sirajudeen-n-2024
    resource: "https://doi.org/10.1007/s00464-024-11341-5"
    title: "Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5"
    author: Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K
---

# Use validated global rating scales with trained, expert raters and consensus sessions when generating ground truth for surgical AI skill assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (1 review, 1 associational), `q2`–`q3` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
The article recommends that, given the need for valid skill ratings in AI development and evaluation, surgical groups should use OSATS and M-GEARS — the most prevalent and most robotically evaluated tools — with "trained, expert, orientated raters who have consensus sessions to align scoring." Raters in this study went through training consensus sessions using JIGSAWS suturing videos to improve reliability before annotating the target dataset.

## Design Implications

### Context
#### Requirements
- Access to validated assessment tools (OSATS, M-GEARS) and time for rater training and consensus sessions
#### Constraints
- Most videos in this study were annotated by only one rater due to time constraints; the authors state errors should ideally be annotated by multiple trained, blinded, expert assessors

### Target Learners
- Surgical trainees and surgeons being assessed in robotic surgery

### Target Learning Goals
- Reliable, objective technical skill and error assessment to support automated feedback

## Claims

- [Blinded gesture-level annotation of real robotic suturing video achieves strong to very strong inter-rater reliability for OSATS, M-GEARS and OCHRA](../claims/ochra-osats-mgears-reliability-real-robotic-video.md) [+M]
- [OSATS and M-GEARS show very strong concurrent validity and both correlate moderately and inversely with OCHRA error counts in robotic suturing](../claims/osats-mgears-concurrent-validity-error-correlation.md) [+M]
- [Structured grading rubrics such as OSATS and GEARS are validated to reliably distinguish levels of surgical expertise and remain the standard approach to surgical skill assessment](../claims/structured-rubrics-standard-surgical-skill-assessment.md) [+M]
- [Skill and error scores did not differ across surgeon seniority groups, so construct validity was not established for the simpler suturing task](../claims/no-construct-validity-seniority-dvc-suturing.md) [~W]

## Related Strategies

- [Validate automated video analytics and reach metric consensus before widespread adoption in surgical training](validate-video-analytics-before-adoption.md)
- [Provide pre-assessment training to raters before video-based quality assessment](pre-assessment-rater-training-strategy.md)
- [Combine a validated global rating scale (GOALS) with a specific suture checklist for scored video assessment and individualized feedback](goals-plus-checklist-combined-assessment-strategy.md)
- [Validate educational videos with both expert judges and the target audience](validate-videos-with-experts-and-target-audience.md)
- [Adopt a modified GESEA-based scoring system for multidirectional suturing assessment](modified-gesea-scoring-multidirectional-suturing.md)

## Examples
-

## Key Sources
- Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5
