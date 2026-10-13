---
type: strategy
id: pattern-recognition
aliases: [pattern_recognition_in_learning]
title: Pattern Recognition
description: Learners identify recurring structures, features, or relationships across multiple examples so they can classify new cases and transfer knowledge beyond the instances they studied.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Pattern Recognition

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 4 studies (2 causal, 2 quant-synthesis), `q3`–`q4` · 2 of 4 report an effect size

## Description
Pattern recognition as a strategy presents learners with multiple, deliberately varied instances of a concept, procedure, or problem type and asks them to identify what the instances share and how they differ. Rather than telling learners the defining features up front, the strategy has them extract the underlying structure themselves — surface features vary, deep structure repeats. It is carried out through example sets, comparison tasks, sorting or classification activities, and prompts that ask "what makes these the same kind of problem?"

## Design Implications

Learning a concept means learning which features matter and which do not; multiple varied examples are the primary way learners acquire that discrimination [Multiple varied examples improve transfer by highlighting invariant structure.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]. Comparison across cases is more effective than studying examples one at a time, because juxtaposition makes the common structure perceptually and cognitively salient [Comparing multiple analogs improves analogical transfer.](https://doi.org/10.1016/0010-0285(83)90018-3) [+S]. However, learners often fail to notice patterns spontaneously; prompting them to compare, explain, or self-explain is usually necessary [Eliciting self-explanations improves understanding.](https://doi.org/10.1207/s15516709cog1804_3) [+S]. A productive sequence is exploration before explanation: letting learners struggle with varied cases first prepares them to learn from the subsequent telling [Preparation for future learning: contrasting cases before instruction improves learning from lecture.](https://doi.org/10.1207/s1532690xci1604_4) [+S].

### Context
#### Requirements
- A set of at least 2–3 examples that share deep structure but differ in surface features
- Prompts that direct attention to comparison ("How are these alike? What category do they belong to?")
- A follow-up task requiring classification or application to a novel case ([Application](../elements/application.md))
- Feedback that names the pattern once learners have attempted to articulate it
- A set of examples that share an underlying structure but vary in surface features, so the deep pattern is the only reliable regularity
- Contrasting cases or non-examples that make the pattern's boundaries visible
- Prompts that direct attention to relationships ("What do these have in common? How do they differ?") rather than to individual items
- Opportunities to name, state, or represent the abstracted pattern ([Articulation](../elements/articulation.md))

#### Constraints
- Examples that are too similar teach learners to match surface features, not structure — near-transfer only [Multiple varied examples improve transfer by highlighting invariant structure.](../claims/cognitive-flexibility-theory-multiple-cases.md) [-M]
- Unguided discovery of patterns can overload novices; without prompts or prior knowledge, learners may extract the wrong regularity [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Learners with high prior knowledge may find guided comparison redundant and benefit more from independent abstraction [~M]
- If the pattern is stated before examples are studied, learners may simply confirm it rather than discriminate features [~M]
- If all examples share surface features, learners induce the wrong pattern and fail to transfer [Chi et al., 1981] [-M]
- Unguided pattern search can overload novices; minimal guidance during discovery is less effective than guided comparison for learners with low prior knowledge [~S]
- Patterns that are artificial or imposed (e.g., arbitrary mnemonics with no structural relation to content) produce brittle, quickly forgotten associations [-W]
- Learners with strong prior knowledge may gain little from guided comparison and benefit more from direct abstraction [~M]

#### Implementation Variability
- **Contrasting cases**: side-by-side pairs differing on one critical dimension, isolating the feature that matters
- **Classification tasks**: learners sort a mixed set into categories, forcing active pattern extraction
- **Invent-a-case**: learners generate their own example fitting the pattern, testing whether they have abstracted it
- **Delayed naming**: pattern is explored first, labeled afterward ("A time for telling")
- **Example comparison:** learners sort or rank worked examples by solution structure before receiving instruction
- **Contrasting cases:** pairs of cases differing in one critical feature isolate the pattern variable
- **Analogical mapping:** learners map structure from a familiar domain onto a new one ([Analogies](../elements/analogies.md))
- **Concept attainment:** learners generate and test hypotheses about what defines the category from positive and negative instances
- **Learner-generated patterns:** students create their own groupings, mnemonics, or visual structures, which supports personalization and deeper processing

### Target Learners
- Novices who otherwise anchor on surface features when classifying problems [Comparing multiple analogs improves analogical transfer.](https://doi.org/10.1016/0010-0285(83)90018-3) [+S]
- Intermediate learners building flexible, multi-case representations of a domain [Multiple varied examples improve transfer by highlighting invariant structure.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]
- Less effective as pure discovery for complete novices without comparison prompts [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Novices who lack organized schemas and default to surface-feature reasoning [Chi et al., 1981] [+M]
- Learners who struggle with rote memorization and benefit from meaningful structure
- Intermediate learners ready to move from recognizing instances to abstracting principles; fully guided comparison may be redundant for experts [~M]

### Target Learning Goals
- Concept formation: learning category boundaries and defining features
- Problem-type identification: recognizing which solution schema applies to a novel problem
- Transfer: applying structure learned in one context to superficially different contexts
- Discrimination: distinguishing genuine instances from plausible non-instances
- Schema formation: building categories organized by deep structure
- Transfer: applying a learned structure to novel problems with different surface features [Schwartz & Bransford, 1998] [+M]
- Discrimination learning: distinguishing superficially similar cases that differ structurally
- Conceptual understanding in domains with strong underlying regularities (mathematics, grammar, scientific classification)

### Instructions
1. Select 3–5 cases sharing deep structure but varying surface features; include at least one borderline or non-instance to sharpen boundaries.
2. Present cases side by side rather than sequentially, so comparison is easy.
3. Ask learners to identify what the cases have in common and generate a rule or label ([Analogies](../elements/analogies.md) can scaffold the mapping to a known structure).
4. Have learners classify new, unseen cases, including near-miss non-instances ([Case Studies](../elements/case-studies.md) work well as source cases).
5. Name and consolidate the pattern after learners attempt articulation, then connect it to the target procedure or concept.

## Related Strategies
- [Case-based learning](../patterns/case-based-learning.md) — cases are the raw material from which patterns are extracted
- [Concept attainment](../patterns/concept-attainment.md) — the classic pattern-recognition routine for concept learning
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — existing schemas are the substrate new patterns attach to
- [Analogical Reasoning](../principles/analogical-reasoning.md) — pattern recognition across domains is the mechanism of analogy

## Examples
- **[CGI for Math](../patterns/cognitively-guided-instruction-cgi-for-math.md)** — teachers learn to recognize problem types (result-unknown, change-unknown, etc.) by sorting and comparing varied word problems, then map student strategies to each type.
- **Physics problem sorting (Chi and colleagues' tradition)** — novices sort mechanics problems by surface features (pulleys, springs); training with comparison shifts sorting to deep structure (energy conservation vs. Newton's laws).
- **[Harvard Business School case method](https://www.hbs.edu/mba/academic-experience/Pages/the-hbs-case-method.aspx)** — repeated case discussion across sessions builds recognition of recurring managerial decision patterns.
- **[Concept Attainment](../patterns/concept-attainment.md)** — Bruner's model presents positive and negative instances; learners induce the defining attributes, making pattern detection the core activity.
- **[Schwartz & Bransford's contrasting cases](https://doi.org/10.1207/s15516709cog2204_2)** — students analyze contrasting graphical data patterns before a lecture, which doubles later learning from the explanation.
- **Chess instruction** — learners study master games position-by-position, building a repertoire of board patterns ([Chase & Simon, 1973](https://doi.org/10.1016/0010-0285(73)90004-0)).
- **Physics problem sorting** — students sort problems into categories by solution principle rather than topic, directly training deep-structure recognition [Chi et al., 1981].

## Key Sources
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)
- Marton, F., & Booth, S. (1997). *Learning and awareness.* Lawrence Erlbaum Associates.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*(1), 55–81. [doi:10.1016/0010-0285(73)90004-2](https://doi.org/10.1016/0010-0285(73)90004-2)
- Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science, 5*(2), 121–152. [doi:10.1207/s15516709cog0502_2](https://doi.org/10.1207/s15516709cog0502_2)
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243. [)01662-4]()01662-4). [doi:10.1016/s1364-6613(00)01662-4](https://doi.org/10.1016/s1364-6613(00)01662-4)

<!-- merged 2026-10-13 from strategies/pattern_recognition_in_learning ("Pattern Recognition in Learning"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Pattern Recognition in Learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 5 studies (2 causal, 2 review, 1 quant-synthesis), `q2`–`q4` · 0 of 5 report an effect size

## Description
Pattern recognition is the cognitive process by which learners identify recurring structures, relationships, or sequences and use them to organize, interpret, and remember new information. As a strategy, it means designing learning activities around *detecting* regularities — comparing cases, sorting examples, and abstracting underlying principles — rather than presenting the pattern as a finished rule to memorize. Expertise research shows that what distinguishes experts from novices is largely the depth and quality of the patterns they perceive: chess masters encode board positions as meaningful chunks, and expert physicists classify problems by deep structure rather than surface features [Chase & Simon, 1973; Chi et al., 1981].

## Design Implications

Pattern recognition converts isolated facts into structured knowledge, reducing working-memory load because a recognized pattern functions as a single chunk [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. The strategy works best when learners actively compare multiple examples and non-examples and induce the pattern themselves, rather than being told the rule first — discovery of structure through contrasting cases prepares learners to understand the explanation that follows [Schwartz & Bransford, 1998] [+M]. Instruction should therefore surface deep structure and vary surface features, so learners do not bind the pattern to irrelevant details [~M].

### Context
#### Requirements
- A set of examples that share an underlying structure but vary in surface features, so the deep pattern is the only reliable regularity
- Contrasting cases or non-examples that make the pattern's boundaries visible
- Prompts that direct attention to relationships ("What do these have in common? How do they differ?") rather than to individual items
- Opportunities to name, state, or represent the abstracted pattern ([Articulation](../elements/articulation.md))

#### Constraints
- If all examples share surface features, learners induce the wrong pattern and fail to transfer [Chi et al., 1981] [-M]
- Unguided pattern search can overload novices; minimal guidance during discovery is less effective than guided comparison for learners with low prior knowledge [~S]
- Patterns that are artificial or imposed (e.g., arbitrary mnemonics with no structural relation to content) produce brittle, quickly forgotten associations [-W]
- Learners with strong prior knowledge may gain little from guided comparison and benefit more from direct abstraction [~M]

#### Implementation Variability
- **Example comparison:** learners sort or rank worked examples by solution structure before receiving instruction
- **Contrasting cases:** pairs of cases differing in one critical feature isolate the pattern variable
- **Analogical mapping:** learners map structure from a familiar domain onto a new one ([Analogies](../elements/analogies.md))
- **Concept attainment:** learners generate and test hypotheses about what defines the category from positive and negative instances
- **Learner-generated patterns:** students create their own groupings, mnemonics, or visual structures, which supports personalization and deeper processing

### Target Learners
- Novices who lack organized schemas and default to surface-feature reasoning [Chi et al., 1981] [+M]
- Learners who struggle with rote memorization and benefit from meaningful structure
- Intermediate learners ready to move from recognizing instances to abstracting principles; fully guided comparison may be redundant for experts [~M]

### Target Learning Goals
- Schema formation: building categories organized by deep structure
- Transfer: applying a learned structure to novel problems with different surface features [Schwartz & Bransford, 1998] [+M]
- Discrimination learning: distinguishing superficially similar cases that differ structurally
- Conceptual understanding in domains with strong underlying regularities (mathematics, grammar, scientific classification)

### Instructions
1. Select or design 3–6 examples sharing the target structure but differing in surface features; include at least one contrasting case ([Case Studies](../elements/case-studies.md), [Comparing Cases](../elements/comparing-cases.md) if available).
2. Activate relevant prior knowledge so learners have something to connect the pattern to ([Activation](../elements/activation.md)).
3. Ask learners to compare, sort, or group the cases and articulate what recurs — before stating the rule ([Analogies](../elements/analogies.md), [Articulation](../elements/articulation.md)).
4. Name and formalize the pattern, connecting it to the principle or schema it instantiates ([Advance Organizers](../elements/advance-organizers.md)).
5. Provide practice with new instances that vary surface features, requiring learners to apply the pattern ([Practice](../elements/practice.md), [Application](../elements/application.md)).
6. Space retrieval of the pattern across sessions so recognition becomes automatic ([Distributed practice improves retention.](../claims/distributed-practice-improves-retention.md) [+S]).

## Related Strategies
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — existing schemas are the substrate new patterns attach to
- [Analogical Reasoning](../principles/analogical-reasoning.md) — pattern recognition across domains is the mechanism of analogy
- [Case-Based Learning](../strategies/case-based-learning.md) — multiple cases supply the raw material for induction

## Examples
- **[Concept Attainment](../patterns/concept-attainment.md)** — Bruner's model presents positive and negative instances; learners induce the defining attributes, making pattern detection the core activity.
- **[Schwartz & Bransford's contrasting cases](https://doi.org/10.1207/s15516709cog2204_2)** — students analyze contrasting graphical data patterns before a lecture, which doubles later learning from the explanation.
- **Chess instruction** — learners study master games position-by-position, building a repertoire of board patterns ([Chase & Simon, 1973](https://doi.org/10.1016/0010-0285(73)90004-0)).
- **Physics problem sorting** — students sort problems into categories by solution principle rather than topic, directly training deep-structure recognition [Chi et al., 1981].

## Key Sources
- Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*(1), 55–81. [doi:10.1016/0010-0285(73)90004-2](https://doi.org/10.1016/0010-0285(73)90004-2)
- Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science, 5*(2), 121–152. [doi:10.1207/s15516709cog0502_2](https://doi.org/10.1207/s15516709cog0502_2)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243. [)01662-4]()01662-4). [doi:10.1016/s1364-6613(00)01662-4](https://doi.org/10.1016/s1364-6613(00)01662-4)
-->
