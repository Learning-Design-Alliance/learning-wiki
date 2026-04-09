---
type: principle
status: review
last_edited: 2026-04-07
edited_by: Codex
---

# Cognitive Load Theory

## Description
Cognitive Load Theory, as a design principle, emphasizes managing the demands placed on working memory so learners can devote more capacity to schema construction rather than avoidable confusion. In practice this means simplifying presentation, sequencing support, and reducing unnecessary processing costs.

## Implications
Cognitive Load Theory implies that performance problems are often design problems, not just learner problems. When instructional materials split attention, add unnecessary complexity, or demand too much search too early, working memory is consumed by coordination rather than learning. Reducing that avoidable load usually helps novices form schemas faster [[claims/chunking-reduces-working-memory-load]] [+S], but the same supports can become redundant for more advanced learners, so the practical goal is calibrated load, not permanent simplification [[claims/expertise-reversal-effect]] [~M].

### Context
#### Requirements
- **Instructional choices that reduce extraneous load**
- **Sequencing or support aligned to learner expertise**
- **Attention to how information is presented, not just what is presented**
#### Constraints
- **Over-simplification can underprepare learners for real complexity**
- **Supports that help novices may burden experts**

### Target Learners
- Especially important for novices and for content with high intrinsic complexity.

### Target Learning Objectives
- Improve comprehension and early schema formation by reducing avoidable overload.

### Theory
#### Supporting
- [[theories/cognitive-load-theory|Cognitive Load Theory]]
#### Contradicting / Qualifying
- Load management should support meaningful learning, not strip away all challenge.

### Claims
- [[claims/chunking-reduces-working-memory-load]] [+S] — design choices that organize information and reduce unnecessary search help preserve working-memory capacity
- [[claims/expertise-reversal-effect]] [~M] — guidance calibrated for novices can lose value or become burdensome as expertise increases

## Related Principles
- [[principles/scaffolding|Scaffolding]]
- [[principles/worked-examples|Worked Examples]]
- [[principles/accessible-vocabulary-syntax|Accessible Vocabulary & Syntax]]

## Examples
- A novice algebra lesson uses a single integrated visual instead of separate text and diagram panels that learners must constantly coordinate.
- A software onboarding flow replaces open-ended exploration with worked examples and progressively harder tasks until users can perform the workflow independently.

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
