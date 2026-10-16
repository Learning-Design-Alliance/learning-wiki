---
type: design
id: role-adaptive-ai-companion-framework-maa
title: "Role-Adaptive AI Companion Framework: a Modular Adaptive Agent that dynamically switches between Student Peer, Teacher Assistant, and Parent Advisor roles"
description: "The framework conceptualizes an AI companion as a Modular Adaptive Agent (MAA), inspired by Multi-Agent Systems role-differentiation principles, that \"dynamically transitions between three primary roles: the ‘Student..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: liao-2026
    resource: "https://doi.org/10.1007/s10639-026-13958-6"
    title: "Liao, C.-Y. (2026). Beyond a single role: Justifying a role-adaptive framework for ai companions through a comparative study in elementary book talk. Education and Information Technologies. https://doi.org/10.1007/s10639-026-13958-6"
    author: Liao, C.-Y
---

# Role-Adaptive AI Companion Framework: a Modular Adaptive Agent that dynamically switches between Student Peer, Teacher Assistant, and Parent Advisor roles

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The framework conceptualizes an AI companion as a Modular Adaptive Agent (MAA), inspired by Multi-Agent Systems role-differentiation principles, that "dynamically transitions between three primary roles: the ‘Student Peer’ (facilitating low-stakes dialogue), the ‘Teacher Assistant’ (providing diagnostic analytics), and the ‘Parent Advisor’ (offering actionable home-based guid - ance)." Its core principle is context-aware role adaptability: the agent perceives the user and pedagogical task and modulates its functions, interactional style, and communication register through a modular configuration mechanism, triggered by cues such as user login or task selection. The framework is grounded in scaffolding theory, Learning Companion System principles, and socio-ecological views of family involvement, and its transition logic is justified by the article's empirical competence-gap findings.

## Design Implications

### Context
#### Requirements
- A unified data backbone with Role-Based Access Control and privacy-preserving data protocols so role-appropriate information is shared selectively
- Triggers such as user identity or task selection to activate the appropriate role
- Access to student interaction data, curriculum data, and student profiles for adaptation
#### Constraints
- Conceptualized specifically for elementary reading education and book talk within programs like MSSR
- The framework itself was not implemented or evaluated; the empirical study tested only a fixed single-role instantiation

### Target Learners
- Elementary school students in reading programs
- Their teachers
- Their parents

### Learning Goals
- Reading comprehension and reflective book talk
- Factual recall, emotional response, and future-oriented application (4F dimensions)
- Teacher instructional decision-making and parental support of reading at home

### Claims
- [Ai Conversational Dominance Lower Student Contribution](../claims/ai-conversational-dominance-lower-student-contribution.md) [+M]
- [Grade4 Teacher Superior All 4F Categories](../claims/grade4-teacher-superior-all-4f-categories.md) [+M]
- [Grade5 Ai Facts Strong Feelings Weak](../claims/grade5-ai-facts-strong-feelings-weak.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Liao, C.-Y. (2026). Beyond a single role: Justifying a role-adaptive framework for ai companions through a comparative study in elementary book talk. Education and Information Technologies. https://doi.org/10.1007/s10639-026-13958-6
