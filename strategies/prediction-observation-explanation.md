---
type: strategy
title: Prediction Observation Explanation
description: Learners commit to a prediction about an event, observe the actual outcome, then reconcile any discrepancy between the two.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Prediction Observation Explanation

## Description
Prediction Observation Explanation (POE) is a three-phase strategy, originally developed by White and Gunstone for science education. Learners first commit to an explicit prediction about the outcome of a demonstration or event, then observe the actual outcome, and finally write an explanation that reconciles prediction and observation — especially when the two diverge. The commitment step is essential: a public or recorded prediction creates the cognitive stakes that make the observation meaningful.

## Design Implications

POE works because committing to a prediction activates prior knowledge — including misconceptions — and makes it available for revision [Activating prior knowledge improves learning.](../claims/activation-improves-learning.md) [+M]. When observation contradicts prediction, the resulting cognitive conflict motivates conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. The strategy is a structured form of [Active Learning](../principles/active-learning.md): every learner must commit before the reveal, preventing passive observation of a demonstration.

### Context
#### Requirements
- An event, demonstration, or dataset with a genuinely uncertain or non-obvious outcome — if the outcome is trivially predictable, the prediction phase is busywork
- A mechanism for every learner to commit individually (written, clicker, or app-based) before any group discussion or reveal
- Time and structure for the explanation phase; the reconciliation writing is where learning consolidates, and truncating it reduces the strategy to a demonstration
- Instructor preparation for common misconceptions, so the explanation phase can target them directly

#### Constraints
- Ineffective when learners can predict correctly without understanding — surface cues let them succeed for the wrong reasons, and no conceptual change occurs [~M]
- If the observation is ambiguous or the demonstration fails, the discrepancy learners resolve is an artifact, not the target concept
- Learners with very low prior knowledge may guess randomly, generating no meaningful prediction to revise; a brief advance organizer or prior [Activation](../principles/activation.md) activity is needed first
- Overuse with the same format breeds ritual compliance — learners predict to match what they think the instructor wants rather than their actual belief [-W]

#### Implementation Variability
- **Peer Instruction variant**: after individual commitment, learners discuss predictions with peers before the reveal, then re-vote — peer discussion substantially improves conceptual gains [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [+S]
- **POE with data**: replace live demonstration with datasets or simulations (e.g., PhET interactive simulations) where learners predict graph or output behavior
- **Delayed observation**: in flipped settings, learners predict as pre-class homework and observe during class, freeing class time for the explanation phase

### Target Learners
- Learners holding common misconceptions in domains like physics, chemistry, and statistics — the discrepancy is the mechanism that surfaces and confronts them [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]
- Undergraduate lecture audiences at scale, where clicker-based commitment is feasible [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [+S]
- Less suitable for complete novices with no basis for prediction; a minimal knowledge foundation is required for the prediction to be meaningful

### Target Learning Goals
- Conceptual change: replacing intuitive but incorrect models with scientific ones
- Causal reasoning: articulating *why* an outcome occurs, not just what occurs
- Metacognitive monitoring: recognizing the gap between what one believes and what is true

### Instructions
1. Present the setup of the event or demonstration without the outcome, and have each learner commit to a written or clicker prediction with a brief rationale.
2. Show or run the observation — live, via simulation, or with data.
3. Have learners write an explanation reconciling prediction and observation, individually first, then optionally in [Class Discussion](../elements/class-discussion.md).
4. Close with instructor consolidation that names the target concept and explicitly addresses the misconception the discrepancy was designed to expose.

## Related Strategies
- **Peer Instruction** — the clicker-based discussion variant of POE developed by Crouch and Mazur; adds peer debate between prediction and reveal
- **Predict-Observe-Explain labs** — the same structure applied to full laboratory investigations rather than single demonstrations
- **Activating Prior Knowledge** ([Activating Prior Knowledge](../strategies/activating-prior-knowledge.md)) — POE's prediction phase is a forced, commitment-based form of activation

## Examples
- **Peer Instruction at Harvard** ([Crouch & Mazur, 2001](https://doi.org/10.1119/1.2345553)) — ConcepTests in introductory physics follow the POE cycle: individual clicker vote, peer discussion, re-vote, instructor explanation.
- **PhET Interactive Simulations** ([https://phet.colorado.edu](https://phet.colorado.edu)) — Learners predict circuit or gas-law behavior, then manipulate the simulation to observe the outcome and explain discrepancies.
- **Chemistry "misconception demos"** — Classic POE tasks such as predicting the mass of dissolved salt or the water level when a candle burns under a jar, each targeting a documented intuitive misconception.

## Key Sources
- White, R., & Gunstone, R. (1992). Probing understanding. *London: Falmer Press.* (Chapter on Prediction–Observation–Explanation)
- Crouch, C. H., & Mazur, E. (2001). Peer Instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970–977. [doi:10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Vosniadou, S. (2013). Conceptual change in learning and instruction: From framework frameworks to productive conceptual change. *International Journal of Educational Research, 61*, 1–4. [doi:10.4324/9780203154472.ch1](https://doi.org/10.4324/9780203154472.ch1)