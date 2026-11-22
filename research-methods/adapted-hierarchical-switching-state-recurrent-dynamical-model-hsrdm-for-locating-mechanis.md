---
type: research-method
id: adapted-hierarchical-switching-state-recurrent-dynamical-model-hsrdm-for-locating-mechanis
title: Adapted hierarchical switching-state recurrent dynamical model (HSRDM) for locating mechanistic reasoning in team conversations
description: "The article's core model is \"a task-specific adaptation of the hierarchical switching-state recurrent dynamical model (HSRDM), a previously proposed [17] general framework for modeling interacting entities over time\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Adapted hierarchical switching-state recurrent dynamical model (HSRDM) for locating mechanistic reasoning in team conversations

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The article's core model is "a task-specific adaptation of the hierarchical switching-state recurrent dynamical model (HSRDM), a previously proposed [17] general framework for modeling interacting entities over time". It uses a shared team-level latent state and per-student entity-level latent states (S0, S1, T0, T1) that evolve turn by turn, with utterances embedded via the EmbeddingGemma encoder (D=128-dimensional embeddings). The model outputs posterior probabilities that a student or the team is in a mechanistic reasoning state at each turn, rather than binary labels.

## Accounts
<!-- How each source describes or uses the method -->
- **Adapted hierarchical switching-state recurrent dynamical model (HSRDM) for locating mechanistic reasoning in team conversations**: The article's core model is "a task-specific adaptation of the hierarchical switching-state recurrent dynamical model (HSRDM), a previously proposed [17] general framework for modeling interacting entities over time". It uses a shared team-level latent state and per-student entity-level latent states (S0, S1, T0, T1) that evolve turn by turn, with utterances embedded via the EmbeddingGemma encoder (D=128-dimensional embeddings). The model outputs posterior probabilities that a student or the team is in a mechanistic reasoning state at each turn, rather than binary labels. (Gili et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C. (2026). Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning. https://arxiv.org/abs/2604.21870. [doi:10.48550/arxiv.2604.21870](https://doi.org/10.48550/arxiv.2604.21870)
