---
type: element
id: singkt-dataset-note-level-singing
title: "singKT: an open dataset of note-level singing practice from Chinese classrooms"
description: The singKT dataset is an openly released corpus of singing interactions collected from Chinese primary and middle schools, distributed by the iTEC Lab at Huazhong University of Science and Technology.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: wei-2026
    resource: "https://doi.org/10.3389/fpsyg.2026.1905847"
    title: "Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847"
    author: Wei, Wang and Dong
---

# singKT: an open dataset of note-level singing practice from Chinese classrooms

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The singKT dataset is an openly released corpus of singing interactions collected from Chinese primary and middle schools, distributed by the iTEC Lab at Huazhong University of Science and Technology. It comprises "2,432 student–song interaction sequences contributed by the 1,074 distinct learners" and "2,458,825 individual pitched-note attempts", with 270 unique pitch identifiers and 2,587 score-position identifiers, an overall mean correctness of 0.7224, and sequence lengths from 34 to 38,387 attempts. The article uses it to estimate repetition curves, register effects and interpretable student models.

## Design Implications

### Context
#### Requirements
- Distributed as a single CSV file in which every five consecutive rows describe one student–song interaction sequence, with binary correctness flags emitted by the singing assessment engine.
#### Constraints
- The release provides no demographic information about participants, and the register analysis assumes pitch identifiers are ordered by pitch height, which the documentation does not explicitly confirm.

### Target Learners
- Chinese primary and middle school students practicing singing on a computer-assisted assessment platform

### Target Learning Goals
- Pitch-matching and note-level singing accuracy

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four model families, but lower AUC than IRT](../claims/bkt-highest-accuracy-lower-auc-than-irt.md) [+W]
- [Low-register pitches are sung more accurately than high-register pitches in Chinese classrooms, reproducing register compression at scale](../claims/register-compression-singing-accuracy-chinese-classrooms.md) [+W]
- [A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts](../claims/irt-outperforms-baselines-discrimination-not-accuracy.md) [+W]
- [Note-level singing correctness rises with practice repetition in a negatively accelerated curve, gaining about 7 percentage points over 30 repetitions](../claims/singing-accuracy-negatively-accurated-repetition-curve.md) [+W]
- [Latent singing ability varies widely across learners, with sequence-level theta estimates spanning −3.79 to 3.36 logits](../claims/wide-latent-ability-spread-singing-learners.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847
