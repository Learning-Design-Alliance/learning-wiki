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
> **Evidence** · no claims cited

## Description
CourseGraph is a four-step methodology for automatically assessing whether an external course overlaps with courses in a home curriculum. As the authors describe, "CourseGraph first extracts information such as course titles, descriptions, and learning outcomes from a course's webpage using a Large Language Model (LLM) and a tailored prompt." The extracted fields are embedded with sBERT, cosine similarities are computed between course pairs, and size-independent features (max, min, mean similarity, and fractions above 0.5, 0.6, 0.7) feed a 15-dimensional feature vector into a Random Forest classifier that outputs an overlap/no-overlap decision. Embedding each course component separately supports explainability of which components drive an overlap prediction.

## Accounts
<!-- How each source describes or uses the method -->
- **CourseGraph: an LLM-plus-sBERT-plus-Random-Forest pipeline for detecting overlap between university courses**: CourseGraph is a four-step methodology for automatically assessing whether an external course overlaps with courses in a home curriculum. As the authors describe, "CourseGraph first extracts information such as course titles, descriptions, and learning outcomes from a course's webpage using a Large Language Model (LLM) and a tailored prompt." The extracted fields are embedded with sBERT, cosine similarities are computed between course pairs, and size-independent features (max, min, mean similarity, and fractions above 0.5, 0.6, 0.7) feed a 15-dimensional feature vector into a Random Forest classifier that outputs an overlap/no-overlap decision. Embedding each course component separately supports explainability of which components drive an overlap prediction. (Arthur Nijdam et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910
