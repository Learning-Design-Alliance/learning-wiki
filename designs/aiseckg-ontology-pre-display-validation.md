---
type: design
id: aiseckg-ontology-pre-display-validation
title: AISecKG ontology as a pre-display validation layer for agent-generated content
description: "CyberAGENTS integrates the AISecKG cybersecurity ontology, which \"defines valid entity types (e.g., tool, technique, attack, vulnerability, defense, system) and permissible relations among them (e.g., exploits, detect..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: hornung-2026
    resource: "https://arxiv.org/abs/2608.07965"
    title: "Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965"
    author: "Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H"
---

# AISecKG ontology as a pre-display validation layer for agent-generated content

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CyberAGENTS integrates the AISecKG cybersecurity ontology, which "defines valid entity types (e.g., tool, technique, attack, vulnerability, defense, system) and permissible relations among them (e.g., exploits, detects, counters, uses, can harm)." Outputs from the Challenge, Buddy, and Critic agents are checked against entity categories, relation patterns, and unsafe-content rules before learner exposure. The article reports that "Content that violates semantic constraints or safety thresholds is flagged and re-prompted under stricter conditions before presentation."

## Design Implications

### Context
#### Requirements
- Ontology-defined entity categories, relation patterns, and unsafe-content rules
- A re-prompting mechanism under stricter conditions when validation fails
#### Constraints
- Validation constrains cybersecurity reasoning and semantic validity; pedagogical behavior is constrained separately by schemas

### Target Learners
- Undergraduate cybersecurity learners

### Learning Goals
- Domain-consistent and safe instructional content in a high-stakes technical domain

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965
