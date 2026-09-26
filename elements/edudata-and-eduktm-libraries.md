---
type: element
id: edudata-and-eduktm-libraries
title: EduData and EduKTM Open-Source Knowledge Tracing Libraries
description: "The survey's authors released two open-source algorithm libraries: \"EduData that enables the download and preprocessing of KT-related datasets, and EduKTM that provides an extensible and unified implementation of exis..."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# EduData and EduKTM Open-Source Knowledge Tracing Libraries

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The survey's authors released two open-source algorithm libraries: "EduData that enables the download and preprocessing of KT-related datasets, and EduKTM that provides an extensible and unified implementation of existing mainstream KT models." They catalogue twelve public datasets (Table II), including ASSISTments2009 to 2017, Junyi, Eedi2020, Statics2011, EdNet-KT1 to KT4 and CodeWorkout; EdNet is the largest, with 131,441,538 learning records from 784,309 students.

## Design Implications

### Context
#### Requirements
- Python-accessible public KT datasets, downloaded and preprocessed through EduData
- Contributors following the provided guidelines to add models to EduKTM, which the authors say will always be under development
#### Constraints
- The authors do not provide performance evaluation of the baselines on the benchmark datasets, because experimental settings differ and prediction accuracy does not directly reflect practical effectiveness
- The original version of ASSISTments2009 had three serious problems that lead to unreliable experimental results, fixed in the latest version

### Target Learners
- Researchers and practitioners implementing or comparing knowledge tracing models

### Target Learning Goals
- Selecting appropriate KT models for specific application scenarios

### Affordances
- [Knowledge Tracing Model Taxonomy](../theories/knowledge-tracing-model-taxonomy.md)

## Related Elements

- [Knowledge Tracing Learner Modeling Task](../theories/knowledge-tracing-learner-modeling-task.md)
- [Four large-scale real-world sequential knowledge tracing benchmark datasets used to evaluate Adaptive G-UKT](adaptive-g-ukt-benchmark-datasets.md)
- [Released learner performance prediction code and public dataset links](learner-performance-prediction-github-code.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
