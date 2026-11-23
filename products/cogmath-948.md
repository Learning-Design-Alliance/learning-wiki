---
type: product
id: cogmath-948
title: CogMath-948
description: CogMath-948 is a dataset constructed by Wei Zhang et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CogMath-948

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
CogMath-948 is a dataset constructed by Wei Zhang et al. containing six months of eighth-grade mathematics interactions from 1,245 students, annotated with responses, reflective reasoning, ICAP-based engagement labels, and misconception categories.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CogMath-948 dataset of eighth-grade math interactions with cognitive state annotations**: CogMath-948 is a dataset the authors constructed from real educational scenarios because suitable open datasets were lacking for fine-grained cognitive evolution research. It "covers real learning data from 1,245 eighth-grade students over six months", with four dimensions per interaction: question and response information, reflective explanations of reasoning or error causes, ICAP-based cognitive engagement labels, and fine-grained misconception classifications for incorrect answers. It serves as the evaluation corpus for all CogEvolution comparisons and ablations. (Wei Zhang et al. (2026))
- **Competition Task 3: unsupervised ranking of question quality evaluated against expert pairwise judgements**: Task 3 asks participants to devise a metric of question quality and submit a full ranking of the 948 questions, with no expert labels provided during training, making it an unsupervised learning problem. Evaluation compares the submitted ranking's implied pairwise ordering against collected judgements of experienced teachers on unseen question pairs, scoring each expert's agreement fraction and taking the maximum across experts. A baseline entropy-based ranking model is provided in the starter kit. (Zichao Wang et al. (2021))

### Claims

- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](../claims/cogevolution-mistake-precision-beats-kt-baseline.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786v1
- Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2021). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061
