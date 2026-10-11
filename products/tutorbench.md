---
type: product
id: tutorbench
title: TutorBench
description: TutorBench is a source-grounded benchmark dataset created by Bingxi Zhao et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# TutorBench

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 1 of 2 report an effect size · 3 claims rest on one study

## Description
TutorBench is a source-grounded benchmark dataset created by Bingxi Zhao et al. for evaluating adaptive multi-turn tutoring and customized practice generation with simulated learner profiles.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Public TutorBench sample: 30 tutoring scenarios with 324 structured rubric items across three use-case families**: The public TutorBench sample is a rubric-level resource containing "30 tutoring scenarios and 324 rubric items across three use-case families: adaptive explanation, assessment and feedback, and active learning." The article analyzes its rubric metadata with a deterministic label mapping to measure agency-dimension and agency-skill density, finding one representative criterion requires the tutor to "provide hint[s] ... by asking at least 2 guiding questions without completely showing next steps." (Junyi Yao et al. (2026))

### Claims
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](../claims/deeptutor-improves-interactive-tutoring-quality-10-76.md) [+M]
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](../claims/human-llm-judge-preference-alignment-deeptutor.md) [+M]
- [In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)](../claims/tutorbench-rubrics-encode-agency-active-learning-highest.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962
- Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206
