---
type: product
id: socratic-debugging-benchmark-dataset
title: Socratic debugging benchmark dataset
description: An openly released benchmark dataset and code repository containing expert-authored multi-turn Socratic dialogues for helping beginner Python programmers debug single-bug programs, created by Al-Hossami et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Socratic debugging benchmark dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An openly released benchmark dataset and code repository containing expert-authored multi-turn Socratic dialogues for helping beginner Python programmers debug single-bug programs, created by Al-Hossami et al.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Socratic debugging benchmark dataset of multi-turn expert dialogues**: A manually created dataset of multi-turn Socratic advice 'aimed at helping a novice programmer ﬁx buggy solutions to simple computational problems'. It contains 38 programming problems, 57 bugs, 151 dialogues and 3,495 utterances created by ten contributors with extensive CS education experience, with main and alternative utterances at every turn to support precision and recall estimation. Code and datasets are freely available at https://github.com/taisazero/socratic-debugging-benchmark. (Erfan Al-Hossami et al. (2023))
- **Socratic code-debugging dataset with 38 problems, 50+ bugs, and 1900+ dialogue turns**: The study uses the Socratic code-debugging dataset introduced by Al-Hossami et al., built on didactic conversations between a novice-programmer Student and an Instructor who asks Socratic questions to help debug buggy code. The article states: "In total, there are 38 problems with more than 50 different bugs in student solutions, and conversations centered around these buggy codes containing more than 1900 dialogue turns." It includes metadata (problem statement, test cases, bug description, code fixes) and is split into train and test sets of 135 and 16 dialogues. (Nischal Ashok Kumar et al. (2024))

### Claims
- [Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances](../claims/human-ita-dataset-recall-validation.md) [+M]
- [GPT-4 outperforms GPT-3.5 in generating relevant and diverse Socratic debugging utterances, but remains below human expert levels](../claims/gpt4-outperforms-gpt35-socratic-debugging.md) [+M]

## Related Products and Programmes

- [DCC Help](dcc-help.md)

## Key Sources
- Erfan Al-Hossami, Razvan Bunescu, Justin Smith and Ryan Teehan. (2023). Can Language Models Employ the Socratic Method? Experiments with Code Debugging. arXiv. https://arxiv.org/abs/2310.03210
- Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. https://arxiv.org/abs/2403.00199
