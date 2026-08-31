---
type: strategy
title: "On-the-Job Training (OJT)"
description: Training delivered at the workplace during real production work, where an experienced worker guides a learner through actual tasks rather than simulated ones.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: jacobs-2003
    title: "Jacobs, R. L. (2003). *Structured on-the-job training: Unleashing employee expertise in the workplace* (2nd ed.). Berrett-Koehler"
    author: "Jacobs, R. L"
  - id: lave-wenger-1991
    resource: "https://doi.org/10.1017/CBO9780511815355"
    title: "Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press"
    author: "Lave, J., & Wenger, E"
  - id: collins-1989
    title: "Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction* (pp. 453–494). Erlbaum"
    author: "Collins, A., Brown, J. S., & Newman, S. E"
  - id: blume-2010
    title: "Blume, B. D., Ford, J. K., Baldwin, T. T., & Huang, J. L. (2010). Transfer of training: A meta-analytic review. *Journal of Management, 36*(4), 1065–1105"
    author: "Blume, B. D., Ford, J. K., Baldwin, T. T., & Huang, J. L"
---

# On-the-Job Training (OJT)

> **Strategy** · [All strategies](index.md)

## Description
On-the-job training places the learner at the actual worksite, doing the actual work, with an experienced worker as trainer. The learner observes the task performed on real equipment with real consequences, attempts it under supervision, and takes over progressively as competence shows. Its defining feature is that the training context and the performance context are the same context — which removes the transfer gap that classroom training has to bridge, and simultaneously removes the safety net that classroom training provides.

The strategy divides sharply into two forms. **Unstructured OJT** — "follow Sam around for a week" — is the most common form of workplace training and the least reliable: what gets taught depends entirely on which tasks happen to come up and on whether Sam can explain what he does. **Structured OJT** applies a defined task analysis, a prepared trainer, a written sequence, and a competence check, and is what the evidence below refers to.

## Design Implications

OJT's central affordance is that it is [situated](../theories/situated-learning.md): the cues, tools, time pressure, and social context of the task are present during learning, so the learner never has to re-map an abstracted classroom version onto reality. This matters because transfer of training from off-site programs to the job is where corporate training most often fails — the conditions that support transfer are largely workplace conditions, not instructional ones (Blume et al., 2010). Its central risk is the mirror image: an expert trainer performing a task fluently is a poor model unless they narrate the decisions behind it, since expertise is largely tacit and experts systematically underestimate what novices do not see ([Think-Aloud](../elements/think-aloud.md)).

