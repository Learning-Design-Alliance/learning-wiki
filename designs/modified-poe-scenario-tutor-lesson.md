---
type: design
id: modified-poe-scenario-tutor-lesson
aliases: [predict-observe-explain-scenario-tutor-lessons]
title: Modified predict-observe-explain cycle for scenario-based tutor lessons with pretest/posttest transfer scenarios
description: "A lesson-level design in which tutors work through authentic scenarios following a modified predict-observe-explain (POE) structure: they predict the best response via an open-ended question and an MCQ, explain their..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: danielle-r-thomas-2025
    resource: "https://doi.org/10.1145/3706468.3706531"
    title: "Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger. 2025. Do Tutors Learn from Equity Training and Can Generative AI Assess It?. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA. https://doi.org/10.1145/3706468.3706531"
    author: Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger
  - id: thomas-2025
    resource: "https://arxiv.org/abs/2506.17006"
    title: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. https://arxiv.org/abs/2506.17006"
    author: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R"
---

# Modified predict-observe-explain cycle for scenario-based tutor lessons with pretest/posttest transfer scenarios

> **Design** · [All designs](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 3 studies (3 causal), `q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
A lesson-level design in which tutors work through authentic scenarios following a modified predict-observe-explain (POE) structure: they predict the best response via an open-ended question and an MCQ, explain their prediction, observe the research-recommended approach with feedback, then complete a transfer scenario (posttest) in the same pattern. The article states these scenarios "follow a modified predict-observe-explain (POE) approach, theoretically connected to Gibbs' Reflective Cycle." Pretest and posttest each carry a maximum of four points, and learning gains are computed by subtracting pretest from posttest score.

## Design Implications

### Context
#### Requirements
- Two analogous scenarios (used interchangeably as pretest or posttest) aligned with research-recommended tutoring competencies
- open-ended and multiple-choice items at both predict and explain steps
- Scenarios presented during instruction must be counterbalanced with analogous posttest scenarios to control for difficulty, as the article states scenarios were "randomly assigned and counterbalanced".
#### Constraints
- Creating scenarios analogous in learning objectives yet different enough to capture genuine learning gains remains a complex task; the study observed difficulty imbalance between scenario batteries

### Target Learners
- novice and intermediate tutors (average self-reported experience 3.2 on a 5-point scale) in remote tutoring organizations
- college-student tutors in online tutor training

### Learning Goals
- recognizing when a student may be experiencing inequity
- applying strategies to help students advocate for themselves
- tutoring skills such as giving effective praise and responding to student errors

### Claims

- [In one single-group pretest-posttest study with no comparison group, tutors' pooled scores rose by a significant 7.4% after scenario-based tutor lessons; three lessons with established construct validity showed gains, while three newer lessons showed no significant gains](../claims/scenario-lessons-pooled-74-percent-gain.md) [+W]
- [Tutors showed a marginally significant improvement in performance from pretest to posttest after the equity-focused scenario-based lesson](../claims/equity-lesson-marginal-learning-gains.md) [+W]
- [Tutors' self-reported confidence in responding to students experiencing potential inequities increased significantly from pretest to posttest](../claims/tutor-confidence-increase-equity-training.md) [+W]
- [Tutors' learning scores rose from pre-test to post-test in the Jeremiah:Alexis order but fell slightly in the Alexis:Jeremiah order, in one uncontrolled pre-post study](../claims/scenario-order-interaction-learning-gains.md) [~W]
- Llm Feedback Tot Higher Posttest [+M]

## Related Designs

- [Modified predict-observe-explain (POE) instructional design for scenario-based tutor lessons](modified-poe-scenario-tutor-lessons.md)

## Examples
-

## Key Sources
- Danielle R. Thomas, Conrad Borchers, Sanjit Kakarla, Jionghao Lin, Shambhavi Bhushan, Boyuan Guo, Erin Gatz, and Kenneth R. Koedinger. 2025. Do Tutors Learn from Equity Training and Can Generative AI Assess It?. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA. https://doi.org/10.1145/3706468.3706531
- Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. https://arxiv.org/abs/2506.17006. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)

<!-- merged 2026-11-21 from designs/predict-observe-explain-scenario-tutor-lessons ("Scenario-based lessons with a modified predict-observe-explain cycle for tutor training"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Scenario-based lessons with a modified predict-observe-explain cycle for tutor training

> **Design** · [All designs](index.md)

## Description
The article's seven lessons follow "a modified predict-observe-explain model", which the authors describe as "a cyclical instructional approach that structures learning through experience". Learners see a scenario (e.g., a student math error), predict the best response via an open-response question and an MCQ, may request LLM feedback on the open response, explain their reasoning, observe research-based recommendations with delayed corrective feedback, explain again, and complete a four-point posttest on an analogous scenario. This lesson-level design pattern delivers scenario-based tutor skill practice in low-risk online environments.

## Design Implications

### Context
#### Requirements
- Scenarios presented during instruction must be counterbalanced with analogous posttest scenarios to control for difficulty, as the article states scenarios were "randomly assigned and counterbalanced".
#### Constraints
- 

### Target Learners
- college-student tutors in online tutor training

### Learning Goals
- tutoring skills such as giving effective praise and responding to student errors

### Claims
- Llm Feedback Tot Higher Posttest [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. https://arxiv.org/abs/2506.17006. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)
-->
