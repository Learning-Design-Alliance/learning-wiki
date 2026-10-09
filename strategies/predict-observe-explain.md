---
type: strategy
id: predict-observe-explain
aliases: [predicting-observing-explaining]
title: Predict Observe Explain
description: Learners commit to a prediction about a phenomenon, observe the actual outcome, and explain any discrepancy between prediction and observation.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Predict Observe Explain

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 9 studies (5 quant-synthesis, 3 causal, 1 associational), `q2`–`q4` · 4 of 9 report an effect size

## Description
Predict Observe Explain (POE) is a three-phase instructional strategy, originally developed by White and Gunstone (1992), in which learners first commit to a written prediction about the outcome of a demonstration or event, then observe the actual outcome, and finally explain what happened — especially any mismatch between their prediction and the observation. The commitment to a prediction before observation is what distinguishes POE from ordinary demonstration: it surfaces prior conceptions and creates a reason to resolve discrepancies.

## Design Implications

POE works because committing to a prediction activates prior knowledge and exposes it to testing, and because observed discrepancies between prediction and outcome create the cognitive conflict that motivates conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. The strategy also leverages the testing effect: making a prediction is a form of retrieval and generation that strengthens subsequent learning even when the prediction is wrong [Retrieval practice improves retention more than restudying.](../claims/retrieval-practice-improves-retention.md) [+S]. The explanation phase is where most learning accrues; without it, learners may dismiss or rationalize discrepant observations [Self-explanation prompts improve learning.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- A demonstration, simulation, or event with a genuinely uncertain or counterintuitive outcome — if the outcome is obvious, the prediction phase is busywork
- A mechanism for every learner to commit privately to a prediction (written, clicker, or digital poll) before observation, so public consensus does not suppress misconceptions
- Time and structure for the explanation phase, ideally with peer discussion before instructor resolution ([Class Discussion](../elements/class-discussion.md))
- Instructor knowledge of common misconceptions in the topic, so the chosen event targets them
- An event or demonstration with a genuinely uncertain or counterintuitive outcome — if the outcome is obvious, prediction adds nothing
- A mechanism for every learner to commit to a prediction (written, clicker, or app-based) before observation, so commitment is real rather than performative
- Time and structure for the explanation phase, ideally with peer discussion before instructor consolidation
- Instructor knowledge of common misconceptions in the topic, to design events that target them

#### Constraints
- Ineffective when learners lack the prior knowledge to generate a meaningful prediction — they guess randomly and learn little from the discrepancy [~M]
- Discrepant observations alone do not change conceptions; learners frequently reinterpret the observation to fit their existing belief unless the explanation phase is carefully facilitated [-M]
- If the instructor reveals the answer immediately after observation, the explain phase collapses into confirmation and the conceptual-change benefit is lost [-M]
- Poorly chosen events (ambiguous outcomes, noisy data) generate confusion rather than productive disequilibrium [-W]
- Ineffective when learners can predict correctly from surface cues without engaging the underlying concept — the event must discriminate between conceptions
- Learners with fragile prior knowledge may guess randomly, producing no productive conflict to resolve [~M]
- If the observation is ambiguous or the explanation phase is skipped, learners may rationalize the discrepancy away or leave more confused than before [-M]
- Poorly designed events can entrench misconceptions if the "surprise" is attributed to experimental error rather than conceptual error [~M]

#### Implementation Variability
- **POE with peer discussion**: after private prediction, learners discuss predictions in pairs before observation (a [Peer Instruction](../patterns/peer-instruction.md)-style variant)
- **Simulation-based POE**: virtual labs and simulations (e.g., PhET) allow repeated observation and manipulation after the initial prediction
- **POE as assessment**: White and Gunstone designed POE partly as a *probing* tool — teachers use written predictions and explanations as formative evidence of students' conceptions ([Assessment](../elements/assessment.md))
- **Delayed observation**: in lecture settings, the observation can be deferred to a later session to add a spacing benefit
- **POE with simulation**: virtual labs such as PhET allow repeated observation and manipulation after the initial prediction
- **FADE variant**: prediction only, with explanation folded into follow-up problem solving, for time-constrained settings
- **Written POE**: full individual written sequence used as a formative assessment artifact

### Target Learners
- Learners who hold intuitive but incorrect conceptions of a phenomenon — the strategy is explicitly designed to surface and confront these [~M]
- Intermediate learners with enough background to make a reasoned (not random) prediction; complete novices benefit less [~M]
- Less effective for learners with strong correct prior knowledge, for whom prediction adds little beyond routine application
- Learners holding intuitive but incorrect conceptions (misconceptions) that conflict with the scientific account [+M]
- Intermediate learners with enough prior knowledge to generate a meaningful prediction; complete novices benefit less because they cannot commit to a reasoned guess [~M]
- Less effective for advanced learners whose predictions are already accurate — the conflict mechanism has nothing to act on

### Target Learning Goals
- Conceptual change: replacing intuitive misconceptions with scientific conceptions
- Causal reasoning: linking observations to underlying mechanisms
- Metacognition: monitoring one's own understanding by comparing expectation against evidence
- Scientific epistemic practice: experiencing hypothesis-testing as a way of knowing
- Conceptual change: replacing intuitive models with scientific ones
- Epistemic practice: treating evidence as arbiter between competing claims
- Formative assessment: the prediction and explanation phases surface thinking the instructor can respond to [Assessment for learning improves achievement by surfacing and responding to learner thinking.](../claims/assessment-for-learning-improves-achievement.md) [+S]

### Instructions
1. **Predict**: Present the setup of a demonstration or event (without the outcome). Each learner privately commits to a prediction and a reason, in writing or via poll. Do not collect correctness at this stage.
2. **Observe**: Run the demonstration, simulation, or data reveal. Keep it short and unambiguous.
3. **Explain**: Ask learners to write whether their prediction matched and why. Use [Peer Instruction](../patterns/peer-instruction.md)-style pair discussion, then whole-class [Class Discussion](../elements/class-discussion.md), before the instructor resolves the science.
4. **Consolidate**: Name the target conception explicitly, connect it to the discrepant event, and follow with application ([Application of Knowledge](../elements/application-of-knowledge.md)) or a second POE on a related phenomenon.

## Related Strategies
- [Peer Instruction](peer-instruction.md) — shares the commit-then-discuss-then-resolve structure, applied to conceptual questions rather than physical events
- [Case-Based Learning](case-based-learning.md) — similarly anchors learning in a concrete, discrepant scenario
- [Think-Pair-Share](../patterns/think-pair-share.md) — the discussion structure most often layered onto the predict and explain phases
- [Comparing Cases](comparing-contrasting-cases.md) — alternative route to discriminating conceptions through structured contrast [Comparing and contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
- [Concept Probing](concept-probing.md) — diagnostic questioning without the observation component

## Examples
- **Physics lecture (Mazur's Peer Instruction lineage)**: Students predict whether a heavy and a light ball dropped together land simultaneously, vote with clickers, discuss, then observe the drop — the same predict-commit-discuss cycle Crouch and Mazur documented at Harvard.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** (University of Colorado Boulder) — teachers run POE cycles around simulations such as circuit construction: predict bulb brightness, then test in the sim.
- **Chemistry misconceptions**: The classic "mass of dissolved salt" POE — students predict whether dissolving salt increases the mass of water, observe a balance reading, and confront the conservation-of-mass misconception.
- **Physics: forces on a coin on a rotating turntable** — learners predict the coin's path when released, observe it, and confront the centrifugal-force misconception.
- **Chemistry: mass change in a closed vs. open system during a reaction** — predictions typically split; the observation forces engagement with conservation of mass.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — simulations such as *Circuit Construction Kit* support POE sequences: predict bulb brightness, run the circuit, explain the result.
- **[CLUE (Chemistry, Life, the Universe and Everything)](https://iws.collaborativelearning.org/clue.html)** — a redesigned general chemistry curriculum built around predict-observe-explain cycles.

## Key Sources
- White, R., & Gunstone, R. (1992). *Probing understanding*. Falmer Press.
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science, 13*(2), 145–182. [doi:10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1)
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970–977. [doi:10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Gunstone, R. F. (1994). The importance of specific science content in the enhancement of metacognition. In P. J. Fensham, R. F. Gunstone, & R. T. White (Eds.), *The content of science: A constructivist approach to its teaching and learning* (pp. 131–146). Falmer Press.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- White, R., & Gunstone, R. (1992). Probing understanding. *London: Falmer Press.*
- Gunstone, R. F., & White, R. T. (1981). Understanding of gravity. *Science Education, 65*(3), 291–299. [doi:10.1002/sce.3730650308](https://doi.org/10.1002/sce.3730650308)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Vosniadou, S. (2013). Conceptual change in learning and instruction. In *International Handbook of Research on Conceptual Change*. Routledge. [doi:10.4324/9780203154472.ch1](https://doi.org/10.4324/9780203154472.ch1)

<!-- merged 2026-10-09 from strategies/predicting-observing-explaining ("Predicting Observing Explaining"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Predicting Observing Explaining

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 11 studies (7 quant-synthesis, 3 causal, 1 review), `q2`–`q4` · 6 of 11 report an effect size

## Description
Predict-Observe-Explain (POE) is a three-phase strategy, typically used in science education. Learners first commit to a written prediction about the outcome of an event or demonstration, then observe the event (live, via video, or through simulation), and finally explain the outcome — especially any mismatch between their prediction and the observation. The strategy was developed by White and Gunstone (1992) as a probe of, and remedy for, learners' prior conceptions.

## Design Implications

POE works because the prediction phase activates prior conceptions and exposes them to challenge: when observation contradicts a committed prediction, learners experience cognitive conflict that motivates conceptual change [Conceptual change is driven by cognitive disequilibrium between expectations and evidence.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. The strategy is a form of active learning that outperforms passive demonstration viewing, since learners must reason before and after the event rather than merely watch [Active learning improves exam performance relative to lecture-only instruction.](../claims/active-learning-improves-exam-performance.md) [+S]. The explain phase is where durable learning happens; omitting it reduces POE to a demonstration with a guess attached.

### Context
#### Requirements
- An event or demonstration with a genuinely uncertain or counterintuitive outcome — if the outcome is obvious, prediction adds nothing
- A mechanism for every learner to commit to a prediction (written, clicker, or app-based) before observation, so commitment is real rather than performative
- Time and structure for the explanation phase, ideally with peer discussion before instructor consolidation
- Instructor knowledge of common misconceptions in the topic, to design events that target them

#### Constraints
- Ineffective when learners can predict correctly from surface cues without engaging the underlying concept — the event must discriminate between conceptions
- Learners with fragile prior knowledge may guess randomly, producing no productive conflict to resolve [~M]
- If the observation is ambiguous or the explanation phase is skipped, learners may rationalize the discrepancy away or leave more confused than before [-M]
- Poorly designed events can entrench misconceptions if the "surprise" is attributed to experimental error rather than conceptual error [~M]

#### Implementation Variability
- **POE with peer discussion**: predictions and explanations debated in pairs before whole-class consolidation (a [Peer Instruction](../patterns/peer-instruction.md)-style adaptation)
- **POE with simulation**: virtual labs such as PhET allow repeated observation and manipulation after the initial prediction
- **FADE variant**: prediction only, with explanation folded into follow-up problem solving, for time-constrained settings
- **Written POE**: full individual written sequence used as a formative assessment artifact

### Target Learners
- Learners holding intuitive but incorrect conceptions (misconceptions) that conflict with the scientific account [+M]
- Intermediate learners with enough prior knowledge to generate a meaningful prediction; complete novices benefit less because they cannot commit to a reasoned guess [~M]
- Less effective for advanced learners whose predictions are already accurate — the conflict mechanism has nothing to act on

### Target Learning Goals
- Conceptual change: replacing intuitive models with scientific ones
- Epistemic practice: treating evidence as arbiter between competing claims
- Formative assessment: the prediction and explanation phases surface thinking the instructor can respond to [Assessment for learning improves achievement by surfacing and responding to learner thinking.](../claims/assessment-for-learning-improves-achievement.md) [+S]

### Instructions
1. **Design the event**: choose a demonstration, video, or simulation whose outcome hinges on the target concept and contradicts a known common misconception.
2. **Predict**: pose the question, give individual think time, and require a committed, visible prediction from every learner (written or clicker). Do not reveal results yet.
3. **Observe**: run the event exactly as described — deviations undermine trust in the evidence.
4. **Explain**: ask learners to reconcile prediction and observation in writing, then discuss with peers before instructor consolidation of the correct conception.
5. **Consolidate**: name the misconception, restate the scientific account, and follow with application tasks ([Practice](../elements/practice.md)) to stabilize the new conception.

## Related Strategies
- [Peer Instruction](peer-instruction.md) — shares the commit-then-confront structure; POE adds the observation phase
- [Comparing Cases](comparing-contrasting-cases.md) — alternative route to discriminating conceptions through structured contrast [Comparing and contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
- [Concept Probing](concept-probing.md) — diagnostic questioning without the observation component

## Examples
- **Physics: forces on a coin on a rotating turntable** — learners predict the coin's path when released, observe it, and confront the centrifugal-force misconception.
- **Chemistry: mass change in a closed vs. open system during a reaction** — predictions typically split; the observation forces engagement with conservation of mass.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — simulations such as *Circuit Construction Kit* support POE sequences: predict bulb brightness, run the circuit, explain the result.
- **[CLUE (Chemistry, Life, the Universe and Everything)](https://iws.collaborativelearning.org/clue.html)** — a redesigned general chemistry curriculum built around predict-observe-explain cycles.

## Key Sources
- White, R., & Gunstone, R. (1992). Probing understanding. *London: Falmer Press.*
- Gunstone, R. F., & White, R. T. (1981). Understanding of gravity. *Science Education, 65*(3), 291–299. [doi:10.1002/sce.3730650308](https://doi.org/10.1002/sce.3730650308)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Vosniadou, S. (2013). Conceptual change in learning and instruction. In *International Handbook of Research on Conceptual Change*. Routledge. [doi:10.4324/9780203154472.ch1](https://doi.org/10.4324/9780203154472.ch1)
-->
