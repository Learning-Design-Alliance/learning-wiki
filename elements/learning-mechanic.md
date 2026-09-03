---
type: element
id: learning-mechanic
title: Learning Mechanic
description: The repeated learner-facing activity at the heart of a game for learning — a design pattern, grounded in learning theory, that a concrete game mechanic instantiates without displacing the learning goal.
status: review
generated:
  by: claude/unspecified
  at: 2026-09-03
sources:
  - id: plass-et-al-2011
    resource: "https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning"
    title: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). Learning mechanics and assessment mechanics for games for learning (G4LI White Paper #01/2011, v0.1). Games for Learning Institute."
    author: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K."
  - id: kirschner-2006
    resource: "https://doi.org/10.1207/s15326985ep4102_1"
    title: "Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. Educational Psychologist, 41(2), 75-86."
    author: "Kirschner, P. A., Sweller, J., & Clark, R. E."
  - id: schnotz-1999
    resource: "https://doi.org/10.1007/bf03172968"
    title: "Schnotz, W., Böckler, J., & Grzondziel, H. (1999). Individual and co-operative learning with interactive animated pictures. European Journal of Psychology of Education, 14(2), 245-265."
    author: "Schnotz, W., Böckler, J., & Grzondziel, H."
  - id: domagk-2010
    resource: "https://doi.org/10.1016/j.chb.2010.03.003"
    title: "Domagk, S., Schwartz, R. N., & Plass, J. L. (2010). Interactivity in multimedia learning: An integrated model. Computers in Human Behavior, 26(5), 1024-1033."
    author: "Domagk, S., Schwartz, R. N., & Plass, J. L."
  - id: isbister-2010
    resource: "https://doi.org/10.1145/1753326.1753637"
    title: "Isbister, K., Flanagan, M., & Hash, C. (2010). Designing games for learning: Insights from conversations with designers. CHI '10 Extended Abstracts, 2041-2044."
    author: "Isbister, K., Flanagan, M., & Hash, C."
---

# Learning Mechanic

> **Element** · [All elements](index.md)

## Description
A **game mechanic** is what a game lets you do — "the various actions, behaviors and control mechanisms afforded to the player within a game context" (Hunicke, LeBlanc, & Zubek, 2004, p. 3), or more narrowly the *core* mechanic, "the essential play activity players perform again and again and again" (Salen & Zimmerman, 2003, p. 316). A **learning mechanic** is the same idea asked of the learning, and Plass and colleagues define it in deliberate parallel:

> Learning mechanics are patterns of behavior or building blocks of learner interactivity, which may be a single action or a set of interrelated actions that form the essential learning activity that is repeated throughout a game.

The distinction this element exists to make is that a learning mechanic is **not itself playable**. It is a *design pattern* — a meta-mechanic, in Christopher Alexander's sense of a general solution to a recurring problem — that has to be instantiated as a concrete game mechanic before anyone can play it. "Apply rules to solve problems" is a learning mechanic. Flinging objects at targets, dragging them into place, or jetpacking them across a screen are three game mechanics that could each instantiate it. The relationship is one-to-many, and the choice among instantiations is a design decision with consequences for what actually gets learned.

That separation is what makes the common failure diagnosable. When a learning game bolts a popup quiz onto a racing or shooter mechanic, the game has a game mechanic and a *question*, not a learning mechanic — the essential repeated activity is still racing, and the learning is an interruption of it. Designers interviewed by Isbister, Flanagan and Hash (2010) made the same point from the practitioner's side: learning has to be embedded in the core mechanic rather than added to an existing one. Game play cannot be a reward for answering questions about facts, and factual quizzes cannot be forced into unrelated game play. See [Learning Embedded in the Core Mechanic](../principles/learning-embedded-in-the-core-mechanic.md) for the design principle and the three requirements that follow from it.

The worked example in the source is *Noobs vs. Leets*, a middle-school geometry game built at the Games for Learning Institute around the angle rules in the Grades 6–8 common core — complementary, supplementary, opposite, and sum-of-angles-in-a-triangle. Its learning mechanic is **apply rules to solve problems**: the learner selects among rules and indicates which problems each applies to. That mechanic was chosen over the obvious alternative — type the missing angle — precisely because it keeps the repeated activity at the conceptual level of the rules rather than at the level of arithmetic, which is where the learning goal lives.

## Design Implications

### Context
#### Requirements
- **Grounded in learning theory.** The source is explicit that this is the first criterion, not a nicety: a learning mechanic is derived from the learning sciences, and the examples given are Cognitive Flexibility Theory (Spiro et al., 1988), [Cognitive Apprenticeship](../theories/cognitive-apprenticeship.md) (Collins, 1988), Anchored Instruction (CTGV, 1990–1993), and [Situated Learning](../theories/situated-learning.md) (Lave, 1988; Lave & Wenger, 1990). *Noobs vs. Leets* draws on Schoenfeld's account of mathematical problem solving, Lave's situated learning, and schema theory.
- **A theoretical model of the interactivity itself**, not just of the content. The source points at the INTERACT model, which separates behavioral, cognitive and emotional interactivity and relates them through feedback and guidance (Domagk, Schwartz, & Plass, 2010).
- **Repetition.** The definition turns on *repeated throughout a game* — a one-off activity is a level, not a mechanic.
- **Learner-generated solutions.** Where the subject matter admits different but equally appropriate answers, the mechanic should let the learner generate their own rather than select from the designer's.
- **A game mechanic that preserves the goal.** Instantiation is where learning mechanics are usually lost; see the principle page for the three requirements a candidate game mechanic has to meet.

#### Constraints
- **A learning mechanic does not describe a tool.** It says the learner should be able to apply rules to solve problems; it says nothing about whether that is flinging, dragging, or jetpacking. Designers looking for buildable specifications will find the abstraction frustrating, and that abstraction is the point — it is what allows one mechanic to be reused across games.
- **Player agency has to survive.** The tension between the player's agency and the game's rule system is what makes a game worth playing; a learning mechanic that removes choice removes the reason to play.
- **Not every instantiation is equally valid.** Each game mechanic that could instantiate a given learning mechanic may only be suitable under specific conditions, and which conditions can often only be settled empirically.
- **"Fun and engaging" is not the bar.** When a game is designed with the explicit goal of facilitating learning, the mechanics have to go beyond engagement and engage players in a meaningful learning activity — engagement is necessary and nowhere near sufficient.

### Target Learners
- Learners for whom the target performance is a *repeated decision* rather than a recalled fact — the definition's insistence on repetition means the mechanic has to be worth doing many times
- Learners whose difficulty is conceptual rather than procedural, where a mechanic that surfaces the reasoning step is worth more than one that collects the answer
- Learners who can be given genuine choice within the rule system without the goal being lost

### Target Learning Goals
- Concept and rule application, at the conceptual level rather than the level of computing the answer [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M]
- Mental models of a system: through the representations and rules of the game, players form understandings of analogous real-world systems, including how the variables in them interact — what Bogost (2008) calls procedural rhetoric, arguments made "through the authorship of rules of behavior, the construction of dynamic models" (p. 125)
- Strategy selection and revision, since games present series of choices and react to them with new challenges

### Affordances
- [Game-based Learning](../principles/game-based-learning.md) — the learning mechanic is the unit that makes a game's mechanics carry the learning rather than surround it
- [Learning Embedded in the Core Mechanic](../principles/learning-embedded-in-the-core-mechanic.md) — the principle that governs instantiation, with the three requirements a game mechanic has to meet
- [Immediate Feedback](../principles/immediate-feedback.md) — feedback mechanisms are how a mechanic guides behaviour, and how the designer communicates what actions should and should not be taken

## Related Elements
- [Assessment Mechanic](assessment-mechanic.md) — the same construction applied to diagnosis rather than to learning; the two are designed together and constrain each other
- [Simulation](simulation.md) — a rule-based system the learner acts within, which is the substrate a learning mechanic usually runs on
- [Practice](practice.md) — the repetition a learning mechanic structures
- [Epistemic Games: Shared Understanding Moves](epistemic-games-shared-understanding-moves.md) — a mechanic-level account of a different game genre, where the repeated activity is the professional community's own work

## Examples
- **Apply rules to solve problems** (*Noobs vs. Leets*): the learner selects among the angle rules and indicates which problems each applies to, keeping the repeated activity at the level of the rules rather than at the level of subtraction.
- **Candidate instantiations of that one mechanic**, all considered by the G4LI team: the Fling mechanic from *Angry Birds*, the Drag mechanic from *Implode!*, and the Bounce mechanic from *Doodle Jump*. The one-to-many relationship is what a library of mechanics is for.
- **A counter-example, named as such by the source**: an established racing or shooter mechanic with a popup question gating the next round. The learning is an addendum to the mechanic, not the mechanic.
- **The G4LI library of learning mechanics** — an ongoing catalogue pairing each learning mechanic with the game mechanics that can instantiate it, published for designers to draw on.

## Key Sources
- Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). *Learning mechanics and assessment mechanics for games for learning* (G4LI White Paper #01/2011, Version 0.1). Games for Learning Institute (New York University, CUNY Graduate Center, Teachers College Columbia University). [researchgate.net/publication/272815253](https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning)
- Isbister, K., Flanagan, M., & Hash, C. (2010). Designing games for learning: Insights from conversations with designers. *CHI '10 Extended Abstracts on Human Factors in Computing Systems*, 2041–2044. [doi:10.1145/1753326.1753637](https://doi.org/10.1145/1753326.1753637)
- Domagk, S., Schwartz, R. N., & Plass, J. L. (2010). Interactivity in multimedia learning: An integrated model. *Computers in Human Behavior, 26*(5), 1024–1033. [doi:10.1016/j.chb.2010.03.003](https://doi.org/10.1016/j.chb.2010.03.003)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Schnotz, W., Böckler, J., & Grzondziel, H. (1999). Individual and co-operative learning with interactive animated pictures. *European Journal of Psychology of Education, 14*(2), 245–265. [doi:10.1007/bf03172968](https://doi.org/10.1007/bf03172968)
- Hunicke, R., LeBlanc, M., & Zubek, R. (2004). MDA: A formal approach to game design and game research. *Proceedings of the Challenges in Game AI Workshop, 19th National Conference on Artificial Intelligence (AAAI '04)*. AAAI Press.
- Salen, K., & Zimmerman, E. (2003). *Rules of play: Game design fundamentals*. MIT Press.
- Bogost, I. (2008). The rhetoric of video games. In K. Salen (Ed.), *The ecology of games: Connecting youth, games and learning* (pp. 117–140). MIT Press.
- Alexander, C. (1977). *A pattern language: Towns, buildings, construction*. Oxford University Press.

<!-- Citation provenance: every DOI above was resolved against Crossref on 2026-09-03 and
     passed scripts/resolve_doi_conflicts.classify_doi as `verified`. Two corrections were
     applied to the white paper's own reference list rather than reproduced from it: it
     gives Kirschner, Sweller & Clark as Educational Psychologist 46(2) (the registry says
     41(2)), and gives the Domagk, Schwartz & Plass title as "Defining interactivity in
     multimedia learning" against the registry's "Interactivity in multimedia learning: An
     integrated model" at the same journal, volume and pages. The books and the AAAI
     workshop paper carry no DOI and none was invented; they are the book backlog
     scripts/citation_worklist.py ranks separately. The G4LI white paper itself is
     self-published and has no DOI. -->
