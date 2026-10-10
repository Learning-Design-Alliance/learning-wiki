---
type: design
id: bespoke-lecture-video-generation-pipeline
title: "Bespoke: a five-stage pipeline that regenerates a complete industry-personalized lecture video from a seed transcript"
description: Bespoke is a directed acyclic pipeline that takes a seed lecture transcript, a learner profile (healthcare, finance, energy, or generic), and a target duration, and compiles a new lecture video with slides, narration,...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: romain-puech-2026
    resource: "https://arxiv.org/abs/2609.26540"
    title: "Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas. (2026). Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale. arXiv preprint. https://arxiv.org/abs/2609.26540"
    author: Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas
---

# Bespoke: a five-stage pipeline that regenerates a complete industry-personalized lecture video from a seed transcript

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Bespoke is a directed acyclic pipeline that takes a seed lecture transcript, a learner profile (healthcare, finance, energy, or generic), and a target duration, and compiles a new lecture video with slides, narration, and charts. Its five stages write audience-specific learning objectives, plan the lecture around a retrieved domain paper, write narration, build slides and charts in parallel, and reveal slide elements as they are spoken. Generation used Claude Sonnet 4.6 with GPT-5.2 validating in a bounded refine loop, following backward design and Mayer's multimedia principles. The article describes it as a pipeline that "regenerates a complete lecture video for a stated professional audience from a seed transcript".

## Design Implications

### Context
#### Requirements
- A human instructor's seed transcript defining topic, scope, and the facts the new lecture may use
- A stated learner profile and target duration
- A bound of three refinement iterations to keep cost finite
#### Constraints
- All videos in the evaluation were generated without instructor intervention at generation time
- The videos have no talking-head instructor
- Mean API cost is about $0.22 per minute of video

### Target Learners
- working professionals in healthcare, finance, and energy seeking upskilling
- graduate analytics, machine learning, and optimization students

### Learning Goals
- industry-appropriate understanding of technical topics such as decision trees, at audience-calibrated depth and with domain-relevant examples

### Claims
- [Bespoke 87 Percent Mooc Comparable Quality](../claims/bespoke-87-percent-mooc-comparable-quality.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas. (2026). Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale. arXiv preprint. https://arxiv.org/abs/2609.26540
