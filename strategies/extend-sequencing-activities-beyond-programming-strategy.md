---
type: strategy
id: extend-sequencing-activities-beyond-programming-strategy
title: Extend sequencing activities with AI-generated personalized puzzles to other subjects and higher-order skills
description: The authors suggest that the concept of sequencing pieces of a solution can be applied to other learning contexts, such as reading, foreign language, and math education, and propose an algorithm-to-code activity in wh...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: xinying-hou-2024
    resource: "https://doi.org/10.1145/3657604.3662032"
    title: "Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. 2024. CodeTailor: LLM-Powered Personalized Parsons Puzzles for Engaging Support While Learning Programming. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662032"
    author: Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson
---

# Extend sequencing activities with AI-generated personalized puzzles to other subjects and higher-order skills

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The authors suggest that the concept of sequencing pieces of a solution can be applied to other learning contexts, such as reading, foreign language, and math education, and propose an algorithm-to-code activity in which students write the algorithm in natural language and, if correct, receive a personalized Parsons puzzle based on it. This would leverage AI's strength in code generation while training students' skills in high-level program design and problem decomposition.

## Design Implications

### Context
#### Requirements
- The activity requires the student's algorithm or sequencing input to be evaluated for correctness before a personalized puzzle is generated
#### Constraints
- The article presents these as future design ideas, not as evaluated implementations

### Target Learners
- novice programmers in introductory programming courses
- K-12 students in reading, foreign language, and math education

### Target Learning Goals
- algorithmic thinking
- problem decomposition
- understanding the sequential flow of a narrative

## Claims

- [Students applied more scaffolded practice elements independently on the posttest after using CodeTailor than after receiving an AI-generated solution](../claims/codetailor-higher-scaffolding-apply-rate.md) [+W]
- [Novice programmers perceive CodeTailor's personalized Parsons puzzles as more engaging support than receiving a direct LLM-generated code solution](../claims/codetailor-more-engaging-than-ai-solution.md) [+W]
- [Posttest programming scores did not differ significantly between CodeTailor support and receiving an AI-generated solution](../claims/codetailor-posttest-performance-null.md) [~W]
- [Most novice programmers (88%) preferred CodeTailor over receiving a direct AI-generated solution for learning](../claims/codetailor-preference-88-percent.md) [+W]
- [CodeTailor's personalized Parsons puzzles contain significantly fewer movable blocks than fully movable puzzles built from the same solution](../claims/codetailor-puzzles-more-concise.md) [+W]
- [CodeTailor generates correct solutions closer to a student's incorrect code than a most common student solution](../claims/codetailor-solution-closeness-technical-eval.md) [+W]

## Related Strategies

- [Adapt the two question-design strategies across disciplines: novel scenarios for logic puzzles, guided reasoning for proofs and critical analyses](cross-disciplinary-adaptation-of-question-strategies.md)
- [Re-arrange and extend the web-assisted flipped-classroom activity materials to other science subjects and disciplines](rearrange-web-assisted-materials-other-subjects.md)
- [Add explanations to completed Parsons puzzle blocks to support understanding of difficult details](add-explanations-to-parsons-blocks-strategy.md)

## Examples
-

## Key Sources
- Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. 2024. CodeTailor: LLM-Powered Personalized Parsons Puzzles for Engaging Support While Learning Programming. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662032
