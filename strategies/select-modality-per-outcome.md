---
type: strategy
id: select-modality-per-outcome
title: Select data modalities to match the learning outcome when applying multimodal learning analytics
description: "The article's implications section states that \"the findings highlight the importance of selecting appropriate data modalities for specific outcomes\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: conrad-borchers-2025
    resource: "https://github.com/conradborchers/collaboration-edm25"
    title: "Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. https://github.com/conradborchers/collaboration-edm25"
    author: Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel
---

# Select data modalities to match the learning outcome when applying multimodal learning analytics

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article's implications section states that "the findings highlight the importance of selecting appropriate data modalities for specific outcomes". Because log features predicted engagement and productivity while dialogue features indicated linguistic characteristics and conceptual understanding, educators and system designers should choose the modality—or fusion configuration—based on the outcome being assessed rather than assuming fusion always helps. The authors add that careful feature selection and tuning are essential given the mixed fusion results.

## Design Implications

### Context
#### Requirements
- Access to both synchronized system logs and dialogue transcripts from collaborative learning sessions
#### Constraints
- The authors caution that their mixed multimodal fusion results mean fusion requires careful feature selection and tuning; models are not deployment-ready and current utility might lie in offline teacher analytics

### Target Learners
- middle school students in K-12 AI education

### Target Learning Goals
- monitoring engagement and productivity during project-based learning
- identifying when students need scaffolding
- understanding students' AI concept mastery for targeted feedback

## Claims

- [Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count](../claims/ablation-without-phrase-count-features.md) [+W]
- [Dialogue features predict lexical density (content richness) of training phrases better than log features](../claims/dialogue-better-predicts-lexical-density.md) [+W]
- [Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation](../claims/fusion-gains-outcome-dependent.md) [+W]
- [System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development](../claims/logs-better-predict-training-phrase-count.md) [+W]

## Related Strategies

- [Use real-world multimodal datasets to predict student engagement and improve adaptive learning selection](real-world-multimodal-data-for-engagement-prediction-strategy.md)
- [Integrate cognitive profiling and task-specific modality selection into surgical simulation training](cognitive-profiling-modality-selection-strategy.md)

## Examples
-

## Key Sources
- Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. https://github.com/conradborchers/collaboration-edm25
