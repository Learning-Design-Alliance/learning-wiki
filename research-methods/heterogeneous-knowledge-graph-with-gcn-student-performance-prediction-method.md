---
type: research-method
id: heterogeneous-knowledge-graph-with-gcn-student-performance-prediction-method
title: Heterogeneous knowledge graph with GCN student-performance prediction method
description: A framework representing online learning environments as heterogeneous knowledge graphs with students, course videos, assessments, and pages as node types, and student-content interactions as weighted edges.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Heterogeneous knowledge graph with GCN student-performance prediction method

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A framework representing online learning environments as heterogeneous knowledge graphs with students, course videos, assessments, and pages as node types, and student-content interactions as weighted edges. Student-video edges encode normalized percentage of video watched; student-assessment edges encode first grade, final grade, and number of attempts; student-page edges encode binary success criteria (>70% on assessments or videos). A Graph Convolutional Network with Sage Convolution layers processes this graph to derive edge-level predictions of whether a student passed a particular page. The article applies this to identify at-risk students and compare engagement patterns across course modalities.

## Accounts
<!-- How each source describes or uses the method -->
- **Heterogeneous Knowledge Graph representation of online learning environments for GCN-based student performance prediction**: A framework representing online learning environments as heterogeneous knowledge graphs with students, course videos, assessments, and pages as node types, and student-content interactions as weighted edges. Student-video edges encode normalized percentage of video watched; student-assessment edges encode first grade, final grade, and number of attempts; student-page edges encode binary success criteria (>70% on assessments or videos). A Graph Convolutional Network with Sage Convolution layers processes this graph to derive edge-level predictions of whether a student passed a particular page. The article applies this to identify at-risk students and compare engagement patterns across course modalities. (Trask et al. (2024))

### Claims
- [A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy](../claims/gcn-hkg-predicts-problem-set-pass-70-90-accuracy.md) [+M]
- [GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape](../claims/gcn-models-non-transferable-across-instances.md) [-M]

## Related Research Methods
-

## Key Sources
- Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. https://arxiv.org/abs/2407.12153
