---
type: strategy
id: collearn-natural-language-strategy-guideline
title: Use a natural-language strategy guideline in the generator prompt so tutoring strategy can be revised without code changes
description: "CoLearn's question generator consults a natural-language guideline appended to its prompt (e.g."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: kailai-he-2026
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
---

# Use a natural-language strategy guideline in the generator prompt so tutoring strategy can be revised without code changes

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
CoLearn's question generator consults a natural-language guideline appended to its prompt (e.g. "when targeting a stored misconception, prefer MCQ with one distractor per misconception"), so revising this text immediately changes how the next item is written, with no code change or redeployment. This is the hook for the agent-side half of co-learning: today the guideline is a fixed text consulted on every generation, and automatic revision from accumulated outcomes is planned but not yet implemented.

## Design Implications

### Context
#### Requirements
- A generator that reads the guideline text on every question generation
#### Constraints
- Automatic strategy self-evolution is designed but not yet implemented; during use the strategy guideline is fixed, so only the agent's memory adapts

### Target Learners
- secondary-school science learners in adaptive tutoring sessions

### Target Learning Goals
- targeted practice on weak topics and diagnosed misconceptions

### Affordances
- [Collearn Human Ai Co Learning Loop](../designs/collearn-human-ai-co-learning-loop.md)

## Related Strategies

- [Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives](ai-nocode-lab-software-development.md)
- [Profile-driven adaptive strategy rules composed dynamically and injected into the system prompt each turn](adaptive-strategy-prompt-injection-rules.md)
- [Revise educational SLM system prompts using the Persona and Context Manager patterns plus cognitive-apprenticeship scaffolding guidelines](educational-prompt-patterns-persona-context-manager-apprenticeship.md)

## Examples
-

## Key Sources
- Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154
