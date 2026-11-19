---
type: product
id: vnhsge-dataset
title: VNHSGE dataset
description: A benchmark dataset compiled and released by Xuan-Quy Dao et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# VNHSGE dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A benchmark dataset compiled and released by Xuan-Quy Dao et al. from Vietnamese National High School Graduation Examination papers, containing physics and other subject questions for evaluating language models on Vietnamese educational assessments.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **VNHSGE physics evaluation subset: 2000 multiple-choice questions in 50 test sets across four difficulty levels**: The VNHSGE dataset is a benchmark compiled from real Vietnamese National High School Graduation Examination papers from 2019 to 2023, covering nine subjects. Its physics subset contains "2000 multiple-choice questions divided into 50 sets of test questions" spanning topics such as mechanical oscillations, electromagnetic waves, and light refraction. Questions are classified into four levels from knowledge to high application, and the dataset is released in JSON and Word formats for LLM evaluation. The study used a five-exam, 200-question evaluation subset from it. (Xuan-Quy Dao et al. (2023))
- **VNHSGE dataset for evaluating LLMs on Vietnamese high school examinations**: The VNHSGE dataset is a benchmark derived from the Vietnamese National High School Graduation Examination and comparable examinations, built by the authors to assess LLM performance in Vietnamese education. It "encompasses nine distinct subjects" and "comprises a total of 300 literary essays and 19,000 multiple-choice questions pertaining to various subjects." The present study uses an evaluation set drawn from it: 30 literature essay questions and 1700 multiple-choice questions from the 2019–2023 exams. It supports multitask evaluation including question answering, text generation, reading comprehension, and visual question answering. (Xuan-Quy Dao et al. (2023))

### Claims
- [ChatGPT and BingChat perform worse than Vietnamese students on high school physics graduation exams](../claims/chatgpt-bingchat-below-vietnamese-students-physics-exams.md) [+M]
- [Neither ChatGPT nor BingChat can reliably answer physics questions at the high application level](../claims/llms-fail-high-application-physics-questions.md) [+M]
- [BingChat outperforms ChatGPT on the VNHSGE in all subjects except literature](../claims/bingchat-beats-chatgpt-vnhsge-except-literature.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo. (2023). Evaluation of ChatGPT and Microsoft Bing AI Chat Performances on Physics Exams of Vietnamese National High School Graduation Examination. arXiv preprint. https://arxiv.org/abs/2306.04538
- Xuan-Quy Dao and Ngoc-Bich Le. (2023). ChatGPT is Good but Bing Chat is Better for Vietnamese Students. arXiv preprint. https://arxiv.org/abs/2307.08272
