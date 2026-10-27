---
type: strategy
id: gpt4-rephrase-incorrect-responses-feedback-strategy
title: Use GPT-4 few-shot rephrasing of incorrect trainee responses to deliver corrective explanatory feedback at scale
description: The authors recommend integrating GPT-4 classification and rephrasing into template-based feedback systems so novice tutors receive real-time explanatory feedback showing the desired response form.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: jionghao-lin-2024
    resource: "https://arxiv.org/abs/2405.00970"
    title: "Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970"
    author: Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger
---

# Use GPT-4 few-shot rephrasing of incorrect trainee responses to deliver corrective explanatory feedback at scale

> **Strategy** · [All strategies](index.md)
> **Evidence** · 9 claims (7 for, 2 mixed) · 4 studies (4 design), `q2`–`q3` · 0 of 4 report an effect size · 9 claims rest on one study

## Description
The authors recommend integrating GPT-4 classification and rephrasing into template-based feedback systems so novice tutors receive real-time explanatory feedback showing the desired response form. Because "including the correct answer within the feedback substantially enhances its efficacy", rephrasing the trainee's own incorrect response into a correct form personalizes corrective feedback while mitigating the time and effort demands of human graders.

## Design Implications

### Context
#### Requirements
- Lesson-specific response principles and scenario context in the prompt
- A small set of paired correct/incorrect example rephrasings for few-shot prompting
- Expert-annotated examples to establish classification reliability
#### Constraints
- Effectiveness on tutor skill acquisition, retention, and real-world application not yet evaluated; the authors plan longitudinal controlled studies
- Results demonstrated on three lessons only

### Target Learners
- novice tutors and trainees in online scenario-based tutoring training

### Target Learning Goals
- giving effective praise
- reacting to errors
- determining what students know

### Affordances
- [Framework Quality Rephrased Responses](../research-methods/framework-for-determining-the-quality-of-rephrased-responses-accuracy-responsiveness.md)

## Claims

- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](../claims/gpt4-few-shot-classifies-trainee-responses.md) [+M]
- [Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)](../claims/few-shot-shots-improve-classification.md) [+M]
- [Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668](../claims/classification-weakest-determining-students-know.md) [~M]
- [For the Giving Effective Praise lesson, GPT-4-rephrased responses were rated significantly more accurate than human-expert rephrasings (p < 0.001), with no significant difference in responsiveness](../claims/gpt4-rephrasing-more-accurate-than-humans-praise.md) [+M]
- [For Determining What Students Know, no significant difference in accuracy or responsiveness was found between GPT-4 and human rephrasings](../claims/gpt4-rephrasing-no-difference-determining-students-know.md) [+M]
- [For Reacting to Errors, GPT-4 rephrasings were rated more accurate than human rephrasings (few-shot p < 0.01, zero-shot p < 0.05) with no significant responsiveness difference](../claims/gpt4-rephrasing-reacting-to-errors-accuracy.md) [+M]
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](../claims/gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) [+M]
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](../claims/gpt4-zero-shot-comparable-finetuned-classifiers.md) [+W]
- [AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses](../claims/ai-mid-range-scoring-degradation-u-shape.md) [~M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970
