---
type: strategy
id: adapt-worked-example-scaffolding-to-expertise
title: "Adapt worked example scaffolding to learner expertise: structured guidance for novices, debugging practice for advanced learners"
description: "Based on the finding that Guided examples helped low prior knowledge students while Buggy examples helped high prior knowledge students, the article recommends that systems \"dynamically adjust interface constraints ba..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: sutapa-dey-tithi-2026
    resource: "https://arxiv.org/abs/2602.16806"
    title: "Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). https://arxiv.org/abs/2602.16806"
    author: Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes
---

# Adapt worked example scaffolding to learner expertise: structured guidance for novices, debugging practice for advanced learners

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 12 studies (5 review, 3 causal, 2 quant-synthesis, 2 theoretical), `q1`–`q4` · 2 of 12 report an effect size · 4 claims rest on one study

## Description
Based on the finding that Guided examples helped low prior knowledge students while Buggy examples helped high prior knowledge students, the article recommends that systems "dynamically adjust interface constraints based on inferred expertise: providing structured scaffolding to novices to manage cognitive load" while giving more advanced learners debugging-oriented practice. This operationalizes the aptitude-treatment interaction the study measured in the logic tutor.

## Design Implications

### Context
#### Requirements
- The system must be able to infer or measure learner expertise, e.g. via pretest scores as the study did with a median split
- Both intervention types must be available so instruction can be matched to proficiency
#### Constraints
- Buggy examples proved ineffective for low prior knowledge students, who showed no improvement over Control; the authors caution these students may lack stable mental models of correct reasoning and could reinforce misconceptions

### Target Learners
- Undergraduate students learning multi-step formal reasoning, spanning novice to advanced proficiency

### Target Learning Goals
- Logic proof construction and rule application
- Critical evaluation and debugging of solutions

### Affordances
- [Icap Aligned Interactive Worked Examples Logic](../theories/icap-four-mode-engagement-taxonomy.md)

## Claims

- [Worked example type interacted with prior knowledge: Guided examples benefited low prior knowledge students while Buggy examples benefited high prior knowledge students](../claims/ati-buggy-high-guided-low-prior-knowledge.md) [+S]
- [Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking](../claims/markov-behavior-patterns-logic-tutor.md) [+M]
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [+M]
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [+S]
- [Expertise reversal: high-guidance worked examples become ineffective or detrimental once learners have developed cognitive schemata](../claims/expertise-reversal-worked-examples.md) [+W]
- [Scaffolding effectiveness depends on knowledge base: high-guidance scaffolding suits less advanced learners, high-self-regulation scaffolding suits advanced learners](../claims/scaffolding-guidance-self-regulation-moderated-by-knowledge-base.md) [+W]
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [+W]

## Related Strategies

- [Scaffolding](scaffolding.md)

## Examples
-

## Key Sources
- Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). https://arxiv.org/abs/2602.16806
