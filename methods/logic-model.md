---
type: method
id: logic-model
title: Logic Model
description: A design method that lays out the chain from a programme's activities and outputs to the outcomes it is meant to produce, so that each link can be examined, and later tested, on its own.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-07
---

# Logic Model

> **Design Method** · [All design methods](index.md)

## Description
A Logic Model states, in one directed diagram, how a programme is supposed to work: the resources it consumes, the activities it runs, the outputs those produce, and the chain of short-, medium- and long-term outcomes it expects to follow. Developed in programme evaluation and made routine by funders' reporting requirements, it exists to make an implicit causal story explicit and inspectable *before* anybody tries to evaluate whether it happened.

For a learning design the useful part is the right-hand side. A goal tree already says what a learner should be able to do; a logic model says what the design believes those capabilities *lead to* — retention past the course, transfer to an untaught case, use on the job, a credential, a change in an organisation's numbers — and it says so as a chain of separately falsifiable links rather than as one leap from "we taught it" to "it mattered".

## Design Implications

The method's whole value is that it forces the links to be placed one at a time. An unstated theory cannot be wrong, and a programme with an unstated theory that fails to produce its outcome leaves nobody able to say whether the theory was mistaken or the implementation was. Theory-driven evaluation exists to separate those two failures, and a logic model is its cheapest instrument.

The second implication is temporal, and it is what makes the model worth writing in a learning design specifically. The links closest to the instruction can be tested in weeks; the far ones need a year and somebody willing to report back. Written as a chain, the near links can be checked long before the distal one is observable, and a break in the middle leaves the competency structure untouched — it is the arrow that was wrong, not the goal.

What the method does **not** supply is warrant. A logic model is a statement of what the designer believes, and drawing it neatly does nothing to make it true. Its literature is consistent on this: the model is a framework for organising evidence and a hypothesis to be tested, not evidence itself.

### Context
#### Requirements
- A stated outcome somebody actually wants, distinct from the activity that is supposed to produce it
- A willingness to mark the design's own reasoning as reasoning — an unmarked arrow reads to a later reader as a finding
- Named capabilities to anchor the chain to; without them the model floats free of the instruction and becomes a funder document

#### Constraints
- Logic models represent simple and complicated programmes well and misrepresent complex ones: where effects are emergent, recursive, or depend on other actors' responses, a linear chain flatters the design and hides where the real uncertainty is [~M]
- The middle links get invented to close the gap. A chain has to reach the goals, and the pressure is to manufacture an intermediate outcome that makes it reach — an honest gap is more useful than a fabricated link, because the fabricated one gets built on [-M]
- Written for a funder rather than for the team, the model becomes a compliance artifact filled in once and never consulted; the inputs–activities–outputs framing is a grant-reporting shape before it is a design one [-M]
- Systematic review of theory-driven evaluation practice finds programme theory is frequently stated and then not actually used to structure the evaluation that follows, which is the failure mode to design against [~M]
- Attribution weakens as the chain lengthens. A distal outcome has many causes, and a model that implies the programme owns it is claiming more than any evaluation of it could support [-M]

#### Implementation Variability
- **Outcomes chain only:** the right-hand side — proximal, intermediate and distal outcomes with the arrows between them. The lightest useful form for a course
- **Full inputs–activities–outputs–outcomes:** the funder-facing form, and the one most published templates describe
- **Backward construction:** start at the distal outcome and work left, which surfaces missing preconditions that forward construction hides — the move [Theory of Change](theory-of-change.md) makes central
- **Nested models:** a programme-level model whose intermediate outcomes are the distal outcomes of individual courses, which is how a curriculum map becomes a causal argument rather than a coverage table
- **With contribution analysis:** the chain used as the frame for assembling evidence about a contribution claim, rather than for attributing an effect

### Target Learners
- Not a learner-facing method. Its subject is the design's own reasoning
- Its clearest indirect beneficiaries are learners on courses whose purpose is distal — retention, transfer, use at work — where an unwritten chain means the design optimises for the assessment it can see. Transfer in particular is a design target that has to be chosen deliberately, since it does not follow from mastery of the taught case [Interleaving improves transfer.](../claims/interleaving-improves-transfer.md) [~M]

