---
type: research-method
id: computational-grounded-theory
title: Computational grounded theory
description: "Computational grounded theory integrates qualitative research with computational techniques to analyze large datasets systematically for theory development, addressing grounded theory's subjective interpretation and replication difficulties."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Computational grounded theory

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 associational, 1 qualitative), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
Computational grounded theory integrates qualitative research with computational techniques to analyze large datasets systematically for theory development, addressing grounded theory's subjective interpretation and replication difficulties. The article describes it as outlining "a three-step process to guide researchers in rubric design and application": pattern detection (unsupervised ML converts text into interpretable, data-driven categories), pattern refinement (human experts interpret and refine the data-driven categories via thematic content analysis, merging or adding categories), and pattern confirmation (computational methods such as supervised ML test reliability and generalizability). This study examines the validity of the first two steps.

## Accounts
<!-- How each source describes or uses the method -->
- **Computational grounded theory: a three-step framework integrating unsupervised ML pattern detection, human refinement, and quantitative confirmation for rubric development**: Computational grounded theory integrates qualitative research with computational techniques to analyze large datasets systematically for theory development, addressing grounded theory's subjective interpretation and replication difficulties. The article describes it as outlining "a three-step process to guide researchers in rubric design and application": pattern detection (unsupervised ML converts text into interpretable, data-driven categories), pattern refinement (human experts interpret and refine the data-driven categories via thematic content analysis, merging or adding categories), and pattern confirmation (computational methods such as supervised ML test reliability and generalizability). This study examines the validity of the first two steps. (Martin et al. (2025))
- **Computational Grounded Theory: a three-step hybrid of machine pattern detection, human refinement, and pattern confirmation**: Computational Grounded Theory (CGT), originally proposed by Nelson, combines unsupervised machine learning and natural language processing with the iterative, interpretive coding practices of grounded theory. The article states the method "unfolds in three steps: pattern detection using computational tools, pattern refinement through deep human reading, and pattern confirmation via further analysis or modeling." In this study, CGT structures the analysis of student-chatbot dialogue: BERTopic detects patterns, researchers interpret and refine clusters and outliers, and supervised classification confirms the macro-themes. The authors argue the hybrid maintains the contextual and theoretical depth of traditional qualitative research while addressing scalability, reproducibility, and efficiency. (Dange et al. (2026))

### Claims
- [HDBSCAN clustering of BERT embeddings yielded fifteen clusters capturing the content and complexity of students' mechanistic reasoning](../claims/hdbscan-clusters-capture-reasoning-content-and-complexity.md) [+M]
- [A logistic-regression classifier predicted the five macro-themes with 0.90 ± 0.02 average accuracy under 10-fold cross-validation](../claims/classifier-tenfold-accuracy-ninety-percent.md) [+M]
- [Semester-wide BERTopic modeling produced 47 topic clusters after iterative human-guided outlier reassignment reduced outliers from 234 to 18](../claims/semester-47-clusters-outlier-reassignment.md) [+M]

## Related Research Methods
-

## Key Sources
- Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y
- Dange, A. and Lopez, R.E. (2026). Chatbot Conversations in Physics Education: Using Artificial Intelligence to Analyze Student Reasoning through Computational Grounded Theory. arXiv:2603.04616. https://arxiv.org/abs/2603.04616
