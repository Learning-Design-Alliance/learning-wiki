---
type: pattern
id: learner-experience-design
title: Learner Experience Design (LXD)
description: A user-centred course design process that treats usability as a pedagogical property rather than presentation polish — investigating learners, prototyping the experience, and testing it with real users, on the argument that effort spent operating the material is effort not spent learning.
status: review
generated:
  by: claude/unspecified
  at: 2026-09-02
author: Schmidt, Earnshaw, Tawfik and Jahnke lineage
grain_size: course
---

# Learner Experience Design (LXD)

> **Pattern** · [All patterns](index.md)

## Description
Learner Experience Design imports the methods of user-centred design — user research, personas and scenarios, prototyping, usability testing, heuristic evaluation — into instructional design, and makes one substantive claim while doing it: **usability is not polish applied after the instruction, it is part of the instruction.**

The argument is a cognitive-load argument. Every unit of attention a learner spends working out where the next activity is, what the interface expects, or which of four similarly-named files is this week's, is attention not spent on the material. That cost is structurally identical to any other source of extraneous load, so a navigational problem and a badly-designed diagram damage learning by the same mechanism. Treating the first as a "UX issue" and the second as an "instructional issue" is an organisational convention, not a distinction the learner experiences.

This reframes what a usability test is *for*. In product design a usability test asks whether people can complete a task. In LXD it asks that and then asks what the difficulty cost them instructionally — which is why LXD's version is run with real learning tasks and real content, not with a clickable shell and invented data.

LXD inherits the empathize-and-test moves from [Design Thinking](design-thinking.md) and adds method: specific instruments for finding out what learners experience, and specific criteria for judging it.

## Implications

### Context
#### Requirements
- **Access to representative learners for testing** — five or six is usually enough to find the serious problems, but they must be from the actual audience, not colleagues
- **A prototype that can be operated**, not described. Usability findings come from watching someone try, not from asking someone to imagine
- **Real content in the test.** Lorem-ipsum prototypes surface interface problems and hide instructional ones
- **Willingness to change structure, not only surface.** If only cosmetic changes are permitted the testing will produce cosmetic findings

#### Constraints
- **Usable is not the same as effective.** A course can be perfectly navigable and teach nothing; optimising for ease of use alone selects against desirable difficulty. Retrieval practice, spacing and productive struggle all feel worse in a usability session and produce better learning
- **Satisfaction is a weak proxy.** Learner ratings track fluency, and fluency is exactly the cue that misleads — the finding [Fluent Illusions Mislead Self Assessment](../claims/fluent-illusions-mislead-self-assessment.md) [~S] records
- **Small-sample qualitative work invites over-reading.** Five learners reliably find usability problems; they do not establish learning effects
- **Method cost.** Recruiting, running and analysing sessions is real effort competing with content production, and is the first thing cut

#### Grain Size
- Course
- Module
- Programme (where the experience crosses course boundaries — enrolment, navigation, assessment rhythm)

### Target Goals
- Self-paced and online courses, where no instructor is present to absorb the confusion an unclear design creates
- Redesigns where completion or engagement is failing and the instructional content is not obviously the cause
- Any design whose learners differ from its designers in access, device, language or confidence

### Target Learners
- Learners with low prior familiarity with the platform or the genre of the course, who bear the largest share of interaction cost
- Learners whose constraints are situational — intermittent connectivity, a phone rather than a laptop, study time in fragments. These are experience problems before they are instructional ones, and only user research surfaces them

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — supplies the argument that makes usability pedagogical rather than cosmetic
- [Situated Learning](../theories/situated-learning.md) — the learner's context is part of the design problem, not noise around it
- [Cultural-Historical Activity Theory](../theories/cultural-historical-activity-theory.md) — tools, rules and community as constituents of the experience being designed

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — desirable difficulty and productive struggle are experiences a usability frame reads as defects

### Claims
#### Supporting
- [Cognitive Load Reduction Improves Learning](../claims/cognitive-load-reduction-improves-learning.md) [+S] — the mechanism the whole argument rests on
- [Coherence Principle Irrelevant Material Hurts Learning](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S] — decoration that costs attention harms learning, which is the usability case stated instructionally
- [Mismatched Graphic Organizers Increase Extraneous Load](../claims/mismatched-graphic-organizers-increase-extraneous-load.md) [+M] — a representation that does not fit the content taxes the learner even when it looks professional

#### Contradicting
- [Fluent Illusions Mislead Self Assessment](../claims/fluent-illusions-mislead-self-assessment.md) [~S] — a smoother experience produces higher confidence and does not, on its own, produce more learning
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — the support that makes a course usable for a newcomer becomes interference for a returning learner

## Design

### Sequence
1. **User research** — interviews, observation, diary or context inquiry with real learners. [Learner and Context Analysis](../strategies/learner-and-context-analysis.md), [Student Shadowing](../strategies/student-shadowing-for-educator-insights.md)
2. **Model the learner** — [Learner Personas](../strategies/learner-personas.md), and where the context matters more than the individual, [personas situated in an activity system](../strategies/activity-system-personas.md); write the scenarios the design must serve
3. **Set experience criteria alongside learning objectives** — what a learner must be able to find, operate and complete, stated as testably as the objectives are
4. **Prototype the experience** — a walkthrough of a whole week, with real content, at the fidelity needed to be tried
5. **Usability-test with real learners** — think-aloud on genuine learning tasks; record where effort goes, not only whether the task completes
6. **Heuristic and accessibility review** — a structured expert pass catching what small-sample testing misses; accessibility conformance belongs here and is not optional
7. **Revise and re-test** — then hand the instrumentation to [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md), which carries the same questions past release

### Elements Used
- [Audience Analysis](../elements/audience-analysis.md)
- [Think Aloud](../elements/think-aloud.md)
- [Learning Analytics Feedback](../elements/learning-analytics-feedback.md)

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md)

### Personalization
- **Where learners cannot be recruited**, run the walkthrough with proxies and label the findings as proxy findings; an instructor imagining a learner is evidence about the instructor
- **Where the platform is fixed**, the design work moves to what you control — naming, sequencing, chunking, the first five minutes of each week — which is where most avoidable interaction cost lives anyway
- **For expert or returning audiences**, test for the opposite failure: scaffolding, hand-holding and mandatory sequencing that a competent learner has to fight through

## Related Patterns
- [Design Thinking](design-thinking.md) — the parent process; LXD is its empathy and testing moves with instruments attached
- [Successive Approximation Model](successive-approximation-model.md) — supplies the iteration cadence LXD's test-and-revise loop needs
- [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md) — the same questions after release, answered with usage data
- [Online Course Design](online-course-design.md)
- [Systematic Instructional Design](systematic-instructional-design.md) — the derivation chain LXD assumes someone else has built; the two are complements, not rivals

## Examples
- **Online programme redesign** — usability sessions revealing that low completion tracked navigation and assessment-deadline confusion rather than content difficulty
- **Mobile-first course delivery** — device research changing chunk length, file formats and offline availability before any content was written

## Key Sources
- Schmidt, Earnshaw, Tawfik, & Jahnke. EdTech Books. [https://edtechbooks.org/eme_6606](https://edtechbooks.org/eme_6606)
- Jahnke et al. EdTech Books. [https://edtechbooks.org/eme_6606](https://edtechbooks.org/eme_6606)

<!-- Chapter titles, editors and publication years for the two entries above were
     not recorded: this wiki's sandbox cannot reach edtechbooks.org, and the
     brief that commissioned this page named the authors and the URL only.
     A field left empty says "not established"; a plausible field invented here
     would say "verified" and be worth nothing. -->
