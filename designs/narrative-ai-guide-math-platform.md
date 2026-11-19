---
type: design
id: narrative-ai-guide-math-platform
title: Narrative AI-guide math tutoring platform with teacher-facing hint authoring dashboard
description: An informal online learning environment teaching volume through a six-task narrative storyline (determining if a box of chocolates weighs more than 320 oz), with a side-panel AI guide that responds to learner messages...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: sherry-ruan-2023
    resource: "https://arxiv.org/abs/2304.04933"
    title: "Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2023). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. https://arxiv.org/abs/2304.04933"
    author: Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill
---

# Narrative AI-guide math tutoring platform with teacher-facing hint authoring dashboard

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An informal online learning environment teaching volume through a six-task narrative storyline (determining if a box of chocolates weighs more than 320 oz), with a side-panel AI guide that responds to learner messages using hints, acknowledgments, encouragement, or guided prompts, plus periodic reminder messages after 120 seconds of inactivity. Hints and message templates were "written and uploaded through an easy-to-use teacher-facing dashboard" by "educators and designers without prior background in machine learning". The platform comprises a ReactJS/TypeScript website, an admin dashboard, and a Python AI guide server, and supported real-time RL updates triggered after the post-quiz.

## Design Implications

### Context
#### Requirements
- An AI guide server computing the observation space and selecting actions in real time
- Guardian prescreening emphasizing task completion without outside help in the remote setting
#### Constraints
- The software did not explicitly check for students repeating the pretest or post-test; students with duplicate test-taking were excluded from analysis

### Target Learners
- elementary school students in grades 3-5 learning math at home remotely

### Learning Goals
- the concept of volume and its knowledge components (measurement and multiplication)

### Claims
- [Rl Narrative Tutor No Overall Gain](../claims/rl-narrative-tutor-no-overall-gain.md) [+M]
- [Rl Tutor Higher Engagement Low Pretest](../claims/rl-tutor-higher-engagement-low-pretest.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2023). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. https://arxiv.org/abs/2304.04933
