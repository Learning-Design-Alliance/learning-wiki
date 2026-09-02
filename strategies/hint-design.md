---
type: strategy
id: hint-design
title: Hint Design
description: Sequenced, graduated hints that provide the minimal information needed to keep a learner progressing without giving away the solution.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Hint Design

> **Strategy** · [All strategies](index.md)

## Description
Hint design is the deliberate structuring of help so that learners receive the smallest increment of support needed to resume productive work. Hints are typically sequenced from general (pointing to relevant principles or strategies) to specific (revealing a step or the solution), and delivered on demand rather than automatically.

## Design Implications

Well-designed hints keep learners in productive struggle rather than either floundering or copying [Hints that support self-explanation improve problem-solving outcomes.](../claims/self-explanation-improves-learning.md) [+M]. The critical design decision is the *first* hint: it should redirect attention or strategy, not supply the answer, because answer-giving short-circuits the retrieval and reasoning that produce learning [Retrieval practice strengthens retention more than restudy.](../claims/retrieval-practice-improves-retention.md) [+S]. Sequencing matters — a ladder of increasingly explicit hints lets learners exit at the level they need, which also gives instructors diagnostic information about where understanding breaks down.

### Context
#### Requirements
- A task analysis identifying the specific points where learners typically stall
- A hint ladder: at least two levels, from conceptual/strategic to procedural/solution-level
- Delivery on learner request or after documented unproductive effort, not immediately
- Hints phrased as questions or prompts where possible ([Socratic questioning](../strategies/socratic_questioning.md)) rather than statements

#### Constraints
- Immediate, unsolicited hints reduce learning compared with allowing an attempt first [Post-question feedback and support are more effective when learners generate an answer first.](../claims/retrieval-practice-improves-retention.md) [-M]
- Bottom-rung hints that simply reveal the answer produce shallow learning and encourage hint abuse in online systems [~S]
- Overly vague hints ("think harder") provide no actionable guidance and increase frustration [-M]
- Learners with very low prior knowledge may not be able to use conceptual hints at all and need more direct procedural support [~M]

#### Implementation Variability
- **On-demand ladders** (e.g., ASSISTments, Khan Academy): learner clicks through hint levels; each click is logged as a measure of need
- **Time- or attempt-triggered**: hints unlock after a fixed number of failed attempts
- **Peer-mediated**: hints come from classmates, trading speed for social explanation benefits
- **Faded full guidance**: in [worked examples](../claims/worked-examples-reduce-novice-search.md), hints are pre-embedded as completion problems where learners fill in decreasing portions of the solution

### Target Learners
- Novices in problem-solving domains who stall without knowing *which* principle applies [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Struggling learners in adaptive systems, where hint-seeking data can trigger remediation [Adaptive systems that respond to learner difficulty improve outcomes.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- Less beneficial for advanced learners, who benefit more from solving unaided and may experience hints as redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural problem solving: mathematics, programming, physics
- Strategic knowledge: learning *when* to apply which approach, not just how
- Self-regulated learning: well-designed hints model help-seeking as a deliberate strategy

### Instructions
1. Analyze the task to identify common sticking points and the knowledge each requires.
2. Write a hint ladder per sticking point: (a) a conceptual prompt pointing to the relevant principle, (b) a strategic prompt suggesting a first step, (c) a worked step or the solution with explanation.
3. Gate delivery: require an attempt or a stated question before the first hint.
4. Phrase early hints as questions that prompt self-explanation rather than statements [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-learning.md) [+M].
5. Log hint usage and use it diagnostically — frequent bottom-rung use signals a task or instruction problem, not a learner problem.
6. Fade hint availability as learners gain competence, consistent with the [expertise-reversal effect](../theories/expertise-reversal-effect.md).

## Related Strategies
- [Scaffolding](../strategies/scaffolding.md) — hints are the fine-grained, in-task form of scaffolding
- [Fading](../elements/fading.md) — hint ladders should fade as competence grows
- [Worked examples](../strategies/use_worked_examples.md) — the top rung of a hint ladder is often a worked example
- [Retrieval practice](../strategies/retrieval_practice.md) — hints must be delayed long enough for retrieval to be attempted

## Examples
- **[ASSISTments](https://www.assistments.org)** — online math homework system with structured hint ladders; research using its logged hint data showed that bottom-out hint usage predicts lower learning gains [+M]
- **[Khan Academy](https://www.khanacademy.org)** — exercises offer sequenced hints ("I need a hint" → progressively more explicit steps) before revealing the full solution
- **[Carnegie Learning MATHia](https://www.carnegielearning.com)** — cognitive-tutor software delivers context-sensitive hints keyed to the learner's current solution step, based on a cognitive model of the task

## Key Sources
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences, 4*(2), 167–207. [doi:10.1207/s15327809jls0402_2](https://doi.org/10.1207/s15327809jls0402_2)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Aleven, V., McLaughlin, E. A., Glenn, R. A., & Koedinger, K. R. (2016). Instruction based on adaptive learning technologies. In R. E. Mayer & P. A. Alexander (Eds.), *Handbook of Research on Learning and Instruction* (2nd ed., pp. 522–560). Routledge.
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. [doi:10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)