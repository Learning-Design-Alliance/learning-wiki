---
type: element
id: performance-support
title: Performance Support
description: Performance support provides task-specific guidance at the moment of need within the work context, reducing reliance on memorized knowledge.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Performance Support

> **Element** · [All elements](index.md)

## Description
Performance support delivers just-in-time, task-specific guidance — job aids, checklists, embedded wizards, tooltips, decision trees — at the moment a learner attempts a task, rather than requiring the task to be recalled from memory. It functions as externalized knowledge: the system or artifact carries procedural detail so the performer can act competently before full mastery is achieved.

## Design Implications

Performance support shifts the instructional goal from "train everything in advance" to "support competent performance now, build fluency over time." By externalizing procedural steps, it reduces the working-memory burden of executing unfamiliar tasks [Chunking and externalizing task structure reduce working-memory load during complex tasks.](../claims/chunking-reduces-working-memory-load.md) [+M]. It is most effective when embedded in the workflow and retrievable in seconds; support that requires leaving the task context is rarely used. Over time, support should be faded or made progressively less detailed as fluency develops [Fading support promotes transfer of responsibility from scaffold to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

### Context
#### Requirements
- Task analysis identifying the specific decision points and steps where performers stall
- Support accessible within the work context (embedded, one or two clicks away), not in a separate manual
- Content structured for scanning — checklists, decision tables, short steps — not prose ([Clear Structure](../principles/clear-structure-presentation.md))
- A maintenance process: stale job aids destroy trust in the whole support system

#### Constraints
- Over-reliance can prevent schema formation; if support is never faded, learners may never internalize the procedure [-M]
- Poorly structured support adds search and interruption costs that exceed its benefit, especially for experts [Guidance that is redundant for experienced performers imposes extraneous load.](../claims/expertise-reversal-effect.md) [~M]
- Ineffective for tasks requiring judgment or tacit knowledge that cannot be captured in steps and rules
- Support used *during* a task divides attention between performing and reading; it should be minimized to the decisive moment, not narrate every step

### Target Learners
- Novices and infrequent performers who have not yet automatized the procedure [Guidance benefits novices most and can hinder experienced performers.](../claims/expertise-reversal-effect.md) [+M]
- Experienced performers facing a rarely used variant of a familiar task (the "forgetting curve" use case)
- Less beneficial for experts performing routine tasks, for whom support is interruption, not aid [~M]

### Target Learning Goals
- Immediate task performance: completing a procedure correctly before mastery
- Procedural knowledge: reinforcing the correct sequence through repeated use
- Error prevention: catching predictable mistakes at the decision point where they occur

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — performance support externalizes procedural detail so working memory is spent on the task itself, not on recalling steps; it is cognitive load management applied at the point of performance
- [Scaffolding](../principles/scaffolding.md) — a job aid is a scaffold that does not require an instructor present; the design question is how it fades as fluency grows
- [Coaching](coaching.md) — embedded hints and contextual prompts function as automated coaching, delivering process-level guidance at the moment of need [Feedback is most effective when delivered at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- [Procedural Information](procedural-information.md) — performance support is procedural information delivered just-in-time rather than just-in-case, per the [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) distinction between supportive and procedural information

## Related Elements
- [Procedural Information](procedural-information.md) — the content type performance support delivers, just-in-time instead of up front
- [Scaffolding](scaffolding.md) — performance support is a self-service scaffold; fading applies here too
- [Coaching](coaching.md) — embedded prompts approximate coaching without a human coach
- [Practice](practice.md) — repeated supported performance builds the fluency that eventually makes support unnecessary
- [Fading](fading.md) — the mechanism for transitioning from supported to independent performance

## Patterns That Use This Element
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — procedural information specified for just-in-time delivery alongside learning tasks
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — scaffolding and articulation phases supported by tools that prompt expert moves
- [Cognitive Load Reduction](../patterns/cognitive-load-reduction-clt-scaffolding-approach.md) — externalizing procedures is a primary load-reduction move for complex task environments

## Examples

**[Scribe](https://scribehow.com)** — Auto-generates step-by-step guides with screenshots from a recorded workflow; teams embed these as just-in-time job aids inside documentation.

**[WalkMe](https://www.walkme.com)** — Digital adoption platform that overlays contextual walkthroughs and tooltips directly inside enterprise software at the point of use.

**[Checklists in the WHO Surgical Safety Checklist](https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery)** — A performance support artifact proven to reduce surgical complications by prompting critical steps at decision points, demonstrating that support works for experts on high-stakes, low-frequency tasks.

**[Salesforce In-App Guidance](https://help.salesforce.com/s/articleView?id=000387061&type=1)** — Embedded prompts and walkthroughs delivered inside the CRM interface, keyed to the specific screen and user role.

## Key Sources
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
- Rossett, A., & Schafer, L. (2007). *Job aids and performance support: Moving from knowledge in the classroom to knowledge everywhere*. Pfeiffer.
- Gawande, A. (2009). *The checklist manifesto: How to get things right*. Metropolitan Books.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)