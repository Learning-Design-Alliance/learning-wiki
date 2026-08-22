---
type: pattern
title: Cognitive Apprenticeship
description: Cognitive apprenticeship adapts the structure of traditional craft apprenticeship to the teaching of complex cognitive skills.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: lave-1991
    resource: "https://doi.org/10.1017/CBO9780511815355"
    title: "Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press"
    author: "Lave, J., & Wenger, E"
  - id: van-merriënboer-2018
    resource: "https://doi.org/10.4324/9781315113210"
    title: "van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge"
    author: "van Merriënboer, J. J. G., & Kirschner, P. A"
author: "Collins, Brown, & Newman (1989)"
grain_size: course, unit
---

# Cognitive Apprenticeship

## Description
Cognitive apprenticeship adapts the structure of traditional craft apprenticeship to the teaching of complex cognitive skills. Experts make their thinking visible through modeling and narration; learners then practice under coaching with gradually fading support until they can perform independently. Where traditional apprenticeship involves observable physical skill, cognitive apprenticeship focuses on surfacing invisible mental processes — how an expert reads, writes, solves problems, or debugs code.

## Implications

The pattern is grounded in the idea that expert performance is largely tacit: practitioners cannot simply tell novices what to do because much of their knowledge is embedded in practice rather than explicit rules. By externalizing expert reasoning through [think-aloud](/elements/think-aloud.md) and [demonstration](/elements/demonstration.md), cognitive apprenticeship makes that tacit knowledge learnable. The sequence of modeling → coaching → fading mirrors the natural progression from high support to independence, reducing cognitive load during acquisition [Worked examples reduce unnecessary search for novices.](/claims/worked-examples-reduce-novice-search.md) [+M] while building the metacognitive awareness needed for self-regulated performance.

### Context
#### Requirements
- An expert or instructor capable of making their reasoning explicit, not just demonstrating correct outcomes
- Structured opportunities for guided practice with feedback ([Coaching](/elements/coaching.md))
- A mechanism for progressively reducing support ([Fading](/elements/fading.md))
- Tasks that are sufficiently complex to require expert thinking — simple procedural tasks don't benefit from the full pattern

#### Constraints
- Time-intensive; difficult to scale in large classrooms without significant support structures
- Quality depends heavily on the instructor's ability to articulate reasoning, which varies widely
- Premature fading (removing support before competence develops) can cause setbacks [Worked-example guidance becomes less effective as learner expertise increases.](/claims/worked-examples-less-effective-with-expertise.md) [~M]
- Less effective for well-defined procedural tasks where direct instruction is more efficient

#### Grain Size
Course or unit — the full modeling → coaching → fading arc typically unfolds over weeks, not a single lesson.

### Target Goals
- Acquisition of complex cognitive skills: writing, mathematical reasoning, scientific inquiry, clinical diagnosis, programming
- Transfer of expert heuristics and strategies that are not easily articulated as rules
- Metacognitive awareness: learners monitoring and regulating their own thinking

### Target Learners
- Novices entering a domain with complex cognitive demands
- Learners who need to internalize expert judgment, not just follow procedures
- Apprentices, graduate students, medical residents, and others in professional formation contexts

### Theory
#### Supporting
- [Situated Learning](/theories/situated-learning.md) (Lave & Wenger) — learning is embedded in authentic practice; cognitive apprenticeship situates skill development in real or realistic tasks
- [Cognitive Load Theory](/theories/cognitive-load-theory.md) (Sweller) — modeling and fading manage cognitive load by providing support during acquisition and withdrawing it as schema develops
- [Self-Regulated Learning](/theories/self-regulated-learning.md) (Zimmerman) — explicit modeling of metacognitive moves supports learners in developing their own monitoring and control

#### Contradicting / Qualifying
- [Constructivism](/theories/constructivism.md) — some constructivist approaches favor learner-driven discovery over expert-led modeling; highly structured apprenticeship may limit generative processing

### Claims
#### Supporting
- [Worked examples reduce unnecessary search for novices.](/claims/worked-examples-reduce-novice-search.md) [+M] — worked examples (the modeling phase) reduce unnecessary search for novices
- [Pairing worked examples with practice or fading supports transfer better than examples alone.](/claims/worked-examples-with-practice-improve-transfer.md) [+S] — pairing demonstration with practice supports transfer
- [Example–problem sequences reduce cognitive load and improve learning outcomes](/claims/worked-examples-example-problem-sequences.md) [+S] — example–problem sequences outperform problem-only practice

#### Contradicting
- [Worked-example guidance becomes less effective as learner expertise increases.](/claims/worked-examples-less-effective-with-expertise.md) [~M] — expertise reversal: too much guidance can impede learners who already have strong prior knowledge

