---
type: strategy
id: schema-based-instruction
aliases: [schema-based_instruction]
title: Schema-Based Instruction
description: Teaching learners to recognize the underlying structure of problem types so they can map problem features to appropriate solution strategies.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Schema-Based Instruction

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 2 mixed) · 9 studies (4 causal, 2 review, 2 theoretical, 1 quant-synthesis), `q1`–`q4` · 1 of 9 report an effect size · 1 claim rests on one study

## Description
Schema-based instruction teaches learners to classify problems by their underlying structure — the semantic relationships among quantities — rather than by surface features or keywords. Learners are explicitly taught a small set of problem schemas (e.g., change, group, compare, rest for arithmetic word problems), given a diagram or map for representing each structure, and taught a routine: identify the schema, represent the relationships in the diagram, then plan and execute the solution. The strategy originated in special education and mathematics education research on word-problem solving [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622) [+S].

## Design Implications

Schema-based instruction works because expert problem solving is driven by recognition of deep structure, not surface features; explicit schema teaching builds the recognition templates novices lack [Cognitive load theory: novices benefit from structure-based guidance rather than unguided search.](../principles/cognitive-load-theory.md) [+S]. Meta-analytic evidence shows it outperforms traditional keyword-based and general strategy instruction for word-problem solving, with the largest gains for learners with learning disabilities and low-achieving students [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622) [+S]. The critical design move is teaching *structure discrimination* — comparing problems that share surface features but differ in schema — so learners do not pattern-match on keywords [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306) [+S].

### Context
#### Requirements
- A curated problem set covering each target schema, including mixed-schema sets for discrimination practice
- Explicit teaching of each schema's structure with a consistent visual representation (schema diagram or number sentence template) ([Direct Instruction](../patterns/direct-instruction.md))
- Modeled solution episodes in which the instructor narrates schema identification ([Think-Aloud](../elements/think-aloud.md) style) before strategy selection
- Distributed [Practice](../elements/practice.md) with feedback, fading the diagram support over time ([Fading](../elements/fading.md))
- A small, well-defined set of problem schemas with names, diagrams, and associated solution strategies
- Mixed practice sets that force discrimination between schemas, not blocked sets of one type

#### Constraints
- Keyword-based shortcuts undermine the approach: teaching "altogether means add" produces systematic errors on inconsistent problems [~S] — keyword instruction is a known failure mode that schema instruction must actively displace
- Less effective when the problem domain has no stable, enumerable set of structures; open-ended modeling problems resist schema classification [-M]
- Requires sustained explicit instruction; brief schema exposure without discrimination practice and fading does not produce durable gains [-M]
- Learners with strong prior knowledge may find the diagrams and routines redundant [Expertise reversal: guidance that helps novices can burden experts.](../claims/expertise-reversal-effect.md) [~M]
- Keyword-based shortcuts ("altogether means add") undermine the approach and produce systematic errors on inconsistent problems [-S] — instruction must emphasize relationships, not cue words
- Effectiveness drops when problems do not fit the taught schemas; learners may force-fit novel problems into a familiar structure [~M]
- Less beneficial for learners with strong prior knowledge, for whom explicit schema training can be redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the [expertise-reversal effect](../theories/expertise-reversal-effect.md) applies to schema scaffolds as well
- Requires substantial instructional time; schemas must be taught one at a time with mastery before mixing

