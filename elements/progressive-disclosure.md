---
type: element
title: Progressive Disclosure
description: Progressive disclosure presents information in sequenced stages, revealing complexity only as the learner is ready, rather than showing everything at once.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Progressive Disclosure

## Description
Progressive disclosure structures content so that learners see a simplified or partial view first, with additional layers of detail, options, or complexity revealed only after the foundational material is mastered. It functions as a sequencing element: the design decision is not *what* to teach but *when* each piece becomes visible, keeping the learner's working-memory load matched to their current competence.

## Design Implications

Progressive disclosure manages intrinsic load by preventing the simultaneous presentation of elements a novice cannot yet integrate [Chunking reduces working-memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. Its effectiveness depends on the segmentation being meaningful — each stage should be a coherent unit, not an arbitrary slice — and on learners controlling or at least anticipating the sequence, since forced pacing without consolidation produces fragmented knowledge [~M]. As expertise grows, the staged structure should be removed; retaining it for advanced learners wastes time and can impair learning [Expertise reverses the benefit of instructional support.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- A task analysis identifying which elements are essential first and which are elaborations
- Meaningful segment boundaries — each stage is a coherent concept or subtask, not an arbitrary chunk
- A consolidation point at each stage (practice, check, or summary) before new material is revealed ([Practice](practice.md), [Check-In](check-in.md))
- A plan for fading the structure as learners gain expertise

#### Constraints
- Hiding information can frustrate learners who already know it or who need the big picture to orient themselves; an advance organizer or visible roadmap mitigates this [~M]
- Over-segmentation fragments knowledge and prevents learners from seeing relationships between parts, harming transfer [~M]
- For experts, staged presentation is redundant and slows performance [Expertise reverses the benefit of instructional support.](../claims/expertise-reversal-effect.md) [-M]
- In exploratory or open-ended tasks, premature restriction of information can block the productive search that generates learning [~W]

### Target Learners
- Novices facing high-element-interactivity material (complex procedures, dense interfaces, multi-step processes) [Chunking reduces working-memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Learners with low prior knowledge who cannot yet integrate many simultaneous elements [Graphic organizers support novice comprehension.](../claims/graphic-organizers-support-novice-comprehension.md) [+M]
- Less beneficial for advanced learners, who benefit from seeing the full structure at once [Expertise reverses the benefit of instructional support.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: building a complex skill one subtask at a time
- Conceptual understanding of layered systems (e.g., software, statistics, grammar)
- Schema construction where element interactivity would otherwise overwhelm working memory

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — progressive disclosure enacts this principle directly by controlling how many interacting elements are visible at once, keeping intrinsic load within working-memory limits
- [Chunking](../principles/chunking.md) — each disclosure stage is a chunk; the sequencing turns isolated chunks into an ordered learning path rather than a wall of content
- [Clear Structure](../principles/clear-structure.md) — a staged reveal gives the material an explicit, predictable shape, which learners can use to orient themselves and anticipate what comes next
- [Scaffolding](../principles/scaffolding.md) — hidden detail is temporary support; the design question is when to fade it, mirroring the fading of worked-example steps

## Related Elements
- [Advance Organizers](advance-organizers.md) — provide the overview that staged disclosure otherwise hides, preventing disorientation
- [Fading](fading.md) — the mechanism for removing staged support as competence grows
- [Practice](practice.md) — the consolidation activity at each stage before new content is revealed
- [Analogies](analogies.md) — a simplified first-stage representation often takes the form of an analogy to familiar material

## Patterns That Use This Element
- [Cognitive Load Reduction (CLT Scaffolding Approach)](../patterns/cognitive-load-reduction-clt-scaffolding-approach.md) — sequencing is a primary load-reduction lever
- [4C/ID (Four-Component Instructional Design)](../patterns/4cid-four-component-instructional-design.md) — learning tasks are ordered from simple to complex with supportive information staged accordingly
- [Elaboration Theory](../patterns/elaboration-theory.md) — epitome-first, increasingly detailed elaborations are a canonical progressive-disclosure structure

## Examples

**Segmented instructional video** — Mayer's segmenting principle: allowing learners to control playback and presenting a continuous animation in learner-paced segments improves retention and transfer compared with continuous presentation (see [Mayer & Chandler, 2001](https://doi.org/10.1037/0022-0663.93.3.638)).

**[Duolingo](https://www.duolingo.com)** — introduces grammar concepts one construction at a time, unlocking later units only after earlier skills reach mastery thresholds.

**[Khan Academy](https://www.khanacademy.org)** — mastery-based unit progression: hints and later lessons are revealed only after earlier exercises, with each hint itself a partial disclosure of the full solution.

**[Codecademy](https://www.codecademy.com)** — early lessons expose only a minimal API surface; additional language features and tooling appear in later modules as prerequisite fluency is established.

## Key Sources
- Mayer, R. E., & Chandler, P. (2001). When learning is harder than it has to be: Simultaneous, successive, and segmented multimedia presentations. *Journal of Educational Psychology, 93*(3), 638–650. [doi:10.1037/0022-0663.93.3.638](https://doi.org/10.1037/0022-0663.93.3.638)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Reigeluth, C. M., & Stein, F. S. (1983). The elaboration theory of instruction. In C. M. Reigeluth (Ed.), *Instructional-Design Theories and Models*. Lawrence Erlbaum Associates.