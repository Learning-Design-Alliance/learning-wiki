---
type: strategy
id: cohort-overview-to-individual-drilldown-workflow
title: "Instructor analysis workflow: filter anomalous COIs at cohort level, then drill down to subgroups and individual learning paths"
description: COIVis operationalizes a concept-driven diagnostic workflow in two moves.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zhiguang-zhou-2025
    resource: "https://arxiv.org/abs/2512.06834"
    title: "Zhiguang Zhou, Ruiqi Yu, Yuming Ma, Hao Ni, Guojun Li, Li Ye, Xiaoying Wang, Yize Li, Yigang Wang, and Yong Wang. (2025). COIVis: Eye-tracking-based Visual Exploration of Concept Learning in MOOC Videos. https://arxiv.org/abs/2512.06834"
    author: Zhiguang Zhou, Ruiqi Yu, Yuming Ma, Hao Ni, Guojun Li, Li Ye, Xiaoying Wang, Yize Li, Yigang Wang, and Yong Wang
---

# Instructor analysis workflow: filter anomalous COIs at cohort level, then drill down to subgroups and individual learning paths

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
COIVis operationalizes a concept-driven diagnostic workflow in two moves. First, instructors use range controls in the Feature Panel to filter COIs with, for example, "consistently high Cognitive Load or large variance in Attention," highlighting problematic concepts and their co-occurring content types. Second, analysis shifts from which concepts are problematic to how problems manifest in different learners: the Projection View supports selecting subgroups with specific patterns, and single-learner mode focuses all views on one learner's COI sequence, gaze traces, and deviations from the class distribution.

## Design Implications

### Context
#### Requirements
- A preprocessed COI dataset with the five learner-state features computed per learner and per COI
#### Constraints
- Requires eye-tracking data collected in instrumented viewing sessions; the workflow is demonstrated within the COIVis system

### Target Learners
- Instructors of MOOC or online video courses

### Target Learning Goals
- Locating problematic concepts and diagnosing individual learners' concept-level difficulties for timely instructional adjustment

### Affordances
- Coivis Visual Analytics System

## Claims

- [Two case studies and user-feedback interviews indicate COIVis provides instructors with insights into the consistency and anomalies of learners' learning patterns in MOOC videos](../claims/coivis-case-studies-instructor-insight-learning-patterns.md) [+W]
- [Semi-structured interviews with eight instructors reveal an urgent need for timely, fine-grained feedback on learner states in online teaching, which coarse indicators like grades cannot supply](../claims/instructor-interviews-urgent-need-fine-grained-feedback.md) [+W]
- [A systematic review of 67 papers indicates current online learning analytics remains at a macro, coarse-grained level that cannot pinpoint concept-level comprehension barriers](../claims/online-learning-analytics-macro-coarse-grained-limitation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zhiguang Zhou, Ruiqi Yu, Yuming Ma, Hao Ni, Guojun Li, Li Ye, Xiaoying Wang, Yize Li, Yigang Wang, and Yong Wang. (2025). COIVis: Eye-tracking-based Visual Exploration of Concept Learning in MOOC Videos. https://arxiv.org/abs/2512.06834
