---
type: strategy
id: pretraining
title: Pretraining
description: Teaching learners the names, characteristics, and functions of key concepts before the main instruction, so that working memory is not consumed by unfamiliar terminology during learning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Pretraining

> **Strategy** · [All strategies](index.md)

## Description
Pretraining provides learners with prior instruction on the names, characteristics, locations, and functions of the key concepts and components that a subsequent lesson will assume. Rather than learning "what it's called" and "how it works" simultaneously, learners first acquire the vocabulary and component knowledge, then encounter the causal model or procedure with those elements already familiar.

## Design Implications

Pretraining reduces extraneous cognitive load during the main lesson: when learners do not know what a labeled component is, they must hold that unknown in working memory while also processing the system's behavior [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. Mayer's multimedia research shows that brief pretraining on component names and functions improves transfer on subsequent explanations of how a system works [Pretraining on component names and functions improves transfer from multimedia explanations.](../claims/pretraining-improves-transfer.md) [+S]. Pretraining is essentially a targeted form of [Activation](../principles/activation.md) — it builds the specific prior knowledge the main lesson depends on, rather than merely retrieving what learners already have.

### Context
#### Requirements
- An analysis of which concepts, terms, or components the main lesson assumes but does not itself teach
- A short, focused pre-instruction segment — names, functions, and key characteristics, not the full causal model
- Clear linkage between pretrained items and their appearance in the main lesson (same labels, same visuals)

#### Constraints
- Pretraining on material unrelated to the main lesson's demands adds load rather than reducing it [~M]
- Overlong pretraining delays the main instruction and can bore learners who already know the components [~M]
- Less effective when the main lesson is designed to teach the component knowledge itself — pretraining duplicates rather than prepares [~M]

#### Implementation Variability
- **Names-and-locations pretraining**: brief exposure to labeled diagrams before a how-it-works explanation (Mayer's original design)
- **Vocabulary pretraining**: teaching key terminology before reading complex disciplinary text
- **Pretraining within the lesson**: a "key concepts" panel or hover definitions that learners can consult on demand
- **Distributed pretraining**: component knowledge delivered in a prior unit or session, reactivated at the start of the main lesson

### Target Learners
- Novices who lack the domain vocabulary the lesson assumes [Pretraining on component names and functions improves transfer from multimedia explanations.](../claims/pretraining-improves-transfer.md) [+S]
- Learners with low prior knowledge, for whom unfamiliar terms consume disproportionate working memory [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]
- Less necessary for learners with relevant prior knowledge, who may find pretraining redundant [~M]

### Target Learning Goals
- Conceptual understanding: comprehending how a system, process, or model works
- Reading comprehension of technical or unfamiliar-domain text
- Reduced cognitive load as a precondition for deeper processing of causal relationships

### Instructions
1. Identify the prerequisite concepts, terms, and components the main lesson assumes ([Task Analysis](task-analysis.md))
2. Design a short pre-instruction segment teaching names, functions, and key characteristics — not the full model ([Advance Organizers](../elements/advance-organizers.md))
3. Present the pretraining immediately before the main lesson, using the same labels and visuals the lesson will use ([Chunking](../principles/chunking.md))
4. Briefly reactivate the pretrained knowledge at the start of the main lesson ([Activation](../principles/activation.md))
5. Proceed to the main explanation, now freed of terminology load ([Clear Structure](../principles/clear-structure.md))

## Related Strategies
- [Advance Organizers](../elements/advance-organizers.md) — a broader framing device; pretraining is a specific, content-focused variant
- [Activating Prior Knowledge](activating-prior-knowledge.md) — retrieves existing knowledge; pretraining builds missing knowledge
- [Vocabulary Pre-Teaching](vocabulary-pre-teaching.md) — the language-focused application in literacy instruction

## Examples
- **Mayer's lightning lesson**: learners first study a multimedia presentation naming the components of a lightning formation (updraft, downdraft, charged regions), then receive the causal explanation — pretrained learners outperformed controls on transfer tests
- **[4C/ID](../patterns/4cid-four-component-instructional-design.md)** — supportive information is presented before learning tasks so that task performance does not require simultaneous concept acquisition
- **Pre-teaching vocabulary in CKLA (Core Knowledge Language Arts)** — key domain terms are taught before students read complex texts on the topic ([https://www.coreknowledge.org](https://www.coreknowledge.org))

## Key Sources
- Mayer, R. E., Mathias, A., & Wetzell, K. (2002). Fostering understanding of multimedia messages through pre-training: Evidence for a two-stage theory of mental model construction. *Journal of Experimental Psychology: Applied, 8*(3), 147–154. [doi:10.1037/1076-898X.8.3.147](https://doi.org/10.1037/1076-898X.8.3.147)
- Pollock, E., Chandler, P., & Sweller, J. (2002). Assimilating complex information. *Learning and Instruction, 12*(1), 61–86. [doi:10.1016/S0959-4752(01)00016-0](https://doi.org/10.1016/S0959-4752(01)00016-0)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)