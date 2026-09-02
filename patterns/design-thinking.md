---
type: pattern
id: design-thinking
title: Design Thinking
description: A course-grain design process — empathize, define, ideate, prototype, test — in which a learning experience is built from investigated learner need rather than from a content outline, and revised against evidence from learners before it is finalized.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-02
author: Stanford d.school (Hasso Plattner Institute of Design) lineage
grain_size: course
---

# Design Thinking

> **Pattern** · [All patterns](index.md)

## Description
Design Thinking organizes the *design* of a course around five moves: empathize with the people who will learn, define the problem their situation actually poses, ideate broadly before committing, prototype cheaply, and test with real learners. Its defining commitment is that the design problem is discovered rather than assumed — the designer begins by investigating learners and their context, and treats the first course outline as a hypothesis to be falsified rather than a plan to be executed.

This makes it a sibling of the other whole-course design processes in this wiki and a contrast to them. Where a [systematic design process](systematic-instructional-design.md) fixes objectives early and derives everything downstream from them, and [Successive Approximation](successive-approximation-model.md) iterates within an agreed scope, design thinking keeps the problem statement itself revisable for longer, which is its strength on ill-defined problems and its weakness where the outcome is already settled by a standard or a regulator.

The same five moves are also used *with learners* — students empathizing with users and prototyping solutions as the work of a course. That reading is the deprecated [Design Thinking strategy](../strategies/design-thinking.md) page, kept for history; when learners run the cycle, the course is applying this pattern to them rather than being designed by it.

## Implications

### Context
#### Requirements
- **Access to learners before the design is fixed** — interviews, observation, or shadowing. Without it the "empathize" move degrades into the designer's own assumptions with a research vocabulary attached
- **Permission for the problem statement to change** — a sponsor who has already fixed the outcome is buying a different process
- **Cheap prototyping** — a storyboard, a paper walkthrough, one lesson built rough enough to throw away
- **At least one real test-and-revise cycle** before the design is committed

#### Constraints
- **Weak where the outcome is externally fixed.** Compliance, licensure and standards-aligned work start from a mandated goal set; the empathize–define moves have little to bite on, and a [standards crosswalk](../strategies/standards-crosswalk.md) is the honest starting point instead
- **The empathy stage produces shallow insight without interview skill**, and shallow insight is more dangerous than none because it is documented
- **Ritual risk**: teams pass through five labelled stages without any iteration, producing an engaging workshop and an unchanged design
- **Costly at small grain.** For one lesson the full cycle rarely pays; the process assumes a design large enough that being wrong about the problem is expensive
- **Divergent ideation is not a substitute for domain knowledge.** Novice designers generating options without knowing what is instructionally sound reproduce the search cost that [guidance becomes more necessary as task complexity and learner inexperience increase.](../claims/expertise-reversal-effect.md) [-S] describes, one level up

#### Grain Size
- Course
- Unit
- Programme (where the unit of redesign is a whole learner journey)

### Target Goals
- A design whose goals were derived from an investigated need rather than inherited from an existing syllabus
- Early detection of a wrong problem statement, when correcting it is still cheap
- Designs for ill-defined situations — a new audience, an unfamiliar context, a course that has been failing for reasons nobody has named

### Target Learners
- Audiences the design team does not already belong to, where assumed need and actual need diverge most
- Contexts where the barrier is situational rather than instructional — access, time, belonging — which a content-first process does not look for

### Theory
#### Supporting
- [Situated Learning](../theories/situated-learning.md) — the design problem is treated as inseparable from the context it sits in
- [Cultural-Historical Activity Theory](../theories/cultural-historical-activity-theory.md) — supplies the vocabulary for what "context" contains when empathy work is done seriously rather than as sentiment
- [Designerly Stances](../theories/designerly-stances.md)

#### Contradicting / Qualifying
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — open exploration is expensive for a novice, and that holds for novice *designers* too; the process presumes enough instructional expertise to evaluate the options it generates

