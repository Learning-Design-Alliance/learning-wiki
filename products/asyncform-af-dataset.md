---
type: product
id: asyncform-af-dataset
title: Asyncform (AF) dataset
description: A corpus of 863 AI-generated educational questions in English, Mathematics, and Science, labeled by K–12 teachers with Bloom Taxonomy levels and related subject, grade-level, objective, and question metadata; it was created and released by Michael Lawrence Castanares et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Asyncform (AF) dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A corpus of 863 AI-generated educational questions in English, Mathematics, and Science, labeled by K–12 teachers with Bloom Taxonomy levels and related subject, grade-level, objective, and question metadata; it was created and released by Michael Lawrence Castanares et al.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Asyncform (AF) dataset of 863 teacher-labeled AI-generated educational questions**: The Asyncform (AF) dataset is an out-of-distribution corpus of AI-assisted educational questions created by the authors to test Bloom-level classifier transfer. The article states: "we generated 863 AEQ covering subjects in English, Mathematics, and Science. AF dataset was labeled with corresponding Bloom Taxonomy level by three K-12 teachers who taught the subjects." Each question received a single Bloom label due to limited staff, and annotation included subject, grade level, learning objectives, and question text. (Michael Lawrence Castanares et al. (2026))

### Claims

- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](../claims/lime-pos-reliance-varies-by-dataset.md) [+W]
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](../claims/learning-objectives-anchor-bloom-classification.md) [+M]
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](../claims/ml-bloom-classifiers-degrade-ood-aeq.md) [+W]
- [AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data](../claims/ood-aeq-textual-characteristics-differ-iid.md) [+W]
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](../claims/llms-robust-ood-bloom-classification.md) [+W]
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](../claims/model-retraining-largest-ood-improvement.md) [~W]

## Related Products and Programmes

- [Dataset of 434 expert-labelled authentic learner questions augmented to balance class distributions](dataset-of-434-expert-labelled-authentic-learner-questions-augmented-to-balance-class-dist.md)

## Key Sources
- Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749
