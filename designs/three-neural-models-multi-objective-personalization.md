---
type: design
id: three-neural-models-multi-objective-personalization
title: Three interconnected neural network models integrated through multi-objective optimization
description: "The article's personalization framework \"implements three interconnected neural network models\": a Student Feature Analysis Model using CNNs and BiLSTM networks to extract patterns from multi-modal student data and ge..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
sources:
  - id: zhang-ke-2026
    resource: "https://doi.org/10.1038/s41598-026-37028-6"
    title: "Zhang Ke, Yang Meng, Li Liying. (2026). Optimization of academic performance and mental health in college students through an AI-driven personalized physical exercise and mindfulness intervention system. Scientific Reports. https://doi.org/10.1038/s41598-026-37028-6"
    author: Zhang Ke, Yang Meng, Li Liying
---

# Three interconnected neural network models integrated through multi-objective optimization

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's personalization framework "implements three interconnected neural network models": a Student Feature Analysis Model using CNNs and BiLSTM networks to extract patterns from multi-modal student data and generate 128-dimensional feature vectors; an Exercise Program Matching Model using a factorization-machine deep neural network to predict exercise efficacy from student profiles and contextual factors; and a Mindfulness Practice Adaptation Model using graph convolutional networks to model relationships between psychological states, mindfulness techniques, and academic contexts. The models are integrated through a multi-objective optimization balancing academic performance, stress reduction, and engagement sustainability, with online learning and adaptive learning rates refining parameters from observed outcomes.

## Design Implications

### Context
#### Requirements
- Multimodal data inputs: physiological time-series, psychological assessments, academic metrics, and behavioral logs
- Cold-start strategies during the initial 2-week adaptation phase for each participant
#### Constraints
- The article notes many deep learning approaches function as black boxes, complicating interpretability, and that algorithmic bias and privacy concerns require careful navigation in university contexts

### Target Learners
- undergraduate university students

### Learning Goals
- personalized exercise recommendation
- personalized mindfulness practice selection
- academic performance support

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zhang Ke, Yang Meng, Li Liying. (2026). Optimization of academic performance and mental health in college students through an AI-driven personalized physical exercise and mindfulness intervention system. Scientific Reports. https://doi.org/10.1038/s41598-026-37028-6