### Claims
#### Supporting
- [Multiple varied cases support learning in ill-structured domains.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M] — the case for encountering several framings of a problem before committing to one
- [Feedback is most effective when directed at the task and process rather than the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — what makes a prototype test informative rather than a popularity check

#### Contradicting
- [Guidance becomes more necessary as task complexity and learner inexperience increase.](../claims/expertise-reversal-effect.md) [-S] — minimally guided design work overloads inexperienced designers the same way it overloads novice learners

## Design

### Sequence
1. **Empathize** — investigate the learners and their situation directly. [Learner and Context Analysis](../strategies/learner-and-context-analysis.md), [Needs Analysis](../strategies/needs-analysis.md), and [Student Shadowing](../strategies/student-shadowing-for-educator-insights.md) are the concrete practices; interview protocols matter more than interview quantity
2. **Define** — state the design problem as a point of view about a specific learner, and write down what would make it false. [Learner Personas](../strategies/learner-personas.md) and [personas situated in an activity system](../strategies/activity-system-personas.md) hold the finding in a form the rest of the design can be checked against
3. **Ideate** — generate several structurally different designs before evaluating any, so the first workable idea does not become the only one considered
4. **Prototype** — build the cheapest artifact that can be wrong in public: a storyboard, one rough lesson, a walkthrough of the assessment
5. **Test** — put it in front of real learners and collect task- and process-level evidence, not preference ratings. [Formative Evaluation](../strategies/formative-evaluation.md) is the established form of this move
6. **Iterate** — return to whichever earlier move the evidence indicts, including the problem statement

### Elements Used
- [Audience Analysis](../elements/audience-analysis.md)
- [Learning Objectives](../elements/learning-objectives.md) — written *after* the define stage rather than before it
- [Formative Assessment](../elements/formative-assessment.md)

### Affordances
- [Formative Assessment](../principles/formative-assessment.md)

### Personalization
- **Sprint form** — a compressed one- or two-day cycle trades depth of empathy work for a complete pass through the process; useful for teams learning the process, weak as the sole basis for a real design
- **Where learners are unreachable**, substitute secondary evidence honestly and mark it as such: prior cohort data, support tickets, instructor accounts. Do not let a persona built from those read as one built from interviews
- **Where the goals are externally fixed**, run the cycle on the *instruction* rather than the goals: the crosswalk fixes what must be learned, and empathy work still decides how

## Related Patterns
- [Systematic Instructional Design](systematic-instructional-design.md) — the objective-first contrast; strongest where design thinking is weakest
- [Successive Approximation Model](successive-approximation-model.md) — shares the iterate-and-prototype commitment but keeps the problem statement fixed
- [Learner Experience Design](learner-experience-design.md) — the closest sibling; LXD inherits design thinking's empathy and testing moves and adds usability method
- [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md) — what happens after a design ships, where design thinking's test move becomes permanent
- [Understanding by Design](understanding-by-design.md) — an outcome-first process; see also [Backward Design](../strategies/backward-design.md)

## Examples
- **Stanford d.school K12 Lab** (https://dschool.stanford.edu) — publishes design challenge curricula and the compressed "wallet project" sprint
- **IDEO Design Kit** (https://www.designkit.org) — the Field Guide to Human-Centered Design, used to structure empathy and prototyping work in education and community programmes

## Key Sources
- Dym, C. L., Agogino, A. M., Eris, O., Frey, D. D., & Leifer, L. J. (2005). Engineering design thinking, teaching, and learning. *Journal of Engineering Education, 94*(1), 103–120. [doi:10.1002/j.2168-9830.2005.tb00832.x](https://doi.org/10.1002/j.2168-9830.2005.tb00832.x)
- Razzouk, R., & Shute, V. (2012). What is design thinking and why is it important? *Review of Educational Research, 82*(3), 330–348. [doi:10.3102/0034654312457429](https://doi.org/10.3102/0034654312457429)
- Dorst, K. (2011). The core of 'design thinking' and its application. *Design Studies, 32*(6), 521–532. [doi:10.1016/j.destud.2011.07.006](https://doi.org/10.1016/j.destud.2011.07.006)
