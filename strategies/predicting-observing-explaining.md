---
type: strategy
title: Predicting Observing Explaining
description: Learners commit to a prediction about an event, observe the actual outcome, and explain any discrepancy between the two.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Predicting Observing Explaining

> **Strategy** · [All strategies](index.md)

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
- Vosniadou, S. (2013). Conceptual change in learning and instruction: From framework frameworks to productive conceptual change thinking. *Advances in Learning Environments Research.* [doi:10.4324/9780203154472.ch1](https://doi.org/10.4324/9780203154472.ch1)