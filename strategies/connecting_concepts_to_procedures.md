---
type: strategy
title: Connecting Concepts to Procedures
description: Instruction explicitly links conceptual understanding with procedural skill so each reinforces the other, rather than teaching algorithms as rote steps.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Connecting Concepts to Procedures

> **Strategy** · [All strategies](index.md)

## Description
This strategy treats conceptual knowledge (why a procedure works) and procedural knowledge (how to execute it) as mutually reinforcing rather than separate instructional tracks. Instruction sequences and interleaves the two: procedures are introduced with explicit reference to the concepts that justify them, and conceptual discussion is grounded in the procedures learners are mastering. The relationship is iterative — procedural fluency creates material for conceptual reasoning, and conceptual insight improves procedural flexibility and error detection.

## Design Implications

The strategy rests on a well-documented reciprocal relationship: growth in one knowledge type predicts subsequent growth in the other across domains such as mathematics [Rittle-Johnson et al. model iterative bidirectional development of conceptual and procedural knowledge.](https://doi.org/10.1111/1467-8624.00377) [+M]. Teaching procedures without conceptual grounding produces brittle, error-prone performance that fails to transfer; teaching concepts without procedural practice leaves learners unable to act. The design problem is sequencing and connection-making, not choosing one over the other.

### Context
#### Requirements
- Instructor command of *both* the concept and the procedure — superficial procedural knowledge cannot be connected to anything
- Explicit connection points: prompts that ask learners to explain *why* a step works, not just *what* to do ([Self-Explanation](../elements/self-explanation.md) or structured questioning)
- Representational variety — concrete, visual, and symbolic forms of the same idea so the procedure can be seen as one instantiation of the concept
- Practice that includes varied problem formats, forcing learners to decide *which* procedure applies and why

#### Constraints
- Time-intensive: building conceptual foundations before or alongside procedures is slower than direct algorithm drill in the short term, and gains may not appear on immediate procedural tests [~M]
- Weak or inaccurate conceptual instruction can actively interfere — misconceptions taught as "understanding" produce worse outcomes than clean procedural instruction alone [-M]
- For learners with very low prior knowledge, heavy conceptual discussion can overload working memory before the procedure is stable [Cognitive load constraints favor part-task practice before integrated reasoning.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]
- The benefit reverses with expertise: advanced learners often gain little from re-deriving concepts they have already integrated [Guidance becomes less effective as expertise grows.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Concepts-first:** develop the conceptual model, then formalize the procedure (common in [Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md))
- **Procedures-first with retroactive connection:** teach the algorithm, then unpack why it works — efficient when the procedure is simple but the concept is abstract
- **Interleaved/iterative:** alternate between the two across a unit, the design most consistent with the bidirectional-development evidence [+M]
- **Comparison-based:** present two procedures side by side and ask what conceptual difference explains their difference [Comparing multiple cases supports abstraction of the underlying structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]

### Target Learners
- Novices in a domain, who otherwise memorize algorithms they cannot adapt or debug [Self-explanation of why steps work improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Intermediate learners who execute procedures accurately but apply them indiscriminately
- Less beneficial for experts, for whom the connection is already consolidated [Expertise reverses the benefit of added conceptual scaffolding.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural flexibility: selecting and adapting methods to problem features
- Conceptual schema formation: understanding why procedures work [Whole-task practice improves transfer better than isolated drill.](../claims/whole-task-performance-improves-transfer.md) [+M]
- Error detection and self-correction: using conceptual understanding to catch procedural slips [Erroneous examples build conceptual knowledge by requiring diagnosis.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Instructions
1. Establish the conceptual foundation with a concrete or visual model ([Analogies](../elements/analogies.md), manipulatives, or a real-world scenario tied to learners' background knowledge)
2. Introduce the procedure as a *consequence* of the concept, narrating why each step is justified ([Direct Instruction](../elements/direct-instruction.md) with explicit connection language)
3. Have learners explain the connection in their own words during early practice ([Practice](../elements/practice.md) with self-explanation prompts) [+S]
4. Present varied and contrasting problems so learners must reason about *when* the procedure applies, not just *how*
5. Use erroneous examples — a worked solution with a conceptual error — and ask learners to find and explain the flaw [+M]
6. Fade the conceptual supports as fluency develops, shifting prompts from "why does this work?" to "which method fits this problem?"

## Related Strategies
- [Worked Examples](worked-examples.md) — worked examples annotated with conceptual rationale are a primary vehicle for connecting the two knowledge types
- [Self-Explanation](../elements/self-explanation.md) — the mechanism by which learners extract the concept–procedure link
- [Comparing Cases](../elements/comparing-cases.md) — contrast supports abstraction of the concept underlying different procedures

## Related Elements
- [Analogies](../elements/analogies.md) — bridge unfamiliar procedures to familiar conceptual structures
- [Practice](../elements/practice.md) — the site where connections are consolidated; practice prompts should require justification, not just execution
- [Coaching](../elements/coaching.md) — in-the-moment questioning that surfaces why a procedure step is warranted
- [Case Studies](../elements/case-studies.md) — contextualize procedures within meaningful conceptual problems

## Patterns That Use This Strategy
- [Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md) — builds procedures from learners' conceptual problem models
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — pairs supportive (conceptual) information with procedural information on learning tasks
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — expert narration makes the conceptual basis of procedures visible

## Examples
- **Cognitively Guided Instruction (CGI)** — elementary mathematics teachers elicit children's informal solution strategies and connect standard algorithms to the conceptual operations children already use ([CGI overview](https://www.education.wisc.edu/wwi/about/))
- **Number Talks** — brief classroom routines where learners solve a computation mentally, share strategies, and the teacher connects each strategy to place-value or operation concepts
- **[Khan Academy](https://www.khanacademy.org)** — math lessons pair procedural video demonstrations with "why this works" conceptual explanations and varied practice sets
- **[Illustrative Mathematics](https://illustrativemathematics.org)** — curriculum explicitly sequenced so conceptual tasks precede and accompany procedural fluency practice

## Key Sources
- Rittle-Johnson, B., Siegler, R. S., & Alibali, M. W. (2001). Developing conceptual understanding and procedural skill in mathematics: An iterative process. *Child Development, 72*(2), 346–361. [doi:10.1037/0022-0663.93.2.346](https://doi.org/10.1037/0022-0663.93.2.346)
- Rittle-Johnson, B., Loehr, A. M., & Durkin, K. (2017). Promoting self-explanation to improve mathematics learning: A meta-analysis and instructional design principles. *ZDM Mathematics Education, 49*, 599–611. [doi:10.1007/s11858-017-0834-z](https://doi.org/10.1007/s11858-017-0834-z)
- Hiebert, J., & Lefevre, P. (1986). Conceptual and procedural knowledge in mathematics: An introductory analysis. In J. Hiebert (Ed.), *Conceptual and procedural knowledge: The case of mathematics* (pp. 1–27). Lawrence Erlbaum.
- Rittle-Johnson, B., & Schneider, M. (2015). Developing conceptual and procedural knowledge of mathematics. In R. C. Kadosh & A. Dowker (Eds.), *Oxford Handbook of Numerical Cognition* (pp. 1118–1134). Oxford University Press.
- Canobi, K. H. (2009). Concept–procedure interactions in children's addition and subtraction. *Journal of Experimental Child Psychology, 102*(2), 131–149. [doi:10.1016/j.jecp.2008.07.008](https://doi.org/10.1016/j.jecp.2008.07.008)