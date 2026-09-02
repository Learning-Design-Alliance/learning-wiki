---
type: strategy
id: predicting
title: Predicting
description: Predicting involves anticipating what will happen next in a text or problem, engaging interest and surfacing prior knowledge before instruction.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Predicting

> **Strategy** · [All strategies](index.md)

## Description
Predicting asks learners to anticipate what will happen next in a text, demonstration, or problem before the answer is revealed. In reading, learners forecast plot, argument, or content; in mathematics, they identify what type of question is being asked, which operations might apply, and what a reasonable answer would look like. The act of committing to a prediction engages interest, exposes gaps in knowledge, and prepares learners to evaluate incoming information against their expectations.

## Design Implications

Prediction functions as a form of pretesting: even when predictions are wrong, generating them activates relevant prior knowledge and improves retention of the correct information that follows [Attempting to answer questions before instruction, even unsuccessfully, enhances subsequent learning.](../claims/activation-improves-learning.md) [+M]. Predictions create curiosity and a need to confirm or disconfirm, which increases attention during the subsequent explanation or reading. The strategy works best when learners must commit to a specific, checkable prediction rather than a vague guess, and when feedback follows quickly enough to resolve the uncertainty it created.

### Context
#### Requirements
- Content with a genuine predictive structure — a narrative, a causal process, a problem with a determinate answer
- Prompts that require a specific commitment ("What will the next step be? What do you think the answer is?") rather than open speculation
- Timely confirmation or disconfirmation, so the prediction is resolved rather than left dangling ([Practice](../elements/practice.md), [Assessment](../elements/assessment.md))

#### Constraints
- Requires some prior knowledge of the topic; learners with none can only guess randomly, and random guessing produces little activation [Activation improves learning only when relevant knowledge exists to be activated.](../claims/activation-improves-learning.md) [~M]
- Predictions based on strong misconceptions can entrench errors if the correction is weak or delayed — high-confidence wrong predictions need explicit disconfirmation [High-confidence errors, once corrected, improve retention more than low-confidence ones.](../claims/high-confidence-errors-improve-retention.md) [~M]
- Overuse of "guess what happens next" in narrative reading can fragment comprehension if predictions interrupt the flow of the text
- In well-structured domains, prediction before any modeling can impose unproductive search on novices; a [Demonstration](../elements/demonstration.md) or worked example may be needed first

#### Implementation Variability
- **Text prediction**: pause at chapter titles, headings, or mid-narrative points and ask learners to forecast content before reading on
- **Mathematical prediction**: before solving, ask what the problem is asking, what operation fits, and whether the answer will be large or small, positive or negative — an estimation and plausibility check
- **Demonstration prediction**: before an experiment or worked example, learners predict the outcome, then compare against the actual result ([Anchored Instruction](../elements/anchored-instruction.md) contexts)
- **Reciprocal teaching**: prediction is one of four strategies students rotate through in small-group reading discussion

### Target Learners
- Learners with moderate prior knowledge, who have enough schema to generate meaningful predictions [Activation improves learning.](../claims/activation-improves-learning.md) [+M]
- Reluctant or passive readers, for whom prediction points create a purpose for reading
- Novices in problem-solving domains benefit from the "what kind of problem is this?" variant, which builds classification skill before computation
- Less effective for complete novices, who lack the knowledge base to predict anything but arbitrarily

### Target Learning Goals
- Comprehension monitoring: noticing when text violates expectations
- Prior knowledge activation: connecting new information to what is already known
- Problem classification: recognizing problem types and appropriate operations before executing them
- Motivation and engagement: curiosity about whether one's prediction was right

### Instructions
1. Select a prediction point — a heading, a pause in a demonstration, or the statement of a problem before its solution.
2. Prompt a specific, committed prediction: "What do you think will happen? What will the answer be close to?" ([Activation](../elements/activation.md))
3. Have learners record or share predictions so they are accountable and comparable to the outcome.
4. Reveal the outcome through reading, [Direct Instruction](../patterns/direct-instruction.md), or completing the problem.
5. Compare prediction to result and discuss discrepancies — the discussion of *why* the prediction was wrong is where much of the learning occurs.
6. Follow with [Practice](../elements/practice.md) in which learners generate their own predictions independently, fading the prompts.

## Related Strategies
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — prediction is a specific mechanism for activation; it forces retrieval rather than merely prompting for it
- [Think-Aloud Modeling](../strategies/think-aloud-modeling.md) — expert prediction ("I expect this to…") models the strategy for learners
- [Pretesting](../strategies/pretesting.md) — the broader family of before-instruction attempts that prediction belongs to

## Related Elements
- [Activation](../elements/activation.md) — the cognitive function prediction serves
- [Advance Organizers](../elements/advance-organizers.md) — a related pre-reading structure; organizers frame content, predictions commit learners to expectations
- [Practice](../elements/practice.md) — where independent prediction becomes a habitual self-regulation move

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — learners predict expert moves before observing the modeled performance
- [Reciprocal Teaching](../elements/reciprocal-teaching.md) — prediction is one of the four cycled comprehension strategies
- [Flipped Classroom](../patterns/flipped-classroom.md) — pre-class prediction prompts prepare learners to check their expectations against instruction

## Examples
- **Reciprocal teaching (Palincsar & Brown)** — small reading groups predict upcoming content at designated points before summarizing, questioning, and clarifying; the routine raised sixth-graders' comprehension substantially in the original studies.
- **Physics "predict–observe–explain"** — students predict the outcome of a demonstration (e.g., which mass hits the ground first), observe it, and explain any discrepancy; widely used to confront misconceptions.
- **Estimation in mathematics** — before computing 47 × 63, students predict whether the answer is closer to 300 or 3,000, building number sense and a plausibility check for their eventual answer.

## Key Sources
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117-175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
- Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)
- Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)