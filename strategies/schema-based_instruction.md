---
type: strategy
title: Schema-Based Instruction
description: Schema-based instruction teaches learners to recognize the underlying structure of problems so they can map surface features to an appropriate solution strategy.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Schema-Based Instruction

## Description
Schema-based instruction teaches learners to recognize and reason about the underlying structure of problems — the relational schema (e.g., change, group, compare, restatement in arithmetic word problems) — rather than relying on surface features or isolated keywords. Learners are explicitly taught to classify a problem by its schema, represent its relationships in a diagram or equation, and then apply the solution strategy associated with that schema. The approach originated in special education and mathematics education research and is now used across domains where problems share identifiable deep structures.

## Design Implications

Schema-based instruction works because expert problem solving is schema-driven: experts classify problems by structure and retrieve a solution method, while novices sort by surface features [Marshall's schema theory of problem solving.](https://doi.org/10.1017/CBO9780511527890) [+M]. Explicitly teaching the classification step converts what experts do tacitly into a learnable procedure, consistent with [Explicit Instruction](../principles/explicit-instruction.md) and [Cognitive Load Management](../principles/cognitive-load-management.md) — a shared schema reduces the working-memory demand of treating every problem as new [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S].

### Context
#### Requirements
- A small, well-defined set of problem schemas with names, diagrams, and associated solution strategies
- [Direct Instruction](../elements/direct-instruction.md) of each schema, including [Think-Aloud](../elements/think-aloud.md) modeling of how to classify and map a problem
- Mixed practice sets that force discrimination between schemas, not blocked sets of one type
- A fade-out path: teacher-modeled diagrams → co-constructed diagrams → learner-generated representations ([Fading](../elements/fading.md))

#### Constraints
- Keyword-based shortcuts ("altogether means add") undermine the approach and produce systematic errors on inconsistent problems [-S] — instruction must emphasize relationships, not cue words
- Effectiveness drops when problems do not fit the taught schemas; learners may force-fit novel problems into a familiar structure [~M]
- Less beneficial for learners with strong prior knowledge, for whom explicit schema training can be redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the [expertise-reversal effect](../theories/expertise-reversal-effect.md) applies to schema scaffolds as well
- Requires substantial instructional time; schemas must be taught one at a time with mastery before mixing

#### Implementation Variability
- **Schema-based transfer instruction** (Jitendra): emphasizes the diagram (schema map) as the central representation
- **Schema-broadening instruction** (Cooper & Sweller): uses [Worked Examples](../principles/worked-examples.md) and faded practice to automate schema application [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
- **Cross-domain variants**: the same logic underlies [Case-Based Learning](../patterns/case-based-learning.md) in professional education, where multiple cases build a flexible schema [Cognitive flexibility theory prescribes multiple representations and cases.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+W]

### Target Learners
- Students with learning disabilities or low mathematics achievement, who show the largest gains [Meta-analytic support for schema-based instruction with struggling learners.](https://doi.org/10.1111/j.1540-5826.2007.00237.x) [+S]
- Novices who classify problems by surface features rather than structure
- Less valuable for advanced learners who already possess problem schemas [~M]

### Target Learning Goals
- Problem classification: mapping novel problems to known structures
- Translation: converting verbal descriptions into equations or diagrams
- Transfer: applying solution strategies across varied surface features [Schema-based instruction improves word-problem solving and transfer.](https://doi.org/10.1080/00220679909597623) [+S]

### Instructions
1. Name and teach one schema at a time using [Direct Instruction](../elements/direct-instruction.md), with a canonical diagram for each structure.
2. Model classification with a [Think-Aloud](../elements/think-aloud.md): "This problem describes a starting amount and a change — that's a change schema."
3. Present a [Worked Example](../principles/worked-examples.md) mapped onto the schema diagram, then a partially worked problem ([Fading](../elements/fading.md)).
4. Run mixed [Practice](../elements/practice.md) sets that interleave schemas so learners must classify before solving.
5. Require learners to draw or complete the schema diagram before computing ([Application](../elements/application.md)), and fade the diagram requirement as accuracy stabilizes.
6. Include [Non-Examples](../elements/non-examples.md) — problems that look similar but belong to a different schema — to sharpen discrimination.

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — worked examples are the primary vehicle for demonstrating a schema in action
- [Think-Aloud Modeling](think-aloud-modeling.md) — the method for making schema classification visible
- [Comparing Cases](../elements/comparing-cases.md) — side-by-side problems with the same schema but different surface features build structural recognition

## Examples
- **Jitendra's schema-based instruction program** — a published intervention sequence for addition/subtraction and multiplication/division word problems using schematic diagrams; validated in multiple randomized trials with upper-elementary students.
- **CGI classrooms** — [Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md) organizes word problems by the same problem-type taxonomy (change, combine, compare) and uses teachers' knowledge of these structures to sequence tasks.
- **Special education math curricula** — schema-based instruction is a recommended practice in teaching word-problem solving to students with mathematics difficulties [Meta-analytic support for schema-based instruction with struggling learners.](https://doi.org/10.1111/j.1540-5826.2007.00237.x) [+S]

## Key Sources
- Xin, Y. P., & Jitendra, A. K. (1999). The effects of instruction in solving mathematical word problems for students with learning problems: A meta-analysis. *The Journal of Educational Research, 92*(6), 345–355. [doi:10.1177/002246699903200402](https://doi.org/10.1177/002246699903200402)
- Jitendra, A. K., George, M. P., Sood, S., & Price, K. (2010). Schema-based instruction: Facilitating students' understanding of linear equations. *Learning Disabilities Quarterly, 33*(3), 179–195. [doi:10.1177/073194871003300304](https://doi.org/10.1177/073194871003300304)
- Jitendra, A. K., et al. (2007). Mathematics instruction for students with learning disabilities: A meta-analysis of instructional components. *Learning Disabilities Research & Practice, 22*(3), 145–157. [doi:10.1007/978-3-642-27702-3_44](https://doi.org/10.1007/978-3-642-27702-3_44)
- Marshall, S. P. (1995). *Schemas in problem solving*. Cambridge University Press. [doi:10.1017/CBO9780511527890](https://doi.org/10.1017/CBO9780511527890)
- Cooper, G., & Sweller, J. (1987). Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology, 79*(4), 347–362. [doi:10.1037/0022-0663.79.4.347](https://doi.org/10.1037/0022-0663.79.4.347)