Well-run OJT is essentially [Cognitive Apprenticeship](cognitive-apprenticeship.md) in an industrial setting: demonstration with narration, then guided attempts, then fading. Skipping the demonstration phase and starting the novice on live work maximizes search and minimizes learning [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Skipping the fading phase — leaving the trainer at the elbow indefinitely — never transfers responsibility [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

### Context
#### Requirements
- A task that can be performed safely, or safely enough, by a supervised novice on live work — errors must be recoverable
- An experienced worker released from production targets for the duration, and prepared to train rather than merely to be shadowed ([Coaching](../elements/coaching.md))
- A written task breakdown so that coverage does not depend on which jobs happen to arrive that week
- A defined competence check that says when the learner is signed off, separate from "the trainer thinks they're fine"
- Immediate corrective feedback while the task is still in the learner's hands [Feedback Improves Learning](../claims/feedback-improves-learning.md) [+S]

#### Constraints
- Unstructured OJT delivers inconsistent coverage: content varies with the day's workload, and errors in one trainer's practice propagate to every learner they train [-M]
- Expert trainers are poor explainers of their own automated skill; without explicit narration of decision points, learners copy the visible motions and miss the reasoning [-M]
- Production pressure crowds out training — when the line is behind, the learner is put on the easiest repeatable task and the harder ones are never covered [-M]
- Unsafe or high-consequence tasks (aviation, surgery, high-voltage work) cannot be learned first on live work; these need [simulation](../elements/simulation.md) before the job-site phase [-S]
- Guidance that is essential for a novice becomes interference for a competent worker; a trainer who stays past the fading point slows the learner down [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]
- Because learning is tied to the tasks that actually occur, OJT gives narrow, near-transfer competence — it teaches this job on this equipment, and generalizes poorly to variants [~M]

#### Implementation Variability
- **Structured OJT** (Jacobs): documented task analysis, trained trainers, fixed sequence, formal sign-off — the form with a defensible evidence base
- **Shadowing / buddy system**: unstructured observation, minimal task analysis; cheapest and least reliable
- **Apprenticeship**: OJT over months to years, alternating with classroom instruction, with staged responsibility and formal credentialing
- **Rotation**: planned movement across stations or departments to broaden coverage beyond whatever one post happens to encounter
- **Job aids and performance support**: checklists and reference cards that let the trainer fade earlier without competence dropping ([Performance Support and Job Aids](performance-support-job-aids.md))

### Target Learners
- New hires and internal transfers who need equipment-, site-, and procedure-specific competence that no general course can supply
- Adult learners in skilled trades, manufacturing, healthcare, hospitality, and service roles where the task is physical, situated, and equipment-bound
- Learners who already hold the underlying theory from formal training and need to convert it into performance under real conditions
- Poor fit for learners who need conceptual grounding first — OJT teaches what to do far better than why it works

### Target Learning Goals
- Procedural fluency on specific equipment, systems, or protocols
- Tacit judgment: recognizing when a task is going wrong from cues that are not in the manual
- Speed and reliability under authentic time and quality pressure [Deliberate Practice Improves Performance](../claims/deliberate-practice-improves-performance.md) [+M]
- Enculturation into workplace norms, safety practice, and who to ask when something is unfamiliar

### Instructions
1. **Analyze the task.** Break the job into discrete tasks and, for each, list the steps, the decision points, the quality standard, and the common errors. This document, not the trainer's memory, defines coverage.
2. **Prepare the trainer.** Brief the experienced worker on how to narrate decisions, not just perform steps, and give them the task breakdown to work from ([Coaching](../elements/coaching.md)).
3. **Demonstrate with narration.** The trainer performs the whole task at working speed once, then again slowly while thinking aloud through each decision ([Demonstration](../elements/demonstration.md), [Think-Aloud](../elements/think-aloud.md)).
4. **Guided attempt.** The learner performs the task with the trainer alongside, intervening at the point of error rather than afterwards ([Practice](../elements/practice.md), [Feedback](../elements/feedback.md)).
5. **Have the learner explain.** Before sign-off, the learner talks through the task and the reasons for each decision — this catches procedural mimicry that a correct performance hides ([Articulation](../elements/articulation.md)).
6. **Fade.** Reduce supervision in planned steps: trainer alongside → trainer in the area → trainer on call → independent ([Fading](../elements/fading.md), [Scaffolding](../elements/scaffolding.md)).
7. **Check and sign off.** Assess against the written standard on a task the learner has not just been walked through, and record which tasks remain uncovered.

## Related Strategies
- [Cognitive Apprenticeship](cognitive-apprenticeship.md) — the instructional model structured OJT implements: modeling, coaching, scaffolding, fading
- [Modeling](modeling.md) — the demonstration phase in isolation; OJT depends on it being narrated rather than silent
- [Instructional Coaching](instructional-coaching.md) — the same trainer-alongside relationship applied to teaching practice
- [Performance Support and Job Aids](performance-support-job-aids.md) — reduces how much has to be trained at all, and lets fading happen sooner

## Examples

**Structured OJT in manufacturing:** A new operator is assigned a documented task list per station; a certified trainer demonstrates and narrates each, observes two supervised runs, and signs off against a written standard before the operator works the station alone.

**Clinical preceptorship:** A newly qualified nurse is paired with a preceptor for a fixed number of shifts, taking a progressively larger patient load, with structured competence assessments at defined points.

**Registered apprenticeships:** Trade apprenticeships alternate paid on-the-job hours with classroom instruction, with wage progression tied to demonstrated competence — the institutionalized form of staged responsibility.

**Aviation line training:** After simulator qualification, a pilot flies revenue sectors under a line training captain, with supervision fading across a defined number of sectors — the standard pattern for tasks too consequential to learn on live work first.

## Key Sources
- Jacobs, R. L. (2003). *Structured on-the-job training: Unleashing employee expertise in the workplace* (2nd ed.). Berrett-Koehler.
- Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press. [doi:10.1017/CBO9780511815355](https://doi.org/10.1017/CBO9780511815355)
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction* (pp. 453–494). Erlbaum.
- Blume, B. D., Ford, J. K., Baldwin, T. T., & Huang, J. L. (2010). Transfer of training: A meta-analytic review. *Journal of Management, 36*(4), 1065–1105.
