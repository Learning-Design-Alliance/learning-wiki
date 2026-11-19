---
type: claim
title: EEG features classify which virtual classroom design a participant is experiencing significantly above scrambled-data chance levels
description: EEG features classify which virtual classroom design a participant is experiencing significantly above scrambled-data chance levels
id: eeg-classifies-virtual-classroom-design-conditions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: jesus-g-cruz-garza-2021
    resource: "https://doi.org/10.48550/arXiv.2102.03629"
    title: "Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari. (2021). EEG-based Investigation of the Impact of Classroom Design on Cognitive Performance of Students. [doi:10.48550/arXiv.2102.03629](https://doi.org/10.48550/arXiv.2102.03629)"
    author: Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jesus-g-cruz-garza-2021-2
    resource: "https://doi.org/10.48550/arXiv.2102.03629"
    title: "Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari. (2021). EEG-based Investigation of the Impact of Classroom Design on Cognitive Performance of Students. [doi:10.48550/arXiv.2102.03629](https://doi.org/10.48550/arXiv.2102.03629)"
    author: Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# EEG features classify which virtual classroom design a participant is experiencing significantly above scrambled-data chance levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A k-SVM classifier trained on frequency band-power and connectivity EEG features distinguished classroom design conditions from unseen participants' data with test-set accuracies significantly higher than scrambled-data baselines. [→ Jesus G. Cruz-Garza 2021](#jesus-g-cruz-garza-2021)

## Evidence

### Jesus G. Cruz-Garza 2021

Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari. (2021). EEG-based Investigation of the Impact of Classroom Design on Cognitive Performance of Students. [doi:10.48550/arXiv.2102.03629](https://doi.org/10.48550/arXiv.2102.03629)

`q2 · i?` · `causal · r2`

Leave-one-participant-out machine-learning analysis (k-SVM, polynomial degree 2; training n=22, test n=1, 23 iterations) of band-power and PDC connectivity features from 57 scalp electrodes during five cognitive tests in four VR classrooms. The article reports "consistent changes in the participants' EEG data" with reported test-set accuracies of 51.5%-61.3%.

> "The classification results show that the different classroom design conditions were associated with consistent changes in the participants' EEG data, and that a classification model could be built with the predictive power to identify which design condition a new participant is experiencing."

### Jesus G. Cruz-Garza 2021 (2)

Jesus G. Cruz-Garza, Michael Darfler, James D. Rounds, Elita Gao, Saleh Kalantari. (2021). EEG-based Investigation of the Impact of Classroom Design on Cognitive Performance of Students. [doi:10.48550/arXiv.2102.03629](https://doi.org/10.48550/arXiv.2102.03629)

`q2 · i?` · `causal · r2`

The same analysis evaluated significance of classification against class-label scrambled EEG control data using Kruskal-Wallis tests with Bonferroni correction; five of the class comparisons reached significance above chance.

> "Statistical significance was evaluated between the classification accuracy in the test set and in the scrambled data with a Kruskal-Wallis test at a significance threshold of p < 0.003 and p < 0.0006"

## Discussion


## Related Claims
- [EEG classification of classroom design conditions is robust only during short-term memory encoding tasks, strongest in the Visual Memory Test](eeg-design-classification-limited-to-memory-tasks.md) — a narrower finding that bears on this claim
- [Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%](eeg-stage-classification-over-80.md) — related
- [Isolated changes in classroom window placement and room width in a virtual classroom produce no significant differences in cognitive test performance](no-behavioral-differences-vr-classroom-window-room-width.md) — related
