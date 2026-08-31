---
type: strategy
title: Modeling Multi Step Processes
description: Explicitly demonstrating each step of a multi-step procedure, with reasoning narrated, so learners can observe the full sequence before performing it themselves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Modeling Multi Step Processes

> **Strategy** · [All strategies](index.md)

## Description
Modeling multi step processes is a strategy in which the instructor or system performs a complex procedure in full view of learners, executing and naming each step in order while articulating the reasoning and decision points between steps. It differs from a single-skill [Demonstration](../elements/demonstration.md) in that the target is a *sequence* — learners must acquire not only each step but the order, transitions, and conditional decisions that connect them. Effective models make the procedure's structure visible (e.g., a step list or flowchart alongside the performance) and are typically followed by guided [Practice](../elements/practice.md) with [Fading](../elements/fading.md).

## Design Implications
Multi-step procedures impose a sequencing problem on working memory: learners must hold the goal, the current step, and the remaining steps simultaneously. An external model offloads this structure so learners can attend to understanding each step rather than reconstructing the order [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Presenting the procedure as grouped, named phases — rather than an undifferentiated stream of actions — further reduces load and supports schema formation. The model's value depends on making decisions explicit: a silent performance shows *what* but not *when* or *why*, which is precisely what learners cannot infer from a multi-step sequence on their own.

### Context
#### Requirements
- A task analysis identifying every step, decision point, and common error in the procedure
- Narration that verbalizes both actions and the conditions that trigger them ([Think-Aloud](../elements/think-aloud.md))
- A persistent external representation of the sequence (step list, flowchart, or annotated checklist) learners can consult during early attempts
- Immediate follow-on practice, ideally with the model available for comparison ([Practice](../elements/practice.md))

#### Constraints
- Modeling a long procedure in one pass can exceed working memory; without segmentation or [Chunking](../principles/chunking.md), later steps displace earlier ones [~M]
- A single correct model can anchor learners to one method and blind them to alternatives or to conditional variations the model did not show [-M]
- Learners with substantial prior knowledge of the procedure find full step-by-step modeling redundant and it can slow them down [Expertise reverses the benefit of detailed instructional guidance.](../claims/expertise-reversal-effect.md) [~S]
- Watching a fluent expert perform quickly can create an illusion of competence; steps that look easy are often the ones learners fail to execute [-M]

#### Implementation Variability
- **Segmented modeling:** demonstrate one phase at a time with practice between phases, rather than the whole sequence at once
- **Part-whole progression:** model and practice individual sub-skills first ([Part-task practice](../elements/part-task-practice.md)), then integrate into the full sequence
- **Faded modeling:** instructor performs the full sequence, then progressively hands steps to learners until they perform independently [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]
- **Erroneous modeling:** deliberately perform a common error and have learners detect it, sharpening discrimination at decision points [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Static vs. dynamic models:** annotated worked solutions on paper versus live or video performance; dynamic models better convey timing and transitions

### Target Learners
- Novices encountering the procedure for the first time, who otherwise cannot know the order or the decision rules connecting steps [+M]
- Learners who benefit from reduced search: the model eliminates trial-and-error discovery of the sequence [+M]
- Less beneficial for experienced learners, for whom full modeling is redundant and can impair performance relative to problem-solving alone [Expertise reverses the benefit of detailed instructional guidance.](../claims/expertise-reversal-effect.md) [~S]

### Target Learning Goals
- Procedural fluency: executing a known sequence accurately and in order
- Conditional knowledge: knowing *when* each step applies and what to do at branch points
- Metacognitive modeling: showing how experts monitor progress, detect errors, and recover mid-procedure

### Instructions
1. Decompose the procedure into named steps and decision points; group steps into phases ([Chunking](../principles/chunking.md))
2. Present the full sequence as an advance organizer so learners have a map before the performance ([Advance Organizers](../elements/advance-organizers.md))
3. Model the procedure while thinking aloud, verbalizing the condition that triggers each step ([Think-Aloud](../elements/think-aloud.md))
4. Re-model with learner participation: prompt learners to supply the next step and its justification before you perform it
5. Fade the model: learners perform with the step list, then without it, with coaching at decision points ([Fading](../elements/fading.md), [Coaching](../elements/coaching.md))
6. Follow with independent [Practice](../elements/practice.md) and feedback targeted at step sequence and transition errors

## Related Strategies
- Worked Examples — the static, problem-solving analogue: a completed solution models the sequence on paper
- Part-Task Practice — isolates and drills sub-skills before whole-procedure integration
- Cognitive Apprenticeship — positions modeling as the first phase of a modeling–coaching–fading cycle
- Direct Instruction — embeds modeling within a scripted demonstrate–guide–independent-practice sequence

## Examples
- **Writing instruction:** the teacher models composing a persuasive paragraph on the board, thinking aloud through planning, drafting, and revising — the core "modelled writing" move in [Explicit Teaching](../patterns/explicit-teaching.md)
- **Khan Academy** (https://www.khanacademy.org) — narrated, segmented video solutions for multi-step math procedures, each step annotated, followed by practice with on-demand hints
- **Codecademy** (https://www.codecademy.com) — annotated multi-step coding walkthroughs preceding learner-written code
- **Clinical skills labs** — instructors model a full patient assessment sequence (inspect, auscultate, palpate…) with decision rules narrated, then observe students performing it with a checklist

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Bandura, A. (1977). *Social learning theory.* Prentice Hall.
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction* (pp. 453–494). Lawrence Erlbaum. [doi:10.4324/9781315044408-14](https://doi.org/10.4324/9781315044408-14)
