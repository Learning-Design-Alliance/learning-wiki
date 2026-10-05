---
type: principle
id: game-based-learning
title: Game-based Learning
description: "For a learner who has not yet reached a stated capability, a game whose winning move is the target reasoning, with modelling for novices and a debrief that asks for the reasoning outside the game, is expected to improve aligned outside-game performance; enjoyment and game score are separate outcomes, and no claim here tests games as a whole against non-game instruction."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: liu-2020
    resource: "https://doi.org/10.3991/ijet.v15i14.14675"
    title: "Liu, Z. Y., Shaikh, Z., & Gazizova, F. (2020). Using the concept of game-based learning in education. *International Journal of Emerging Technologies in Learning, 15*(14), 53-64"
    author: "Liu, Z. Y., Shaikh, Z., & Gazizova, F"
  - id: an-2020
    resource: "https://doi.org/10.46328/ijte.v3i2.27"
    title: "An, Y. (2020). Designing effective gamified learning experiences. *International Journal of Technology in Education, 3*(2), 62-69"
    author: An, Y
---

# Game-based Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 15 claims (7 for, 8 mixed) · 15 studies (6 causal, 5 quant-synthesis, 2 review, 1 associational, 1 theoretical), `q2`–`q4` · 5 of 15 report an effect size · 13 claims rest on one study

## Conditional relationship

For a learner who has not yet reached a stated capability, a game in which **the repeated move that wins is the target reasoning itself** (place the counter on the numbered square, choose the next equation step, pick the trade-off) is expected to improve performance on that capability measured *outside* the game, when three conditions hold: the mechanic demands the target thinking and cannot be won by a shortcut; a learner without a usable strategy is shown one (a model, a worked example, an adult naming what happens); and play is followed by a task that asks for the same reasoning without the game. The expected change is in `immediate-performance` and, where it has been tested, `delayed-retention` and `near-transfer` on an aligned measure. Enjoyment, time played and in-game score are separate outcomes (`motivation-affect`, `persistence`); they are not evidence of the capability, and the one comparison here that set a game against a tutoring system found them moving in opposite directions.

This page is about learning **through a full game**: the game is the learning activity. It is not about adding points, badges, levels or leaderboards to ordinary instruction, which is [Gamification](gamification.md); the wiki's one synthesis with a pooled effect is about gamification, and its numbers do not transfer to games (see below). The design discipline the relationship depends on, choosing a game mechanic that carries the learning without adding confounds, is set out in [Learning Embedded in the Core Mechanic](learning-embedded-in-the-core-mechanic.md); this page does not repeat it. No converted pattern instantiates this principle yet; [Game-Based Mastery Learning](../patterns/game-based-mastery-learning.md) and [Epistemic Games](../patterns/epistemic-games.md) are related unconverted patterns. Studying worked examples before or between rounds is modelled in [Worked Examples](worked-examples.md).

The wiki has **no claim that tests game-based learning as a whole** against a matched non-game condition across learners and domains. What it has is one randomized test of a game's mechanic with young children, one randomized test of adding worked examples to a puzzle game with adults, a confounded classroom comparison, and three second-hand reports. The default design below is therefore mostly the earlier page's guidance, labelled.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step says what supports it; most are untested as written.

