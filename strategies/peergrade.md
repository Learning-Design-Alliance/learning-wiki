---
type: strategy
title: Peergrade
description: A digital platform for structured, rubric-based anonymous peer feedback in which learners evaluate each other's work, rate the feedback received, and flag disagreements for teacher review.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Peergrade

> **Strategy** · [All strategies](index.md)

## Description
Peergrade is a platform that allows learners to give and receive feedback effectively. Learners anonymously offer different types of feedback using a rubric set by the teacher, which allows for some objective and some open feedback questions. The feedback receivers can then go through the feedback and react to it, rating the feedback itself and offering tips for improvement. In the case of disagreement, learners can flag responses so that teachers can intervene and respond to the feedback. The platform's core design move is to make peer feedback *structured* — the rubric constrains what reviewers attend to — and *accountable* — receivers evaluate the usefulness of the feedback they receive.

## Design Implications

Peer assessment works best when it is criterion-referenced rather than impressionistic: rubric-guided peer feedback produces feedback quality and learner outcomes comparable to instructor feedback in many contexts [~M], and the act of evaluating peers' work against criteria itself builds evaluative judgement — the ability to judge quality in one's own work [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]. Anonymity and the feedback-rating loop are the platform's distinctive contributions: anonymity reduces social-evaluative threat, and requiring receivers to rate feedback forces engagement with it rather than passive receipt.

### Context
#### Requirements
- Access to the Peergrade platform and reliable internet connectivity
- A clear rubric or set of success criteria, ideally with both closed (objective) and open (qualitative) items
- Structured class time for the full cycle: submission, review, receiving, and reacting to feedback
- A draft worth revising — peer feedback pays off when learners act on it in a subsequent revision

#### Constraints
- Requires access to technology and internet connectivity, which can exclude some learners or shift the activity toward logistics rather than critique
- Some learners may be hesitant to provide honest feedback due to fear of being identified, even in nominally anonymous settings, particularly in small classes where writing style is recognizable
- Novice reviewers often give vague or inaccurate feedback; without rubric scaffolding and exemplar calibration, peer comments can mislead receivers [~M]
- Feedback that is not acted upon produces little learning gain — the platform supports the exchange but cannot enforce revision
- Grading stakes distort behavior: when peer scores count toward grades, leniency bias and strategic scoring increase [~M]

#### Implementation Variability
- Rubrics can be customized to any content area, from writing to code review to design critique
- Feedback can be formative-only (revision-oriented) or contribute a small portion of assessment grades
- The feedback-rating step can be used as its own learning object: discussing why some comments were rated useful and others not builds criteria for quality feedback
- Teachers can intervene on flagged disagreements, turning disputes into whole-class teaching moments about criteria

### Target Learners
- High school and higher education students with enough literacy and domain exposure to interpret criteria and critique work
- Learners developing evaluative judgement; reviewing peers' work against a rubric helps them internalize quality standards [~M]
- Less suitable for young learners or novices so inexperienced that they cannot distinguish competent from incompetent work, since their feedback will be unreliable [~M]

### Target Learning Goals
- Improving work quality through revision informed by peer critique
- Critical thinking: analyzing others' work against explicit criteria
- Self-reflection and evaluative judgement: using criteria applied to peers' work as a mirror for one's own
- Feedback literacy: giving, receiving, and appraising feedback

### Instructions
1. Teacher creates an assignment and a rubric mixing objective criteria and open-ended prompts, aligned to the target learning goals ([Assess Performance](../elements/assess-performance.md)).
2. Learners submit their work by a deadline.
3. The platform distributes submissions anonymously; each learner reviews a small set of peers' work, answering rubric questions ([Provide Feedback](../elements/provide-feedback.md)).
4. Receivers read their feedback, rate its helpfulness, and reply with clarifications or improvement tips ([Peer Discussion](../elements/peer-discussion.md)).
5. Disagreements or inappropriate feedback are flagged; the teacher reviews flags and intervenes where needed.
6. Learners revise their work using the feedback; the teacher reviews the feedback quality and ratings as formative evidence.

## Related Strategies
- Structured peer review more broadly — Peergrade is one platform implementation of the general peer assessment strategy; the design principles (rubrics, anonymity, feedback appraisal) transfer to any tool.

## Related Elements
- [Assess Performance](../elements/assess-performance.md) — the rubric-based evaluation step that structures what reviewers attend to
- [Collaboration](../elements/collaboration.md) — peer feedback is a structured form of learner-to-learner collaboration
- [Feedback](../elements/feedback.md) — the core mechanism; the platform adds anonymity and an appraisal loop to it

## Tools
- [Peergrade / Peergrade.io](https://www.peergrade.io) — the platform itself (now part of [FeedbackFruits](https://feedbackfruits.com)), offering rubric creation, anonymous distribution, feedback ratings, and flagging

## Examples
- A high school teacher uses Peergrade to facilitate peer feedback on writing assignments, allowing learners to provide anonymous and rubric-based critique, then revise their drafts before final submission.
- A university instructor runs a two-stage cycle: learners first rate sample essays against the rubric to calibrate, then review live peers' submissions; the instructor discusses highly-rated and poorly-rated feedback in class to build criteria for quality critique.

## Key Sources
- Topping, K. (1998). Peer assessment between students in colleges and universities. *Review of Educational Research, 68*(3), 249–276. [doi:10.3102/00346543068003249](https://doi.org/10.3102/00346543068003249)
- Falchikov, N., & Goldfinch, J. (2000). Student peer assessment in higher education: A meta-analysis comparing peer and teacher marks. *Review of Educational Research, 70*(3), 287–322. [doi:10.3102/00346543070003287](https://doi.org/10.3102/00346543070003287)
- Double, K. S., McGrane, J. A., & Hopfenbeck, T. N. (2020). The impact of peer assessment on academic performance: A meta-analysis of control group studies. *Educational Psychology Review, 32*, 481–509. [doi:10.1007/s10648-019-09510-3](https://doi.org/10.1007/s10648-019-09510-3)
- Panadero, E., & Alqassab, M. (2019). An empirical review of anonymity in educational assessment: The effects of anonymity on peer assessment. *Educational Psychology Review, 31*, 1043–1077. [doi:10.1080/02602938.2019.1600186](https://doi.org/10.1080/02602938.2019.1600186)
