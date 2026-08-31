---
type: strategy
title: Worked Examples Types
description: Worked example types range from fully worked modelling examples (expert narrates every step and why) through completion problems and case studies, forming a guidance continuum from maximum support toward independent problem solving.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Worked Examples Types

## Description
Worked example types form a guidance continuum rather than a single technique. At the maximum-support end sit **fully worked examples** — a complete solution presented step by step, often with expert reasoning narrated. **Completion problems** (also called faded or fadeout examples) present a fully solved model followed by a partially solved problem the learner must finish. **Erroneous examples** present a flawed solution for learners to diagnose and correct, and **case-based examples** embed the worked solution in a rich, situated scenario. Selecting among these types is a decision about how much structure to provide at a given point in skill acquisition.

## Design Implications

The choice of worked example type should track learner expertise: high guidance early, fading as competence grows. Alternating examples with problems (example–problem pairs) consistently outperforms either examples alone or problem solving alone for novices [Example-problem sequences reduce cognitive load and improve learning for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]. As expertise develops, the same guidance becomes redundant and can even impose extraneous load [Guidance that helps novices becomes less effective or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S].

### Context
#### Requirements
- A well-structured task domain with clear solution steps; worked examples are poorly suited to ill-structured problems with no canonical solution path
- Subgoal labeling or annotation that explains *why* each step is taken, not just *what* is done — unlabeled steps force learners to infer structure on their own
- A sequencing plan: which type to use at which point, and how support will be faded ([Fading](../elements/fading.md))
- Paired practice problems matched in structure to each example

#### Constraints
- Presenting fully worked examples to learners with substantial prior knowledge wastes time and can depress performance relative to unguided practice [Guidance that helps novices becomes less effective or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [-M]
- Examples without accompanying problem solving produce shallow encoding and overconfident self-assessment; learners who only study examples often believe they can solve problems they cannot [-S]
- Splitting attention between a problem statement, the solution, and separate explanatory text (split-attention effect) negates much of the example's benefit; integrate steps and commentary physically [-S]
- Erroneous examples used with novices who lack the knowledge to spot the flaw can reinforce the error rather than correct it [Erroneous examples build conceptual knowledge when learners can engage the error productively.](../claims/erroneous-examples-build-conceptual-knowledge.md) [~M]

#### Implementation Variability
- **Fully worked examples**: maximum support; best for the first encounter with a new task category
- **Completion problems**: intermediate support; the learner completes the final steps, then progressively earlier steps are removed — the standard fading sequence
- **Erroneous examples**: learners find and fix a planted error; effective for building conceptual understanding and error detection once basic procedures are known [Erroneous examples build conceptual knowledge when learners can engage the error productively.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Case-based examples**: the worked solution is embedded in a narrative or professional scenario; adds context but also added load, so reserve for learners who can handle the extra processing
- **Example–problem pairs**: each example is immediately followed by an isomorphic problem; the most robustly supported arrangement [Example-problem sequences reduce cognitive load and improve learning for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]

### Target Learners
- Novices in a structured domain (algebra, programming, physics, grammar), for whom worked examples substitute for effortful, error-prone search [Example-problem sequences reduce cognitive load and improve learning for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]
- Learners with low prior knowledge benefit most; for them, unguided problem solving imposes search-related extraneous load
- More advanced learners should shift toward completion problems and then independent problems, since full examples become redundant [Guidance that helps novices becomes less effective or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S]

### Target Learning Goals
- Procedural fluency: acquiring and automating solution schemas in well-structured domains
- Schema construction: building mental models of problem categories and their canonical solution paths
- Error detection and conceptual understanding: diagnosing flawed solutions sharpens discrimination between correct and incorrect reasoning [Erroneous examples build conceptual knowledge when learners can engage the error productively.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Instructions
1. Identify the problem category and write a complete, correct solution with each step annotated for its rationale (subgoal labeling).
2. Present the fully worked example first, integrated with the problem statement to avoid split attention; chunk steps so each is processed as a unit [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M].
3. Follow immediately with an isomorphic problem the learner solves alone (example–problem pairing) [Example-problem sequences reduce cognitive load and improve learning for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S].
4. Fade support across the sequence: move from full examples to completion problems, removing progressively more of the solution ([Fading](../elements/fading.md)) [Fading support promotes transfer of responsibility to the learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].
5. Once procedures are secure, introduce erroneous examples for learners to diagnose, deepening conceptual understanding [Erroneous examples build conceptual knowledge when learners can engage the error productively.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M].
6. Monitor expertise and drop example support as soon as learners solve problems efficiently — continuing examples past this point wastes time [Guidance that helps novices becomes less effective or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S].

## Related Strategies
- [Fading](../elements/fading.md) — the mechanism by which example types progress from full support to independence
- [Erroneous Examples](../claims/erroneous-examples-build-conceptual-knowledge.md) — the diagnosis-and-correction variant that builds conceptual knowledge
- [Completion Problems](../elements/fading.md) — the intermediate type on the guidance continuum

## Examples
- **Sweller & Cooper's algebra studies** — the foundational example–problem pair design: learners studied a fully worked algebra example, then solved an isomorphic problem, outperforming learners who solved all problems themselves.
- **[Khan Academy](https://www.khanacademy.org)** — narrated step-by-step video examples followed by practice exercises with on-demand hints, which function as progressive completion problems.
- **[Codecademy](https://www.codecademy.com)** — annotated code examples presented inline before learners write their own version, a completion-problem structure in a programming context.
- **Fractions erroneous-example tutoring (Adams et al.)** — tutoring systems that present incorrect fraction solutions for diagnosis improved conceptual knowledge beyond correct-only examples.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Adams, D. M., McLaren, B. M., Durkin, K., Mayer, R. E., Rittle-Johnson, B., Isotani, S., & van Velsen, M. (2014). Using erroneous examples to improve mathematics learning with a tutoring system. *Computers & Education, 72*, 323–337. [doi:10.1016/j.chb.2014.03.053](https://doi.org/10.1016/j.chb.2014.03.053)