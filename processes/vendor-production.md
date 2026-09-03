---
type: process
id: vendor-production
title: Vendor Production (Alpha–Beta–Gold)
description: The contract production process used by e-learning studios — macro design, storyboard, then alpha, beta and gold builds, each ending in a client review, with the final sign-off closing the design to further change.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-03
author: 
grain_size: course
---

# Vendor Production (Alpha–Beta–Gold)

> **Design Process** · [All design processes](index.md)

## Description
Vendor production is the process a studio runs when a client is paying for a course. Its stages are named for build fidelities rather than design activities — **alpha**, **beta** and **gold** — and each ends in a client review. It is the dominant production model in commercial e-learning, and it is documented in trade practice rather than in the research literature.

What distinguishes it from every other design process is not its activities, which are broadly those of [Systematic Instructional Design](systematic-instructional-design.md), but **who holds the gate**. The approver at each stage is the party paying for the work. The gates are contract milestones, and the last one is a signature that closes the design: further change becomes a change order rather than a revision.

Two consequences shape the whole process. First, **content is frozen at the storyboard, not at the end** — practitioners are unanimous that nothing passes to development without storyboard sign-off, and that changes accepted after it are a conversation about timeline and budget rather than about design. The stages after the storyboard are about execution. Second, **the number of review rounds is bounded by the contract**, which is what makes the sequence a discipline rather than a description; a practitioner's warning at the alpha stage is that "you really only have two more shots after this."

The characteristic failure is the bound not holding. The same account reports the observed drift plainly: "I've seen the full array: Alpha, Beta, Beta2, Pre-Gold, Gold, Gold2." Every stage that is added is paid for by somebody, and the model's value is almost entirely in the agreement that there are three.

## Implications

### Context
#### Requirements
- **A client with authority to sign.** The process assumes a single decision-making party per gate; a client organisation whose reviewers disagree with each other converts each gate into an unbounded round
- **A contract that states the number of review rounds.** Without it the stages are labels rather than constraints
- **Content available early enough to storyboard.** The freeze point only works if the subject matter exists to be frozen

#### Constraints
- **The client sees a working build for the first time at alpha.** However good the storyboard and visual concept were, reactions to a live build differ from reactions to a document, and the alpha review absorbs that shock
- **Voiceover is expensive to redo**, so the narration script is signed separately and later than the storyboard, and locked before studio time is booked
- **Sign-off is not evaluation.** The gates establish that the client accepts the deliverable, not that learners learned anything — nothing in the model measures the latter
- **The storyboard drifts from the build** unless it is deliberately kept in step, and keeping two documents in step by hand is the process's standing maintenance cost

#### Grain Size
- Course
- Module

### Target Goals
- Fixed-scope, fixed-price course production where the deliverable is contractually defined in advance
- Projects where the client organisation needs auditable acceptance at defined points
- Production at volume, where a repeatable stage structure matters more than adapting the process per course

### Target Learners
- Any; the process constrains the commercial relationship rather than the audience. Learners are not participants in it — the reviewer at every gate is the client, and no gate is passed by evidence about learners

### Theory
#### Supporting
- [Design Layers Theory](../theories/design-layers-theory.md) — the fidelity ladder is a layered design revised at different rates, with content settled before presentation

#### Contradicting / Qualifying
- [Designerly Stances](../theories/designerly-stances.md) — a design frozen at the storyboard forecloses the reframing that designerly practice treats as the point of iterating

### Claims
#### Supporting
- [Feedback Most Effective At Task And Process Levels](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — the standard a client review round has to meet if the rounds are to be worth their cost

#### Contradicting
- [Critical constructive feedback is neglected at multiple, independently measurable processing stages](../claims/critical-constructive-feedback-is-neglected-at-multiple-stages.md) [-M] — review rounds concentrated in a party with a commercial relationship to the producer are exactly the conditions under which critical feedback is softened or withheld

## Design

### Sequence
1. **Macro design** — the course as a proposal: outline, objectives, treatment, seat time, media mix, and what is out of scope. The client approves a description of a course that does not yet exist, and the scope section is where later disputes are settled
2. **Storyboard** — the screen-by-screen specification, with a **visual design concept** alongside it: one or two screens rendered at final fidelity so that approving the look means something. This gate freezes content
3. **Alpha** — the first working build, and the first time the client experiences the course rather than reading it. Complete enough to be judged; incompleteness here is spent from a budget of two remaining rounds
4. **Beta** — media complete: finished imagery, interactions, and voiceover recorded against a separately signed narration script. Assessments are functional
5. **Gold** — final quality assurance, then sign-off and no further edits

### Elements Used
- [Continuous Review](../elements/continuous-review.md)
- [Feedback](../elements/feedback.md)

### Affordances
- [Formative Assessment](../principles/formative-assessment.md) — applied to the design rather than to learners: each build stage is a formative check on the deliverable

### Personalization
- **Where the client cannot convene a single approver**, add an internal consolidation step that reconciles reviewer comments before they reach the studio; do not let the gate absorb the disagreement
- **Where scope is genuinely unsettled**, this is the wrong process — [Successive Approximation](successive-approximation-model.md) iterates within an agreed problem and [Design Thinking](design-thinking.md) iterates the problem itself. Running vendor production on unsettled scope is what produces Beta2 and Gold2
- **Where the storyboard can be generated from the design specification** rather than maintained beside it, the standing sync cost disappears; this is the main improvement available to the model

## Related Processes
- [Systematic Instructional Design](systematic-instructional-design.md) — supplies the activities; vendor production supplies the commercial gates and the fidelity ladder
- [Successive Approximation Model](successive-approximation-model.md) — also reaches alpha, beta and gold, but treats them as convergence markers inside iteration rather than as contract milestones. The contrast is the clearest way to see what is commercial and what is designerly in each
- [Learner Experience Design](learner-experience-design.md) — supplies evaluation with actual users, which this process has no stage for
- [Continuous Improvement of Learning Materials](continuous-improvement-of-learning-materials.md) — what would happen after gold if the contract paid for it

## Examples
- **Outsourced compliance and onboarding courses** — the setting the model was formed in, where a defined deliverable and auditable acceptance matter more than iteration
- **Agency work under a fixed-price statement of work**, where the round count is a contract term

## Key Sources
- Thinkdom / eLearning Industry. *What Are Alpha, Beta, Gold Stages In eLearning Content Development?* [https://elearningindustry.com/what-are-alpha-beta-gold-stages-in-elearning-content-development](https://elearningindustry.com/what-are-alpha-beta-gold-stages-in-elearning-content-development)
- Omniplex Learning. *The ABCs of the eLearning content development stages.* [https://omniplexlearning.com/insights/blog/the-abcs-of-the-elearning-content-development-stages/](https://omniplexlearning.com/insights/blog/the-abcs-of-the-elearning-content-development-stages/)
