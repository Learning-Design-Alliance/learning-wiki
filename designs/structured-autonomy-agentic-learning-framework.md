---
type: design
id: structured-autonomy-agentic-learning-framework
title: "Structured autonomy: bounding generative agent behavior through layered pedagogical and domain constraints"
description: CyberAGENTS is a layered, ontology-guided multi-agent framework for gamified cybersecurity learning built on the principle of structured autonomy.
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

# Structured autonomy: bounding generative agent behavior through layered pedagogical and domain constraints

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CyberAGENTS is a layered, ontology-guided multi-agent framework for gamified cybersecurity learning built on the principle of structured autonomy. The article states it "enables structured autonomy through ontology-guided validation, schema-governed behavioral control, and competency-based progression." Three layers regulate the system: a competency graph initializes gameplay, behavioral schemas bound each agent's instructional role, and a cybersecurity ontology validates all generated content before display. The design principle is that "generative flexibility should be bounded through structured autonomy rather than eliminated through static scripting."

## Design Implications

### Context
#### Requirements
- A central orchestrator maintaining shared state across turns, including topic, difficulty, hint usage, feedback history, and XP trajectory
- Behavioral schemas encoding operational modes, trigger conditions, progression logic, and evaluation criteria for each agent
- A domain ontology defining valid entity types and permissible relations for pre-display validation
#### Constraints
- Evaluated only in cybersecurity education at novice difficulty with short 5-15 minute sessions
- The authors state the small-scale deployment and preliminary ablation limit broader claims about long-term learning outcomes

### Target Learners
- Undergraduate cybersecurity students

### Learning Goals
- Cybersecurity reasoning about attacks, defenses, vulnerabilities, and tools
- Sustained engagement and iterative skill-building in practice-driven technical domains

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965
