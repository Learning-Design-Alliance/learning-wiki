---
type: principle
id: game-based-learning
aliases: [learning-embedded-in-the-core-mechanic, add-worked-examples-to-commercial-off-the-shelf-games-for-training]
title: Game-based Learning
description: "For a learner who has not yet reached a stated capability, a game whose winning move is the target reasoning, played over several sessions inside a course of instruction, with modelling for novices and a debrief that asks for the reasoning outside the game, is expected to improve aligned outside-game performance over passive or no instruction; meta-analyses find small-to-moderate average gains that vary widely and disappear against active non-game instruction, and enjoyment and game score are separate outcomes."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: an-2020
    resource: "https://doi.org/10.46328/ijte.v3i2.27"
    title: "An, Y. (2020). Designing effective gamified learning experiences. *International Journal of Technology in Education, 3*(2), 62-69"
    author: An, Y
  - id: plass-et-al-2011
    resource: "https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning"
    title: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). Learning mechanics and assessment mechanics for games for learning (G4LI White Paper #01/2011, v0.1). Games for Learning Institute."
    author: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K."
  - id: isbister-2010
    resource: "https://doi.org/10.1145/1753326.1753637"
    title: "Isbister, K., Flanagan, M., & Hash, C. (2010). Designing games for learning: Insights from conversations with designers. CHI '10 Extended Abstracts, 2041-2044."
    author: "Isbister, K., Flanagan, M., & Hash, C."
  - id: kirschner-2006
    resource: "https://doi.org/10.1207/s15326985ep4102_1"
    title: "Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. Educational Psychologist, 41(2), 75-86."
    author: "Kirschner, P. A., Sweller, J., & Clark, R. E."
  - id: schnotz-1999
    resource: "https://doi.org/10.1007/bf03172968"
    title: "Schnotz, W., Böckler, J., & Grzondziel, H. (1999). Individual and co-operative learning with interactive animated pictures. European Journal of Psychology of Education, 14(2), 245-265."
    author: "Schnotz, W., Böckler, J., & Grzondziel, H."
  - id: shen-2006
    resource: "https://eric.ed.gov/?id=ED491961"
    title: "Shen, C.-Y., & O’Neil, H. (2006). The Effectiveness of Worked Examples in a Game-Based Learning Environment. Paper presented at the annual meeting of the American Educational Research Association (AERA), San Francisco, CA. https://eric.ed.gov/?id=ED491961"
    author: "Shen, C.-Y., & O’Neil, H"
  - id: clark-2016
    resource: "https://doi.org/10.3102/0034654315582065"
    title: "Clark, D. B., Tanner-Smith, E. E., & Killingsworth, S. S. (2016). Digital games, design, and learning: A systematic review and meta-analysis. Review of Educational Research, 86(1), 79-122."
    author: "Clark, D. B., Tanner-Smith, E. E., & Killingsworth, S. S."
  - id: arztmann-2023
    resource: "https://doi.org/10.1080/03057267.2022.2057732"
    title: "Arztmann, M., Hornstra, L., Jeuring, J., & Kester, L. (2023). Effects of games in STEM education: A meta-analysis on the moderating role of student background characteristics. Studies in Science Education, 59(1), 109-145."
    author: "Arztmann, M., Hornstra, L., Jeuring, J., & Kester, L."
---

# Game-based Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 69 claims (33 for, 35 mixed, 1 against) · 54 studies (16 causal, 14 quant-synthesis, 12 review, 4 design, 4 theoretical, 3 associational, 1 qualitative), `q1`–`q4` · 16 of 54 report an effect size · 63 claims rest on one study

## Conditional relationship

For a learner who has not yet reached a stated capability, a game in which **the repeated move that wins is the target reasoning itself** (place the counter on the numbered square, choose the next equation step, pick the trade-off) is expected to improve performance on that capability measured *outside* the game, when three conditions hold: the mechanic demands the target thinking and cannot be won by a shortcut; a learner without a usable strategy is shown one (a model, a worked example, an adult naming what happens); and play is followed by a task that asks for the same reasoning without the game. Two further conditions come from the syntheses: the game is played over **more than one session**, and it is **part of a course of instruction** rather than the whole of it. The expectation is against no instruction or passive instruction (reading, lecture); against active non-game instruction on the same content, the one synthesis that split its comparisons this way found no advantage for the game. The expected change is in `immediate-performance` and, where it has been tested, `delayed-retention` and `near-transfer` on an aligned measure. Enjoyment, time played and in-game score are separate outcomes (`motivation-affect`, `persistence`); they are not evidence of the capability, and the one comparison here that set a game against a tutoring system found them moving in opposite directions.

This page is about learning **through a full game**: the game is the learning activity. It is not about adding points, badges, levels or leaderboards to ordinary instruction, which is [Gamification](gamification.md); the gamification meta-analysis's numbers and the game meta-analyses' numbers below do not transfer to each other. The design discipline the relationship depends on, choosing a game mechanic that carries the learning without adding confounds, is set out in [Learning Embedded in the Core Mechanic](game-based-learning.md); this page does not repeat it. No converted pattern instantiates this principle yet; [Game-Based Mastery Learning](../patterns/game-based-mastery-learning.md) and [Epistemic Games](../patterns/epistemic-games.md) are related unconverted patterns. Studying worked examples before or between rounds is modelled in [Worked Examples](worked-examples.md).

Three meta-analyses in the wiki compare games with non-game conditions as a whole: digital games for K–16 learners (57 studies, g = 0.33), games in primary and lower-secondary STEM (cognition g = .67, with a prediction interval from −0.38 to 1.76) and computer-based simulation games in workplace and university training (published studies d = .52, unpublished d = −.10). They give an average over very different games, not a forecast for one: effects vary widely, shrink with secondary-school learners, depend on the comparison condition, the number of sessions and whether play is competitive, and show signs of publication bias. They do not test the page's mechanism (whether the winning move carries the target reasoning). For that the wiki has one randomized test of a game's mechanic with young children, one randomized test of adding worked examples to a puzzle game with adults, and a pooled comparison of enhanced against standard versions of the same games (g = 0.34). The default design below now rests on these where it can; the rest is the earlier page's guidance, labelled.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step says what supports it; most are untested as written.

1. **Name the capability, then make the winning move require it.** Write the one decision or action the learner must get better at, and check that the game's win condition cannot be reached without it (no guessing, button-mashing or reward route around it). Evidence: in [one randomized study](../claims/number-board-games-improve-numerical-knowledge.md) [+M] the same board game raised preschoolers' number knowledge when its squares were numbered 1–10 in a line, and not when they differed only in colour. One study, one domain; it does not show which features of other games matter.
2. **Show a novice the strategy before or between rounds.** Give one or two worked examples or a modelled round of play before the learner plays unaided, or between a first and second round. Evidence: adults who [studied worked examples between two rounds of a puzzle game](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [~M] improved more than those who did not, but [still learned a small fraction of what experts showed](../claims/worked-example-gains-in-a-puzzle-game-remain-small-relative-to-expert-knowledge-maps.md) [~M]. Across games, versions with added scaffolding (personalised hints, agents, adaptation to the learner) beat the standard version of the same game ([enhanced designs](../claims/value-added-augmented-designs-benefit-learning.md) [+M], g = 0.41 for scaffolding, 9 studies). How many examples is not reported on the claim pages. Fade the support in later levels as the learner succeeds unaided: carried from non-game instruction, where [fading support](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M] and [example–problem sequences](../claims/worked-example-problem-sequences.md) [+M] help novices and [guidance that helps novices can become redundant for the more expert](../claims/expertise-reversal-effect.md) [~M]; untested inside a game.
3. **Give an immediate, informative consequence for each move.** The game shows what the move did and, after an error, a hint toward the target reasoning rather than only a lost life. Keep the controls and screen free of demands the target does not need, since [reducing extraneous load](../claims/cognitive-load-reduction-improves-learning.md) [+M] helps in multimedia instruction (not tested in games). Otherwise untested; from the earlier page.
4. **Let learners fail safely and try again, and let them play individually by default.** Several attempts per level, with no penalty that ends play. Competition is optional: across digital-game studies, single-player play with no formal competition gave the largest effects (g = 0.45) and single-player competitive play none (g = −0.06) ([player configuration](../claims/single-noncompetitive-play-largest-effects.md) [~M]; after controls only the gap to single competitive play held, [same analysis](../claims/single-noncompetitive-play-largest-media-effects.md) [~M]). If scores are shared, see the team-score design in [Gamification](gamification.md).
5. **Spread play over several sessions and leave the game open between them.** In the digital-game meta-analysis, games played over more than one session beat non-game conditions (g = 0.44) and single-session games did not (g = 0.08), while total minutes of play were unrelated to the effect ([sessions](../claims/multiple-sessions-benefit-single-session-null.md) [+M]; [same analysis](../claims/multiple-sessions-moderator-games.md) [+M]). In workplace and university simulation games, unlimited access gave a larger advantage than limited access (d = .68 against .31; [unlimited access](../claims/unlimited-access-enhances-simulation-game-learning.md) [+M]). The tested child dose was four 15–20 minute sessions over two weeks, with an adult playing alongside ([board-game study](../claims/number-board-games-improve-numerical-knowledge.md) [+M]); the K–16 media comparisons averaged 11 sessions over 38 days, about 350 minutes in all. Proposed arc, untested as a whole: session 1 a modelled round and short unaided play; sessions 2–4 unaided play with hints and a worked example between rounds where play stalls; later sessions harder levels with hints faded, the game left open for voluntary replay; move on when the learner succeeds at the outside-game task in step 7, not when the levels are finished. Record the dose given.
6. **Put the game inside instruction, and debrief after play.** Teach the content around the game (before, between or after sessions) rather than letting the game replace it, and ask learners to state the rule or strategy that won, why it worked and where it would fail, then apply it to one task with no game around it. Evidence is mixed: in workplace and university simulation-game studies, games used as a supplement beat the comparison (d = .51) and standalone games lost to it (d = −.12) ([supplement, not standalone](../claims/simulation-games-as-supplement-not-standalone.md) [+M]), but in K–16 digital-game studies adding non-game instruction made no detectable difference (b = 0.04, [null moderator](../claims/variety-actions-and-supplemental-instruction-null.md) [~M]). The debrief's self-explanation prompts are carried from non-game instruction ([self-explanation](../claims/self-explanation-improves-conceptual-understanding.md) [+M]); untested in games.
7. **Judge the design outside the game**, on an aligned task at the horizon the objective sets, and record enjoyment separately. A game score or completion rate is not the outcome. See [the DragonBox report](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W]; and Tetris training, in a review of casual-game studies, produced gains mostly on tests resembling the game, not on general cognitive tasks ([Tetris](../claims/tetris-gains-test-resemblance-only.md) [~M]).

How far the neighbouring claims may be carried: the board-game study is low-income preschoolers learning number with an experimenter playing alongside; the puzzle-game studies are 72 university students in one session-length experiment. The session, competition and supplement findings are moderator analyses inside meta-analyses: they compare studies that differ in many ways at once, so they show which designs went with larger effects, not that changing one feature in a given game will produce the difference. The simulation-game findings come from workplace and university training, the digital-game findings from K–16.

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether the learner already has a strategy for the target task.** A learner with none tends to flail through trial and error; one with a usable strategy can use play as practice. If unstated, ask: have they solved a task like this before, unaided, outside a game?
- **Whether an adult or peer will play alongside.** The tested child gains came with an adult running the game, and the board-game claim's own Discussion names the facilitator as a possible critical ingredient. If unstated, ask: who is present while they play, and will that person talk about the content or only the rules?
- **What outcome must change, and where it will be measured.** A game can raise enjoyment while a plainer tool raises test scores. If unstated, ask: what will the learner be able to do afterwards, outside the game, and how will you check?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on the target task | Add one or two worked examples or a modelled round before unaided play and again between rounds; keep game controls minimal | [Worked examples between rounds, puzzle game](../claims/worked-examples-improve-problem-solving-strategy-transfer-in-a-puzzle-game.md) [~M]; tested with university students, untested with children |
| Learners are preschool or early-primary `child`ren | Use a simple game whose board or move *is* the representation (e.g. a numbered linear track); an adult plays alongside naming the numbers or quantities; four sessions of 15–20 min over two weeks | [Board-game study](../claims/number-board-games-improve-numerical-knowledge.md) [+M]; [guided play](../claims/play-based-learning-improves-outcomes.md) [~W] (guided play, not games specifically); in K–8 STEM games beat conventional teaching on average ([STEM meta-analysis](../claims/games-stem-moderate-positive-effects-cognition-motivation-behaviour.md) [+M], cognition g = .67) |
| Learners are `secondary`-school students | Expect a smaller gain than with primary pupils; keep the game to the one move that carries the target, pair it with taught content and a debrief (step 6), and check the outside-game task before committing more time | [School level](../claims/school-level-moderates-game-cognitive-effects.md) [~M] (K–8 STEM: secondary pupils gained less than primary, difference g = −0.67, 12 against 28 studies; why is not established) |
| Learners are `adult` or professionals in a `workplace-clinical` setting | Build the game around one job decision with real consequences in its rules; use it as one part of a training programme, not the whole of it; leave it open for repeated voluntary play; debrief against the real procedure; keep competition optional | [Supplement, not standalone](../claims/simulation-games-as-supplement-not-standalone.md) [+M] and [unlimited access](../claims/unlimited-access-enhances-simulation-game-learning.md) [+M] (simulation games in training, pooled); the whole-task argument behind building around one job decision is untested |
| The game would replace active non-game teaching of the same content (practice with feedback, discussion, problem solving) | Keep the active teaching; add the game alongside it only for a reason other than a learning gain (access, practice volume, interest), and check the outside-game task | [Active comparison](../claims/active-comparison-instruction-reverses-simulation-game-advantage.md) [~M] (simulation games: d = −.19 against active instruction, d = .38 against passive, d = .61 against none) |
| The goal is `verbal-association` (vocabulary, facts) | A quiz or practice game is a reasonable vehicle; add glosses or supplementary word material inside it, and test recall a week later, not only at the end of play | [Kahoot! and outdoor games with migrant children](../claims/game-based-practice-outperforms-traditional-l2-vocabulary-instruction.md) [+W] (confounded); [adventure game with supplementary material](../claims/adventure-games-supplementary-material-vocabulary.md) [+W] (second-hand); [long-term vocabulary retention](../claims/dgbl-long-term-vocabulary-retention.md) [+W] (a meta-analysis known only through a later review, no effect size) |
| The goal is a `concept`, `principle` or `complex-skill` | Make the core move the reasoning itself; add a debrief and one non-game transfer task; expect slower gains than for facts | untested; from the earlier page |
| The goal is `attitude-motivation` (interest, confidence) | Measure enjoyment and the capability separately; do not report one as the other; a game can win on the first and lose on the second; do not buy entertainment value expecting more learning | [DragonBox vs Lynnette](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W]; [entertainment value did not moderate learning](../claims/entertainment-value-does-not-moderate-simulation-game-learning.md) [~M]; games raised motivation over conventional K–8 STEM teaching on average (g = .51, [STEM meta-analysis](../claims/games-stem-moderate-positive-effects-cognition-motivation-behaviour.md) [+M]) |
| The brief wants competition, a leaderboard or head-to-head play | Make individual non-competitive play the default; if competition is wanted, use team scores built from each member's learning ([Gamification](gamification.md), step 5) rather than individual head-to-head play | [Player configuration](../claims/single-noncompetitive-play-largest-effects.md) [~M] (single competitive play g = −0.06 against non-game conditions); [after controls](../claims/single-noncompetitive-play-largest-media-effects.md) [~M] |
| `online-self-paced`, no teacher present | Put the modelling, hints and debrief questions inside the game (a worked example screen between levels, a "why did that work?" prompt after each level); log attempts per level to find where learners stall | untested proposal; the tested child gains had an adult present |
| Time is a `single-session` | Use one short game round, a worked example, a second round and a debrief; do not expect a gain over non-game teaching; if `days-weeks` are available, spread play over several sessions rather than lengthening one | [Sessions](../claims/multiple-sessions-benefit-single-session-null.md) [+M] (single-session games g = 0.08, not different from non-game conditions; total minutes unrelated to effect); the single-session plan itself is an untested proposal |
| Stakes are high or the game feeds a grade | Do not grade the in-game score unless its measurement has been designed for that ([Assessment Mechanic](../elements/assessment-mechanic.md)); assess on an aligned external task | untested; from the earlier page |
| Devices, motor demands, reading load or disability limit access | Choose a mechanic with no timing or precision demands beyond the target; offer a paper or board version; read text aloud or reduce it | untested; from the earlier page |

Nine of the thirteen rows rest on a claim. The novice, child, vocabulary and motivation rows rest on single studies in narrow populations or on second-hand reports; the secondary, workplace, active-comparison, competition and single-session rows rest on moderator analyses in three meta-analyses, which compare studies rather than versions of one game. The other four are untested proposals, most from the earlier page. Team scoring built from individual learning is set out in [Gamification](gamification.md) and is not tested in full games here.

## Observation, state and explanation

What can be observed is play under stated conditions: moves made, levels reached, attempts per level, time spent, what a learner says while playing, and performance on a task outside the game. "Understands the concept" and "is motivated" are inferred states. Winning a level is an observation about the game, not about the capability, unless the winning move is the capability. Record the game version, any help given, who was present, and the dose.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Wins levels, fails the same idea outside the game | The game can be won by a shortcut that bypasses the target reasoning; knowledge tied to the game's representation; the outside task is unfamiliar in format | Ask the learner to explain the winning move; give the outside task once in the game's representation and once without it. |
| Enjoys the game, little gain on the test | The mechanic does not demand the target reasoning; play displaced practice time; the test is misaligned with what the game trains | Compare the test items with the moves the game requires; record time on the target move against total play time. |
| Many failed attempts, no improvement across them | No strategy to learn from consequences (novice); feedback says only "wrong"; controls or reading load are the barrier | Show one worked example or modelled round and see whether the next attempts change; replay with simplified controls or text read aloud. In one biology game's logs, students who restarted and failed a cell cycle more often gained less from pre- to posttest (r ≈ −.30 and −.34, 39 students), while total attempts were unrelated ([Progenitor X logs](../claims/cell-cycle-starts-destroys-negative-correlation.md) [~W]): count repeated failures on the target move, not attempts in general. |
| Stops playing early | Too hard; competition discourages a low scorer; the learner does not value the task | Note where play stops; offer a non-competitive mode and an easier entry level, separately; ask what they wanted from it. Difficulty alone is a weak explanation: in Physics Playground, harder game mechanics went with slightly *more* persistence (3% per unit of difficulty; [difficulty and persistence](../claims/gm-difficulty-positively-predicts-persistence.md) [~W], associational). |
| Improves after the game and a debrief | Gain from play, from the debrief, from added time on the topic, or from the adult's talk | Keep all exposures recorded. Only a comparison holding time and talk constant can credit the game. |

These are proposals, untested with learners. A probe can shift confidence between explanations; it does not identify a cause, and probing itself teaches.

## Evidence and qualifications

Three meta-analyses in the wiki compare games with non-game conditions on average; the remaining claims test parts of the relationship.

- **Digital games, K–16** (Clark, Tanner-Smith & Killingsworth 2016; 57 studies, 209 effect sizes; `quant-synthesis`): [game conditions beat non-game conditions](../claims/digital-games-outperform-nongame-media-comparisons.md) [+M] (g = 0.33, 95% CI 0.19–0.48; cognitive g = 0.35, intrapersonal g = 0.35). Its moderator analyses: [multi-session games g = 0.44, single-session g = 0.08, total play time unrelated](../claims/multiple-sessions-benefit-single-session-null.md) [+M]; [single-player non-competitive play g = 0.45, single competitive play g = −0.06](../claims/single-noncompetitive-play-largest-effects.md) [~M]; [no detectable difference from adding non-game instruction, or from the variety of player actions](../claims/variety-actions-and-supplemental-instruction-null.md) [~M]; and, in value-added studies of the same game in two versions, [enhanced designs beat standard ones](../claims/value-added-augmented-designs-benefit-learning.md) [+M] (g = 0.34 over 20 studies; scaffolding g = 0.41 over 9). The value-added comparisons are the closest the syntheses come to this page's mechanism, because only the design differs. Games with a relevant story showed a smaller effect (g = 0.17) than games with no story or an irrelevant one ([story relevance](../claims/irrelevant-story-larger-effects-than-relevant.md) [~M]); between-study comparisons, so the reason is not established, and it does not change the default.
- **Games in K–8 STEM** ([Arztmann et al. 2023](https://doi.org/10.1080/03057267.2022.2057732); 43 studies; `quant-synthesis`): [games beat conventional teaching](../claims/games-stem-moderate-positive-effects-cognition-motivation-behaviour.md) [+M] on cognition (g = .67), motivation (g = .51) and behaviour (g = .93), but [effects vary enormously](../claims/games-stem-substantial-heterogeneity-prediction-intervals.md) [~M] (I² 76–92%; cognition prediction interval −0.38 to 1.76, so some settings will see a loss), [small studies show larger effects](../claims/publication-bias-small-study-effects-games-stem.md) [~M] (motivation 0.51 falls to 0.43 after adjustment), and [secondary pupils gained less than primary](../claims/school-level-moderates-game-cognitive-effects.md) [~M] (difference g = −0.67). The average is a property of these studies, not a forecast for a new game.
- **Simulation games in workplace and university training** ([Sitzmann 2011](https://doi.org/10.1111/j.1744-6570.2011.01190.x); about 60 samples; `quant-synthesis`): [supplementing other instruction d = .51, standalone d = −.12](../claims/simulation-games-as-supplement-not-standalone.md) [+M]; [against active instruction d = −.19, passive d = .38, none d = .61](../claims/active-comparison-instruction-reverses-simulation-game-advantage.md) [~M]; [games actively conveying the content d = .49](../claims/simulation-games-effective-when-instruction-active.md) [+M]; [unlimited access d = .68 against limited .31](../claims/unlimited-access-enhances-simulation-game-learning.md) [+M]; [high- and low-entertainment games equally effective](../claims/entertainment-value-does-not-moderate-simulation-game-learning.md) [~M] (d = .26 and .38); and [published studies d = .52 against unpublished d = −.10](../claims/publication-bias-in-simulation-games-research.md) [~M], which means the published average overstates what a typical game delivers. The active-comparison result limits the conditional relationship: the expected gain is over passive or no instruction.

- [Number Board Games Improve Numerical Knowledge](../claims/number-board-games-improve-numerical-knowledge.md) [+M]: 124 low-income preschoolers (mean age 4 years 9 months) were randomly assigned within centres to four 15–20 minute sessions over two weeks of a board game with an experimenter, on a linear board numbered 1–10 or an identical board varying only in colour (`randomized`). The numbered-board group improved on numeral identification, counting, magnitude comparison and number-line estimation at immediate posttest and at a 9-week follow-up (d = 0.65–1.08 across tasks at posttest); the colour group changed little. This is the closest test here of the relationship: same game, same play, only the content of the move differs. It does not show that a game beats non-game instruction, and the claim's Discussion notes the adult's naming of numbers may be a critical ingredient. One study; not yet checked against its source.
- Worked examples inside a puzzle game (one randomized experiment, 72 university students, the SafeCracker puzzle game): those who [studied worked examples between two rounds improved more on a knowledge map](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [~M] (2.21 against 0.62), and scored higher on a [problem-solving retention question](../claims/worked-examples-improve-problem-solving-strategy-retention-in-a-puzzle-game.md) [~M] and a [transfer question](../claims/worked-examples-improve-problem-solving-strategy-transfer-in-a-puzzle-game.md) [~M]; yet the worked-example group [learned only 2.7% of the experts' knowledge-map knowledge](../claims/worked-example-gains-in-a-puzzle-game-remain-small-relative-to-expert-knowledge-maps.md) [~M]. It qualifies learning through play alone: modelling added to the game helped, and play left most of the content unlearned. No test statistic or effect size is printed; the knowledge-map entry is checked by the judge on full text, the others not yet.
- [DragonBox users enjoyed the experience more, while Lynnette users performed better on the test](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W]: a review's report of a classroom experiment comparing an equation-solving game with an intelligent tutoring system. It limits the relationship: enjoyment and test performance went in opposite directions. Second-hand, no statistics printed, not yet checked.
- [Game-based vocabulary practice produced larger gains than traditional instruction for newly arrived migrant children](../claims/game-based-practice-outperforms-traditional-l2-vocabulary-instruction.md) [+W]: 48 Ukrainian children aged 6–7 in Italy for about a month, four weeks of game-based (Kahoot! and outdoor games) or traditional teaching, 40.29 to 171.91 words against 40.54 to 139.29. The claim page rates it weak deliberately: "game-based" confounds format, novelty, competition and being outdoors, so it motivates building a game but does not show a given game will work. The judge could not settle it on the abstract.
- [Game design, not learner age or linguistic background, determines DGBL effectiveness](../claims/game-design-moderates-dgbl-effectiveness.md) [~W]: a vocabulary-games review's report of another study that design, not age or language background, drove effectiveness, with adventure-oriented games more efficient than others. With [an adventure game plus supplementary vocabulary material beating a control](../claims/adventure-games-supplementary-material-vocabulary.md) [+W] from the same review, it suggests the game's design and what surrounds it matter more than "game" as a category. Both second-hand, no effect sizes, not yet checked.
- [Tetris cognitive gains mostly appear on tests resembling the game itself](../claims/tetris-gains-test-resemblance-only.md) [~M]: a critical review of casual-game studies reports that Tetris gains appear mostly on game-like tests, and that one training study found no gains on six cognitive tasks even with explicit instruction over four sessions. No effect size printed. It supports judging a game on a task outside it, and warns against expecting a game to train a general ability its move does not demand.
- [Moderate learner agency in game-based learning yields better outcomes than no agency or high agency](../claims/moderate-agency-better-learning-outcomes.md) [~W]: a 2026 position paper's report of one game-based learning study (Taub et al.); moderate agency beat both no and full agency on learning while keeping interest. Second-hand, no effect size; it fits offering bounded choice ([Autonomy](autonomy.md); [Gamification](gamification.md), step 6) but is too thin to set how much.
- [Gamification has small positive effects on cognitive, motivational and behavioral learning outcomes](../claims/gamification-has-small-positive-effects-on-learning-outcomes.md) [~M]: a meta-analysis of game elements added to non-game instruction (cognitive g = .49; only the cognitive effect held among the more rigorous designs). It is cited here to mark a boundary, not to support this page: it is about gamification, not learning through a full game, and its pooled effects should not be quoted for games.

Taken together: on average, games beat no or passive instruction by a small-to-moderate amount, more with several sessions, inside a course, without head-to-head competition and with primary rather than secondary pupils, and not at all against active non-game instruction; the averages are inflated by publication bias and hide wide variation (three meta-analyses). Within that, a game helps when its move carries the content (one randomized child study), added scaffolding improves a game (pooled value-added comparisons), novices learn more when shown worked examples and still learn little from play alone (one adult study), and enjoyment and entertainment value are not evidence of learning (a moderator analysis and a second-hand report). The vocabulary-game evidence is confounded or second-hand. Learners, domains and outcomes differ across these claims; do not rank them by effect label.

## The evidence by question

- *Does learning through a full game raise capability on a measure outside the game more than non-game instruction?* On average, yes, by a small-to-moderate amount against no or passive instruction: [digital games, K–16](../claims/digital-games-outperform-nongame-media-comparisons.md) [+M]; [K–8 STEM](../claims/games-stem-moderate-positive-effects-cognition-motivation-behaviour.md) [+M]; [a review citing these](../claims/serious-games-better-content-knowledge-than-traditional.md) [+W]. Not against active instruction ([active comparison](../claims/active-comparison-instruction-reverses-simulation-game-advantage.md) [~M]), and with wide variation and publication bias ([heterogeneity](../claims/games-stem-substantial-heterogeneity-prediction-intervals.md) [~M]; [published versus unpublished](../claims/publication-bias-in-simulation-games-research.md) [~M]; [small-study effects](../claims/publication-bias-small-study-effects-games-stem.md) [~M]).
- *Does what the game's moves ask of the learner decide whether it teaches?* [Number board, numbered versus coloured](../claims/number-board-games-improve-numerical-knowledge.md) [+M]; [Game design, not learner age or linguistic background, determines DGBL effectiveness; adventure games outperform non-adventure games](../claims/game-design-moderates-dgbl-effectiveness.md) [~W]; [enhanced versus standard versions of the same game](../claims/value-added-augmented-designs-benefit-learning.md) [+M].
- *Do modelling, tutoring or bridging instruction added around play raise what learners take from a game?* [Studying worked examples between two rounds of a computer puzzle game produced significantly greater knowledge map improvement than no worked examples for adult players](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [~M]; [supplement, not standalone](../claims/simulation-games-as-supplement-not-standalone.md) [+M], against [no difference from added non-game instruction](../claims/variety-actions-and-supplemental-instruction-null.md) [~M].
- *How many sessions, and how much play?* [Several sessions, not more minutes](../claims/multiple-sessions-benefit-single-session-null.md) [+M]; [unlimited access](../claims/unlimited-access-enhances-simulation-game-learning.md) [+M].
- *Should play be competitive?* [Single competitive play showed no benefit](../claims/single-noncompetitive-play-largest-effects.md) [~M].
- *For whom?* [Secondary pupils gained less than primary in STEM games](../claims/school-level-moderates-game-cognitive-effects.md) [~M]; the adult evidence is workplace and university simulation games.
- *Does a more entertaining game teach more?* [No](../claims/entertainment-value-does-not-moderate-simulation-game-learning.md) [~M]; [DragonBox against Lynnette](../claims/intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) [~W].
- *How much control should the learner have?* [Moderate agency](../claims/moderate-agency-better-learning-outcomes.md) [~W] (one study, second-hand).
- *Does a game's own log show learning?* Repeated failures on the target move went with smaller gains in one game ([Progenitor X](../claims/cell-cycle-starts-destroys-negative-correlation.md) [~W]); gains appear mostly on game-like tests ([Tetris](../claims/tetris-gains-test-resemblance-only.md) [~M]).

## Further evidence, not yet read against this model
<!-- Claims this page cited before the 2026-10-02 rewrite, plus claims the orphan-claim linker attached later in a "## Claims" section. Re-read 2026-10-19 (wave 2) from each claim's Evidence entries: of the 27 bullets, 21 moved into the model (default steps 2–7, the situation table, the observation table, Evidence and qualifications and the evidence by question), and the linker's Claims section was removed once every link in it appeared elsewhere on the page; the six below were read and do not change it. Markers capped by each claim's recorded evidence (strength_cap). -->
Claims read against this model that do not change it. Each says what it is and why it stays here.

- [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [+M] — read 2026-10-19: a narrative review and one memory experiment on correcting confidently held wrong answers to general-knowledge questions; no game, and no effect size. The earlier page used it for "fail safely and retry", which it does not test; step 4 stands as an untested proposal.
- [Desirable difficulties enhance learning.](../claims/desirable-difficulties-enhance-learning.md) [+M] — read 2026-10-19: three meta-analyses of retrieval practice, spacing and interleaving (g = 0.42–0.74); none concerns a game mechanic doing the learner's work. Its spacing and testing findings belong to [Spaced Learning](spaced-learning.md) and [Retrieval Practice](retrieval-practice.md).
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+W] — read 2026-10-19: a narrative review proposing a training-design approach, with no study recorded; it is the argument behind the workplace row's "one job decision", which remains untested.
- [Specific game features scaffold scientific thinking in ways the authors claim are non-existent in most inquiry-based learning environments](../claims/ar-game-features-scaffold-argumentation.md) [~W] — read 2026-10-19: the designers' argument about their place-based augmented-reality game (Mad City Mystery), not a tested comparison; consistent with step 2's scaffolding but adds no evidence.
- [Descriptive analyses suggest game-based learning may be less beneficial for cognitive outcomes in low-SES students than high-SES students, but this is preliminary](../claims/ses-descriptive-lower-cognitive-benefit-low-ses.md) [~W] — read 2026-10-19: in the K–8 STEM meta-analysis, two studies with high-SES samples reported larger effects than two with low-SES samples, but the moderator test over nine studies was not significant. Outcomes differing by group reflect circumstances and treatment, not a cause; too thin to change any row.
- [Simulation games were the most-used game type for educational assessment (N = 7, 33%), followed by immersive (N = 6, 29%) and video games (N = 5, 24%)](../claims/gba-game-types-simulation-most-used.md) [~W] — (not about this page) read 2026-10-19: a count of genres in 21 game-based assessment studies; no learning outcome. Relevant to [Assessment Mechanic](../elements/assessment-mechanic.md).
- [Playing modern board games in class produced greater pre-post improvement in working-memory updating than regular classes, in both first-grade and second-to-sixth-grade samples](../claims/board-games-improve-updating-primary.md) [+W] — attached 2026-10-22 from Nuria Vita-Barrull et al. (2024), which proposed "Include board-game play in primary classrooms as an alternative or complement to regular direct instruction for cognitive and academic development"; tests this page's relationship.
- [The board-game group showed greater pre-post improvement than controls in reading fluency, maths fluency and calculus in grades two to six](../claims/board-games-improve-reading-maths.md) [+W] — attached 2026-10-22 from Nuria Vita-Barrull et al. (2024), which proposed "Include board-game play in primary classrooms as an alternative or complement to regular direct instruction for cognitive and academic development"; tests this page's relationship.
- [Classroom board-game play improved inhibition in first grade but not in grades two to six, where inhibition and flexibility improved in both groups](../claims/board-games-inhibition-grade-dependent.md) [~W] — attached 2026-10-22 from Nuria Vita-Barrull et al. (2024), which proposed "Include board-game play in primary classrooms as an alternative or complement to regular direct instruction for cognitive and academic development"; tests this page's relationship.
- [Playing the empathy training game Crystals of Kaydor produced no greater improvement in adolescents' empathic accuracy than playing the commercial control game Bastion](../claims/crystals-no-group-difference-empathic-accuracy-change.md) [~W] — attached 2026-10-27 from Kral et al. (2018), which proposed "Design empathy training games so that engagement with empathy-specific mechanics, not generic playtime, drives the targeted learning processes"; tests this page's relationship.
- [CS students who learned CT concepts through the iThinkSmart VR game-based application demonstrated significantly better CT competency scores than students in the control group](../claims/ithinksmart-vr-better-ct-competency-scores.md) [+M] — attached 2026-10-29 from Friday Joseph Agbo et al. (2023), which proposed "Visualize abstract CT concepts through game-based approaches rather than theoretical instruction alone"; tests this page's relationship.
- [Progressive engagement through the PFO model shifted students' reasoning about the game system from micro-level to macro-level abstraction](../claims/pfo-progression-micro-to-macro.md) [+W] — attached 2026-10-29 from Marianthi Grizioti (2025), which proposed "PFO model of progressive engagement: Play, Focused Modifications, Open Modifications & Design".
- [Ke's (2016) systematic review synthesized five major themes as guideposts for designing research-based learning games](../claims/ke-2016-five-themes-learning-game-design.md) [+W] — attached 2026-10-29 from Andri Ioannou (2021), which proposed "Treat learning content as integral to gameplay, rules, and actions when designing learning games".
- [The GraphoGame effect on decoding was greatest when both students and teachers played the game](../claims/graphogame-teacher-plus-student-exposure-greatest.md) [+W] — attached 2026-10-29 from Jere-Folotiya et al. (2014), which proposed "Supplementary computer-assisted phonics games should expose both students and teachers to the game to maximize early literacy gains".

## Objective and learner-valued goal

The designer's objective names the capability the game is meant to build and how it will be checked outside the game. Elicit separately what the learner wants from playing: to win, to beat a friend, to finish quickly, to get better at something they care about. Agreement and divergence are both observations; do not infer motivation from time played.

For example, a secondary-school student playing a city-budget simulation game may value topping the class leaderboard, while the designer's objective is reasoning about trade-offs between spending choices. If the leaderboard rewards the fastest balanced budget, the student can pursue what they value by repeating one safe pattern and never reason about trade-offs. Recording both aims shows where to change the scoring (reward an explained trade-off) and keeps a high score from being read as the objective met.

## What would revise this model?

The model should weaken if games whose core move carries the content, with modelling and a debrief, fail to beat a non-game version with the same content, time and talk on an aligned outside measure; or if, like the colour-only board, games with content-free moves produce the same gains, which would point to the adult's talk or the time spent rather than the game. If modelling inside games keeps helping while play alone adds little, the model should be restated as practice with modelling, delivered in a game format. If enjoyment and later persistence turn out to predict learning well, revise the separation of the two outcomes. If within-game comparisons (the same game played in one session against several, or embedded against standalone) fail to reproduce the between-study moderators, drop steps 5 and 6's reliance on them. If games keep matching but not beating active non-game instruction, restate the page's case for a game as access, practice volume or interest rather than a learning gain. Do not protect the model by calling every failure a badly designed game.

A gain in the game, a gain on an aligned outside test, delayed retention, transfer to a new task and continued voluntary practice are separate claims. The wiki's evidence does not yet establish a dose beyond one preschool schedule and the meta-analyses' averages, which game genres help which goals, why secondary pupils gain less than primary, or whether games beat active non-game practice for anyone.

## Claims

- [Mastery-approach and performance-approach goal instructions do not interact on learning outcomes in game-based learning](../claims/goal-instructions-no-interaction-gbl.md) [~W]
- [Students learned chemistry content from the game-based learning session, with significant pretest-to-posttest gains](../claims/learning-occurred-cosmiclean-session.md) [+W]
- [Serious games are frequently successful in teaching, training, or assessing professional competencies, with reported success rates of 84% for cognitive skills, 83% for knowledge, and 100% for motor skills](../claims/serious-games-successful-professional-competencies.md) [+W]
- [Higher adult-observed cognitive engagement during GL play was related to larger gains in word reading and reading fluency](../claims/observed-cognitive-engagement-predicts-gains.md) [~W]
- [Nearly all reviewed serious games include game mechanics providing freedom of gameplay, most commonly choice options, interactive elements, and free exploration](../claims/freedom-of-gameplay-mechanics-common.md) [+W]
- [Total joining times in microgame-based learning overshot the number of students, reaching 448 times for 129 students](../claims/joining-times-overshoot-student-numbers.md) [~W]
- [No consistent learning effect of repeated TrackFX gameplay was found across children, though 37% showed positive performance slopes and improvement reached an asymptote after six sessions](../claims/no-consistent-trackfx-practice-effect.md) [-W]
- [Scaffolding in a handheld sensor-based vocabulary game significantly improved low-achieving EFL students' motivation and performance](../claims/scaffolding-sensor-vocabulary-game-improves-low-achievers.md) [~W]
- [The authors contend that a new design paradigm must be developed if academic learning is to take place in educational games](../claims/new-design-paradigm-needed-for-game-learning.md) [~W]
- [Motivation increased significantly from before activity to in activity in the game-based group but showed no significant stage-to-stage change in the traditional guide group](../claims/role-playing-guide-motivation-increase-during-activity.md) [+W]
- [Barach argues game-based learning needs more pedagogical rigor, scaffolding integration, and learner accountability through design](../claims/need-pedagogical-rigor-learning-games.md) [~W]
- [A digital board game for genuine communication improved EFL students' learning performance](../claims/digital-board-game-efl-performance.md) [+W]
- [A two-tier test-based migratory bird identification game outperformed conventional e-learning on motivation, achievement and technology acceptance](../claims/two-tier-test-game-beats-e-learning.md) [+W]
- [A computer-based simulation game helped students apply theoretical team-role knowledge to identify team roles in practice and evaluate their own performance in a role](../claims/simulation-game-team-role-self-reflection.md) [+W]
- [Worked-example effects in a 3D role-playing game for chemical formulas: significant on knowledge comprehension, marginal on knowledge application](../claims/worked-example-effect-3d-game-chemical-formulas.md) [~W]

## Related Principles
- [Simulations & Immersive Virtual Environments](simulations-immersive-virtual-environments.md) — simulations overlap with game-based learning when the experience models a system learners must navigate.
- [Immediate Feedback](immediate-feedback.md) — games depend on fast consequence signals to support adaptation and persistence.
- [Error Analysis](error-analysis.md) — game loops often create repeated opportunities to learn from mistakes.
- [Guided Practice](guided-practice.md) — many instructional games work best after some initial modeling or guided rehearsal.
- [Formative Assessment](formative-assessment.md) — the measurement counterpart, where the same bolt-on failure appears as a test wrapped around a game
- [Worked Examples](worked-examples.md)

## Examples

- [Learning Mechanic](../elements/learning-mechanic.md) — the unit a game's teaching is actually built from: the theory-grounded activity repeated throughout play, which a concrete game mechanic instantiates.
- [Assessment Mechanic](../elements/assessment-mechanic.md) — its measurement counterpart, designed so the game's own log yields interpretable evidence rather than only a score.
- **Scenario-based digital games**: Learners manage resources, make choices, and see consequences unfold across rounds or levels.
- **Board or card games for concept practice**: Structured turn-taking and rules create repetition with feedback while keeping attention high.
- **Quiz-show style review games**: Fast cycles of attempt and feedback can increase practice volume when questions still align to real objectives.
- **Collaborative mission games**: Teams solve a shared problem, requiring explanation, coordination, and iterative strategy updates.
- [Epistemic Games](../patterns/epistemic-games.md) — a pattern where the embedding is total: the repeated activity is the professional community's actual work, so there is no separable "learning part" to bolt on
- [Game-Based Mastery Learning](../patterns/game-based-mastery-learning.md) — a pattern where the tension is live, since the mechanics sustaining repetition are not the mechanics carrying the concept
- [Frame simulation lessons as a movie-director game with scaffolding, varied texts, and reflective discussion to sustain engagement](../strategies/movie-director-framing-scaffolding-engagement.md)

## Key Sources
- Eseryel, D., Law, V., Ifenthaler, D., Ge, X., & Miller, R. (2014). An investigation of the interrelationships between motivation, engagement, and complex problem solving in game-based learning. *Educational Technology & Society, 17*(1), 42-53.
- Boghian, I., Cojocariu, V. M., Popescu, C. V., & Mâţă, L. (2019). Game-based learning - Using board games in adult education. *Journal of Educational Sciences and Psychology, 9*(1).
- An, Y. (2020). Designing effective gamified learning experiences. *International Journal of Technology in Education, 3*(2), 62-69. [https://doi.org/10.46328/ijte.v3i2.27](https://doi.org/10.46328/ijte.v3i2.27)
- Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). *Learning mechanics and assessment mechanics for games for learning* (G4LI White Paper #01/2011, Version 0.1). Games for Learning Institute (New York University, CUNY Graduate Center, Teachers College Columbia University). [researchgate.net/publication/272815253](https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning)
- Isbister, K., Flanagan, M., & Hash, C. (2010). Designing games for learning: Insights from conversations with designers. *CHI '10 Extended Abstracts on Human Factors in Computing Systems*, 2041–2044. [doi:10.1145/1753326.1753637](https://doi.org/10.1145/1753326.1753637)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Schnotz, W., Böckler, J., & Grzondziel, H. (1999). Individual and co-operative learning with interactive animated pictures. *European Journal of Psychology of Education, 14*(2), 245–265. [doi:10.1007/bf03172968](https://doi.org/10.1007/bf03172968)
- Swink, S. (2008). *Game feel: A game designer's guide to virtual sensation*. Morgan Kaufmann. [doi:10.1201/9781482267334](https://doi.org/10.1201/9781482267334)
- Juul, J. (2003). The game, the player, the world: Looking for a heart of gameness. In M. Copier & J. Raessens (Eds.), *Level up: Digital Games Research Conference Proceedings* (pp. 30–45). Utrecht University. [doi:10.26503/dl.v2003i1.65](https://doi.org/10.26503/dl.v2003i1.65)
- Shen, C.-Y., & O’Neil, H. (2006). The Effectiveness of Worked Examples in a Game-Based Learning Environment. Paper presented at the annual meeting of the American Educational Research Association (AERA), San Francisco, CA. https://eric.ed.gov/?id=ED491961
- Clark, D. B., Tanner-Smith, E. E., & Killingsworth, S. S. (2016). Digital games, design, and learning: A systematic review and meta-analysis. *Review of Educational Research, 86*(1), 79–122. [https://doi.org/10.3102/0034654315582065](https://doi.org/10.3102/0034654315582065)
- Arztmann, M., Hornstra, L., Jeuring, J., & Kester, L. (2023). Effects of games in STEM education: A meta-analysis on the moderating role of student background characteristics. *Studies in Science Education, 59*(1), 109–145. [https://doi.org/10.1080/03057267.2022.2057732](https://doi.org/10.1080/03057267.2022.2057732)
- Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation games. *Personnel Psychology, 64*, 489–528. [doi:10.1111/j.1744-6570.2011.01190.x](https://doi.org/10.1111/j.1744-6570.2011.01190.x)

<!-- deprecated 2026-10-02: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Game-based learning is the instructional principle of using a game itself as the learning environment, with goals, rules, feedback, and progression aligned to specific learning outcomes. Unlike light gamification layered onto ordinary tasks, game-based learning makes the core learning activity intrinsically game-like: learners make decisions, test strategies, receive immediate consequences, and improve through repeated attempts. When designed well, it can increase time on task, support mastery through iteration, and make complex systems or decisions easier to experience directly.

## Implications
Game-based learning is strongest when the game mechanics require the same thinking the learning goal requires. Repeated attempts, immediate consequences, and visible progression can support mastery and persistence, especially when learners are allowed to fail safely and try again [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [+S]. But engagement alone is not evidence of learning: if the reward structure can be optimized without understanding the target concept or strategy, the game teaches the wrong thing. Reflection and debriefing are therefore essential for turning in-game success into transferable understanding [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M], and some goals are still better served by giving novices worked models before asking them to learn through play alone [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M]. Game-based learning is strongest when the game also approximates whole-task decision making closely enough to support later transfer [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M].

### Context
#### Requirements
- **Aligned learning goals**: The win conditions and mechanics need to reflect the target skill, not merely add entertainment.
- **Tight feedback loops**: Learners need immediate in-game consequences, hints, or progress signals so they can adjust strategy during play.
- **Repeatable challenge**: The design should support multiple attempts, safe failure, and a visible path toward improvement [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [+S].
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
- Some learning goals are better served by direct explanation or worked examples before game-based practice, especially for novices [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M].

### Claims

- [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [+S] — safe failure and rapid retry can make corrections inside games especially memorable
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+M] — debrief and reflection are what convert in-game experience into explicit understanding
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M] — novices often need modeled play or strategy examples before game-based practice becomes productive
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M] — games support transfer best when their decisions and constraints resemble the real target performance
-->

<!-- merged 2026-10-07 from principles/learning-embedded-in-the-core-mechanic ("Learning Embedded in the Core Mechanic"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Learning Embedded in the Core Mechanic

> **Principle** · [All principles](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 12 studies (5 quant-synthesis, 3 review, 2 causal, 2 theoretical), `q1`–`q4` · 4 of 12 report an effect size · 1 claim rests on one study

## Description
The most common way a learning game fails is structural rather than aesthetic: the learning and the play are two activities, and the play is the reward for surviving the learning. A racing game with a popup question before each lap, a shooter that pauses for a vocabulary item — in both, the essential repeated activity is still racing or shooting, and the learning is an interruption of it. Plass and colleagues put the prescription plainly, reporting the same conclusion from the designers Isbister, Flanagan and Hash (2010) interviewed: **learning needs to be embedded in the core mechanics of a game rather than added on to existing mechanics.** Game play cannot be used as a reward for answering questions about facts, and factual quizzes cannot be forced into unrelated game play.

The constructive form of this is the [Learning Mechanic](../elements/learning-mechanic.md): a theory-grounded design pattern naming the essential learning activity, which a concrete game mechanic then instantiates. The instantiation is a real design act with real freedom — "apply rules to solve problems" can be flung, dragged, or jetpacked — and it is where the learning goal is most often lost. Beyond the game feel a designer adds (the interactive, visual, emotional and sound elements that make a mechanic satisfying to engage; Swink, 2008), three requirements constrain which game mechanics may legitimately carry a given learning mechanic. Two of them pull in opposite directions, which is what makes this a principle rather than a checklist.

**1. The game mechanic must not introduce excessive extraneous cognitive load.** Making a learning mechanic playable *necessarily* adds processing demands unrelated to the content — narrative, resource management, incentive systems. Traditional cognitive load researchers would remove all of it (Kirschner, Sweller, & Clark, 2006), but the success of many games suggests the motivational benefit of those features can, under some conditions, outweigh the cost of the processing they demand. The requirement is therefore calibration, not elimination: not so much extraneous load that the advantage becomes a disadvantage. The source's example is *Dimenxian X*, which asks learners to retrieve data packets from an underwater cavern — a task only peripherally related to the learning goal, and one whose net effect the authors say can often only be settled empirically.

**2. The game mechanic must not reduce the required mental effort by too much.** The mirror-image error, and the less obvious one. A mechanic that hands the learner the result of the processing removes the germane load that the learning depends on. The source's example is an algebra game whose mechanic shows the learner that a term *b* on the right becomes *−b* on the left — eliminating both the decision about where to place it and the decision to change its sign. Unless a later level fades that scaffolding, the learner is less likely to solve a similar problem unaided or in a new context. Reducing germane load this way has been shown to hurt learning (Schnotz, Böckler, & Grzondziel, 1999).

**3. The game mechanic must not introduce unnecessary confounds.** Every instantiation risks requiring additional knowledge or skill the learner is not being taught: fine motor control, unrelated content knowledge, content-adjacent skills. *Angry Birds*' sling mechanic requires judging angle and force, so a learner who knows exactly which bird should hit which part of the structure still needs basic Newtonian intuition and the motor precision to execute the shot. Borrowed wholesale into a learning game, that mechanic makes success depend on two things the game is not teaching.

The same discipline applies on the measurement side, where the confounds are more damaging still because they corrupt the inference rather than the instruction — see [Assessment Mechanic](../elements/assessment-mechanic.md). One asymmetry is worth holding on to: **integrating several subject areas is a desirable feature of a learning mechanic and a defect in an assessment mechanic.** The same design move, opposite verdicts, depending on which job the mechanic is doing.

## Implications

### Context
#### Requirements
- **A learning mechanic to instantiate.** The principle presupposes that the essential learning activity has been named, grounded in learning theory, before any game mechanic is chosen — otherwise "embedded in the core mechanic" has nothing to embed.
- **Freedom to choose the game mechanic.** The one-to-many relationship is the point: several mechanics can instantiate one learning mechanic, and the requirements above are the filter. A project committed to a mechanic before naming the learning has already lost the choice.
- **Willingness to test empirically.** The source is explicit that whether an added game task enhances or suppresses learning can often only be decided through research, not from the design alone.
- **A fading plan.** Requirement 2 permits scaffolding inside a mechanic only if a later level removes it [Fading support promotes transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

#### Constraints
- **Requirements 1 and 2 are in tension by construction.** Strip everything extraneous and you approach a worksheet; add enough to make it a game and you are spending processing capacity. The principle does not resolve the tension — it names both walls and says stay between them.
- **The cognitive-load literature does not straightforwardly endorse this.** Kirschner, Sweller and Clark (2006) would remove extraneous load outright; the source's position is a deliberate qualification of that view, argued from the observed success of games rather than from load theory itself. Treat the qualification as a live empirical question, not a settled result.
- **Borrowed mechanics carry their own skill requirements.** A mechanic proven in a commercial game was optimised for enjoyment, not for isolating a construct; *Angry Birds* is the source's example and the general case.
- **Motivational benefit is conditional.** "Under some conditions" is the source's own hedge, and the conditions are not enumerated.

### Target Learners
- Learners for whom the target performance is a repeated decision that a mechanic can be built around
- Novices, for whom requirement 3 bites hardest — an unfamiliar control scheme is a confound for the learner who has least spare capacity [Reducing extraneous cognitive load improves learning outcomes.](../claims/cognitive-load-reduction-improves-learning.md) [+M]
- Learners with varying fine motor skill, device access, or prior gaming experience, all of which requirement 3 turns into measurable disadvantage

### Target Learning Objectives
- Conceptual understanding that survives outside the game, which requirement 2 exists to protect [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M]
- Rule and strategy application at the conceptual level rather than at the level of computing an answer
- Mental models of a system, built from acting inside its rules

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — supplies both requirement 1 (extraneous load) and requirement 2 (germane load), and the fact that the two requirements oppose each other is a direct consequence of the theory's own three-way split
- [Situated Learning](../theories/situated-learning.md) — the case for the learning activity being the game's real activity rather than an aside from it
- [Cognitive Apprenticeship](../theories/cognitive-apprenticeship.md) — named by the source among the theories a learning mechanic can be grounded in

#### Contradicting / Qualifying
- Strict cognitive load minimisation (Kirschner, Sweller, & Clark, 2006) would reject requirement 1's allowance for narrative, resource management and incentive systems altogether. The source's qualification is explicit and reasoned; it is not a finding.
- Engagement is not evidence of learning, and a mechanic that satisfies all three requirements can still teach the wrong thing if the learning mechanic it instantiates was poorly chosen. The requirements govern instantiation, not selection.

### Claims
- [Reducing extraneous cognitive load improves learning outcomes.](../claims/cognitive-load-reduction-improves-learning.md) [~M] — requirement 1 accepts some extraneous load for motivational return, so the claim constrains the principle rather than simply supporting it
- [Desirable difficulties enhance learning.](../claims/desirable-difficulties-enhance-learning.md) [+M] — requirement 2's insistence that the mechanic not do the learner's work for them
- [Fading support promotes transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M] — the escape clause on requirement 2: scaffolding inside a mechanic is acceptable if a later level removes it
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — why a mechanic that keeps the activity at the conceptual level beats one that collects the answer
- [Guidance that helps novices can become redundant as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — the scaffolding a mechanic bakes in is calibrated to one level of expertise and will be wrong for another

## Related Principles
- [Game-based Learning](game-based-learning.md) — the broader principle this one supplies the design discipline for
- [Immediate Feedback](immediate-feedback.md) — feedback mechanisms are how a mechanic guides behaviour and communicates what the designer wants
- [Formative Assessment](formative-assessment.md) — the measurement counterpart, where the same bolt-on failure appears as a test wrapped around a game
- [Guided Practice](guided-practice.md) — the source's requirement 2 is a statement about how much guidance a mechanic may embed before the practice stops working

## Examples
- [Learning Mechanic](../elements/learning-mechanic.md) — the construct this principle governs the instantiation of
- [Assessment Mechanic](../elements/assessment-mechanic.md) — the same principle applied to eliciting evidence, where the confounds are more costly
- [Epistemic Games](../patterns/epistemic-games.md) — a pattern where the embedding is total: the repeated activity is the professional community's actual work, so there is no separable "learning part" to bolt on
- [Game-Based Mastery Learning](../patterns/game-based-mastery-learning.md) — a pattern where the tension is live, since the mechanics sustaining repetition are not the mechanics carrying the concept

## Key Sources
- Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). *Learning mechanics and assessment mechanics for games for learning* (G4LI White Paper #01/2011, Version 0.1). Games for Learning Institute (New York University, CUNY Graduate Center, Teachers College Columbia University). [researchgate.net/publication/272815253](https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning)
- Isbister, K., Flanagan, M., & Hash, C. (2010). Designing games for learning: Insights from conversations with designers. *CHI '10 Extended Abstracts on Human Factors in Computing Systems*, 2041–2044. [doi:10.1145/1753326.1753637](https://doi.org/10.1145/1753326.1753637)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Schnotz, W., Böckler, J., & Grzondziel, H. (1999). Individual and co-operative learning with interactive animated pictures. *European Journal of Psychology of Education, 14*(2), 245–265. [doi:10.1007/bf03172968](https://doi.org/10.1007/bf03172968)
- Swink, S. (2008). *Game feel: A game designer's guide to virtual sensation*. Morgan Kaufmann.
- Juul, J. (2003). The game, the player, the world: Looking for a heart of gameness. In M. Copier & J. Raessens (Eds.), *Level up: Digital Games Research Conference Proceedings* (pp. 30–45). Utrecht University.

<!- - Citation provenance: the three DOIs above were resolved against Crossref on 2026-09-03
     and passed scripts/resolve_doi_conflicts.classify_doi as `verified`. The white paper's
     own reference list gives Kirschner, Sweller & Clark at Educational Psychologist 46(2);
     the registry says 41(2) and the registry value is used here. Swink and Juul carry no
     DOI and none was invented. - ->
-->

<!-- merged 2026-10-15 from principles/add-worked-examples-to-commercial-off-the-shelf-games-for-training ("Add instructional strategies such as worked examples to commercial off-the-shelf games used for training"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Add instructional strategies such as worked examples to commercial off-the-shelf games used for training

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors conclude that game play alone can be supplemented with instruction: providing worked examples "could enhance the training effectiveness with commercial off-the-shelf computer games." They present the study as providing design principles to promote learning from such games, while noting that the validity of this approach still needs evaluation in future studies.

## Design Implications

### Context
#### Requirements
- An effective instructional strategy, here worked examples, delivered alongside play of a commercial off-the-shelf game
#### Constraints
- The authors state the validity of this new system needs to be evaluated in future studies
- Tested with one puzzle game and adult students only

### Target Learners
- Adults: undergraduate or graduate students playing a computer puzzle game (SafeCracker)

### Target Learning Objectives
- Problem solving learned from commercial off-the-shelf computer games

### Claims

- [Worked Examples Improve Knowledge Map Content Understanding In A Puzzle Game](../claims/worked-examples-improve-knowledge-map-content-understanding-in-a-puzzle-game.md) [+M]
- [Worked Examples Improve Problem Solving Strategy Transfer In A Puzzle Game](../claims/worked-examples-improve-problem-solving-strategy-transfer-in-a-puzzle-game.md) [+M]
- [Adult players who studied worked examples scored significantly higher on a game-based problem-solving retention question than a control group](../claims/worked-examples-improve-problem-solving-strategy-retention-in-a-puzzle-game.md) [+W]
- [Worked-example gains in a puzzle game remained small relative to expert performance, with the worked example group learning only 2.7% of experts' knowledge-map knowledge](../claims/worked-example-gains-in-a-puzzle-game-remain-small-relative-to-expert-knowledge-maps.md) [~W]

## Related Principles
- [Game Based Learning](game-based-learning.md)
- [Worked Examples](worked-examples.md)

## Examples
-

## Key Sources
- Shen, C.-Y., & O’Neil, H. (2006). The Effectiveness of Worked Examples in a Game-Based Learning Environment. Paper presented at the annual meeting of the American Educational Research Association (AERA), San Francisco, CA. https://eric.ed.gov/?id=ED491961
-->

<!-- deprecated 2026-10-25: retracted (International Journal of Emerging Technologies in Learning, 2022-07-04); no longer cited.
- Liu, Z. Y., Shaikh, Z., & Gazizova, F. (2020). Using the concept of game-based learning in education. *International Journal of Emerging Technologies in Learning, 15*(14), 53-64. [https://doi.org/10.3991/ijet.v15i14.14675](https://doi.org/10.3991/ijet.v15i14.14675)
-->
