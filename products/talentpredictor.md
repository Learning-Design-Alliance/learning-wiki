---
type: product
id: talentpredictor
title: TalentPredictor
description: "TalentPredictor is a semi-supervised multimodal neural-network system developed by Xinzhe Zheng and colleagues to predict secondary students' talent types from examination, award, demographic, and learning-behavior data."
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# TalentPredictor

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
TalentPredictor is a semi-supervised multimodal neural-network system developed by Xinzhe Zheng and colleagues to predict secondary students' talent types from examination, award, demographic, and learning-behavior data.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **TalentPredictor semi-supervised multimodal neural network for multi-type talent prediction**: TalentPredictor is a semi-supervised multimodal model combining a clustering auto-labeler with Transformer, LSTM and ANN encoders. Award descriptions are embedded with a Chinese-and-English BERT variant and clustered into seven talent types to act as "an auto labeler, so TalentPredictor can also apply to data without human labels on award records". Sequential exam data go to LSTM, text to transformer, and discrete data to ANN; encoder outputs are concatenated, normalized by LayerNorm, and passed to a final classifier outputting seven confidence values. It was trained and evaluated on offline data from 1,041 secondary students and deployed in local schools. (Xinzhe Zheng et al. (2025))

### Claims
- [TalentPredictor predicts seven talent types in secondary school students with a best test micro ROCAUC of 0.908 on a real-world dataset of 1,041 students](../claims/talentpredictor-0908-micro-rocauc-seven-talent-types.md) [+M]
- [Clustering fine-tuned BERT embeddings of award descriptions yields an accurate automatic award labeler, with Agglomerative Clustering using Ward linkage performing best (Rand Index 0.990)](../claims/finetuned-bert-clustering-award-autolabeler.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. https://arxiv.org/abs/2509.00863
