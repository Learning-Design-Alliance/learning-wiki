---
type: element
id: kdd-cup-2010-bridge-to-algebra-dataset
title: KDD Cup 2010 Bridge to Algebra dataset and the hmmsclbl fitting tool
description: The KDD Cup 2010 Bridge to Algebra dataset, donated by Carnegie Learning and downloadable from the PSLC DataShop, is the validation corpus for Spectral BKT.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: falakmasir-2015
    resource: "http://pslcdatashop.web.cmu.edu/KDDCup"
    title: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup"
    author: "Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K"
---

# KDD Cup 2010 Bridge to Algebra dataset and the hmmsclbl fitting tool

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The KDD Cup 2010 Bridge to Algebra dataset, donated by Carnegie Learning and downloadable from the PSLC DataShop, is the validation corpus for Spectral BKT. It "contains about 20 million transactions belonging to over 6 thousand students working on nearly 150 sections of mathematics curriculum practicing around 1650 skills", including curriculum and problem context, cognitive skill labels, timing, first-attempt correctness, and assistance information. The authors describe it as the largest freely available collection of learner data. Models were fit and cross-validated with hmmsclbl, a C/C++ utility available at the standard-bkt GitHub repository.

## Design Implications

### Context
#### Requirements
- Skills are treated as unique within each curriculum section, with null skills treated as a special skill
#### Constraints
- Only the Bridge to Algebra dataset of the two available KDD Cup 2010 datasets was used

### Target Learners
- middle-grade mathematics students using Carnegie Learning's Cognitive Tutor

### Target Learning Goals
- predicting student correctness on math problem steps and modeling skill mastery

## Related Elements
- 

## Examples
-

## Key Sources
- Falakmasir, M., Yudelson, M., Ritter, S., & Koedinger, K. (2015). Spectral Bayesian Knowledge Tracing. Proceedings of the 8th International Conference on Educational Data Mining. http://pslcdatashop.web.cmu.edu/KDDCup
