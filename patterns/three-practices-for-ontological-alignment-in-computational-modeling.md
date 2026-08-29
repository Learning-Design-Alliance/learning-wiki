---
type: pattern
title: Three Practices for Ontological Alignment in Computational Modeling
description: Three classroom practices — elevating student ideas that match a tool's representational units, explicitly testing links between conceptual and computational models, and introducing evidence that speaks directly to the tool's representational claims — for introducing a computational modeling tool so its structure aligns with students' existing thinking.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
author: "Wagh, A., Rosenbaum, L. F., Fuhrmann, T., Eloy, A., Blikstein, P., & Wilkerson, M."
grain_size: unit
sources:
  - id: wagh-et-al-2025
    resource: "https://doi.org/10.1080/07370008.2024.2427400"
    title: "Wagh, A., Rosenbaum, L. F., Fuhrmann, T., Eloy, A., Blikstein, P., & Wilkerson, M. (2025). Toward Ontological Alignment: Coordinating Student Ideas with the Representational System of a Computational Modeling Unit for Science Learning. Cognition and Instruction, 43(1-2), 1-32."
    author: "Wagh, A., Rosenbaum, L. F., Fuhrmann, T., Eloy, A., Blikstein, P., & Wilkerson, M."
---

# Three Practices for Ontological Alignment in Computational Modeling

## Description
When students first encounter an agent-based modeling (ABM) tool, they often have relevant intuitive ideas about a phenomenon but no way to see how those ideas map onto the tool's specific representational units (e.g., individual particle behaviors and interactions). This pattern names three teacher practices, developed and documented in a diffusion unit, for closing that gap: elevating and labeling student ideas in terms the tool's building blocks can express; making the translation between a conceptual idea and its coded/simulated implementation explicit and checkable in both directions; and introducing external evidence that can adjudicate between competing models when the tool's own simulation cannot.

## Implications

### Context
#### Requirements
- Students with no prior experience with the specific modeling tool, so their existing ideas have not yet been shaped by its representational conventions
- A whole-class structure (e.g., persistent reference whiteboards) for tracking and naming student theories consistently across a multi-day unit
- Access to external, independent evidence (e.g., a physical experiment or video data) that speaks to the same phenomenon the computational model represents, for use when the model's own simulation cannot distinguish between competing theories
#### Constraints
- Documented within a single topic (particle diffusion) and tool (an ABM environment called MoDa); transfer to other computational modeling domains is plausible but untested here
- The third practice (external evidence) depends on the teacher first recognizing that the model's own simulation *cannot* falsify a given theory — a judgment call that requires disciplinary insight into the tool's representational limits
#### Grain Size
Unit (a 6-day computational modeling unit in the source study)

### Target Goals
- Making a computational modeling tool's representational system align with, rather than replace or ignore, students' existing ideas about a phenomenon
- [External empirical evidence can refute a computational model of particle interactions when the model's own simulation cannot](../claims/external-evidence-can-refute-computational-models-of-particle-interactions.md)

### Target Learners
- Middle-school students (studied at grade 6) with no prior experience with agent-based modeling tools

### Theory
#### Supporting
- [Ontological Alignment](../theories/ontological-alignment.md)
- Representational systems / epistemic forms (Collins & Ferguson) — different tools foreground different levels of perspective on a system
#### Contradicting / Qualifying
- (none yet linked)

### Claims
#### Supporting
- [External empirical evidence can refute a computational model of particle interactions when the model's own simulation cannot](../claims/external-evidence-can-refute-computational-models-of-particle-interactions.md) [+M]
#### Contradicting
- (none yet linked)

## Design

### Sequence
1. **Elevate student ideas**: elicit causal explanations of the phenomenon at the particle/agent level (e.g., "why do you think the data looks this way?"), then categorize and label student theories using canonical terms tied to the tool's building blocks (e.g., "bounce," "attach," "infect"); keep these labels visible and persistent (e.g., on reference whiteboards) throughout the unit.
2. **Test conceptual-computational links**: before coding, ask students how a conceptual idea would be implemented in the tool; if it resists straightforward translation, push students to rephrase it in agent-level terms; provide a shared "code cheat sheet" of worked examples per theory so students can compare implementations.
3. **Introduce resonant evidence**: when the model's own simulation cannot distinguish between competing theories (e.g., because two theories look visually similar in simulation), recognize this limitation explicitly and introduce an external experiment or data source that directly tests the underlying particle-level claim.

### Affordances
- (none yet linked)

### Personalization
- The specific labeled theories, code examples, and external evidence source are tied to the diffusion topic in the source study; the reusable structure is the three-step sequence (elevate, test links, introduce resonant evidence), applicable to other computational-modeling topics with an analogous representational mismatch.

## Related Patterns
- (none yet linked)

## Examples
- A teacher asked a student to explain how he'd "take an ink particle and split it apart" in code, surfacing that his conceptual model ("infect") did not straightforwardly translate into the tool's agent-based primitives.
- Recognizing that a "diffusion looks like infection" theory could not be visually distinguished from the correct theory in simulation, the teacher introduced an evaporation experiment (evaporated water/food-coloring mixture turned clear) that directly contradicted the "infect" theory's prediction; 7 of 18 students explicitly cited this experiment as changing their theory.

## Key Sources
- Wagh, A., Rosenbaum, L. F., Fuhrmann, T., Eloy, A., Blikstein, P., & Wilkerson, M. (2025). Toward Ontological Alignment: Coordinating Student Ideas with the Representational System of a Computational Modeling Unit for Science Learning. *Cognition and Instruction, 43*(1-2), 1-32. [https://doi.org/10.1080/07370008.2024.2427400](https://doi.org/10.1080/07370008.2024.2427400)