#### Implementation Variability
- Schema-*based* instruction (diagram the structure, then solve) vs. schema-*broadening* instruction (teach a schema, then vary surface features and problem formats to promote transfer) [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306)
- Fixed diagram templates per schema vs. a single flexible "problem map" (known/unknown boxes with relation arrows)
- Teacher-led modeling vs. worked-example pairs in which students complete partially drawn diagrams [Worked example–problem pairs reduce load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- **Schema-based transfer instruction** (Jitendra): emphasizes the diagram (schema map) as the central representation
- **Schema-broadening instruction** (Cooper & Sweller): uses [Worked Examples](../principles/worked-examples.md) and faded practice to automate schema application [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
- **Cross-domain variants**: the same logic underlies [Case-Based Learning](../patterns/case-based-learning.md) in professional education, where multiple cases build a flexible schema [Cognitive flexibility theory prescribes multiple representations and cases.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+W]

### Target Learners
- Middle school students struggling with word problems, especially those with learning disabilities or weak reading comprehension [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622) [+S]
- Novices who otherwise rely on keyword matching or random operation selection
- Less beneficial for advanced students, who can induce structures independently [Expertise reversal: guidance that helps novices can burden experts.](../claims/expertise-reversal-effect.md) [~M]
- Students with learning disabilities or low mathematics achievement, who show the largest gains [Meta-analytic support for schema-based instruction with struggling learners.](https://doi.org/10.1111/j.1540-5826.2007.00237.x) [+S]
- Novices who classify problems by surface features rather than structure
- Less valuable for advanced learners who already possess problem schemas [~M]

### Target Learning Goals
- Translating verbal problem statements into mathematical representations
- Procedural fluency in selecting and executing solution strategies
- Transfer: recognizing a familiar structure in unfamiliar surface contexts [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306) [+S]
- Problem classification: mapping novel problems to known structures
- Translation: converting verbal descriptions into equations or diagrams
- Transfer: applying solution strategies across varied surface features [Schema-based instruction improves word-problem solving and transfer.](https://doi.org/10.1080/00220679909597623) [+S]

### Instructions
1. Select 3–5 core schemas for the target domain and design a consistent visual map for each ([Advance Organizers](../elements/advance-organizers.md) can introduce the schema set).
2. Model schema identification aloud on a worked problem, showing how to map quantities into the diagram before computing ([Think-Aloud](../elements/think-aloud.md)).
3. Have students complete partially completed diagrams, then full diagrams, then solve without diagrams — a fading sequence [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].
4. Interleave mixed-schema problem sets and near-transfer variants so students must discriminate structures, not recognize keywords ([Comparing Cases](../elements/comparing-cases.md) if available; otherwise side-by-side problem pairs).
5. Assess by asking students to name the schema and justify the classification, not only to produce the answer ([Assessment](../elements/assessment.md)).

## Related Strategies
- [Worked Examples](../strategies/use_worked_examples.md) — solved problems are the vehicle for demonstrating each schema in action
- [Erroneous Examples](../strategies/erroneous_examples.md) — flawed keyword-based solutions sharpen schema discrimination
- [Graphic Organizers](graphic-organizers.md) — schema diagrams are a domain-specific instance of this family
- [Think-Aloud Modeling](think-aloud-modeling.md) — the method for making schema classification visible
- [Comparing Cases](../elements/comparing-cases.md) — side-by-side problems with the same schema but different surface features build structural recognition

## Examples
- **Jitendra's schema-based instruction program** — a line of intervention studies teaching addition/subtraction and multiplication/division schemas with diagrams to elementary and middle school students, including students with disabilities; consistently improved word-problem accuracy relative to comparison instruction [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622).
- **Fuchs et al.'s schema-broadening instruction** — third-grade word-problem curriculum that taught problem-type schemas and then broadened them to novel variants, improving transfer to unfamiliar problems [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306).
- **[Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md)** — a related research-based framework in which teachers learn the taxonomy of addition/subtraction problem structures and use it to interpret student thinking; the teacher-facing analogue of schema-based instruction.
- **Jitendra's schema-based instruction program** — a published intervention sequence for addition/subtraction and multiplication/division word problems using schematic diagrams; validated in multiple randomized trials with upper-elementary students.
- **Special education math curricula** — schema-based instruction is a recommended practice in teaching word-problem solving to students with mathematics difficulties [Meta-analytic support for schema-based instruction with struggling learners.](https://doi.org/10.1111/j.1540-5826.2007.00237.x) [+S]

## Key Sources
- Xin, Y. P., & Jitendra, A. K. (1999). The effects of instruction in solving mathematical word problems for students with learning problems: A meta-analysis. *The Journal of Special Education, 32*(4), 207-225. [doi:10.1177/002246699903200402](https://doi.org/10.1177/002246699903200402)
- Fuchs, L. S., Fuchs, D., Finelli, R., Courey, S. J., & Hamlett, C. L. (2004). Expanding schema-based transfer instruction to help third graders solve real-life mathematical problems. *American Educational Research Journal, 41*(2), 419–445. [doi:10.3102/00028312041002419](https://doi.org/10.3102/00028312041002419)
- Jitendra, A. K., Griffin, C. C., Haria, P., Leh, J., Adams, A., & Kaduvettoor, A. (2007). A comparison of single and multiple strategy instruction on third-grade students' mathematical problem solving. *Journal of Educational Psychology, 99*(1), 115–127. [doi:10.1037/0022-0663.99.1.115](https://doi.org/10.1037/0022-0663.99.1.115)
- Marshall, S. P. (1995). *Schemas in problem solving*. Cambridge University Press. [doi:10.1017/CBO9780511527890](https://doi.org/10.1017/CBO9780511527890)
- Jitendra, A. K., George, M. P., Sood, S., & Price, K. (2010). Schema-based instruction: Facilitating students' understanding of linear equations. *Learning Disabilities Quarterly, 33*(3), 179–195.
- Jitendra, A. K., et al. (2007). Mathematics instruction for students with learning disabilities: A meta-analysis of instructional components. *Learning Disabilities Research & Practice, 22*(3), 145–157.
- Cooper, G., & Sweller, J. (1987). Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology, 79*(4), 347–362. [doi:10.1037/0022-0663.79.4.347](https://doi.org/10.1037/0022-0663.79.4.347)

<!-- merged 2026-10-09 from strategies/schema-based_instruction ("Schema-Based Instruction"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Schema-Based Instruction

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 8 studies (3 causal, 3 review, 1 quant-synthesis, 1 theoretical), `q2`–`q4` · 1 of 8 report an effect size

## Description
Schema-based instruction teaches learners to recognize and reason about the underlying structure of problems — the relational schema (e.g., change, group, compare, restatement in arithmetic word problems) — rather than relying on surface features or isolated keywords. Learners are explicitly taught to classify a problem by its schema, represent its relationships in a diagram or equation, and then apply the solution strategy associated with that schema. The approach originated in special education and mathematics education research and is now used across domains where problems share identifiable deep structures.

## Design Implications

Schema-based instruction works because expert problem solving is schema-driven: experts classify problems by structure and retrieve a solution method, while novices sort by surface features [Marshall's schema theory of problem solving.](https://doi.org/10.1017/CBO9780511527890) [+M]. Explicitly teaching the classification step converts what experts do tacitly into a learnable procedure, consistent with [Explicit Instruction](../principles/direct-instruction.md) and [Cognitive Load Management](../principles/cognitive-load-management.md) — a shared schema reduces the working-memory demand of treating every problem as new [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S].

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
- **Schema-broadening instruction** (Cooper & Sweller): uses [Worked Examples](../principles/worked-examples.md) and faded practice to automate schema application [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
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
- Xin, Y. P., & Jitendra, A. K. (1999). The effects of instruction in solving mathematical word problems for students with learning problems: A meta-analysis. *The Journal of Special Education, 32*(4), 207-225. [doi:10.1177/002246699903200402](https://doi.org/10.1177/002246699903200402)
- Jitendra, A. K., George, M. P., Sood, S., & Price, K. (2010). Schema-based instruction: Facilitating students' understanding of linear equations. *Learning Disabilities Quarterly, 33*(3), 179–195.
- Jitendra, A. K., et al. (2007). Mathematics instruction for students with learning disabilities: A meta-analysis of instructional components. *Learning Disabilities Research & Practice, 22*(3), 145–157.
- Marshall, S. P. (1995). *Schemas in problem solving*. Cambridge University Press. [doi:10.1017/CBO9780511527890](https://doi.org/10.1017/CBO9780511527890)
- Cooper, G., & Sweller, J. (1987). Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology, 79*(4), 347–362. [doi:10.1037/0022-0663.79.4.347](https://doi.org/10.1037/0022-0663.79.4.347)
-->
