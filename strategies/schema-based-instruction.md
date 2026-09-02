---
type: strategy
id: schema-based-instruction
title: Schema-Based Instruction
description: Teaching learners to recognize the underlying structure of problem types so they can map problem features to appropriate solution strategies.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Schema-Based Instruction

> **Strategy** · [All strategies](index.md)

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

#### Constraints
- Keyword-based shortcuts undermine the approach: teaching "altogether means add" produces systematic errors on inconsistent problems [~S] — keyword instruction is a known failure mode that schema instruction must actively displace
- Less effective when the problem domain has no stable, enumerable set of structures; open-ended modeling problems resist schema classification [-M]
- Requires sustained explicit instruction; brief schema exposure without discrimination practice and fading does not produce durable gains [-M]
- Learners with strong prior knowledge may find the diagrams and routines redundant [Expertise reversal: guidance that helps novices can burden experts.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- Schema-*based* instruction (diagram the structure, then solve) vs. schema-*broadening* instruction (teach a schema, then vary surface features and problem formats to promote transfer) [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306)
- Fixed diagram templates per schema vs. a single flexible "problem map" (known/unknown boxes with relation arrows)
- Teacher-led modeling vs. worked-example pairs in which students complete partially drawn diagrams [Worked example–problem pairs reduce load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]

### Target Learners
- Middle school students struggling with word problems, especially those with learning disabilities or weak reading comprehension [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622) [+S]
- Novices who otherwise rely on keyword matching or random operation selection
- Less beneficial for advanced students, who can induce structures independently [Expertise reversal: guidance that helps novices can burden experts.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Translating verbal problem statements into mathematical representations
- Procedural fluency in selecting and executing solution strategies
- Transfer: recognizing a familiar structure in unfamiliar surface contexts [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306) [+S]

### Instructions
1. Select 3–5 core schemas for the target domain and design a consistent visual map for each ([Advance Organizers](../elements/advance-organizers.md) can introduce the schema set).
2. Model schema identification aloud on a worked problem, showing how to map quantities into the diagram before computing ([Think-Aloud](../elements/think-aloud.md)).
3. Have students complete partially completed diagrams, then full diagrams, then solve without diagrams — a fading sequence [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].
4. Interleave mixed-schema problem sets and near-transfer variants so students must discriminate structures, not recognize keywords ([Comparing Cases](../elements/comparing-cases.md) if available; otherwise side-by-side problem pairs).
5. Assess by asking students to name the schema and justify the classification, not only to produce the answer ([Assessment](../elements/assessment.md)).

## Related Strategies
- [Worked Examples](../strategies/use_worked_examples.md) — solved problems are the vehicle for demonstrating each schema in action
- [Erroneous Examples](../strategies/erroneous_examples.md) — flawed keyword-based solutions sharpen schema discrimination
- [Graphic Organizers](../strategies/graphic_organizers.md) — schema diagrams are a domain-specific instance of this family

## Examples
- **Jitendra's schema-based instruction program** — a line of intervention studies teaching addition/subtraction and multiplication/division schemas with diagrams to elementary and middle school students, including students with disabilities; consistently improved word-problem accuracy relative to comparison instruction [Xin & Jitendra, 1999](https://doi.org/10.1080/00220679909597622).
- **Fuchs et al.'s schema-broadening instruction** — third-grade word-problem curriculum that taught problem-type schemas and then broadened them to novel variants, improving transfer to unfamiliar problems [Fuchs et al., 2003](https://doi.org/10.1037/0022-0663.95.2.306).
- **[Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md)** — a related research-based framework in which teachers learn the taxonomy of addition/subtraction problem structures and use it to interpret student thinking; the teacher-facing analogue of schema-based instruction.

## Key Sources
- Xin, Y. P., & Jitendra, A. K. (1999). The effects of instruction in solving mathematical word problems for students with learning problems: A meta-analysis. *The Journal of Special Education, 32*(4), 207-225. [doi:10.1177/002246699903200402](https://doi.org/10.1177/002246699903200402)
- Fuchs, L. S., Fuchs, D., Finelli, R., Courey, S. J., & Hamlett, C. L. (2004). Expanding schema-based transfer instruction to help third graders solve real-life mathematical problems. *American Educational Research Journal, 41*(2), 419–445. [doi:10.3102/00028312041002419](https://doi.org/10.3102/00028312041002419)
- Jitendra, A. K., Griffin, C. C., Haria, P., Leh, J., Adams, A., & Kaduvettoor, A. (2007). A comparison of single and multiple strategy instruction on third-grade students' mathematical problem solving. *Journal of Educational Psychology, 99*(1), 115–127. [doi:10.1037/0022-0663.99.1.115](https://doi.org/10.1037/0022-0663.99.1.115)
- Marshall, S. P. (1995). *Schemas in problem solving*. Cambridge University Press. [doi:10.1017/CBO9780511527890](https://doi.org/10.1017/CBO9780511527890)