---
type: strategy
id: dragonbox-algebra-5-app
title: DragonBox Algebra 5+ App
description: A game-based app that teaches algebraic reasoning by having learners manipulate cards to isolate a "box," implicitly solving equations before formal notation is introduced.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# DragonBox Algebra 5+ App

> **Strategy** · [All strategies](index.md)

## Description
DragonBox Algebra 5+ (WeWantToKnow AS) is a commercial game-based learning app that introduces algebraic equation solving through a fantasy card game. Learners drag cards and apply operations to isolate a glowing "box" on one side of a balance-like field; each move corresponds to a legal algebraic operation (adding to both sides, dividing both sides, etc.). Only after learners have mastered the implicit manipulation rules does the app progressively substitute formal notation — variables, coefficients, operators — for the game objects, mapping the game world onto standard equation syntax.

## Design Implications

The app exemplifies *implicit scaffolding through representational sequencing*: it teaches the structure of equation solving before the symbol system, reducing the simultaneous demands of learning procedures and decoding notation [Cognitive load theory: novices fail when intrinsic element interactivity is compounded by unfamiliar representations.](../theories/cognitive-load-theory.md) [+S]. The card-manipulation rules are discovered through play rather than stated, which works here because the rule space is small, deterministic, and immediately consequential — conditions under which guided discovery outperforms pure exposition [Unguided discovery is ineffective for novices, but constrained environments with immediate feedback narrow the gap.](../patterns/direct-instruction.md) [~M]. The progressive substitution of formal symbols for game objects is a form of fading the concrete representation, analogous to fading worked-example support [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

### Context
#### Requirements
- A tightly constrained rule space where every game action maps one-to-one onto a target-domain operation
- Immediate, visual feedback (illegal moves are impossible or visibly fail) so learners can infer rules from consequences
- A deliberate transition phase where game objects are replaced by formal notation — without this bridge, transfer to paper algebra is weak
- Adult or teacher support to name and consolidate what was learned implicitly ([Coaching](../elements/coaching.md))

#### Constraints
- Learning the game mechanics is not the same as learning algebra; learners can become fluent at isolating the box without ever verbalizing the underlying principle, producing shallow encoding [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [-M] — the app's implicit design provides no prompt for learners to articulate the rule
- Transfer to standard symbolic notation is limited if the notation-substitution phase is rushed or skipped; some studies of DragonBox-style apps find game performance does not predict paper-and-pencil equation solving without supplementary instruction [-M]
- The discovery-based mechanics demand more time than explicit instruction for equivalent procedural coverage, and weaker players can stall on game fluency rather than algebraic reasoning [~W]
- Effectiveness declines for learners who already know symbolic manipulation; the concrete game layer becomes redundant [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- Classroom use: play sessions interleaved with teacher-led notation lessons, so each game mechanic is named in algebraic terms shortly after it is discovered
- Home use: parent co-play with prompts ("what did that move do to both sides?") to add [Self-Explanation](../elements/self-explanation.md)-style articulation the app omits
- Remedial/intervention use for adolescents and adults with math anxiety, where the game frame lowers threat before formal instruction

### Target Learners
- Young learners (ages 5–12) encountering equation structure for the first time, for whom simultaneous notation decoding would overload working memory [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Novices who benefit from concrete, manipulable representations before abstract ones [~M]
- Older learners with existing symbolic fluency gain little and may find the game layer inefficient [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Implicit procedural schemas: the invariant structure "do the same operation to both sides to isolate the unknown"
- Pre-algebraic readiness: preparing learners to attach meaning to formal notation before it is introduced
- Not appropriate as a standalone route to symbolic fluency, word-problem interpretation, or algebraic justification

### Instructions
1. Let learners play the early levels without explanation, allowing the feedback loop to establish the manipulation rules ([Application](../elements/application.md) through immediate consequence).
2. At the notation-transition levels, co-play and name each move in algebraic language ("you divided both sides by 3") — the app fades the concrete representation, the adult supplies the formal label.
3. Follow game sessions with paper-and-pencil equations using the same structures, so the schema transfers off-screen.
4. Ask learners to explain *why* a move is legal, converting implicit procedure into articulable principle [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

## Related Strategies
- Concrete–representational–abstract sequencing — DragonBox automates the concrete-to-abstract transition that this instructional sequence manages manually
- Worked-example fading — the app's progressive symbol substitution parallels fading example completeness, though it fades representation rather than steps

## Examples
- **DragonBox Algebra 5+ / 12+** ([https://wewanttoknow.com](https://wewanttoknow.com)) — the app itself; the 12+ version introduces notation earlier and covers more equation types for older learners.
- **Norwegian classroom pilots** — WeWantToKnow reported school deployments in Norway where DragonBox play preceded formal algebra units; independent evaluations caution that game mastery must be paired with explicit notation instruction to show paper-test gains.
- **DragonBox Big Numbers** — the same developer applies the implicit-manipulation approach to place value and long addition/subtraction.

## Key Sources
- Clark, D. B., Tanner-Smith, E. E., & Killingsworth, S. S. (2016). Digital Games, Design, and Learning *Review of Educational Research, 86*(1), 79–122. [doi:10.3102/0034654315582065](https://doi.org/10.3102/0034654315582065)
- Wouters, P., van Nimwegen, C., van Oostendorp, H., & van der Spek, E. D. (2013). A meta-analysis of the cognitive and motivational effects of serious games. *Journal of Educational Psychology, 105*(2), 249–265. [doi:10.1037/a0031311](https://doi.org/10.1037/a0031311)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Mayer, R. E. (2019). *Computer games for learning: An evidence-based approach*. MIT Press.