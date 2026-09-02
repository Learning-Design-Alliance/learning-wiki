---
type: strategy
id: activity-system-personas
title: Activity-System Personas and Scenarios
description: Building learner personas and design scenarios around the activity system a learner acts within — object, mediating tools, rules, community and division of labour — so that the design responds to what constrains the learner rather than to who they are demographically.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-02
---

# Activity-System Personas and Scenarios

> **Strategy** · [All strategies](index.md)

## Description
An ordinary [learner persona](learner-personas.md) describes a person: age, background, prior knowledge, goals, a photograph and a name. It is a real improvement on designing for nobody, and it has a characteristic weakness — it locates every design-relevant fact *inside the learner*. Read back later, it invites explanations of the form "Maria struggles because she is not confident", and confidence is not something a course can be pointed at.

An activity-system persona describes the same learner as a **subject acting on an object within a system**, using the vocabulary of [Cultural-Historical Activity Theory](../theories/cultural-historical-activity-theory.md):

- **Object** — what the learner is actually trying to accomplish, which is frequently not the course's stated outcome. Passing, keeping a job, satisfying a supervisor, getting through the week
- **Mediating tools** — the device, the connection, the software, the notation, the language of instruction. What they have, not what the design assumes
- **Rules** — deadlines, attendance policies, assessment regulations, workplace shift patterns, family obligations
- **Community** — who else is in this with them: cohort, family, colleagues, supervisor, the people whose opinion of them is at stake
- **Division of labour** — who does what, and what is expected of the learner specifically as against the instructor, the peer group or the employer

The design payoff is that this account produces **actionable findings**. "Maria's object is keeping her supervisor satisfied, her tool is a phone on an intermittent connection, and the rule that binds is a Friday shift that collides with the synchronous session" names three things a designer can change. "Maria is not confident" names none.

**Scenarios then narrate a contradiction, not a happy path.** A UX scenario usually walks a persona through a successful task. The version worth writing here narrates a point where the system's own elements pull against each other — the assessment rule against the shift pattern, the tool against the collaboration requirement — because that is where a design either accommodates the learner or loses them. In CHAT's terms these are the system's *contradictions*, and they are where change originates.

## Design Implications

### Context
#### Requirements
- **Real contact with learners.** The whole method is a way of *recording* what user research found. Written from the designer's imagination it produces a fluent sociological fiction, which is worse than a thin honest persona because it reads as evidence
- **Interviews that ask about the surrounding situation**, not only about the subject: how study time is found, on what device, around what obligations, and who else has a claim on the outcome
- **Enough learners to see variation.** One activity system is a case; the value is in the two or three genuinely different systems a cohort contains
- **A design with room to respond.** Naming a rule the design cannot change is worth doing once, as a constraint, and is otherwise demoralising documentation

#### Constraints
- **Heavier than a standard persona.** Six dimensions, evidenced, per persona; the cost only pays where context is genuinely doing the work
- **Theoretical vocabulary is a barrier.** "Division of labour" on a workshop wall will be ignored or misread; rename the boxes for the team and keep the analysis
- **Composites can smuggle in stereotype.** Building "the working parent" from two interviews and a preconception produces a persona nobody can argue with because nobody exists to contradict it. Keep each persona traceable to the sessions behind it
- **A persona is a design instrument, not a finding about a population** — it does not license claims about how common anything is
- **Fixing the system statically misses the point.** Activity systems change, and the learner's object frequently changes mid-course; a persona written in week zero can be false by week six

#### Implementation Variability
- **Lightweight** — add object, tools and rules to an existing persona template and leave community and division of labour out until they earn a place
- **Full six-element** analysis with a drawn triangle per persona, used where the design crosses institutions — school and workplace, course and employer
- **Contradiction-first** — skip the persona and write the two or three contradictions the cohort reports, each with the learners it applies to. Faster, and often where the design work actually is
- **Boundary-crossing pairs** — two systems mapped side by side, for designs that move learners between them, with the boundary objects that must hold meaning in both

### Target Learners
- Designers serving learners whose barriers are situational rather than cognitive — access, time, competing obligations, workplace rules
- Work-based, community-partnered and boundary-crossing designs, where the learner is simultaneously a member of another system with its own object and rules
- Cohorts unlike the design team, where the assumed context is most likely to be wrong
- Less useful for a homogeneous cohort in a single, well-understood setting, where a conventional persona carries the same information for less effort

### Target Learning Goals
- Design decisions that respond to constraint: pacing, modality, assessment timing, group composition, offline availability
- An explicit record of which learners a design has decided not to serve, and why — a decision that is otherwise made silently
- Scenarios usable as test cases in a usability or walkthrough session, rather than as illustration

### Instructions
1. **Interview and observe** real learners, asking about the surrounding activity as much as the learning. [Learner and Context Analysis](learner-and-context-analysis.md), [Student Shadowing](student-shadowing-for-educator-insights.md), and empathy interviews are all suitable sources
2. **For each participant, record the six elements**: object, mediating tools, rules, community, division of labour, and the subject's own account of the difficulty. Quote where you can
3. **Cluster by system, not by demographics.** Two learners with nothing biographical in common but the same object and the same binding rule belong to one persona; two learners of the same age and background with different objects do not
4. **Write each persona** as a subject-in-a-system, with each element traceable to the sessions behind it. Mark anything inferred rather than heard as inferred
5. **Name the contradictions** — where the elements of one persona's system pull against each other, or against what the course requires
6. **Write one scenario per contradiction**, narrating what the learner does when it bites: what they try, what they give up, what the course sees. Give the scenario an outcome, including the bad one
7. **Turn each contradiction into a design decision** — accommodate, mitigate, or explicitly decline — and record the decision beside it
8. **Test with the scenarios.** They are the cases a walkthrough or usability session should run, in preference to invented happy paths
9. **Revisit after a cohort.** A persona that no learner recognises is a hypothesis that failed, and should be corrected rather than kept for the deck

## Related Strategies
- [Learner Personas](learner-personas.md) — the base practice this extends; use it where context is not the problem
- [Learner and Context Analysis](learner-and-context-analysis.md) — the analysis step that feeds this
- [Student Shadowing](student-shadowing-for-educator-insights.md) — the observational source that most reliably surfaces rules and division of labour
- [Needs Analysis](needs-analysis.md)
- [Cognitive Task Analysis](cognitive-task-analysis.md) — the same commitment to eliciting what is not volunteered, aimed at expertise rather than at context

## Examples
- **Work-based and apprenticeship programmes** — the learner is simultaneously an employee, and the employer's object regularly overrides the course's; the crosswalk of the two systems is the design's central problem
- **Community-partnered projects** — several groups act on one shared object with different motives, and the persona set has to represent more than the enrolled learner
- **Widening-participation redesign** — where completion tracks connectivity, shift patterns and caring responsibilities rather than prior attainment, and a demographic persona records exactly the wrong variables

## Key Sources
- Schmidt, & Tawfik. EdTech Books. [https://edtechbooks.org/eme_6606](https://edtechbooks.org/eme_6606)
- Engeström, Y. (2015). *Learning by expanding: An activity-theoretical approach to developmental research* (2nd ed.). Cambridge University Press.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

<!-- The first entry carries only what the commissioning brief stated: authors and
     URL. Chapter title, editors and year were not established — this sandbox
     cannot reach edtechbooks.org. An absent field says "not established". -->