## Design

### Sequence
1. **Modeling** — Expert performs the target task while thinking aloud, using [worked examples](/elements/demonstration.md) or [think-aloud](/elements/think-aloud.md) to surface reasoning and decision points
2. **Coaching** — Learner attempts the task while the expert observes, gives targeted [feedback](/elements/feedback.md), and prompts reflection with [questions](/elements/eliciting-student-thinking.md)
3. **Scaffolding** — Expert provides [structured support](/elements/scaffolding.md) (hints, partial solutions, checklists) calibrated to where the learner struggles
4. **Fading** — Support is progressively reduced as competence develops, using [fading](/elements/fading.md) to shift responsibility to the learner
5. **Articulation** — Learner explains their reasoning aloud or in writing ([Articulation](/elements/articulation.md)), making tacit knowledge explicit
6. **Reflection** — Learner compares their performance to the expert model and identifies gaps ([Reflection](/elements/reflection.md))
7. **Exploration** — Learner applies skills to novel problems with minimal guidance

### Affordances
- [Worked Examples](/principles/worked-examples.md) — enacts this principle by making the modeling phase a narrated, annotated demonstration of expert problem-solving, giving learners a complete cognitive model to study before attempting tasks themselves
- [Scaffolding](/principles/scaffolding.md) — applies this principle by calibrating support (hints, partial solutions, checklists) to exactly where the learner struggles, providing just enough assistance to keep them progressing without removing the cognitive work that drives learning
- [Guided Practice](/principles/guided-practice.md) — implements this principle through the coaching phase, where learners attempt authentic tasks with expert observation and targeted feedback rather than practicing in isolation or receiving only after-the-fact grades
- [Purposeful Reflection](/principles/purposeful-reflection.md) — builds this principle directly into the sequence: the articulation and reflection phases require learners to compare their own performance to the expert model and name specific gaps, turning implicit self-assessment into deliberate metacognitive work

### Personalization

**Novices with no prior knowledge:** Extend the modeling phase — provide multiple worked examples across varied problem types before moving to coaching. Use explicit think-alouds at every decision point, not just key steps. Keep tasks simple and well-defined during early modeling so the process itself is the focus.

**Learners with some background knowledge:** Compress or skip early modeling; start at the coaching phase with more complex or ambiguous tasks. Reduce the amount of narrated reasoning and shift responsibility for articulation to the learner earlier.

**Learners with anxiety or low confidence:** Consider peer modeling rather than expert modeling — watching someone of similar status struggle and succeed reduces the intimidation of expert performance. Build early wins with simpler tasks before increasing challenge.

**Learners with diverse prior knowledge in the same cohort:** Use differentiated fading — keep scaffolds available for those who need them while allowing more advanced learners to bypass them. Pair-based coaching (stronger with weaker) can extend reach in large classrooms.

**Learners with language or learning differences:** Supplement verbal think-alouds with written annotations or visual step-maps so the reasoning is persistent and reviewable, not just heard once. Extend the coaching phase and reduce the pace of fading.

## Related Patterns
- [Four-Component Instructional Design](/patterns/4cid-four-component-instructional-design.md) — shares the principle of worked examples fading to full tasks; provides more formal scaffolding design rules for complex learning
- [Guided Discovery Learning](/patterns/guided-discovery-learning.md) — similar progression from support to independence, but begins with learner exploration rather than expert modeling

## Examples

**Medical education — clinical rounds:** Attending physicians model diagnostic reasoning by thinking aloud through a patient case, then coach residents through their own case assessments with progressively less guidance over weeks.

**Writing instruction — writer's workshop:** Teacher models drafting and revision strategies on a shared text, thinking aloud about audience and structure; students write alongside with peer and teacher coaching; feedback is gradually reduced as writers develop independent revision habits. Uses [teacher modeling](/elements/demonstration.md), [conferencing](/elements/feedback.md), and [author's chair](/elements/articulation.md) sharing.

**Engineering education — design studios:** Expert designers walk through a design decision process on a real project; students work on their own projects with structured critiques (charettes) that fade from expert-led to peer-led over the semester.

**[Replit](https://replit.com) and paired programming environments:** Expert-novice pairing where the expert narrates code decisions; over time the novice takes the keyboard while the expert coaches. Fading occurs as the novice's contributions increase.

## Key Sources
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453–494). Lawrence Erlbaum.
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator, 15*(3), 6–11, 38–46.
- Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press. [doi:10.1017/CBO9780511815355](https://doi.org/10.1017/CBO9780511815355)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315113210](https://doi.org/10.4324/9781315113210)
