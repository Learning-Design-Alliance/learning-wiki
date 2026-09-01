---
type: element
id: coaching
title: Coaching
description: Instructors provide individualized, ongoing support and guidance as learners perform a task, offering hints, feedback, and modeling tailored to current performance.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Coaching

> **Element** · [All elements](index.md)

## Description
Coaching is the provision of individualized support and guidance while learners actively perform a task. The coach observes performance, diagnoses gaps between current and target performance, and intervenes with hints, questions, modeling, or [Feedback](feedback.md) calibrated to what the learner needs at that moment. Unlike one-time instruction, coaching is sustained and adaptive — support rises and falls with learner performance.

## Design Implications

Coaching accelerates skill development by keeping learners in a productive struggle zone: tasks remain challenging while the coach supplies just enough support to prevent failure or unproductive search [Scaffolding contingent on learner performance improves learning outcomes.](../claims/contingent-scaffolding-improves-learning.md) [+S]. Its effectiveness depends on diagnosis — the coach must accurately read the learner's current understanding and respond to it, not deliver generic advice. Coaching also builds self-efficacy through early success experiences with expert support [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M].

### Context
#### Requirements
- Opportunities for learners to perform authentic tasks while being observed ([Practice](practice.md))
- Small learner-to-coach ratios or structured peer-coaching protocols; individualized attention is the defining resource
- Coach expertise in both the domain and in diagnostic questioning ([Articulation](articulation.md), [Think-Aloud](think-aloud.md))
- A mechanism for fading support as competence grows ([Fading](fading.md)) [Fading support promotes transfer of responsibility to the learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

#### Constraints
- Resource-intensive: low learner-to-instructor ratios are difficult to scale, which is why large-enrollment courses substitute [Demonstration](demonstration.md) and structured practice
- Overly frequent or intrusive hints can create dependence and undermine self-regulation; support must be contingent and faded, not constant [Scaffolding contingent on learner performance improves learning outcomes.](../claims/contingent-scaffolding-improves-learning.md) [~M]
- Less effective when the coach lacks domain expertise — inaccurate diagnosis and feedback can entrench errors
- For well-structured procedural content with strong [worked examples](../claims/worked-examples-improve-math-performance.md), coaching adds cost without proportional benefit for novices [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learners
- Novices in hands-on, technical, or complex domains where errors are costly and expert judgment is not visible in the final product
- Learners who have foundational knowledge but struggle to apply it under real task conditions
- Advanced learners refining technique — coaching shifts toward fine-tuning and [Feedback](feedback.md) as expertise grows

### Target Learning Goals
- Procedural and technical skill development through guided repetition with corrective feedback
- Transfer of expert strategies and tacit knowledge that cannot be conveyed by explanation alone
- Self-regulation: coaching conversations model monitoring and evaluation moves learners eventually internalize [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]

### Affordances
- [Scaffolding](../principles/scaffolding.md) — coaching is scaffolding enacted person-to-person: the coach supplies contingent support and progressively withdraws it as competence develops
- [Cognitive Load Management](../principles/cognitive-load-management.md) — by intervening at the moment of difficulty, the coach removes exactly the obstacle blocking progress rather than front-loading all guidance, keeping working memory focused on the task
- [Cognitive Apprenticeship](../principles/cognitive-apprenticeship.md) — coaching is the second phase of this pattern, following [Demonstration](demonstration.md) (modeling) and preceding learner [Articulation](articulation.md) and reflection
- [Assessment for Learning](../principles/assessment-for-learning.md) — continuous observation during coaching is formative assessment in its most direct form; feedback is immediate and tied to visible performance

## Related Elements
- [Scaffolding](scaffolding.md) — the structural principle coaching operationalizes; coaching is scaffolding delivered interactively
- [Feedback](feedback.md) — the core intervention a coach delivers; coaching wraps feedback in diagnosis and relationship
- [Fading](fading.md) — the mechanism by which coaching responsibility transfers to the learner
- [Demonstration](demonstration.md) — the modeling phase that typically precedes coaching in expert-guided sequences
- [Articulation](articulation.md) — coaches elicit learner reasoning to diagnose understanding, not just observe output
- [Practice](practice.md) — coaching only functions during performance; it is support *for* practice, not a substitute

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — the coaching phase, between modeling and articulation
- [Direct Instruction](../patterns/direct-instruction.md) — guided practice with teacher monitoring and corrective feedback
- [4C/ID Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — supportive information and corrective feedback delivered during learning-task performance

## Examples

**[5-Minute Writing Conferences](../strategies/5-minute_writing_conferences.md)** — Brief individualized teacher–student conferences on writing in progress; a time-boxed coaching format that scales one-on-one diagnosis in classrooms.

**[National Writing Project](https://www.nwp.org)** — Teachers coach other teachers through writing instruction via sustained demonstration, co-planning, and side-by-side guidance — coaching applied to professional learning.

**[Codecademy](https://www.codecademy.com)** — Hints, solution reveals, and AI-assisted Q&A approximate coaching at scale during coding [practice](practice.md), though with weaker diagnosis than a human coach.

**Athletic and music instruction** — The paradigm case: a coach observes each repetition, corrects technique immediately, and adjusts drills to the individual performer's errors.

## Key Sources
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453–494). Lawrence Erlbaum Associates. [doi:10.4324/9781315044408-14](https://doi.org/10.4324/9781315044408-14)
- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review, 100*(3), 363–406. [doi:10.1037/0033-295X.100.3.363](https://doi.org/10.1037/0033-295X.100.3.363)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction: A decade of research. *Educational Psychology Review, 22*(3), 271–296. [doi:10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)