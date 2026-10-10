---
type: research-method
id: edubehaviors
title: EduBehaviors
description: EduBehaviors is an interpretable annotation framework in which researchers write explicit binary assertions about conversational behavior; LLMs annotate each assertion as true or false, and a rule or trained statistical model combines these values into a construct label.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# EduBehaviors

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
EduBehaviors is an interpretable annotation framework in which researchers write explicit binary assertions about conversational behavior; LLMs annotate each assertion as true or false, and a rule or trained statistical model combines these values into a construct label. The article formalizes this as a decomposable schema S=(A,R), noting it is "an example of a concept bottleneck model". It is designed to make coding decisions inspectable and revisable.

## Accounts
<!-- How each source describes or uses the method -->
- **EduBehaviors: decomposable assertion-based schemas separating behavior identification from construct labeling**: EduBehaviors is an interpretable annotation framework in which researchers write explicit binary assertions about conversational behavior; LLMs annotate each assertion as true or false, and a rule or trained statistical model combines these values into a construct label. The article formalizes this as a decomposable schema S=(A,R), noting it is "an example of a concept bottleneck model". It is designed to make coding decisions inspectable and revisable. (Julian Bernado et al. (2026))

### Claims
- [EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting](../claims/edubehaviors-matches-direct-llm-prompting-talkmoves.md) [+M]
- [Adding a cross-model agreement filter improves performance for the top three LLM annotators](../claims/cross-model-agreement-filter-improves-top-annotators.md) [+M]

## Related Research Methods
-

## Key Sources
- Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043
