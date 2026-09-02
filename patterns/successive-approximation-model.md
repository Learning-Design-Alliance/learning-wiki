---
type: pattern
id: successive-approximation-model
title: Successive Approximation Model (SAM)
description: An iterative, agile course design process that replaces a single analyse-build-evaluate pass with short rounds of design, prototype and review, starting from a collaborative Savvy Start and converging on a design by repeated approximation rather than by up-front specification.
status: review
generated:
  by: claude/unspecified
  at: 2026-09-02
author: Michael W. Allen
grain_size: course
---

# Successive Approximation Model (SAM)

> **Pattern** · [All patterns](index.md)

## Description
SAM is an iterative design process for courses, formulated by Michael Allen as an explicit alternative to running [ADDIE](systematic-instructional-design.md) as a waterfall. Its argument is empirical rather than philosophical: the phases of a systematic process are all sound, but performing each one *completely* before starting the next means the first real evidence about whether the design works arrives after the budget is spent.

SAM keeps the same activities and re-orders them into short cycles. Each cycle produces something reviewable — a sketch, a prototype, a working module — and each review is allowed to change the design. Convergence is by **successive approximation**: the design is deliberately rough early, and the roughness is the point, because a rough artifact is cheap to reject.

The process opens with a **Savvy Start**: a short, intensive session in which stakeholders, subject-matter experts and designers sketch and critique candidate designs together, rather than the designer interviewing them and going away to write a specification. Later cycles alternate design–prototype–review, with development running behind design rather than after it.

Where the scope itself is unsettled, SAM is the wrong tool and [Design Thinking](design-thinking.md) is the right one: SAM iterates *within* an agreed problem, and assumes the goals are broadly known even when the design is not.

## Implications

### Context
#### Requirements
- **Stakeholders who will show up repeatedly.** The process substitutes recurring short reviews for one long specification, and collapses to a waterfall without them
- **Tolerance for visibly unfinished work.** A reviewer who reads a rough prototype as a poor product will drive the team back to specifying up front
- **A team that can prototype quickly** — storyboards, clickable shells, one built module
- **A change budget.** Iteration is only real if review findings are allowed to alter the design after work has been done

#### Constraints
- **Scope creep is the standing risk.** Each review is an invitation to add, and without an agreed scope the cycles do not converge
- **Poor fit for a fixed, auditable derivation chain.** Where an accreditor needs objective-to-item traceability, the systematic process produces that artifact and SAM does not, by design
- **Rework is real cost, not waste avoided.** SAM trades late expensive rework for early cheap rework; where the analysis is genuinely reliable up front, that trade loses
- **Depends on review quality.** Reviews that collect preference rather than performance evidence steer the design confidently in the wrong direction — the same failure [Feedback is most effective when directed at the task and process rather than the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] names for learners
- **Distributed or asynchronous teams** lose most of the Savvy Start's value, which comes from co-present sketching and immediate critique

#### Grain Size
- Course
- Module
- Programme (run per course, coordinated across)

### Target Goals
- Designs where the requirement is understood but the right solution is not
- Projects with real delivery deadlines, where a partially-complete but working design beats a complete specification
- Redesigns of courses that are known to be failing, where the failure's cause is contested

### Target Learners
- Any; SAM constrains the design *process*, not the audience. Its learner-facing leverage is indirect — the early cycles put a prototype in front of real learners sooner, so learner evidence reaches the design while it can still be acted on

### Theory
#### Supporting
- [Design Layers Theory](../theories/design-layers-theory.md) — a design decomposed into layers that can be revised at different rates is what makes iteration tractable
- [Designerly Stances](../theories/designerly-stances.md)

#### Contradicting / Qualifying
- [Behaviorism](../theories/behaviorism.md) — the criterion-referenced tradition assumes objectives are fixed before design begins, which SAM deliberately relaxes

### Claims
#### Supporting
- [Feedback is most effective when directed at the task and process rather than the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — the standard each review cycle has to meet
- [Goal setting improves performance.](../claims/goal-setting-improves-performance.md) [~M] — iteration does not remove the need for a target; it defers how precisely it is specified

#### Contradicting
- [Guidance becomes more necessary as task complexity and learner inexperience increase.](../claims/expertise-reversal-effect.md) [-M] — a design team without instructional expertise iterates without a criterion, and repeated approximation converges on whatever the loudest reviewer prefers

## Design

### Sequence
1. **Preparation** — gather background and known constraints; keep it short. This is information collection, not analysis-to-completion
2. **Savvy Start** — stakeholders, subject-matter experts and designers sketch, critique and reject candidate designs in one session. Expect several designs to be discarded; that is the deliverable
3. **Iterative design** — cycles of *design → prototype → review*. Each cycle is short and produces something a reviewer can react to
4. **Iterative development** — cycles of *develop → implement → evaluate*, overlapping the design cycles rather than following them. Alpha, beta and gold releases mark convergence, not phases
5. **Roll out**, with the evaluation instrumentation already built in — see [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md) for what happens next

### Elements Used
- [Learning Objectives](../elements/learning-objectives.md) — sharpened across cycles rather than fixed at the start
- [Formative Assessment](../elements/formative-assessment.md)
- [Iterative Learning](../elements/iterative-learning.md)

### Affordances
- [Formative Assessment](../principles/formative-assessment.md)

### Personalization
- **Two-phase variant.** Allen distinguishes a lighter form for small projects — preparation plus a single iterative design-and-develop phase — from the fuller form that separates design and development cycles. Choose by whether development is expensive enough to deserve its own loop
- **Where stakeholders cannot convene**, replace the Savvy Start with a sequence of short paired reviews and accept slower convergence; do not replace it with a written specification, which reintroduces the failure the process exists to avoid
- **Where an audit trail is required**, run SAM for the design and generate the objective-to-assessment map as a release artifact at gold, rather than as the design's starting point

## Related Patterns
- [Systematic Instructional Design](systematic-instructional-design.md) — the process SAM was formulated against; its phases survive, its ordering does not
- [Design Thinking](design-thinking.md) — iterates the problem statement as well as the solution; SAM keeps the problem fixed
- [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md) — the same iterative logic applied after release, driven by usage data
- [Learner Experience Design](learner-experience-design.md) — supplies the evaluation methods the review cycles need

## Examples
- **Corporate e-learning production** — the setting SAM was developed in, where fixed delivery dates and shifting subject-matter make a full up-front specification unaffordable
- **Course redesign with a live cohort** — successive rounds released to consecutive cohorts, each informed by the last

## Key Sources
- Cullen. Ch. 26 in *Design for Learning*. EdTech Books. [https://edtechbooks.org/id/agile_design](https://edtechbooks.org/id/agile_design)
- Allen, M. W. (2012). *Leaving ADDIE for SAM*. ASTD Press.
