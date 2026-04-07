---
type: element
status: review
last_edited: 2026-04-06
edited_by: Claude
---

# Demonstration

## Description
A demonstration presents a complete or partial model of a skill, process, or solution so learners can observe expert performance before attempting it themselves. The instructor or system makes thinking visible — articulating what is being done and why — rather than simply showing the end result.

## Design Implications

Demonstrations reduce the cognitive burden of initial skill acquisition by giving learners a reference model to study and imitate [[claims/we-1]] [+M]. Their value depends heavily on how thinking is made visible: narrated or annotated demonstrations that explain reasoning produce better learning than silent ones. Demonstrations should be followed by practice opportunities, since passive observation without application leads to shallow encoding [[claims/we-2]] [+S].

### Context
#### Requirements
- A clear, accurate model of the target performance
- Narration or annotation that makes reasoning explicit, not just actions ([[elements/think-aloud|Think-Aloud]] or written commentary)
- A follow-on activity that requires learners to apply what they observed ([[elements/practice|Practice]])

#### Constraints
- Passive observation without prompts or practice creates illusions of understanding [[claims/we-2]] [-S] — learners often overestimate how much they have learned from watching alone
- Less effective for open-ended or creative tasks where there is no single correct approach
- Can anchor learners to a single solution method; pairing with [[elements/non-examples|Non-Examples]] or [[elements/comparing-cases|Comparing Cases]] reduces this risk

### Target Learners
- Novices encountering a skill or process for the first time [[claims/we-1]] [+M]
- Learners with limited prior knowledge who would otherwise spend effort on unguided search
- Less beneficial for learners with strong prior knowledge, who may find explicit modeling redundant [[claims/we-3]] [~M]

### Target Learning Goals
- Procedural skill acquisition: understanding the steps of a process
- Schema formation: building a mental model of task structure
- Metacognitive modeling: learning what expert monitoring and decision-making looks like

### Affordances
- [[principles/worked-examples|Worked Examples]] — a demonstration applied to a problem-solving context enacts this principle by giving learners a complete solution to study before attempting their own; the worked example *is* the demonstration with added reasoning annotation
- [[principles/explicit-instruction|Explicit Instruction]] — demonstration enacts this principle by having the expert narrate decisions aloud ("I'm choosing this approach because…"), converting tacit knowledge into observable, learnable steps rather than leaving learners to infer intent from outcomes
- [[principles/cognitive-load-management|Cognitive Load Management]] — by externalizing each step of a task, demonstration lets learners attend to *understanding* the structure rather than holding intermediate states in working memory while simultaneously figuring out what to do next
- [[principles/scaffolding|Scaffolding]] — a demonstration functions as temporary external structure; the key design decision is when and how to fade it — moving from full worked examples to partial examples to problem-only as competence grows

## Related Elements
- [[elements/practice|Practice]] — the necessary follow-on; demonstration without practice rarely transfers
- [[elements/think-aloud|Think-Aloud]] — the narration method that makes demonstration effective
- [[elements/fading|Fading]] — progressively reduces the completeness of demonstrations as expertise grows
- [[elements/non-examples|Non-Examples]] — contrasting a correct demonstration with a flawed one sharpens discrimination
- [[elements/procedural-information|Procedural Information]] — text or diagram form of the same function

## Patterns That Use This Element
- [[patterns/cognitive-apprenticeship|Cognitive Apprenticeship]] — modeling phase
- [[patterns/4cid-four-component-instructional-design|Four-Component Instructional Design]] — worked examples as the demonstration component of learning tasks
- [[patterns/gagnés-9-events-of-instruction|Gagné's 9 Events]] — "present the content" event

## Examples

**[[strategies/use_worked_examples|Use Worked Examples]]** — Presents a fully solved problem with step-by-step reasoning, then asks learners to solve a similar problem. The worked example is the demonstration component.

**[[strategies/think-aloud-modeling|Think-Aloud Modeling]]** — Instructor verbalizes their reasoning while solving a problem or reading a text, making metacognitive moves visible (monitoring confusion, checking work, revising approach).

**[Khan Academy](https://www.khanacademy.org)** — Video demonstrations with narrated step-by-step problem solving, followed by [[elements/practice|practice exercises]] with hints. The hint system itself delivers sub-demonstrations on demand.

**[Codecademy](https://www.codecademy.com)** — Annotated code demonstrations inline with [[elements/practice|coding exercises]]; learners see a working example before writing their own version.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Bandura, A. (1977). Social learning theory. *Englewood Cliffs, NJ: Prentice Hall.*
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)

