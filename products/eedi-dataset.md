---
type: product
id: eedi-dataset
title: Eedi dataset
description: A large English-language mathematics dataset of multiple-choice word-problem exercises and student response interactions, maintained by Eedi and used for knowledge-tracing research.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Eedi dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
A large English-language mathematics dataset of multiple-choice word-problem exercises and student response interactions, maintained by Eedi and used for knowledge-tracing research.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Eedi diagnostic-question answer dataset released for the NeurIPS 2020 Education Challenge**: The article releases a large-scale dataset of student responses to crowd-sourced multiple-choice diagnostic mathematics questions from Eedi, an online education provider used in tens of thousands of schools, covering answers given between September 2018 and May 2020. After filtering, the training sets comprise "27613 questions, 118971 students, 15867850 answers" for tasks 1 and 2 and "948 questions, 4918 students, 1382727 answers" for tasks 3 and 4. Metadata cover subjects in a tree structure, student demographics, and per-answer confidence and timing. (Zichao Wang et al. (2021))
- **Competition Tasks 1 and 2: predicting binary correctness and four-way answer choice as sparse matrix completion**: Tasks 1 and 2 ask participants to predict, on held-out student-question pairs, first whether a student answers a question correctly (binary) and second which of the four multiple-choice options the student selects (categorical). Both are framed as matrix completion on an extremely sparse student-by-question matrix, akin to recommender-system challenges; Task 2 adds the harder wrinkle of "unordered categorical data", which is rare in recommender settings. Evaluation for both tasks is prediction accuracy. (Zichao Wang et al. (2021))

### Claims

## Related Products and Programmes
-

## Key Sources
- Max Norris, Kobi Gal and Sahan Bulathwela. (2026). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. https://arxiv.org/abs/2511.02599
- Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2021). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061
