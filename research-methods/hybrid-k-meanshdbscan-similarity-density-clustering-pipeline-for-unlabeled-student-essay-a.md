---
type: research-method
id: hybrid-k-meanshdbscan-similarity-density-clustering-pipeline-for-unlabeled-student-essay-a
title: Hybrid K-Means/HDBSCAN similarity-density clustering pipeline for unlabeled student essay analysis
description: "The article proposes a novel unsupervised clustering pipeline that \"combines the strengths of K-Means and HDBSCAN\" to uncover reasoning patterns in student essays without pre-defined labels."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Hybrid K-Means/HDBSCAN similarity-density clustering pipeline for unlabeled student essay analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a novel unsupervised clustering pipeline that "combines the strengths of K-Means and HDBSCAN" to uncover reasoning patterns in student essays without pre-defined labels. K-Means is first applied to TF-IDF-vectorized essays to build a similarity matrix, which is smoothed with exponentially weighted pairwise Euclidean distances and converted to a distance matrix; HDBSCAN then extracts refined clusters from this precomputed distance matrix. The method was applied to physics problem-solving strategy essays from an online multiple-choice quiz.

## Accounts
<!-- How each source describes or uses the method -->
- **Hybrid K-Means/HDBSCAN similarity-density clustering pipeline for unlabeled student essay analysis**: The article proposes a novel unsupervised clustering pipeline that "combines the strengths of K-Means and HDBSCAN" to uncover reasoning patterns in student essays without pre-defined labels. K-Means is first applied to TF-IDF-vectorized essays to build a similarity matrix, which is smoothed with exponentially weighted pairwise Euclidean distances and converted to a distance matrix; HDBSCAN then extracts refined clusters from this precomputed distance matrix. The method was applied to physics problem-solving strategy essays from an online multiple-choice quiz. (Winter Allen (2025))

### Claims
- [A hybrid K-Means/HDBSCAN clustering method outperforms K-Means and HDBSCAN alone on silhouette score and Davies-Bouldin Index for physics strategy essays](../claims/hybrid-clustering-outperforms-kmeans-hdbscan-essays.md) [+M]
- [Hybrid cluster membership is statistically significantly associated with students' multiple-choice answer selection on a physics quiz question](../claims/cluster-membership-associated-with-mc-answers.md) [+M]

## Related Research Methods
-

## Key Sources
- Winter Allen, N. Sanjay Rebello. (2025). Exploring the Feasibility of Employing a Hybrid Machine Learning Method to Unpack Student Reasoning Patterns in Physics Essays. https://arxiv.org/abs/2504.08904
