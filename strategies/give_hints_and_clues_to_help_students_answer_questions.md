---
type: strategy
title: Give Hints and Clues to Help Students Answer Questions
description: When a learner struggles to answer, the instructor provides graduated hints and rephrased questions that narrow the search space without supplying the answer.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Give Hints and Clues to Help Students Answer Questions

## Description
When a learner is unable to answer a question, the instructor responds with a sequence of graduated hints — rephrasing the question, narrowing its scope, or pointing to relevant prior knowledge — rather than either repeating the question verbatim or supplying the answer. The goal is to keep the learner doing the cognitive work while reducing the difficulty of the search. Hints should be contingent: the smallest prompt that allows the learner to proceed, escalating only as needed [Contingent scaffolding improves learning outcomes.](../claims/contingent-scaffolding-improves-learning.md) [+M].

## Design Implications

Hinting is a form of [Scaffolding](../principles/scaffolding.md) delivered in the moment of need: it keeps learners within their zone of proximal development by transferring only the part of the task they cannot yet do themselves. Effective hints direct attention to task features and reasoning steps rather than to answers, which preserves the generative processing that produces learning [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. The sequence matters — moving from general ("What is the question really asking?") to specific ("Look at the second term") lets the instructor diagnose where the breakdown occurred.

### Context
#### Requirements
- Instructor knowledge of the learner's current understanding, so hints target the actual point of failure
- A planned hint hierarchy for predictable difficulties, from rephrasing to narrowing to directing attention
- Wait time after each hint; hints delivered too quickly become answer-giving
- Willingness to let learners struggle productively before intervening

#### Constraints
- Over-hinting converts retrieval practice into passive reception and signals to the learner (and class) that they are failing [-M]
- Hints that reveal the answer eliminate the desirable difficulty of retrieval, reducing retention compared with successful retrieval after a lighter prompt [-S]
- The same hint level does not fit all learners; identical prompting can be redundant for some and insufficient for others as expertise grows [Guidance effectiveness reverses with learner expertise.](../claims/expertise-reversal-effect.md) [~M]
- In whole-class settings, extended hinting of one student can lose the rest of the group; brief hints or redirecting to peers mitigates this

#### Implementation Variability
- **Verbal hinting in discussion** — rephrasing, delving ("Why do you think that?"), and narrowing the question
- **Hint systems in software** — on-demand hints ordered from least to most specific (e.g., Khan Academy, ASSISTments), often with a worked example as the final level
- **Peer hinting** — structured partner prompts where students give clues rather than answers
- **Written hint cards or hint tokens** — learners exchange a token for a hint, making help-seeking deliberate and limiting over-reliance

### Target Learners
- Struggling learners and novices, who lack the knowledge to generate their own prompts [Contingent scaffolding improves learning outcomes.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- Learners with low academic self-confidence, for whom a successful answer after a hint builds efficacy [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]
- Less beneficial for advanced learners, who benefit more from extended struggle and minimal prompting [Guidance effectiveness reverses with learner expertise.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Retrieval and application of recently taught concepts during questioning
- Problem-solving persistence: staying engaged with a difficult task rather than giving up
- Metacognitive awareness of what makes a question answerable (what to check, what to recall)

### Instructions
1. Ask the question and provide adequate wait time before intervening.
2. Diagnose the failure: is the learner misreading the question, missing a fact, or lacking a strategy?
3. Give the least specific useful hint — typically rephrasing or narrowing the question rather than adding content.
4. Escalate through the hint hierarchy only if the learner remains stuck, pausing after each level.
5. When the learner answers, ask them to explain their reasoning so the hint leads to [Self-Explanation](../elements/self-explanation.md) rather than mere agreement.
6. Fade hints over successive encounters with the same difficulty, consistent with [Fading](../elements/fading.md).

## Related Strategies
- [Wait Time](wait-time.md) — the pause that makes hinting diagnostic rather than reactive
- [Cold Calling](cold-calling.md) — the questioning context in which hints are most often needed
- [Activating Prior Knowledge](activating-prior-knowledge.md) — hints frequently work by pointing learners to relevant prior knowledge

## Examples
- **Khan Academy** (https://www.khanacademy.org) — math exercises offer a sequence of hints, each revealing one step; the final hint is a fully worked step, and hint use is tracked as a signal of struggle.
- **ASSISTments** (https://www.assistments.org) — delivers scaffolded hints and reports to teachers which hint level each student needed, treating hint level as a formative assessment measure.
- **Reciprocal teaching** — students learn to give each other clarifying prompts ("What does this word mean here?") when a peer cannot answer, transferring the hinting role to learners.

## Key Sources
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. [doi:10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)
- Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist, 49*(4), 219–243. [doi:10.1080/00461520.2014.965823](https://doi.org/10.1080/00461520.2014.965823)
- Pino-Pasternak, D., van Deur, P., & Volet, S. (2014). Interventions scaffolding children's self-regulated learning: A review. *Educational Psychology Review, 26*(3), 361–397. [doi:10.1007/s10648-014-9262-y](https://doi.org/10.1007/s10648-014-9262-y)
- Hmelo-Silver, C. E., Duncan, R. G., & Chinn, C. A. (2007). Scaffolding and achievement in problem-based and inquiry learning: A response to Kirschner, Sweller, and Clark (2006). *Educational Psychologist, 42*(2), 99–107. [doi:10.1080/00461520701263368](https://doi.org/10.1080/00461520701263368)