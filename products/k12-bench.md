---
type: product
id: k12-bench
title: K12-Bench
description: K12-Bench is a 23,640-item multi-select benchmark dataset created by Hao Liang et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# K12-Bench

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 3 studies (3 design), `q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
K12-Bench is a 23,640-item multi-select benchmark dataset created by Hao Liang et al. for evaluating large language models' structural understanding of K–12 curricula.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Grade-anchored benchmark design: measuring model proficiency against K-12 curriculum levels and human exam scores**: The benchmark's organizing framework is to evaluate machines against fundamental K-12 curricular skills rather than expert-level tasks. Because skills and grades are embedded metadata, the design enables "grade-level performance of models" — for instance, finding models "only competitive with first graders in understanding certain STEM skills." Evaluation mirrors real-world exams: the IXL SmartScore "is designed to measure how well humans understand a STEM skill," starting at 0 and adjusting with each answer, with a score above 90.0 considered excellent for a mastered skill. (Jianhao Shen et al. (2024))

### Claims
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](../claims/omniedu-27b-best-curriculum-grounding-k12-bench.md) [+W]
- [Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest](../claims/llms-lack-curriculum-cognition-k12-bench.md) [+W]
- [State-of-the-art foundation models remain well below average elementary students on STEM, mastering only 2.5% of third-grade skills](../claims/foundation-models-below-elementary-students-stem.md) [+M]
- [Neural models show no obvious performance drop across grade levels, unlike the human learning curve](../claims/no-grade-level-performance-drop-models.md) [+M]

## Related Products and Programmes

- [K12-KGraph](k12-kgraph.md)
- [K12-Train](k12-train.md)

## Key Sources
- Hao Liang, Qihan Lin, Mingrui Chen, Hengyi Feng, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, Meiyi Qiang, Linzhuang Sun, Wentao Zhang. (2026). K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs. arXiv preprint. https://arxiv.org/abs/2605.09635
- Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang. (2024). MEASURING VISION-LANGUAGE STEM SKILLS OF NEURAL MODELS. Published as a conference paper at ICLR 2024. https://arxiv.org/abs/2402.17205
