---
type: strategy
title: Pre Training
description: Teaching names, characteristics, and key concepts of a system or domain before presenting the main instruction, so learners build prior knowledge that reduces load during the core lesson.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Pre Training

## Description
Pre training teaches learners the names, characteristics, and key concepts of a system, process, or domain *before* the main instruction begins. Instead of learning what something is called and how it works simultaneously, learners first acquire the vocabulary and component knowledge, then encounter the full explanation. It is carried out through short pre-lessons, glossaries, concept introductions, or orientation activities placed before the primary learning task.

## Design Implications

Pre training works by splitting learning into two manageable phases: first acquiring component knowledge, then integrating it into a causal model. Without it, learners must hold unfamiliar terms and relationships in working memory while simultaneously processing the main explanation, which overloads capacity [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. Mayer's multimedia research shows that learners who receive pre training on component names and behaviors produce better transfer from a subsequent full explanation than learners who receive the same content without it [+S]. Pre training is closely related to [Advance Organizers](../elements/advance-organizers.md), but is more specific: it teaches actual prerequisite content rather than providing a structural frame.

### Context
#### Requirements
- Task analysis identifying the concepts, terms, and component behaviors the main lesson presupposes
- A short, focused pre-lesson covering only what is needed — not a full unit of instruction
- Explicit connection during the main lesson back to the pre-trained concepts, so learners retrieve and use them

#### Constraints
- Pre training that is too long or too detailed becomes its own lesson and delays or dilutes the main instruction [~M]
- If the pre-trained concepts are never referenced in the main lesson, the benefit largely disappears — activation at the point of use matters [Activation improves learning.](../claims/activation-improves-learning.md) [~M]
- For learners with substantial prior knowledge, pre training is redundant and wastes time [~M]
- Pre training cannot substitute for the main explanation; component knowledge alone does not produce integrated understanding [-M]

#### Implementation Variability
- **Concept pre training**: teach names and characteristics of key components (e.g., "a tire pump has a piston, inlet valve, outlet valve") before explaining how pumping works
- **Vocabulary pre training**: front-load domain terminology via glossary or flashcards before reading
- **Procedural pre training**: teach tool or interface basics before a complex task
- **Prior-knowledge activation**: brief recall or discussion of related existing knowledge, a lighter variant ([Activation](../elements/activation.md))

### Target Learners
- Novices with low prior knowledge of the domain, who lack the component schemas the main lesson assumes [+S]
- Learners in multimedia or technical contexts where unfamiliar terms and components appear simultaneously
- Less beneficial for high-knowledge learners, for whom pre training adds redundancy [~M]

### Target Learning Goals
- Conceptual understanding: building a causal model of how a system works
- Vocabulary acquisition: establishing shared terminology before explanation
- Transfer: pre training on components improves later transfer of the integrated model [+S]

### Instructions
1. Analyze the main lesson to list the terms, components, and concepts learners must already know to follow it.
2. Design a short pre-lesson teaching only those components — names, characteristics, and basic behavior — using [Chunking](../principles/chunking.md) to keep the pre-lesson itself within working memory limits.
3. Optionally open with an [Advance Organizer](../elements/advance-organizers.md) showing how the components relate, or an [Analogy](../elements/analogies.md) linking them to familiar knowledge.
4. Deliver the main lesson, explicitly naming and using the pre-trained concepts so learners retrieve them at the moment of integration.
5. Follow with [Practice](../elements/practice.md) on the integrated material.

## Related Strategies
- [Advance Organizers](../strategies/advance_organizers.md) — a structural frame before instruction; pre training goes further by teaching actual prerequisite content
- [Activating Prior Knowledge](../strategies/activating_prior_knowledge.md) — retrieves existing knowledge rather than building new component knowledge
- [Chunking](../principles/chunking.md) — the segmentation logic that pre training applies to the *sequence* of instruction

## Examples
- **Mayer's pump experiments** — learners first studied the names and characteristics of a tire pump's components, then received a multimedia explanation of how it works; pre-trained learners outperformed controls on transfer tests (Mayer, Mathias, & Wetzell, 2002).
- **[Khan Academy](https://www.khanacademy.org)** — unit "Get ready" courses teach prerequisite skills (e.g., key algebra operations) before the main grade-level course begins.
- **Technical onboarding** — software tutorials that first introduce interface vocabulary ("canvas," "layer," "timeline") before walking through a full workflow.

## Key Sources
- Mayer, R. E., Mathias, A., & Wetzell, K. (2002). Fostering understanding of multimedia messages through pre-training: Evidence for a two-stage theory of mental model construction. *Journal of Experimental Psychology: Applied, 8*(3), 147–154. [doi:10.1037/1076-898X.8.3.147](https://doi.org/10.1037/1076-898X.8.3.147)
- Pollock, E., Chandler, P., & Sweller, J. (2002). Assimilating complex information. *Learning and Instruction, 12*(1), 61–86. [doi:10.1016/S0959-4752(01)00016-0](https://doi.org/10.1016/S0959-4752(01)00016-0)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)