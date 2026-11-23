---
type: strategy
id: dast-ai-bias-study-extension-plan
title: Extend AI-image bias research with multiple models, a modified DAST prompt, larger balanced samples and multiple scorers and VLMs
description: "The author's future-work plan (Table 2) lays out an expanded methodology: multiple image generators (Midjourney, Stable Diffusion, OpenAI DALL·E 3, Google Imagen3), the modified DAST prompt of Farland-Smith (2012), mo..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: gyeonggeon-lee-2025
    resource: "https://arxiv.org/abs/2504.19005"
    title: "Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. https://arxiv.org/abs/2504.19005"
    author: Gyeonggeon Lee
---

# Extend AI-image bias research with multiple models, a modified DAST prompt, larger balanced samples and multiple scorers and VLMs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The author's future-work plan (Table 2) lays out an expanded methodology: multiple image generators (Midjourney, Stable Diffusion, OpenAI DALL·E 3, Google Imagen3), the modified DAST prompt of Farland-Smith (2012), more than 5,000 images, an additional scoring rubric, at least two human scorers on a validation dataset, multiple cutting-edge VLMs plus custom CNN comparators, iterative prompt engineering, and collecting more balanced data to secure validity. The author also recommends figuring out ways to correct current representations of scientists by prominent image generation AI models.

## Design Implications

### Context
#### Requirements
- Access to multiple image generation models and VLMs, a validation dataset with at least two human scorers, and more balanced data across the 15 stereotype features
#### Constraints
- The pilot's data were imbalanced across the 15 stereotype features, complicating judgment of the MHA performance index

### Target Learners
- science education researchers
- the general public exposed to AI-generated scientist images

### Target Learning Goals
- public understanding of scientists
- equitable STEM education free of amplified stereotypes

## Claims

- [gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images](../claims/gpt-mini-detects-dast-stereotypes-79-mha.md) [+W]
- [Machine-human agreement on DAST-C features varies widely, from 49-100%, being high for concrete features and low for uncertain ones such as scientist working indoors and middle-aged/elderly appearance](../claims/mha-varies-concrete-vs-uncertain-features.md) [~W]
- [Generative AI (Midjourney v 6.1) produces stereotypical images of scientists, with lab coat in 97%, eyeglasses in 97%, male gender in 81% and Caucasian in 85% of the 100 human-scored images](../claims/midjourney-scientist-images-stereotyped-dast.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. https://arxiv.org/abs/2504.19005
