---
type: strategy
title: Calibrated Peer Review
description: A structured peer assessment process in which learners first evaluate benchmark samples to calibrate their judgment, then review peers' work and receive reviews of their own.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Calibrated Peer Review

> **Strategy** · [All strategies](index.md)

## Description
Calibrated Peer Review (CPR) is a peer assessment strategy in which learners first evaluate benchmark samples of work — typically strong, average, and weak exemplars — and compare their judgments against expert ratings. Only after demonstrating acceptable calibration do they review peers' work and receive reviews of their own. The calibration phase converts peer review from an unstructured exchange into a training sequence for evaluative judgment.

## Design Implications

Calibration addresses the central weakness of peer review — untrained reviewers give unreliable feedback — by building evaluative skill before it is applied [~M]. Comparing one's own ratings against expert ratings on the same artifacts provides immediate feedback on judgment quality, and the exemplar comparison itself supports abstraction of quality criteria [Multiple contrasting cases support abstraction of criteria.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]. Reviewing others' work also prompts self-explanation and comparison with one's own drafts, which can improve the reviewer's own performance as much as receiving feedback does [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]. The strategy thus enacts [Assessment for Learning](../principles/assessment-for-learning.md): the assessment activity itself is the learning activity.

### Context
#### Requirements
- A set of benchmark artifacts with expert ratings (typically 3+, spanning quality levels)
- An explicit rubric or criteria list used consistently across calibration, review, and self-review
- A mechanism for comparing reviewer judgments to expert judgments and gating progression on calibration accuracy
- Multiple peer reviews per artifact (3–5) so that unreliable individual judgments average out

#### Constraints
- Calibration on exemplars does not transfer well when peer submissions differ substantially from the benchmark genre or difficulty [~M]
- Reviewer reliability remains low for highly subjective or tacit-criteria domains (e.g., creative voice) even after calibration [-M]
- Students with weak prior knowledge may calibrate superficially — matching surface features of exemplars rather than underlying quality — and then apply those surface heuristics to peers [-M]
- The expertise reversal pattern applies: highly structured calibration scaffolds can burden learners who already possess evaluative skill [Guidance that helps novices can reduce performance for experts.](../claims/expertise-reversal-effect.md) [~M]
- Grade-bearing peer review invites gaming (lenient collusion, retaliatory scoring); formative-only use reduces but does not eliminate this [-M]

#### Implementation Variability
- **Gated vs. open calibration**: require passing a calibration threshold before reviewing, or allow all students to proceed with calibration feedback in hand
- **Self-review inclusion**: have students apply the same rubric to their own draft before submission, aligning self-assessment with the peer process
- **Feedback-only vs. grade-bearing**: peer ratings can inform grades or serve purely formative purposes; formative use reduces gaming incentives
- **Domain adaptation**: used for writing (e.g., the original Calibrated Peer Review system in chemistry), code review, design critique, and clinical case evaluation

### Target Learners
- Undergraduate and graduate students producing complex artifacts (papers, designs, code) where quality criteria are learnable through exemplars
- Novice evaluators benefit most from the calibration phase; experienced practitioners in the domain may find it redundant [Guidance that helps novices can reduce performance for experts.](../claims/expertise-reversal-effect.md) [~M]
- Large-enrollment courses where instructor feedback capacity is the bottleneck

### Target Learning Goals
- Evaluative judgment: internalizing what distinguishes strong from weak work
- Domain concepts: diagnosing strengths and flaws in others' work deepens understanding of the criteria themselves
- Feedback literacy: interpreting, filtering, and acting on feedback received [Feedback is most effective when directed at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- Self-regulation: comparing one's own work against criteria and peer work

### Instructions
1. **Publish criteria and exemplars.** Provide the rubric plus 3+ benchmark artifacts spanning quality levels, with expert ratings hidden initially.
2. **Calibrate.** Students evaluate each benchmark artifact against the rubric, then see expert ratings and the rationale; require a minimum agreement score before proceeding.
3. **Review peers.** Assign each student 3–5 anonymized peer submissions; require criterion-referenced comments, not just scores, since process-level comments drive improvement [Feedback is most effective when directed at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
4. **Self-review.** Students apply the same rubric to their own submission, ideally before seeing peer comments ([Self-Assessment](../elements/self-assessment.md)).
5. **Receive and reflect.** Students receive aggregated peer feedback, rate the helpfulness of each review, and revise. Rating reviews builds reviewer accountability.
6. **Close the loop.** Instructor spot-checks review quality and addresses systematic misreadings of the rubric in class.

## Related Strategies
- [Rubric-Based Assessment](rubric-based-assessment.md) — the rubric is the shared instrument that makes calibration possible
- [Worked Examples](worked-examples.md) — benchmark exemplars function as worked examples of evaluative judgment
- [Reciprocal Peer Critique](reciprocal-peer-critique.md) — a lighter-weight variant without the calibration gate

## Examples
- **Calibrated Peer Review™ (CPR)** ([https://cpr.molsci.ucla.edu](https://cpr.molsci.ucla.edu)) — UCLA-originated web system originally developed for chemistry writing assignments; implements the full calibrate → review → self-review → back-review cycle.
- **SWoRD (Scaffolded Writing and Rewriting in the Discipline)** — University of Pittsburgh system in which students review writing samples for calibration, then review peers' drafts with review quality itself rated by recipients [Cho & Schunn, 2007](https://doi.org/10.1016/j.compedu.2005.02.004).
- **Peergrade / PeerStudio-style MOOC assessment** — large online courses use calibration on graded sample submissions before releasing peer grading at scale.

## Key Sources
- Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science, 18*(2), 119–144. [doi:10.1007/bf00117714](https://doi.org/10.1007/bf00117714)
- Topping, K. (1998). Peer assessment between students in colleges and universities. *Review of Educational Research, 68*(3), 249–276. [doi:10.3102/00346543068003249](https://doi.org/10.3102/00346543068003249)
- van Zundert, M., Sluijsmans, D., & van Merriënboer, J. (2010). Effective peer assessment processes: Research findings and future directions. *Learning and Instruction, 20*(4), 270–300. [doi:10.1016/j.learninstruc.2009.08.004](https://doi.org/10.1016/j.learninstruc.2009.08.004)
- Gielen, S., Dochy, F., & Onghena, P. (2011). An inventory of peer assessment diversity. *Assessment & Evaluation in Higher Education, 36*(2), 137–155. [doi:10.1080/02602930903221444](https://doi.org/10.1080/02602930903221444)
- Cho, K., & Schunn, C. D. (2007). Scaffolded writing and rewriting in the discipline: A web-based reciprocal peer review system. *Computers & Education, 48*(3), 409–426. [doi:10.1016/j.compedu.2005.02.004](https://doi.org/10.1016/j.compedu.2005.02.004)