---
type: design
id: paper-based-gai-feedback-recommendation-system
title: Paper-based GAI-powered physics feedback system with spaced-repetition error recommendation
description: The article describes a researcher-developed system integrating error reporting, spaced-repetition recommendation, and GAI-generated feedback, delivered entirely on paper to comply with school device policies.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: xusheng-dai-2025
    resource: "https://arxiv.org/abs/2505.08672"
    title: "Xusheng Dai, Zhaochun Wen, Jianxiao Jiang, Huiqin Liu, Yu Zhang. (2025). How Students Use AI Feedback Matters: Experimental Evidence on Physics Achievement and Autonomy. Preprint, under review. https://arxiv.org/abs/2505.08672"
    author: Xusheng Dai, Zhaochun Wen, Jianxiao Jiang, Huiqin Liu, Yu Zhang
---

# Paper-based GAI-powered physics feedback system with spaced-repetition error recommendation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article describes a researcher-developed system integrating error reporting, spaced-repetition recommendation, and GAI-generated feedback, delivered entirely on paper to comply with school device policies. Its recommendation rule is that "after learners submit their errors in daily homework, they receive repeated recommendations of previously incorrectly answered problems on the second- and seventh-days following submission." GAI hints were generated via a retrieval-augmented, multi-agent workflow characterized by personalized diagnosis, emotional support, and heuristic rather than direct answer provision; Experiment 2 added a vector-retrieved question bank of approximately 6,000 physics problems and a learning-factor algorithm for tiered feedback.

## Design Implications

### Context
#### Requirements
- Students' daily submission of marked homework errors (via scanned answer sheets) so the system can generate recommendations
- OCR scanning and a printing workflow to deliver paper-based feedback
#### Constraints
- Implemented paper-based to comply with the school's policy prohibiting smart electronic devices in classrooms

### Target Learners
- Grade 10 high school physics students

### Learning Goals
- physics problem-solving through review of incorrectly answered problems within the zone of proximal development

### Claims
- [Gai Hint Workflow Quality Validation](../claims/gai-hint-workflow-quality-validation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Xusheng Dai, Zhaochun Wen, Jianxiao Jiang, Huiqin Liu, Yu Zhang. (2025). How Students Use AI Feedback Matters: Experimental Evidence on Physics Achievement and Autonomy. Preprint, under review. https://arxiv.org/abs/2505.08672
