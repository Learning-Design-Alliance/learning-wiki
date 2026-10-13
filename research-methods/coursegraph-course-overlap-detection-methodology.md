---
type: research-method
id: coursegraph-course-overlap-detection-methodology
title: CourseGraph course-overlap detection methodology
description: CourseGraph is a four-step methodology for automatically assessing whether an external course overlaps with courses in a home curriculum.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CourseGraph course-overlap detection methodology

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
CourseGraph is a four-step methodology for automatically assessing whether an external course overlaps with courses in a home curriculum. As the authors describe, "CourseGraph first extracts information such as course titles, descriptions, and learning outcomes from a course's webpage using a Large Language Model (LLM) and a tailored prompt." The extracted fields are embedded with sBERT, cosine similarities are computed between course pairs, and size-independent features (max, min, mean similarity, and fractions above 0.5, 0.6, 0.7) feed a 15-dimensional feature vector into a Random Forest classifier that outputs an overlap/no-overlap decision. Embedding each course component separately supports explainability of which components drive an overlap prediction.

## Accounts
<!-- How each source describes or uses the method -->
- **CourseGraph: an LLM-plus-sBERT-plus-Random-Forest pipeline for detecting overlap between university courses**: CourseGraph is a four-step methodology for automatically assessing whether an external course overlaps with courses in a home curriculum. As the authors describe, "CourseGraph first extracts information such as course titles, descriptions, and learning outcomes from a course's webpage using a Large Language Model (LLM) and a tailored prompt." The extracted fields are embedded with sBERT, cosine similarities are computed between course pairs, and size-independent features (max, min, mean similarity, and fractions above 0.5, 0.6, 0.7) feed a 15-dimensional feature vector into a Random Forest classifier that outputs an overlap/no-overlap decision. Embedding each course component separately supports explainability of which components drive an overlap prediction. (Arthur Nijdam et al. (2026))

### Claims

- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](../claims/rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) [+W]
- [CourseGraph's nearest-neighbor course mappings largely align with a program director's judgments on real Erasmus+ decisions, with errors traced to ignored pedagogical differences](../claims/coursegraph-mappings-align-with-program-director.md) [+W]
- [Component-level embeddings make CourseGraph interpretable: learning outcomes contributed most to an example overlap decision](../claims/coursegraph-component-level-interpretability.md) [+W]

## Related Research Methods
-

## Key Sources
- Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910
