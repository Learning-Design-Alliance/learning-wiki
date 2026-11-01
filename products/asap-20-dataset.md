---
type: product
id: asap-20-dataset
title: ASAP 2.0 dataset
description: The ASAP 2.0 dataset is a public benchmark of approximately 24,000 student argumentative essays with human-assigned scores from 1 to 6, developed for automated essay-scoring research.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# ASAP 2.0 dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The ASAP 2.0 dataset is a public benchmark of approximately 24,000 student argumentative essays with human-assigned scores from 1 to 6, developed for automated essay-scoring research.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ASAP 2.0 dataset of argumentative student essays with 1–6 human-assigned scores**: The ASAP 2.0 dataset (Crossley et al. 2024) is the public AES benchmark used to evaluate RACES. It "contains approximately 24,000 argumentative essays written by students, covering diverse topics and writing styles", with about 17,000 used for training and the rest for validation and testing. Each essay carries a human-assigned score from 1 to 6 based on strict evaluation criteria, serving as the only human-assigned labels in the experiments. (Zhenxin Zhang et al. (2026))
- **ASAP '12 SAS Kaggle competition dataset for short answer scoring**: The Automated Student Assessment Prize (ASAP) short answer scoring competition was hosted on Kaggle in 2012, covering ten questions of varied high-school-level subject matter from arts to science. "The participants were given 1,800 student answers for training, which were randomly taken from a pool of 3,000." A further 6,000 student answers were used for testing, and agreement between predicted and human-judge-resolved scores was evaluated with quadratic weighted kappa. The review examines the top three systems from a modified ranking: Tandella '12, Zbontar '12, and Conort '12. (Steven Burrows et al. (2015))

### Claims

- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](../claims/llm-essay-scoring-weak-human-agreement.md) [+W]
- [Newer LLM generations do not consistently agree better with human essay graders](../claims/no-consistent-generational-improvement-llm-grading.md) [+W]
- [In Support & Evidence and Claim & Focus, teacher and AES scores agreed at the lowest and highest rubric points but diverged in the middle, with teachers more likely to score a 2 and the AES a 3](../claims/teacher-aes-agree-tails-diverge-middle.md) [~W]

## Related Products and Programmes

- [IELTS Writing Scored Essays Dataset](ielts-writing-scored-essays-dataset.md)
- [ASAP-SAS corpus of short-answer scoring prompts and rubrics](asap-sas-corpus-of-short-answer-scoring-prompts-and-rubrics.md)

## Key Sources
- Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8
- Steven Burrows, Iryna Gurevych, Benno Stein. (2015). The Eras and Trends of Automatic Short Answer Grading. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0026-8
