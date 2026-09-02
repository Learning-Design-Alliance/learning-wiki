---
type: strategy
id: predict-observe-explain
title: Predict Observe Explain
description: Learners commit to a prediction about a phenomenon, observe the actual outcome, and explain any discrepancy between prediction and observation.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Predict Observe Explain

> **Strategy** · [All strategies](index.md)

## Description
Predict Observe Explain (POE) is a three-phase instructional strategy, originally developed by White and Gunstone (1992), in which learners first commit to a written prediction about the outcome of a demonstration or event, then observe the actual outcome, and finally explain what happened — especially any mismatch between their prediction and the observation. The commitment to a prediction before observation is what distinguishes POE from ordinary demonstration: it surfaces prior conceptions and creates a reason to resolve discrepancies.

## Design Implications

POE works because committing to a prediction activates prior knowledge and exposes it to testing, and because observed discrepancies between prediction and outcome create the cognitive conflict that motivates conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. The strategy also leverages the testing effect: making a prediction is a form of retrieval and generation that strengthens subsequent learning even when the prediction is wrong [Retrieval practice improves retention more than restudying.](../claims/retrieval-practice-improves-retention.md) [+S]. The explanation phase is where most learning accrues; without it, learners may dismiss or rationalize discrepant observations [Self-explanation prompts improve learning.](../claims/self-explanation-improves-learning.md) [+S].

### Context
#### Requirements
- A demonstration, simulation, or event with a genuinely uncertain or counterintuitive outcome — if the outcome is obvious, the prediction phase is busywork
- A mechanism for every learner to commit privately to a prediction (written, clicker, or digital poll) before observation, so public consensus does not suppress misconceptions
- Time and structure for the explanation phase, ideally with peer discussion before instructor resolution ([Class Discussion](../elements/class-discussion.md))
- Instructor knowledge of common misconceptions in the topic, so the chosen event targets them

#### Constraints
- Ineffective when learners lack the prior knowledge to generate a meaningful prediction — they guess randomly and learn little from the discrepancy [~M]
- Discrepant observations alone do not change conceptions; learners frequently reinterpret the observation to fit their existing belief unless the explanation phase is carefully facilitated [-M]
- If the instructor reveals the answer immediately after observation, the explain phase collapses into confirmation and the conceptual-change benefit is lost [-M]
- Poorly chosen events (ambiguous outcomes, noisy data) generate confusion rather than productive disequilibrium [-W]

#### Implementation Variability
- **POE with peer discussion**: after private prediction, learners discuss predictions in pairs before observation (a [Peer Instruction](../patterns/peer-instruction.md)-style variant)
- **Simulation-based POE**: virtual labs and simulations (e.g., PhET) allow repeated observation and manipulation after the initial prediction
- **POE as assessment**: White and Gunstone designed POE partly as a *probing* tool — teachers use written predictions and explanations as formative evidence of students' conceptions ([Assessment](../elements/assessment.md))
- **Delayed observation**: in lecture settings, the observation can be deferred to a later session to add a spacing benefit

### Target Learners
- Learners who hold intuitive but incorrect conceptions of a phenomenon — the strategy is explicitly designed to surface and confront these [~M]
- Intermediate learners with enough background to make a reasoned (not random) prediction; complete novices benefit less [~M]
- Less effective for learners with strong correct prior knowledge, for whom prediction adds little beyond routine application

### Target Learning Goals
- Conceptual change: replacing intuitive misconceptions with scientific conceptions
- Causal reasoning: linking observations to underlying mechanisms
- Metacognition: monitoring one's own understanding by comparing expectation against evidence
- Scientific epistemic practice: experiencing hypothesis-testing as a way of knowing

### Instructions
1. **Predict**: Present the setup of a demonstration or event (without the outcome). Each learner privately commits to a prediction and a reason, in writing or via poll. Do not collect correctness at this stage.
2. **Observe**: Run the demonstration, simulation, or data reveal. Keep it short and unambiguous.
3. **Explain**: Ask learners to write whether their prediction matched and why. Use [Peer Instruction](../patterns/peer-instruction.md)-style pair discussion, then whole-class [Class Discussion](../elements/class-discussion.md), before the instructor resolves the science.
4. **Consolidate**: Name the target conception explicitly, connect it to the discrepant event, and follow with application ([Application of Knowledge](../elements/application-of-knowledge.md)) or a second POE on a related phenomenon.

## Related Strategies
- [Peer Instruction](peer-instruction.md) — shares the commit-then-discuss-then-resolve structure, applied to conceptual questions rather than physical events
- [Case-Based Learning](case-based-learning.md) — similarly anchors learning in a concrete, discrepant scenario
- [Think-Pair-Share](../patterns/think-pair-share.md) — the discussion structure most often layered onto the predict and explain phases

## Examples
- **Physics lecture (Mazur's Peer Instruction lineage)**: Students predict whether a heavy and a light ball dropped together land simultaneously, vote with clickers, discuss, then observe the drop — the same predict-commit-discuss cycle Crouch and Mazur documented at Harvard.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** (University of Colorado Boulder) — teachers run POE cycles around simulations such as circuit construction: predict bulb brightness, then test in the sim.
- **Chemistry misconceptions**: The classic "mass of dissolved salt" POE — students predict whether dissolving salt increases the mass of water, observe a balance reading, and confront the conservation-of-mass misconception.

## Key Sources
- White, R., & Gunstone, R. (1992). *Probing understanding*. Falmer Press.
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanation: How students study and use examples in learning to solve problems. *Cognitive Science, 13*(2), 145–182. [doi:10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1)
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970–977. [doi:10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Gunstone, R. F. (1994). The importance of specific science content in the enhancement of metacognition. In P. J. Fensham, R. F. Gunstone, & R. T. White (Eds.), *The content of science: A constructivist approach to its teaching and learning* (pp. 131–146). Falmer Press.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)