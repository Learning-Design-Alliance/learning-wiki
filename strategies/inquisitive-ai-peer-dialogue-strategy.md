---
type: strategy
id: inquisitive-ai-peer-dialogue-strategy
title: "Make AI peer dialogue more inquisitive: identify the student's misconception first, ask them to elaborate, and let dialogue length be flexible"
description: "Based on grader feedback, the article recommends the AI \"should first identify the students' misconception, ask them to explain why it's wrong, and elaborate on their reasoning\" instead of giving lengthy generic expla..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: weijers-2025
    resource: "https://arxiv.org/abs/2504.00408"
    title: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. https://arxiv.org/abs/2504.00408"
    author: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K"
---

# Make AI peer dialogue more inquisitive: identify the student's misconception first, ask them to elaborate, and let dialogue length be flexible

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Based on grader feedback, the article recommends the AI "should first identify the students' misconception, ask them to explain why it's wrong, and elaborate on their reasoning" instead of giving lengthy generic explanations with repetitive analogies. Interaction length should not be fixed at three rounds; students should engage as long or briefly as they prefer. Prompting the AI to be more inquisitive could increase engagement and better reduce underlying misconceptions.

## Design Implications

### Context
#### Requirements
- System prompts that elicit the student's own reasoning rather than delivering one-size-fits-all explanations
#### Constraints
- Graders noted the current AI rarely asks students to elaborate before explaining, and longer interactions revealed the AI can get sidetracked when students ask probing questions

### Target Learners
- undergraduate students interacting with LLM-based learning tools

### Target Learning Goals
- misconception correction
- student engagement in dialogue

## Claims

- [Targeted dialogue with a fallible AI Peer raised post-test FCI scores by 10.5 percentage points and normalized gain by over 20 points versus a control group](../claims/ai-peer-dialogue-improves-fci-gains.md) [+M]
- [Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation](../claims/ai-peer-interaction-quality-annotations.md) [~M]
- [Post-test performance was approximately equal regardless of AI explanation quality, suggesting the dialogue process rather than explanation correctness drives the gain](../claims/post-test-performance-independent-of-ai-explanation-quality.md) [+M]

## Related Strategies

- [Directly teach students when, why, and how to elaborate on new information](directly-teach-elaborative-processing-strategies.md)
- [Three recommendations for effective feedback practice: open up the floor, leave the floor open, and be careful in mitigating feedback](open-and-leave-open-floor-careful-mitigation-strategy.md)
- [Describe AI instructional role and learner–AI interaction design in detail (prompts, scaffolds, modality, dialogue structures)](describe-ai-role-and-interaction-design-in-detail.md)

## Examples
-

## Key Sources
- Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. https://arxiv.org/abs/2504.00408