### Target Learning Goals
- None directly; the method takes goals as given and asks what they are *for*
- It bears hardest on goals whose value is downstream — a grammar rule whose point is fluency, a procedure whose point is safety on a job

### Instructions
1. **Name the outcome somebody actually wants,** and name who wants it. An outcome with no interested party is a metric.
2. **Work backward one link at a time.** For each outcome, ask what has to happen immediately before it. Stop when the chain reaches a capability the goal structure already claims.
3. **Anchor the near end to named capabilities.** The point at which the chain touches [Backward Design](backward-design.md)'s desired results is the join between what is graded and what is believed.
4. **Write the reason for each arrow** — not the generic claim, which belongs in the literature, but why this link is plausible for *this* design and *these* learners.
5. **Mark each link's warrant.** Published finding, held position, or the design's own reasoning. Three different things, and only the first is evidence.
6. **Say where each link becomes observable.** A link nobody can ever check is a belief; a link checkable in six weeks is a plan.
7. **Check the shape.** A chain that loops back on itself is not modelling feedback, it is failing to distinguish two outcomes at two horizons.

## Related Methods
- [Theory of Change](theory-of-change.md) — the heavier sibling, which adds the preconditions and assumptions a chain depends on but does not control
- [Backward Design](backward-design.md) — the same backward reasoning applied one level down, from desired results to evidence to instruction
- [Needs Analysis](needs-analysis.md) — establishes the outcome the chain terminates in

## Related Processes
- [Understanding by Design](../processes/understanding-by-design.md) — outcome-first course design, whose "desired results" stage is where a logic model's near end attaches
- [Continuous Improvement of Learning Materials](../processes/continuous-improvement-of-learning-materials.md) — the process with the strongest use for one, since it revises against observed results rather than against review
- [Data Wise Improvement Process](../processes/data-wise-improvement-process.md) — makes the same move with school data: an explicit theory of action, then evidence against it

## Examples
- **W. K. Kellogg Foundation's development guide** — the template most widely used in the non-profit and education sectors, and the reason the inputs–activities–outputs–outcomes shape is the default one people picture
- **Programme performance reporting** — McLaughlin and Jordan's account of the model as the device for "telling your program's performance story" to a funder, which is both its most common use and the origin of its compliance-artifact failure mode
- **Multimethod evaluation design** — Cooksy, Gill and Kelly's use of the model as the integrative frame that decides which methods answer which link, rather than as a diagram appended to a report

## Key Sources
- W. K. Kellogg Foundation. (2004). *Logic Model Development Guide*. W. K. Kellogg Foundation.
- McLaughlin, J. A., & Jordan, G. B. (1999). Logic models: A tool for telling your program's performance story. *Evaluation and Program Planning, 22*(1), 65–72. [doi:10.1016/S0149-7189(98)00042-1](https://doi.org/10.1016/S0149-7189(98)00042-1)
- Cooksy, L. J., Gill, P., & Kelly, P. A. (2001). The program logic model as an integrative framework for a multimethod evaluation. *Evaluation and Program Planning, 24*(2), 119–128. [doi:10.1016/S0149-7189(01)00003-9](https://doi.org/10.1016/S0149-7189(01)00003-9)
- Rogers, P. J. (2008). Using programme theory to evaluate complicated and complex aspects of interventions. *Evaluation, 14*(1), 29–48. [doi:10.1177/1356389007084674](https://doi.org/10.1177/1356389007084674)
- Coryn, C. L. S., Noakes, L. A., Westine, C. D., & Schröter, D. C. (2011). A systematic review of theory-driven evaluation practice from 1990 to 2009. *American Journal of Evaluation, 32*(2), 199–226. [doi:10.1177/1098214010389321](https://doi.org/10.1177/1098214010389321)
- Funnell, S. C., & Rogers, P. J. (2011). *Purposeful Program Theory: Effective Use of Theories of Change and Logic Models*. Jossey-Bass.
- Mayne, J. (2012). Contribution analysis: Coming of age? *Evaluation, 18*(3), 270–280. [doi:10.1177/1356389012451663](https://doi.org/10.1177/1356389012451663)
