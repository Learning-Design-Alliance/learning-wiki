---
type: product
id: studentsyn-benchmark
title: STUDENTSYN benchmark
description: "A benchmark dataset created by Singla and Theodoropoulos for evaluating student-attempt synthesis in Code.org's block-based Hour of Code: Maze Challenge, with reference and target tasks, misconception scenarios, ground-truth attempts, expert solutions, and synthetic training data."
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# STUDENTSYN benchmark

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A benchmark dataset created by Singla and Theodoropoulos for evaluating student-attempt synthesis in Code.org's block-based Hour of Code: Maze Challenge, with reference and target tasks, misconception scenarios, ground-truth attempts, expert solutions, and synthetic training data.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **STUDENTSYN benchmark for student attempt synthesis in visual programming**: STUDENTSYN is an existing benchmark from Singla and Theodoropoulos (2022) for evaluating student attempt synthesis in the block-based visual programming domain of Hour of Code: Maze Challenge by Code.org (HoCMaze). It comprises "two reference tasks T ref, namely HoCMaze-4 and HoCMaze-18" with three target tasks each and six misconception types (e.g., left/right turn confusion, repetitive turn commands, ignoring If-Else/While structure), yielding 36 evaluation scenarios with ground-truth student attempts. It also supplies a synthetic (task, solution) dataset used for pre-training or fine-tuning. (Manh Hung Nguyen et al. (2024))

### Claims
- [GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data](../claims/gpt4-ss-outperforms-neurss-qoverall.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2024). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. https://arxiv.org/abs/2310.10690
