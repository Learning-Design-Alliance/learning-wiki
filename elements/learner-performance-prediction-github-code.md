---
type: element
id: learner-performance-prediction-github-code
title: Released learner performance prediction code and public dataset links
description: The article releases its experimental code and links to the nine public benchmark datasets used in the comparison.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: theophile-gervet-2020
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
---

# Released learner performance prediction code and public dataset links

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The article releases its experimental code and links to the nine public benchmark datasets used in the comparison. The implementations include deep learning algorithms in PyTorch, the logistic regression implementation from scikit-learn, and the BKT+ implementation from Khajah et al. 2016 in C++; the authors state "Our code and links to public datasets we used are freely available on GitHub". This artifact supports replication of the cross-dataset comparison and ablation studies.

## Design Implications

### Context
#### Requirements
- Deep learning algorithms require the PyTorch implementation; logistic regression uses scikit-learn; BKT+ requires the C++ implementation from Khajah et al. 2016
#### Constraints
- Algorithms requiring timestamps (like DAS3H) were only applicable to the subset of datasets containing timestamp information

### Target Learners
- educational data mining researchers and learning engineers replicating learner performance model comparisons

### Target Learning Goals
- accurate prediction of learner correctness in intelligent tutoring systems

## Related Elements

- [EduData and EduKTM Open-Source Knowledge Tracing Libraries](edudata-and-eduktm-libraries.md)

## Examples
-

## Key Sources
- Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction
