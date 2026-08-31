---
type: strategy
title: Self Explanation Prompting
description: Prompts that ask learners to explain to themselves how new information relates to what they know, or why each step of a solution works, generating elaborations that improve understanding.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Self Explanation Prompting

> **Strategy** · [All strategies](index.md)

## Description
Self explanation prompting asks learners to generate explanations *to themselves* while studying material — articulating why a step in a worked solution was taken, how a new concept connects to prior knowledge, or what a text segment means in their own words. The prompt can be open ("explain this step to yourself") or scaffolded with specific question stems. The critical feature is that the learner, not the instructor, produces the explanatory content; the prompt only triggers the generative process.

## Design Implications

Self explanation works because it forces the learner to actively integrate new material with existing schemas rather than passively reading or observing, converting study time into [generative processing](../principles/active-learning.md) [+S]. A meta-analysis of 64 studies found self explanation prompts produce moderate positive effects on learning outcomes, with effects holding across domains and age groups [Bisra et al. (2018)](https://doi.org/10.1007/s10648-018-9434-x) [+S]. The quality of the explanation matters more than its mere production: prompts that elicit principled, accurate explanations outperform prompts that elicit restatement [~M].

### Context
#### Requirements
- Study material with enough structure that correct explanations are discoverable (e.g., worked examples, well-organized texts)
- Prompt stems that direct attention to *why* and *how*, not just *what*
- Some mechanism for learners to detect and repair flawed explanations — feedback, [Comparing Cases](../elements/comparing-cases.md), or access to correct reasoning — since self-generated explanations can be wrong and errors go uncorrected [-M]
- Time: self explanation slows study; schedules must accommodate it

#### Constraints
- Inaccurate self explanations can entrench misconceptions when no corrective mechanism exists [-M]
- Learners with high prior knowledge may gain little and experience the prompts as redundant, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]
- Overly frequent or rigid prompting adds extraneous load and interrupts comprehension of the base material [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- For rote or procedural fluency goals, explanation adds little beyond direct practice [~M]

#### Implementation Variability
- **Prompted during study** (inline prompts after each step or paragraph) vs. **prompted after study** (end-of-section explanation tasks); inline prompting produces stronger effects but costs more time [+M]
- **Open prompts** ("explain what this means to you") vs. **directed prompts** ("why is this step valid?"); directed prompts are more reliable for novices [~M]
- **Training in self explanation** followed by unprompted use — the long-term goal is a self-initiated study habit, part of [self-regulated learning](../theories/self-regulated-learning.md)
- **Peer explanation** (explaining to another student) as a social variant, though this shades into [collaborative learning](../principles/collaborative-learning.md) and changes the mechanism

### Target Learners
- Novices and low-prior-knowledge learners, who otherwise read worked examples superficially [Bisra et al. (2018)](https://doi.org/10.1007/s10648-018-9434-x) [+S]
- Middle school through adult learners; effects are weaker but present for younger children, who may need more scaffolded stems [+M]
- Less valuable for experts, for whom prompted explanation of familiar material is redundant [~M]

### Target Learning Goals
- Conceptual understanding: why procedures work, not just how to execute them
- Integration: connecting new material to prior knowledge and across topics
- Metacognitive monitoring: explaining exposes gaps the learner didn't know they had [+M]
- Transfer: principled explanations support applying methods to novel problems [+M]

### Instructions
1. Select material with discrete, explainable units — worked solution steps, causal claims in a text, rules with exceptions.
2. Write prompt stems targeting principles, not restatement: "Why is this step legitimate here?", "How does this relate to what you already know about X?"
3. Insert prompts at natural breakpoints ([Chunking](../principles/chunking.md) the material so each prompt covers a manageable unit).
4. Provide a way to check explanations — reveal expert reasoning after the prompt, or pair with [Comparing Cases](../elements/comparing-cases.md) so learners can test their explanation against contrasting outcomes [Comparing and contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S].
5. Fade the prompts as learners internalize the habit, moving toward unprompted self explanation ([Fading](../elements/fading.md)).

## Related Strategies
- **Worked example study** — self explanation prompts are the standard companion to worked examples, converting passive example reading into active principle extraction
- **Retrieval practice** — complementary generative activity; explanation targets understanding, retrieval targets accessibility
- **Comparing contrasting cases** — comparison prompts often elicit self explanations as a byproduct

## Examples
- **Chi et al.'s (1989) physics studies** — the foundational paradigm: students studying worked mechanics examples who spontaneously self explained learned far more; prompted versions replicate the effect for non-explainers.
- **[Khan Academy](https://www.khanacademy.org)** — hint sequences in practice exercises function as scaffolded explanation prompts, revealing one reasoning step at a time before the full solution.
- **[ASSISTments](https://www.assistments.org)** — math homework platform that inserts "explain your reasoning" prompts and uses explanation quality to route feedback.
- **Reading comprehension instruction** — reciprocal teaching (Palincsar & Brown) embeds self explanation within summarizing and questioning routines.

## Key Sources
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science, 13*(2), 145–182. [doi:10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1)
- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*(3), 703–725. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)
- Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. *Journal of Educational Psychology, 95*(4), 774–789. [doi:10.1037/0022-0663.95.4.774](https://doi.org/10.1037/0022-0663.95.4.774)
- Fonseca, B. A., & Chi, M. T. H. (2011). Instruction based on self-explanation. In R. E. Mayer & P. A. Alexander (Eds.), *Handbook of research on learning and instruction* (pp. 296–321). Routledge.
- Roy, M., & Chi, M. T. H. (2005). The self-explanation principle in multimedia learning. In R. E. Mayer (Ed.), *The Cambridge handbook of multimedia learning* (pp. 271–286). Cambridge University Press.