1. **Name the capability, then make the winning move require it.** Write the one decision or action the learner must get better at, and check that the game's win condition cannot be reached without it (no guessing, button-mashing or reward route around it). Evidence: in [one randomized study](../claims/number-board-games-improve-numerical-knowledge.md) [+M] the same board game raised preschoolers' number knowledge when its squares were numbered 1–10 in a line, and not when they differed only in colour. One study, one domain; it does not show which features of other games matter.
2. **Show a novice the strategy before or between rounds.** Give one or two worked examples or a modelled round of play before the learner plays unaided, or between a first and second round. Evidence: adults who [studied worked examples between two rounds of a puzzle game](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [~M] improved more than those who did not, but [still learned a small fraction of what experts showed](../claims/worked-example-gains-in-a-puzzle-game-remain-small-relative-to-expert-knowledge-maps.md) [~M]. How many examples is not reported on the claim pages.
3. **Give an immediate, informative consequence for each move.** The game shows what the move did and, after an error, a hint toward the target reasoning rather than only a lost life. Untested; from the earlier page.
4. **Let learners fail safely and try again.** Several attempts per level, with no penalty that ends play. Untested in games; from the earlier page, which leaned on a claim about correcting confident errors that was not studied in a game (listed under Further evidence).
5. **Keep sessions short and repeat them.** The tested child dose was four 15–20 minute sessions over two weeks, with an adult playing alongside ([board-game study](../claims/number-board-games-improve-numerical-knowledge.md) [+M]). For other ages and domains, no dose is tested here; start with several short sessions rather than one long one, and record the dose given.
6. **Debrief after play.** Ask learners to state the rule or strategy that won, why it worked, and where it would fail, then apply it to one task with no game around it. Untested in games; from the earlier page.
7. **Judge the design outside the game**, on an aligned task at the horizon the objective sets, and record enjoyment separately. A game score or completion rate is not the outcome. See [the DragonBox report](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W].

How far the neighbouring claims may be carried: the board-game study is low-income preschoolers learning number with an experimenter playing alongside; the puzzle-game studies are 72 university students in one session-length experiment; neither says anything about older children in classrooms, workplace games, or games played with no adult present.

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether the learner already has a strategy for the target task.** A learner with none tends to flail through trial and error; one with a usable strategy can use play as practice. If unstated, ask: have they solved a task like this before, unaided, outside a game?
- **Whether an adult or peer will play alongside.** The tested child gains came with an adult running the game, and the board-game claim's own Discussion names the facilitator as a possible critical ingredient. If unstated, ask: who is present while they play, and will that person talk about the content or only the rules?
- **What outcome must change, and where it will be measured.** A game can raise enjoyment while a plainer tool raises test scores. If unstated, ask: what will the learner be able to do afterwards, outside the game, and how will you check?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on the target task | Add one or two worked examples or a modelled round before unaided play and again between rounds; keep game controls minimal | [Worked examples between rounds, puzzle game](../claims/worked-examples-improve-problem-solving-strategy-transfer-in-a-puzzle-game.md) [~M]; tested with university students, untested with children |
| Learners are preschool or early-primary `child`ren | Use a simple game whose board or move *is* the representation (e.g. a numbered linear track); an adult plays alongside naming the numbers or quantities; four sessions of 15–20 min over two weeks | [Board-game study](../claims/number-board-games-improve-numerical-knowledge.md) [+M]; [guided play](../claims/guided-play-improves-academic-outcomes.md) [~W] (guided play, not games specifically) |
| Learners are `adult` or professionals in a `workplace-clinical` setting | Build the game around one job decision with real consequences in its rules; debrief against the real procedure; keep competition optional | untested proposal; the earlier page's whole-task argument is a design argument, not a tested effect |
| The goal is `verbal-association` (vocabulary, facts) | A quiz or practice game is a reasonable vehicle; add glosses or supplementary word material inside it, and test recall a week later, not only at the end of play | [Kahoot! and outdoor games with migrant children](../claims/game-based-practice-outperforms-traditional-l2-vocabulary-instruction.md) [+W] (confounded); [adventure game with supplementary material](../claims/adventure-games-supplementary-material-vocabulary.md) [+W] (second-hand) |
| The goal is a `concept`, `principle` or `complex-skill` | Make the core move the reasoning itself; add a debrief and one non-game transfer task; expect slower gains than for facts | untested; from the earlier page |
| The goal is `attitude-motivation` (interest, confidence) | Measure enjoyment and the capability separately; do not report one as the other; a game can win on the first and lose on the second | [DragonBox vs Lynnette](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W] |
| `online-self-paced`, no teacher present | Put the modelling, hints and debrief questions inside the game (a worked example screen between levels, a "why did that work?" prompt after each level); log attempts per level to find where learners stall | untested proposal; the tested child gains had an adult present |
| Time is a `single-session` | Use one short game round, a worked example, a second round and a debrief; do not expect durable gains; if `days-weeks` are available, prefer several short sessions | untested proposal; the board-game dose is the only tested schedule here |
| Stakes are high or the game feeds a grade | Do not grade the in-game score unless its measurement has been designed for that ([Assessment Mechanic](../elements/assessment-mechanic.md)); assess on an aligned external task | untested; from the earlier page |
| Devices, motor demands, reading load or disability limit access | Choose a mechanic with no timing or precision demands beyond the target; offer a paper or board version; read text aloud or reduce it | untested; from the earlier page |

Four rows rest on a claim (novice, child, vocabulary and motivation), each tested in one narrow population or reported second-hand; the other six are untested proposals, most from the earlier page. Where competition or leaderboards are part of the brief, prefer team or self-referenced scoring and see [Gamification](gamification.md); that is untested here.

## Observation, state and explanation

What can be observed is play under stated conditions: moves made, levels reached, attempts per level, time spent, what a learner says while playing, and performance on a task outside the game. "Understands the concept" and "is motivated" are inferred states. Winning a level is an observation about the game, not about the capability, unless the winning move is the capability. Record the game version, any help given, who was present, and the dose.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Wins levels, fails the same idea outside the game | The game can be won by a shortcut that bypasses the target reasoning; knowledge tied to the game's representation; the outside task is unfamiliar in format | Ask the learner to explain the winning move; give the outside task once in the game's representation and once without it. |
| Enjoys the game, little gain on the test | The mechanic does not demand the target reasoning; play displaced practice time; the test is misaligned with what the game trains | Compare the test items with the moves the game requires; record time on the target move against total play time. |
| Many failed attempts, no improvement across them | No strategy to learn from consequences (novice); feedback says only "wrong"; controls or reading load are the barrier | Show one worked example or modelled round and see whether the next attempts change; replay with simplified controls or text read aloud. |
| Stops playing early | Too hard; competition discourages a low scorer; the learner does not value the task | Note where play stops; offer a non-competitive mode and an easier entry level, separately; ask what they wanted from it. |
| Improves after the game and a debrief | Gain from play, from the debrief, from added time on the topic, or from the adult's talk | Keep all exposures recorded. Only a comparison holding time and talk constant can credit the game. |

These are proposals, untested with learners. A probe can shift confidence between explanations; it does not identify a cause, and probing itself teaches.

## Evidence and qualifications

No claim in the wiki tests game-based learning as a general approach against a matched non-game condition. The claims below test parts of it.

- [Number Board Games Improve Numerical Knowledge](../claims/number-board-games-improve-numerical-knowledge.md) [+M]: 124 low-income preschoolers (mean age 4 years 9 months) were randomly assigned within centres to four 15–20 minute sessions over two weeks of a board game with an experimenter, on a linear board numbered 1–10 or an identical board varying only in colour (`randomized`). The numbered-board group improved on numeral identification, counting, magnitude comparison and number-line estimation at immediate posttest and at a 9-week follow-up (d = 0.65–1.08 across tasks at posttest); the colour group changed little. This is the closest test here of the relationship: same game, same play, only the content of the move differs. It does not show that a game beats non-game instruction, and the claim's Discussion notes the adult's naming of numbers may be a critical ingredient. One study; not yet checked against its source.
- Worked examples inside a puzzle game (one randomized experiment, 72 university students, the SafeCracker puzzle game): those who [studied worked examples between two rounds improved more on a knowledge map](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [~M] (2.21 against 0.62), and scored higher on a [problem-solving retention question](../claims/worked-examples-improve-problem-solving-strategy-retention-in-a-puzzle-game.md) [~M] and a [transfer question](../claims/worked-examples-improve-problem-solving-strategy-transfer-in-a-puzzle-game.md) [~M]; yet the worked-example group [learned only 2.7% of the experts' knowledge-map knowledge](../claims/worked-example-gains-in-a-puzzle-game-remain-small-relative-to-expert-knowledge-maps.md) [~M]. It qualifies learning through play alone: modelling added to the game helped, and play left most of the content unlearned. No test statistic or effect size is printed; the knowledge-map entry is checked by the judge on full text, the others not yet.
- [DragonBox users enjoyed the experience more, while Lynnette users performed better on the test](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W]: a review's report of a classroom experiment comparing an equation-solving game with an intelligent tutoring system. It limits the relationship: enjoyment and test performance went in opposite directions. Second-hand, no statistics printed, not yet checked.
- [Game-based vocabulary practice produced larger gains than traditional instruction for newly arrived migrant children](../claims/game-based-practice-outperforms-traditional-l2-vocabulary-instruction.md) [+W]: 48 Ukrainian children aged 6–7 in Italy for about a month, four weeks of game-based (Kahoot! and outdoor games) or traditional teaching, 40.29 to 171.91 words against 40.54 to 139.29. The claim page rates it weak deliberately: "game-based" confounds format, novelty, competition and being outdoors, so it motivates building a game but does not show a given game will work. The judge could not settle it on the abstract.
- [Game design, not learner age or linguistic background, determines DGBL effectiveness](../claims/game-design-moderates-dgbl-effectiveness.md) [~W]: a vocabulary-games review's report of another study that design, not age or language background, drove effectiveness, with adventure-oriented games more efficient than others. With [an adventure game plus supplementary vocabulary material beating a control](../claims/adventure-games-supplementary-material-vocabulary.md) [+W] from the same review, it suggests the game's design and what surrounds it matter more than "game" as a category. Both second-hand, no effect sizes, not yet checked.
- [Gamification has small positive effects on cognitive, motivational and behavioral learning outcomes](../claims/gamification-has-small-positive-effects-on-learning-outcomes.md) [~M]: a meta-analysis of game elements added to non-game instruction (cognitive g = .49; only the cognitive effect held among the more rigorous designs). It is cited here to mark a boundary, not to support this page: it is about gamification, not learning through a full game, and its pooled effects should not be quoted for games.

Taken together: a game helps when its move carries the content (one randomized child study); novices learn more from a game when shown worked examples, and still learn little from play alone (one adult study); enjoyment is not evidence of learning (one second-hand report); and the vocabulary-game evidence is confounded or second-hand. Learners, domains and outcomes differ across these claims; do not rank them by effect label.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M] — not settled: the text available could not confirm the entries (abstract)
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+M] — not yet checked against its sources
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — checked by the judge: all 1 entries pass (abstract)

## Objective and learner-valued goal

The designer's objective names the capability the game is meant to build and how it will be checked outside the game. Elicit separately what the learner wants from playing: to win, to beat a friend, to finish quickly, to get better at something they care about. Agreement and divergence are both observations; do not infer motivation from time played.

For example, a secondary-school student playing a city-budget simulation game may value topping the class leaderboard, while the designer's objective is reasoning about trade-offs between spending choices. If the leaderboard rewards the fastest balanced budget, the student can pursue what they value by repeating one safe pattern and never reason about trade-offs. Recording both aims shows where to change the scoring (reward an explained trade-off) and keeps a high score from being read as the objective met.

## What would revise this model?

The model should weaken if games whose core move carries the content, with modelling and a debrief, fail to beat a non-game version with the same content, time and talk on an aligned outside measure; or if, like the colour-only board, games with content-free moves produce the same gains, which would point to the adult's talk or the time spent rather than the game. If modelling inside games keeps helping while play alone adds little, the model should be restated as practice with modelling, delivered in a game format. If enjoyment and later persistence turn out to predict learning well, revise the separation of the two outcomes. Do not protect the model by calling every failure a badly designed game.

A gain in the game, a gain on an aligned outside test, delayed retention, transfer to a new task and continued voluntary practice are separate claims. The present evidence does not establish an effective dose beyond one preschool schedule, which game genres help which goals, or whether games help adults and older children at all compared with non-game practice.

## Related Principles
- [Learning Embedded in the Core Mechanic](learning-embedded-in-the-core-mechanic.md) — the design discipline this principle needs to be actionable: the learning has to be the repeated activity, not a gate around it.
- [Simulations & Immersive Virtual Environments](simulations-immersive-virtual-environments.md) — simulations overlap with game-based learning when the experience models a system learners must navigate.
- [Immediate Feedback](immediate-feedback.md) — games depend on fast consequence signals to support adaptation and persistence.
- [Error Analysis](error-analysis.md) — game loops often create repeated opportunities to learn from mistakes.
- [Guided Practice](guided-practice.md) — many instructional games work best after some initial modeling or guided rehearsal.

## Examples
- [Learning Mechanic](../elements/learning-mechanic.md) — the unit a game's teaching is actually built from: the theory-grounded activity repeated throughout play, which a concrete game mechanic instantiates.
- [Assessment Mechanic](../elements/assessment-mechanic.md) — its measurement counterpart, designed so the game's own log yields interpretable evidence rather than only a score.
- **Scenario-based digital games**: Learners manage resources, make choices, and see consequences unfold across rounds or levels.
- **Board or card games for concept practice**: Structured turn-taking and rules create repetition with feedback while keeping attention high.
- **Quiz-show style review games**: Fast cycles of attempt and feedback can increase practice volume when questions still align to real objectives.
- **Collaborative mission games**: Teams solve a shared problem, requiring explanation, coordination, and iterative strategy updates.

## Key Sources
- Eseryel, D., Law, V., Ifenthaler, D., Ge, X., & Miller, R. (2014). An investigation of the interrelationships between motivation, engagement, and complex problem solving in game-based learning. *Educational Technology & Society, 17*(1), 42-53.
- Liu, Z. Y., Shaikh, Z., & Gazizova, F. (2020). Using the concept of game-based learning in education. *International Journal of Emerging Technologies in Learning, 15*(14), 53-64. [https://doi.org/10.3991/ijet.v15i14.14675](https://doi.org/10.3991/ijet.v15i14.14675)
- Boghian, I., Cojocariu, V. M., Popescu, C. V., & Mâţă, L. (2019). Game-based learning - Using board games in adult education. *Journal of Educational Sciences and Psychology, 9*(1).
- An, Y. (2020). Designing effective gamified learning experiences. *International Journal of Technology in Education, 3*(2), 62-69. [https://doi.org/10.46328/ijte.v3i2.27](https://doi.org/10.46328/ijte.v3i2.27)

<!-- deprecated 2026-10-02: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Game-based learning is the instructional principle of using a game itself as the learning environment, with goals, rules, feedback, and progression aligned to specific learning outcomes. Unlike light gamification layered onto ordinary tasks, game-based learning makes the core learning activity intrinsically game-like: learners make decisions, test strategies, receive immediate consequences, and improve through repeated attempts. When designed well, it can increase time on task, support mastery through iteration, and make complex systems or decisions easier to experience directly.

## Implications
Game-based learning is strongest when the game mechanics require the same thinking the learning goal requires. Repeated attempts, immediate consequences, and visible progression can support mastery and persistence, especially when learners are allowed to fail safely and try again [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+S]. But engagement alone is not evidence of learning: if the reward structure can be optimized without understanding the target concept or strategy, the game teaches the wrong thing. Reflection and debriefing are therefore essential for turning in-game success into transferable understanding [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M], and some goals are still better served by giving novices worked models before asking them to learn through play alone [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S]. Game-based learning is strongest when the game also approximates whole-task decision making closely enough to support later transfer [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M].

### Context
#### Requirements
- **Aligned learning goals**: The win conditions and mechanics need to reflect the target skill, not merely add entertainment.
- **Tight feedback loops**: Learners need immediate in-game consequences, hints, or progress signals so they can adjust strategy during play.
- **Repeatable challenge**: The design should support multiple attempts, safe failure, and a visible path toward improvement [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+S].
- **Debrief or reflection**: Without explanation and transfer prompts, learners may improve at the game without extracting the intended concept or strategy [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].
#### Constraints
- **Reward distraction**: Points, badges, or competition can crowd out the learning goal if they are easier to optimize than the target skill.
- **Misaligned mechanics**: A game can be engaging while still teaching the wrong habits if the mechanics reward shortcuts unrelated to the intended outcome.
- **Accessibility barriers**: Reading load, pace, device demands, or sensory complexity can exclude learners if not deliberately designed for.
- **Transfer gap**: Success in a simulated or fictional environment does not guarantee transfer unless the task structure and debrief connect clearly to real use.

### Target Learners
- **Learners who benefit from active experimentation**: Particularly useful when understanding improves through trying, observing consequences, and iterating.
- **Learners with low engagement in traditional formats**: Game structure can increase participation when it clarifies goals and makes progress visible.
- **Learners practicing decision-making in systems**: Strong fit for content involving strategy, tradeoffs, sequencing, and dynamic feedback.
- **Groups learning social or collaborative skills**: Multiplayer or team-based formats can surface communication, coordination, and role-taking.

### Target Learning Objectives
- **Procedural fluency through repetition**: Repeated attempts can support mastery when each round gives useful feedback.
- **Strategic decision-making**: Learners practice selecting, testing, and revising plans under constraints.
- **Complex problem solving**: Simulated systems let learners observe interactions, consequences, and tradeoffs.
- **Motivation and persistence**: Progression systems can sustain effort when challenge and feedback are well calibrated.

### Theory
#### Supporting
- Flow theory (Csikszentmihalyi) — game-based environments can sustain attention when challenge and skill are well matched.
- Constructivist learning theory — learners build understanding by acting in an environment, seeing consequences, and revising mental models.
- Self-Regulated Learning (Zimmerman) — games with clear goals and feedback support monitoring, persistence, and strategy adjustment.
#### Contradicting / Qualifying
- The motivational benefits of games are not automatic; novelty can mask weak instructional design.
- Some learning goals are better served by direct explanation or worked examples before game-based practice, especially for novices [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S].

### Claims
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+S] — safe failure and rapid retry can make corrections inside games especially memorable
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M] — debrief and reflection are what convert in-game experience into explicit understanding
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S] — novices often need modeled play or strategy examples before game-based practice becomes productive
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M] — games support transfer best when their decisions and constraints resemble the real target performance
-->
