---
type: strategy
id: student-disjoint-dataset-split-strategy
title: Split skill-assessment video datasets by student identity so pre- and post-training videos of the same student stay in one subset
description: "The article proposes a concrete data-splitting practice for skill assessment benchmarks: use 70% training, 15% validation, and 15% test data, keeping \"pre- and post-training videos of the same student, identified by t..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: hoffmann-hanna-2024
    resource: "https://doi.org/10.1007/s11548-024-03093-3"
    title: "Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3"
    author: Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus
---

# Split skill-assessment video datasets by student identity so pre- and post-training videos of the same student stay in one subset

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a concrete data-splitting practice for skill assessment benchmarks: use 70% training, 15% validation, and 15% test data, keeping "pre- and post-training videos of the same student, identified by the unique student identifier" within one subset. This ensures the model generalizes across different students' suturing styles and techniques, with disjoint splits and each video included only once.

## Design Implications

### Context
#### Requirements
- A unique student identifier linking each video to its source student
- Disjoint splits with each video included only once
#### Constraints
- Class balance within splits is approximate: beginner and proficient classes each comprised 30–40% of the data and the intermediate class approximately 20–30%

### Target Learners
- researchers building surgical skill assessment models

### Target Learning Goals
- generalizable automated skill classification across learners

## Claims

- [Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models](../claims/shorter-snippet-lengths-aid-skill-assessment.md) [+W]
- [Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters](../claims/video-models-three-level-open-suturing-skill-classification.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3
