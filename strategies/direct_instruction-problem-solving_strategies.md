---
type: strategy
title: Direct Instruction: Problem-Solving Strategies
description: Instructors explicitly teach and model a repertoire of problem-solving strategies, then give learners supported opportunities to choose which strategies to apply and reflect on the outcomes of their choices.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Direct Instruction: Problem-Solving Strategies

## Description
This strategy makes the *strategic layer* of problem solving an explicit object of instruction. Rather than assuming learners will absorb heuristics implicitly, the instructor names, models, and compares strategies (e.g., means-ends analysis, working backwards, drawing a diagram, identifying an analogous problem), demonstrates when each is useful, and then structures practice in which learners select, apply, and evaluate strategies for themselves. The goal is transferable strategic knowledge — knowing *which* approach fits *which* problem — not just execution of a single procedure.

## Design Implications

Explicit strategy instruction works because novices lack the schemas to recognize problem types and select appropriate methods on their own; teaching the selection criteria directly reduces unproductive search [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]. The critical design move is the shift from *modeling* strategies to *learner choice*: having learners select among taught strategies and compare outcomes builds conditional knowledge (when and why each strategy applies) that pure imitation does not [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Strategy instruction should be embedded in domain content rather than taught as context-free heuristics — generic "problem-solving skills" taught in isolation transfer poorly.

### Context
#### Requirements
- A curated, small repertoire of strategies (typically 3–5) appropriate to the domain's problem types
- Modeled demonstrations that verbalize strategy selection, not just execution ([Think-Aloud](../elements/think-aloud.md) modeling within [Direct Instruction](../patterns/direct-instruction.md))
- Practice problems that vary in type so strategy *choice* matters, not just execution
- Structured reflection prompts after solving: "Which strategy did you use? Why? Would another have worked better?"

#### Constraints
- Teaching strategies as abstract, domain-general rules produces weak transfer; effectiveness depends on anchoring strategies in varied, domain-specific problems [~M]
- Overly prescriptive strategy lists can produce rigid application — learners apply a favored strategy even when ill-suited, and the instruction itself adds load for novices [Cognitive load theory](../theories/cognitive-load-theory.md) [~S]
- Benefits diminish with expertise: advanced learners who already possess strategies find explicit strategy teaching redundant and sometimes harmful [Expertise reversal effect.](../claims/expertise-reversal-effect.md) [~S]
- If practice never requires choosing among strategies (all problems match one taught method), learners acquire procedures without conditional knowledge

#### Implementation Variability
- **Strategy comparison format**: present the same problem solved two ways side by side, then discuss fit [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]
- **Faded responsibility**: instructor models selection first, then learners justify choices before solving, then choose silently ([Fading](../elements/fading.md) within [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md))
- **Error-focused variant**: analyze why a chosen strategy failed, using the mismatch to sharpen selection criteria
- **Embedded in [Case-Based Learning](../patterns/case-based-learning.md)**: cases supply the varied problem types that make strategy choice consequential

### Target Learners
- Novices who lack a repertoire of approaches and default to trial-and-error search [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- Intermediate learners who can execute procedures but cannot diagnose which procedure a novel problem requires
- Less beneficial for experts, who already possess and flexibly deploy strategies [Expertise reversal effect.](../claims/expertise-reversal-effect.md) [~S]

### Target Learning Goals
- Conditional knowledge: matching problem types to solution approaches
- Transfer: applying strategies to unfamiliar problems within the domain
- Metacognitive monitoring: evaluating whether a chosen strategy is working and switching when it is not [Process goals outperform outcome goals for novices.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]

### Instructions
1. **Name and situate the strategies.** Introduce a small set of strategies with [Analogies](../elements/analogies.md) or familiar examples, specifying what *kind* of problem each fits.
2. **Model selection aloud.** Demonstrate solving problems while verbalizing how you recognized the problem type and chose the strategy ([Think-Aloud](../elements/think-aloud.md) within [Explicit Teaching](../patterns/explicit-teaching.md)).
3. **Compare strategies on the same problem.** Show two strategies applied to one problem; discuss cost, fit, and reliability [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M].
4. **Practice with forced choice.** Assign problems that require learners to first state which strategy they will use and why, before solving ([Application of Knowledge](../elements/application-of-knowledge.md)).
5. **Reflect and compare outcomes.** After solving, learners explain their choice and evaluate it against alternatives; instructor feedback should target strategy selection, not just answers [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
6. **Fade the scaffolds.** Progressively remove the forced-choice prompts so learners internalize selection ([Fading](../elements/fading.md)).

## Related Strategies
- [Worked Examples](../strategies/use_worked_examples.md) — the modeling vehicle for demonstrating strategy execution step by step
- [Think-Aloud Modeling](../strategies/think-aloud-modeling.md) — the method for making strategy *selection* visible, not just execution
- [Reciprocal Teaching](../elements/reciprocal-teaching.md) — a canonical instance of explicit strategy instruction with faded group practice

## Examples
- **Cognitively Guided Instruction (CGI) in mathematics** — teachers elicit and build on children's informal strategies, making strategy repertoires explicit classroom content ([CGI for Math](../patterns/cognitively-guided-instruction-cgi-for-math.md)).
- **Polya-inspired heuristics in physics problem-solving courses** (e.g., Heller & Heller's University of Minnesota cooperative problem-solving curriculum) — explicit strategy framing ("describe, plan, implement, check") taught and practiced across varied contexts.
- **Reciprocal Teaching (Palincsar & Brown)** — four reading-comprehension strategies explicitly taught, modeled, then rotated among students with fading support.

## Key Sources
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117–175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)