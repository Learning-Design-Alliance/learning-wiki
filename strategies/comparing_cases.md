---
type: strategy
title: Comparing Cases
description: Learners study two or more contrasting cases side by side to abstract the deep structure that distinguishes them.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Comparing Cases

## Description
Comparing cases asks learners to examine two or more worked instances — problems, examples, or scenarios — side by side and identify what varies and what stays constant. The comparison itself, not any single case, is the instructional event: alignment of the cases makes the underlying relational structure visible, supporting abstraction of general principles.

## Design Implications

Comparison is one of the most reliable routes to schema abstraction, because variation across cases isolates which features are incidental and which are structural [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]. Comparisons also prompt self-explanation, which independently improves conceptual understanding [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. The design burden is on case selection and alignment: cases must be isomorphic enough to map onto each other, and learners need explicit prompts to compare rather than merely read each case in sequence.

### Context
#### Requirements
- Two or more cases that share deep structure but differ in surface features (or, for discrimination learning, differ in structure)
- Spatial or visual alignment of the cases so corresponding elements can be mapped directly
- Comparison prompts that direct attention to relations ("How are these solution methods alike?") rather than leaving comparison to chance
- Sufficient time; comparison is effortful and truncated comparison yields surface-level noticing

#### Constraints
- Sequential presentation (studying cases one at a time) largely eliminates the benefit; simultaneous side-by-side viewing is what drives structural alignment [-M]
- Novices may compare on surface features unless prompts direct attention to relations, producing spurious generalizations [-M]
- Poorly chosen cases — too dissimilar, or differing in too many ways — overload working memory and prevent mapping [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M]
- For learners with strong prior knowledge, comparison of near-identical cases adds little beyond studying one case well [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Different-solution comparison:** two correct methods for the same problem (e.g., algebraic vs. graphical), building flexible procedural knowledge
- **Correct–incorrect comparison:** a worked solution paired with an erroneous one, sharpening discrimination of the critical feature [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Multiple surface variants:** several isomorphic problems with different cover stories, supporting transfer to novel contexts
- **Invention before comparison:** learners attempt to invent a solution first, then compare cases — the "time for telling" sequence that prepares learners to benefit from instruction

### Target Learners
- Novices, who otherwise encode only surface features of a single example [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]
- Learners prone to overgeneralizing from one instance or anchoring to a single solution method
- Intermediate learners comparing alternative solution strategies; less valuable for experts, for whom a single case suffices [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding: abstracting principles and relational structure from instances
- Transfer: recognizing when the same structure recurs under different surface features
- Procedural flexibility: knowing multiple methods and when each is advantageous
- Discrimination learning: distinguishing correct from flawed reasoning or designs

### Instructions
1. Select or author cases that share the target structure and differ in surface features (or differ in the critical feature for discrimination goals).
2. Present cases simultaneously and aligned, so corresponding elements sit side by side — not sequentially.
3. Pose explicit comparison prompts directing attention to relations between cases, and require written or discussed answers ([Self-Explanation](../elements/self-explanation.md), [Class Discussion](../elements/class-discussion.md)).
4. Follow with explicit instruction that names the abstracted principle — comparison prepares for, but does not replace, telling ([Advance Organizers](../elements/advance-organizers.md)).
5. Fade to independent comparison: present new case pairs and ask learners to generate the comparison themselves ([Fading](../elements/fading.md), [Practice](../elements/practice.md)).

## Related Strategies
- [Use Worked Examples](../strategies/use_worked_examples.md) — comparing two worked examples is the natural extension of single-example study
- [Erroneous Examples](../elements/erroneous-examples.md) — a correct–incorrect comparison is a special case of case comparison
- [Analogical Encoding](../strategies/analogical-encoding.md) — comparison as the mechanism of analogical transfer

## Examples
- **Rittle-Johnson & Star's algebra studies** — students compared pairs of worked problems using different solution methods (e.g., subtract first vs. distribute first), improving conceptual and procedural flexibility over studying the same examples sequentially.
- **Schwartz & Bransford's "A Time for Telling"** — statistics students analyzed contrasting datasets before lecture; the comparison phase dramatically improved learning from subsequent instruction.
- **[Khan Academy](https://www.khanacademy.org)** — worked example pairs showing alternative solution paths for the same problem, with prompts to identify which method is more efficient and why.
- **Case-based business teaching ([Harvard Business School method](../patterns/case-based-learning-harvard-method.md))** — discussion sections explicitly juxtapose prior cases with the current one, prompting students to map structural similarities across contexts.

## Key Sources
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)
- Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? An experimental study on learning to solve equations. *Journal of Educational Psychology, 99*(3), 561–574. [doi:10.1037/0022-0663.99.3.561](https://doi.org/10.1037/0022-0663.99.3.561)
- Marton, F. (2014). Necessary conditions of learning. *New York, NY: Routledge.*
