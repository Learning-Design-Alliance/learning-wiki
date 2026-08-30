---
type: element
title: Prediction
description: A prediction asks learners to commit to an answer or outcome before instruction, activating prior knowledge and creating a gap that subsequent teaching resolves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Prediction

## Description
A prediction asks learners to commit to an answer, outcome, or explanation *before* receiving instruction — guessing the result of an experiment, the next step in a demonstration, or the answer to a question about material not yet taught. The act of committing, even incorrectly, prepares learners to encode the corrective information that follows.

## Design Implications

Predictions leverage the pretesting effect: attempting to answer before instruction improves retention of the correct answer relative to studying without a prior attempt, even when the initial guess is wrong [Unsuccessful retrieval attempts enhance subsequent learning.](../claims/high-confidence-errors-improve-retention.md) [+S]. Predictions work by activating relevant prior knowledge and creating a state of curiosity or disequilibrium that makes the eventual answer more memorable [Activation improves learning outcomes.](../claims/activation-improves-learning.md) [+M]. They are most effective when followed promptly by feedback or instruction that resolves the uncertainty — a prediction left unresolved yields little benefit [Prequestions improve learning from video when followed by relevant instruction.](../claims/activation-improves-learning.md) [+M].

### Context
#### Requirements
- A question or scenario that is answerable with the upcoming instruction — the prediction must target content the lesson will actually address
- A genuine commitment from learners (written, clicked, or stated publicly), not a rhetorical question
- Timely resolution: instruction or feedback that confirms or corrects the prediction soon after it is made
- Low stakes — learners must feel safe guessing wrong, since errors are the mechanism, not a failure ([Assessment](assessment.md) for learning, not of it)

#### Constraints
- Predictions about content unrelated to subsequent instruction can divert attention and *impair* learning of the material actually presented [Prequestions can impair learning of material not targeted by the question.](../claims/activation-improves-learning.md) [-S] — the "prequestioning penalty" for incidental content
- If learners lack any relevant prior knowledge, guesses are random and the activation benefit shrinks [~M]
- High-stakes grading of predictions suppresses the willingness to commit, eliminating the effect
- Overly difficult predictions that produce frustration rather than curiosity can disengage learners [~W]

### Target Learners
- Novices with some, but incomplete, prior knowledge — enough to generate a plausible guess [Unsuccessful retrieval attempts enhance subsequent learning.](../claims/high-confidence-errors-improve-retention.md) [+S]
- Learners prone to illusions of knowing; a failed prediction exposes gaps that passive reading conceals
- Less effective for complete novices with no relevant schema to activate, or for advanced learners who already know the answer and gain no new uncertainty

### Target Learning Goals
- Conceptual understanding: surfacing and revising intuitive misconceptions before formal explanation
- Procedural learning: predicting the next step in a [Demonstration](demonstration.md) keeps learners actively processing rather than passively watching
- Scientific reasoning: hypothesis generation and evidence-based revision of expectations

### Affordances
- [Activation](../principles/activation.md) — prediction enacts this principle by forcing retrieval of relevant prior knowledge before new material arrives, preparing schemas to incorporate it
- [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md) — a committed-but-wrong prediction creates a knowledge gap that motivates and focuses the resolution that follows
- [Active Learning](../principles/active-learning.md) — prediction converts passive reception (watching, reading) into a generative act, even within a lecture or video format
- [Assessment for Learning](../principles/assessment-for-learning.md) — aggregated predictions give instructors a real-time map of misconceptions to address in the lesson

## Related Elements
- [Activation](activation.md) — prediction is a specific, commitment-forcing form of prior-knowledge activation
- [Demonstration](demonstration.md) — pausing a demonstration to ask "what happens next?" interleaves prediction with modeling
- [Advance Organizers](advance-organizers.md) — both prepare learners for incoming content; prediction adds a verifiable commitment
- [Case Studies](case-studies.md) — predictions about case outcomes create engagement before the resolution is revealed
- [Check-In](check-in.md) — low-stakes response formats that make committing to a guess safe

## Patterns That Use This Element
- [Case-Based Learning](../patterns/case-based-learning.md) — learners predict outcomes before the case resolution is disclosed
- [Flipped Classroom](../patterns/flipped-classroom.md) — pre-class prediction questions prime learners for in-class resolution
- [Cognitively Guided Instruction (CGI for Math)](../patterns/cognitively-guided-instruction-cgi-for-math.md) — students estimate and predict solutions before formal strategies are taught

## Examples

**[Peer Instruction](https://www.peerinstruction.net)** (Eric Mazur, Harvard) — Students commit to a conceptual answer via clicker before and after peer discussion; the initial prediction exposes misconceptions that peer debate then resolves.

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Many simulations prompt learners to predict circuit or gas behavior before running the model, then compare outcome to prediction.

**Prequestioning in video learning** — Embedding a multiple-choice prediction before each segment of an instructional video; research shows improved learning of the queried content [Carpenter & Toftness, 2017](https://doi.org/10.1037/xap0000125).

**Predict-Observe-Explain (POE)** — A published science-teaching routine (White & Gunstone, 1992) in which learners predict a demonstration's outcome, observe it, and explain any discrepancy — directly targeting misconception revision.

## Key Sources
- Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)
- Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)
- Carpenter, S. K., & Toftness, A. R. (2017). The effect of prequestions on learning from video presentations. *Journal of Experimental Psychology: Applied, 23*(1), 83–92. [doi:10.1016/j.jarmac.2016.07.014](https://doi.org/10.1016/j.jarmac.2016.07.014)
- White, R., & Gunstone, R. (1992). Probing understanding. *London: Falmer Press.*