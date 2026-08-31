---
type: element
title: Mental Models
description: A mental model is a learner's internal representation of how a system, process, or domain works, which they use to explain phenomena, predict outcomes, and reason about new situations.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Mental Models

> **Element** · [All elements](index.md)

## Description
A mental model is a learner's internal representation of how a system, process, or domain works — a runnable structure they can use to explain phenomena, predict outcomes, and simulate "what happens if…" scenarios. Instruction that targets mental models aims to build, refine, or repair these representations rather than only transmitting facts or procedures.

## Design Implications

Instruction is more durable when it helps learners construct a coherent causal model of *why* something works, not just *what* to do [~M]. Because learners arrive with pre-existing (often partial or incorrect) models, effective design surfaces those models first and creates conditions for revision [Activation improves learning by preparing relevant prior knowledge.](../claims/activation-improves-learning.md) [+M]. External representations — diagrams, simulations, concept maps — support model construction by offloading structure onto the visual channel [Dual coding of verbal and visual information improves recall.](../claims/dual-coding-improves-recall.md) [+S], and by reducing the working-memory burden of holding a system's structure in mind [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M].

### Context
#### Requirements
- Diagnosis of learners' existing models (pretests, prediction tasks, [Think-Aloud](think-aloud.md) protocols) so instruction can target the gap
- Multiple representations of the target system (verbal, visual, symbolic) linked explicitly to one another
- Opportunities to *run* the model — predict, test, and receive feedback — so learners discover where their model fails
- Sequencing from simple to complex cases so the model can be elaborated incrementally

#### Constraints
- Learners' naive models are resistant to change; simply presenting the correct model rarely displaces misconceptions — prediction-then-feedback sequences are needed [~M]
- Analogies used to build models can import unwanted structure from the source domain, creating new misconceptions [~M]
- Rich visualizations can overload novices or be processed superficially as decorative detail [Decorative illustrations do not improve learning.](../claims/decorative-illustrations-do-not-improve-learning.md) [-M]
- A model built from a single case or context tends to be oversimplified and misapplied; multiple varied cases are needed for robust models [Multiple varied cases support flexible knowledge under Cognitive Flexibility Theory.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]

### Target Learners
- Novices in a domain, who lack any serviceable model and benefit from explicit advance structure [Graphic organizers support comprehension for novice learners.](../claims/graphic-organizers-support-novice-comprehension.md) [+M]
- Learners holding misconceptions, who need their models surfaced and confronted rather than bypassed
- Advanced learners may need less external model support, consistent with the expertise-reversal pattern [Expertise reverses the benefit of high instructional support.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding: grasping causal structure and underlying mechanisms
- Transfer and prediction: reasoning about novel cases by simulating the model
- Misconception repair: replacing intuitive-but-wrong models with scientifically accurate ones

### Affordances
- [Analogical Reasoning](../principles/analogical-reasoning.md) — analogies are the primary tool for bootstrapping a new mental model from a familiar domain; the mapping must be made explicit so learners import the right structure
- [Activation](../principles/activation.md) — eliciting learners' current model before instruction determines what must be built, revised, or dismantled
- [Cognitive Load Management](../principles/cognitive-load-management.md) — external models (diagrams, simulations) hold the system's structure outside working memory so learners can attend to relationships rather than storage
- [Cognitive Flexibility](../principles/cognitive-flexibility.md) — presenting the same model across multiple cases and representations prevents the model from being welded to a single context

## Related Elements
- [Advance Organizers](advance-organizers.md) — provide the skeletal model before detailed content fills it in
- [Analogies](analogies.md) — the mapping mechanism by which new models are built from known ones
- [Case Studies](case-studies.md) — varied cases that test and elaborate a model across contexts
- [Think-Aloud](think-aloud.md) — a diagnostic window into learners' current models
- [Application](application.md) — running the model against real problems reveals its gaps

## Patterns That Use This Element
- [Anchored Instruction](../patterns/anchored-instruction.md) — models are built in the service of solving a rich, situated problem
- [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) — multiple criss-crossed cases build models that survive transfer
- [4CID Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — supportive information explicitly targets mental models of the task domain

## Examples

**[Activate Prior Knowledge](../strategies/activating-prior-knowledge.md)** — Eliciting learners' existing explanations before instruction surfaces the naive model that instruction must revise.

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Research-based physics and chemistry simulations that let learners manipulate variables and observe system behavior, supporting model construction through prediction and testing.

**[Analogies and Prior Knowledge Activation](analogies-and-prior-knowledge-activation.md)** — Uses a familiar system (e.g., water flow for electricity) as the source model, with explicit mapping of correspondences and limits.

**[Advance Organizers](advance-organizers.md)** — Ausubel's expository organizers supply a general model into which subsequent detail can be assimilated.

## Key Sources
- Johnson-Laird, P. N. (1983). *Mental models: Towards a cognitive science of language, inference, and consciousness.* Harvard University Press.
- Norman, D. A. (1983). Some observations on mental models. In D. Gentner & A. L. Stevens (Eds.), *Mental models* (pp. 7–14). Lawrence Erlbaum.
- Mayer, R. E. (1989). Models for understanding. *Review of Educational Research, 59*(1), 43–64. [doi:10.3102/00346543059001043](https://doi.org/10.3102/00346543059001043)
- Gentner, D., & Stevens, A. L. (Eds.). (1983). *Mental models.* Lawrence Erlbaum.
- Vosniadou, S. (2013). Conceptual change in learning and instruction: From framework frameworks to framework theory. In S. Vosniadou (Ed.), *International handbook of research on conceptual change* (2nd ed., pp. 11–30). Routledge. [doi:10.4324/9780203154472.ch1](https://doi.org/10.4324/9780203154472.ch1)
