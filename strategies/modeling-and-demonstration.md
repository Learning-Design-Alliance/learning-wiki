---
type: strategy
title: Modeling And Demonstration
description: The instructor or system performs a skill while making reasoning visible, so learners can observe expert performance before attempting it themselves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Modeling And Demonstration

## Description
Modeling and demonstration involve an expert performing a task — solving a problem, executing a procedure, applying a strategy — while learners observe. Its power comes from making thinking visible: the modeler narrates decisions, monitors their own understanding, and shows how errors are detected and corrected, rather than merely displaying the finished product.

## Design Implications

Observing a model reduces the unguided search that overwhelms novices during initial skill acquisition [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M], and demonstrations that verbalize the reasoning behind actions produce better learning than silent ones [van Gog & Rummel, 2010]. Demonstration must be paired with opportunities to apply what was observed; observation alone yields shallow encoding and overconfidence [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S].

### Context
#### Requirements
- An accurate, complete (or deliberately partial) model of the target performance
- Narration or annotation that exposes decision points and criteria, not just actions ([Think-Aloud](../elements/think-aloud.md))
- A planned follow-on activity requiring immediate application ([Practice](../elements/practice.md))
- Segmented presentation — pausing, chunking, or replay controls — so learners can process each step ([Chunking](../principles/chunking.md))

#### Constraints
- Watching without applying creates an illusion of competence; learners systematically overestimate what they learned from observation [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- Overly fluent, error-free demonstrations can make performance look easier than it is; showing productive struggle and self-correction improves learners' persistence and self-efficacy [-M]
- Less effective for open-ended or creative tasks with no single correct approach
- Can anchor learners to one solution method; contrasting multiple models or including flawed examples reduces this risk
- Learners with high prior knowledge gain little and may be slowed by explicit modeling [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

#### Implementation Variability
- **Live vs. recorded:** recorded demonstrations allow replay and pacing control; live modeling allows responsiveness to learner questions
- **Full vs. faded:** begin with complete models and progress to partial ones ([Fading](../elements/fading.md))
- **Multiple models:** presenting two or three contrasting competent models supports comparison and generalization better than a single model [~M]
- **Coping models:** models who struggle, err, and recover produce stronger self-efficacy gains than mastery models for anxious or low-confidence learners [~M]

### Target Learners
- Novices encountering a skill or process for the first time [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners with low self-efficacy for the task, who benefit from seeing a peer-like model succeed [Bandura, 1977]
- Less beneficial for experts or near-experts, for whom modeling is redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: learning the steps and sequence of a process
- Strategic and metacognitive skill: seeing how experts monitor, evaluate, and revise their approach
- Schema construction: building a mental model of task structure before independent problem solving

### Instructions
1. Identify the target skill and the expert decisions it involves; script the reasoning, not just the actions.
2. Deliver the demonstration with [Think-Aloud](../elements/think-aloud.md) narration, segmented into digestible steps ([Chunking](../principles/chunking.md)).
3. Follow immediately with [Practice](../elements/practice.md) on a similar task, ideally with [Fading](../elements/fading.md) from full to partial models.
4. Include [Coaching](../elements/coaching.md) and feedback as learners attempt the task themselves.

## Related Strategies
- [Worked Examples](worked-examples.md) — demonstration applied to problem solving, with written reasoning annotation
- [Scaffolding](scaffolding.md) — demonstration is the most supportive rung, faded as competence grows
- [Direct Instruction](direct-instruction.md) — instructional sequence in which modeling precedes guided and independent practice

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — narrated video demonstrations of problem solving followed by practice exercises with on-demand hints.
- **[Codecademy](https://www.codecademy.com)** — annotated code demonstrations shown inline before learners write their own version.
- **Writing conferences and mentor texts** — teachers model drafting and revision decisions aloud before students write, a core move in workshop-model literacy instruction.
- **Cognitive Apprenticeship** ([Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)) — positions modeling as the first phase, followed by coaching and articulation.

## Key Sources
- Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review, 84*(2), 191–215. [doi:10.1037/0033-295X.84.2.191](https://doi.org/10.1037/0033-295X.84.2.191)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction* (pp. 453–494). Lawrence Erlbaum. [doi:10.4324/9781315044408-14](https://doi.org/10.4324/9781315044408-14)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)