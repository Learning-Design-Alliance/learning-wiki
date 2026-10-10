---
type: research-method
id: engagement-based-evaluation-framework-for-ai-tutors-relscore-and-succscore
title: Engagement-based evaluation framework for AI tutors (RelScore and SuccScore)
description: The framework extends AI tutor evaluation with a behavioral dimension grounded in student interaction data, complementing pedagogical assessment.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Engagement-based evaluation framework for AI tutors (RelScore and SuccScore)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework extends AI tutor evaluation with a behavioral dimension grounded in student interaction data, complementing pedagogical assessment. It quantifies "engagement qualityof tutor feedback by examiningwhetherandhowstudents used the AI tutor's feedback, conditioned on their subsequent code revisions". An LLM judge labels each feedback sentence for relevance (whether it influenced the student's code edit) and success (whether the suggested change was applied correctly), yielding RelScore, the fraction of feedback sentences students engage with, and SuccScore, the fraction of engaged feedback applied correctly.

## Accounts
<!-- How each source describes or uses the method -->
- **Engagement-based evaluation framework for AI tutors (RelScore and SuccScore)**: The framework extends AI tutor evaluation with a behavioral dimension grounded in student interaction data, complementing pedagogical assessment. It quantifies "engagement qualityof tutor feedback by examiningwhetherandhowstudents used the AI tutor's feedback, conditioned on their subsequent code revisions". An LLM judge labels each feedback sentence for relevance (whether it influenced the student's code edit) and success (whether the suggested change was applied correctly), yielding RelScore, the fraction of feedback sentences students engage with, and SuccScore, the fraction of engaged feedback applied correctly. (Rose Niousha et al. (2026))

### Claims
- [Engagement-based metrics are more robust predictors of students' perceived feedback helpfulness than pedagogical dimensions](../claims/engagement-metrics-predict-perceived-helpfulness.md) [+M]
- [MisconceptionTutor achieves substantially higher feedback relevance (RelScore) than BaselineTutor on every assignment](../claims/misconception-tutor-higher-relscore-all-assignments.md) [+M]

## Related Research Methods
-

## Key Sources
- Rose Niousha, Samantha Boatright Smith, Bita Akram, Peter Brusilovsky, Arto Hellas, Juho Leinonen, John DeNero, and Narges Norouzi. (2026). The Missing Evaluation Axis: What 10,000 Student Submissions Reveal About AI Tutor Effectiveness. arXiv preprint. https://arxiv.org/abs/2605.05648
