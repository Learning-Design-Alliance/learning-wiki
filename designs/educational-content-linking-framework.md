---
type: design
id: educational-content-linking-framework
title: Educational content linking framework
description: "A framework in which learning contents scattered across different MOOC material types \"such as lecture videos, slides, discussions forums, or quizzes, are linked based on their conceptual relation\" and organized into..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: shang-wen-li-2021
    resource: "https://arxiv.org/abs/2012.15826"
    title: "Shang-Wen Li. (2021). Educational Content Linking for Enhancing Learning Need Remediation in MOOCs. arXiv preprint. https://arxiv.org/abs/2012.15826"
    author: Shang-Wen Li
---

# Educational content linking framework

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A framework in which learning contents scattered across different MOOC material types "such as lecture videos, slides, discussions forums, or quizzes, are linked based on their conceptual relation" and organized into a tree presented to learners alongside the content. One material type forms the trunk (carrying the syllabus) and the rest become leaves corresponding to related learning objects. The framework aims to provide guidance for navigating content so learners can resolve confusion and tailor their learning path to their background. Learning objects need only convey concepts self-containedly; an object may be a textbook section, a discussion thread, or a video vignette.

## Design Implications

### Context
#### Requirements
- A linking annotation (conceptual relations among learning objects), produced by human annotators or a machine learning method
- Learning objects that convey concepts in a self-contained way so learners can understand
- A trunk material type used to extract the syllabus
#### Constraints
- Conceptual relation is the only property that is inferred, which the authors argue keeps the framework simple enough for state-of-the-art machine learning and HLTs

### Target Learners
- MOOC learners with heterogeneous backgrounds
- novice learners

### Learning Goals
- self-regulated learning
- efficient content navigation to resolve confusion

### Claims
- [Content Linking Interface Faster Search Retention](../claims/content-linking-interface-faster-search-retention.md) [+M]
- Automatic Linking Smaller But Real Gains [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Shang-Wen Li. (2021). Educational Content Linking for Enhancing Learning Need Remediation in MOOCs. arXiv preprint. https://arxiv.org/abs/2012.15826
