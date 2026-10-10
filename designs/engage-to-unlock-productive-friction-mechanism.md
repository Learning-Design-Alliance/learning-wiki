---
type: design
id: engage-to-unlock-productive-friction-mechanism
title: "Engage-to-Unlock: engagement-based access as a productive-friction mechanism for GenAI"
description: Engage-to-Unlock is an interaction method in which generative capabilities become available only after users show task-relevant engagement.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: xiaotian-su-2026
    resource: "https://arxiv.org/abs/2610.01518"
    title: "Xiaotian Su, Laura Rimell, Jiazheng Li, Amal Rannen-Triki, Ulrich Paquet, Lisa Anne Hendricks, Rida Qadri, Daphne Ippolito and Piotr Mirowski. (2026). Who Thinks First? Designing Productive Friction with Engage-to-Unlock GenAI. https://arxiv.org/abs/2610.01518"
    author: Xiaotian Su, Laura Rimell, Jiazheng Li, Amal Rannen-Triki, Ulrich Paquet, Lisa Anne Hendricks, Rida Qadri, Daphne Ippolito and Piotr Mirowski
---

# Engage-to-Unlock: engagement-based access as a productive-friction mechanism for GenAI

> **Design** · [All designs](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
Engage-to-Unlock is an interaction method in which generative capabilities become available only after users show task-relevant engagement. The article describes it as "a form of productive friction in which access to generative capabilities responds to each writer's engagement rather than elapsed time alone." In argumentative writing, the Tell-me text-generation mode unlocks when the essay contains a complete position and at least one distinct argumentative development linked to that position, detected by an LLM-based discourse classifier (micro-averaged F1 of 91.5%, macro-averaged F1 of 83.6%). Until unlock, users work with a pedagogical Teach-me assistant.

## Design Implications

### Context
#### Requirements
- An LLM-based discourse classifier to detect the required engagement elements (position and argumentative development) in the user's draft
- A restricted assistant mode (Teach-me) available before unlock and a generative mode (Tell-me) gated behind the criterion
#### Constraints
- In the study, 9 of 107 Engage-to-Unlock participants (8.4%) did not reach the contribution criterion and never unlocked Tell-me
- The mechanism was implemented and tested for argumentative writing, where engagement is reflected in a position and supporting rationale

### Target Learners
- Adult crowd workers (Prolific participants) completing argumentative writing tasks

### Learning Goals
- Developing one's own position and argumentative rationale before receiving generative AI text generation
- Accurate evaluation of AI-generated content for evidence and reasoning errors

### Claims
- [Engage To Unlock Redistributes Effort Across Tasks](../claims/engage-to-unlock-redistributes-effort-across-tasks.md) [+M]
- [Engage To Unlock Increases Prompt Submission](../claims/engage-to-unlock-increases-prompt-submission.md) [+M]
- [Engage To Unlock Faster More Efficient Evaluation](../claims/engage-to-unlock-faster-more-efficient-evaluation.md) [+M]
- [Engage To Unlock Error Classification Advantage](../claims/engage-to-unlock-error-classification-advantage.md) [+M]
- [Time Matched Unlock Does Not Reproduce Engagement State](../claims/time-matched-unlock-does-not-reproduce-engagement-state.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Xiaotian Su, Laura Rimell, Jiazheng Li, Amal Rannen-Triki, Ulrich Paquet, Lisa Anne Hendricks, Rida Qadri, Daphne Ippolito and Piotr Mirowski. (2026). Who Thinks First? Designing Productive Friction with Engage-to-Unlock GenAI. https://arxiv.org/abs/2610.01518
